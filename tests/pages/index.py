from .general import General
import config


class IndexPage(General):
    testing_page = config.PROFIREADER_URL

    def __init__(self, driver, device='PC'):
        self.device = device
        self.driver = driver
        self.set_config()
        super().__init__(driver=self.driver, device=self.device, testing_page=self.testing_page)
