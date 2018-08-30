from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from DriverFactory import DriverFactory
from VideoPage import VideoPage
class PlaylistPage:
    def __init__(self):
        pass

    def clickFirstVideo(self):
        print("Clicking first video")
        idExpression = "video-title"
        elementExpression = (By.ID, idExpression)
        WebDriverWait(DriverFactory.getDriver(), 30).until(expected_conditions.visibility_of_element_located(elementExpression))
        firstVideo = DriverFactory.getDriver().find_element_by_id(idExpression)
        firstVideo.click()
        return VideoPage()