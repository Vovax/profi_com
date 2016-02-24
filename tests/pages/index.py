from .general import General
from utils.db_init import db_con, cur
import config

class IndexPage(General):
    testing_page = config.PROFIREADER_URL

    def __init__(self, driver, device='PC'):
        cur.execute("SELECT * FROM test_data;")
        print(cur.fetchall())
        self.device = device
        self.driver = driver
        self.set_config()
        super().__init__(driver=self.driver, device=self.device, testing_page=self.testing_page)
