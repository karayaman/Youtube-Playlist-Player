from DriverFactory import DriverFactory
from easygui import enterbox
from PlaylistPage import PlaylistPage
from constants import programName
from PlaylistPanel import App

driver = DriverFactory.getDriver()
playListUrl = enterbox("Please enter youtube playlist url below.",programName)
driver.get(playListUrl)
playlistPage = PlaylistPage()
videoPage = playlistPage.clickFirstVideo()
app = App()




