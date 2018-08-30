from DriverFactory import DriverFactory

class VideoPage:
    def __init__(self):
        pass

    def clickSkipAdvertisement(self):
        print("Skipping Advertisement")
        cssExpression = ".videoAdUiExperimentalSkipIcon"
        skipButton = DriverFactory.getDriver().find_element_by_css_selector(cssExpression)
        skipButton.click()
        return self




