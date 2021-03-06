from reader import read_xls_csv
from headers import UserAgents
from scraper import Amazon
import json

from writer import GoogleSheet


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def work():
    EXCEL_FILE: str = "/home/light-bringer/Downloads/keywords.xlsx"
    products_to_scrape = read_xls_csv(EXCEL_FILE)
    UA = UserAgents()
    '''
    "sku": row[0],
    "asin": row[1],
    "product_name": row[2],
    "keyword1": row[3],
    "keyword2": row[4],
    "keyword3": row[5],
    '''
    google_sheet = GoogleSheet()
    amzn_products = []
    for product in products_to_scrape:
        ua_header = {
            'User-Agent': UA.getRandomUA()
        }
        # print(ua_header)
        product_details = Amazon.scrape(asin=product["asin"], product_name=product["product_name"],
                                        keyword=product["keyword1"] or product["keyword2"] or product["keyword3"],
                                        headers=ua_header
                                        )
        amzn_products.append(product_details)

    print(amzn_products)
    for amzn_product in amzn_products:
        a = google_sheet.writeLineToSheet(amzn_product)
        print(a)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    work()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
