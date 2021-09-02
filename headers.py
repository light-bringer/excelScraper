from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class UserAgents(object, metaclass=Singleton):

    def __init__(self):
        software_names = [SoftwareName.CHROME.value, SoftwareName.EDGE.value, SoftwareName.SAFARI.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.MAC.value]
        self.user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems)

    # you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
    # you can also set number of user agents required by providing `limit` as parameter
    def getRandomUA(self):
        user_agent = self.user_agent_rotator.get_random_user_agent()
        return user_agent
