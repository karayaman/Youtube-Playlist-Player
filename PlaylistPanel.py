import Tkinter as tk
from Tkinter import Button,Label,Frame
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from DriverFactory import DriverFactory
from constants import programName
from VideoPage import VideoPage

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(programName)
        self.root.geometry("320x60")
        self.label = Label(self.root, text = "")
        self.label.grid(row=1, column=0)
        self.buttonFrame = Frame(self.root)
        self.buttonFrame.grid(row=2, column=0, columnspan=2)
        self.previousVideo = Button(self.buttonFrame, text = "<",command = self.goPreviousVideo)
        self.previousVideo.grid(row=0, column=0)
        self.stopVideo = Button(self.buttonFrame, text = "||",command = self.stopVideo)
        self.stopVideo.grid(row=0, column=1)
        self.nextVideo = Button(self.buttonFrame, text = ">",command = self.goNextVideo)
        self.nextVideo.grid(row=0, column=2)
        self.updateVideoName()
        self.root.mainloop()

    def updateVideoName(self):
        self.label.configure(text="Now playing: "+self.readVideoName())
        self.root.after(1000, self.updateVideoName)

    def readVideoName(self):
        videoPage = VideoPage()
        try:
            videoPage.clickSkipAdvertisement()
        except:
            print("No Advertisement Found")
        cssExpression = "h1 .ytd-video-primary-info-renderer"
        elementExpression = (By.CSS_SELECTOR, cssExpression)
        WebDriverWait(DriverFactory.getDriver(), 5).until(expected_conditions.visibility_of_all_elements_located(elementExpression))
        videoHeader = DriverFactory.getDriver().find_element_by_css_selector(cssExpression)
        return videoHeader.text

    def goPreviousVideo(self):
        print("Clicking prev button")
        cssExpression = ".ytp-prev-button"
        prevButton = DriverFactory.getDriver().find_element_by_css_selector(cssExpression)
        prevButton.click()

    def stopVideo(self):
        print("Clicking stop button")
        cssExpression = ".ytp-play-button"
        playButton = DriverFactory.getDriver().find_element_by_css_selector(cssExpression)
        playButton.click()

    def goNextVideo(self):
        print("Clicking next button")
        cssExpression = ".ytp-next-button"
        nextButton = DriverFactory.getDriver().find_element_by_css_selector(cssExpression)
        nextButton.click()



