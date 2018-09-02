from selenium import webdriver
from easygui import fileopenbox,msgbox,ynbox
from constants import programName

class DriverFactory:
    driver = None
    def __init__(self):
        driverPath = "geckodriver.exe"
        options = webdriver.FirefoxOptions()
        if ynbox("Do you want to run in headless mode? Sound will work.",programName):
            options.add_argument("--headless")
        DriverFactory.driver = webdriver.Firefox(executable_path=driverPath, firefox_options=options)


    @staticmethod
    def getDriver():
        if DriverFactory.driver:
            pass
        else:
            DriverFactory()
        return DriverFactory.driver