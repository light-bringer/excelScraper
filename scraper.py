from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


class Scraper(ABC):
    @staticmethod
    def getRankFromPosition(listPos=()):
        if not len(listPos):
            return "No Rank"
        else:
            return listPos[0] + 1

    @abstractmethod
    def scrape(self):
        pass


class Amazon(Scraper):
    base_url = "https://www.amazon.in/"
    def_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    @staticmethod
    def getAmazonSearchString(string=""):
        interfix = "+"
        return interfix.join(string.split(" "))

    @staticmethod
    def scrape(product_name="", keyword="", asin="", headers=def_headers):
        url = f"{Amazon.base_url}s?k={Amazon.getAmazonSearchString(keyword)}&ref=nb_sb_noss"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        all_products = soup.find_all("div", class_="s-asin")
        sponsored_products = list(filter(lambda x: x.find(class_="s-sponsored-label-text"), all_products))
        non_sponsored_products = list(filter(lambda x: not x.find(class_="s-sponsored-label-text"), all_products))
        all_rank = [idx for idx, element in enumerate(all_products) if element.attrs["data-asin"] == asin]
        sponsored_rank = [idx for idx, element in enumerate(sponsored_products) if element.attrs["data-asin"] == asin]
        non_sponsored_rank = [idx for idx, element in enumerate(non_sponsored_products) if
                              element.attrs["data-asin"] == asin]
        amz_global_rank = Amazon.getRankFromPosition(all_rank)
        amz_sponsored_rank = Amazon.getRankFromPosition(sponsored_rank)
        amz_non_sponsored_rank = Amazon.getRankFromPosition(non_sponsored_rank)
        result_string = f"Amazon rank for {product_name}: Global: {amz_global_rank}, " \
                 f"Sponsored: {amz_sponsored_rank}, " \
                 f"Non-sponsored: {amz_non_sponsored_rank}"
        result_dict = {
            'Product Name': product_name,
            'Asin': asin,
            'Site': "Amazon",
            'Rank': {
                'Global': amz_global_rank,
                'Sponsored': amz_sponsored_rank,
                'Non-Sponsored': amz_non_sponsored_rank
            }
        }
        return result_dict


# result_data = [[run("mars by GHC Hair Shampoo for Anti Hair fall | DHT Blocker | Sulphate Free Hair Growth Shampoo for Men (200ml)",
#    "dht blocker shampoo for men", "B08QMRYP1S"),],]

