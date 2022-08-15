import time
import io
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from datetime import date


"""init variables"""
#variable for naming files
today = date.today()

#paths
output_path = "C:/Users/Pinheiro/Documents/output/"
path_to_players_ranking = 'https://%s.tribalwars.com.pt/guest.php?screen=ranking&mode=player'
path_to_tribes_ranking = 'https://%s.tribalwars.com.pt/guest.php?screen=ranking&mode=ally'
path_to_chromedriver = 'C:/Users/Pinheiro/Documents/chromedriver.exe'
xpath_value = '//*[@id="content_value"]/tbody/tr/td/table[2]/tbody/tr/td[2]'

#page_size
page_width = 1920
page_height = 1100

#pre-defined worlds
predefined_worlds = ['ptc2', 'ptp4', 'pt80', 'pt81', 'pt82', 'pt83', 'pt84', 'pt85', 'pt86']

#generates the images for the worlds
def screenshotsGenerator(self):
    driverOptions(self, 'Players')
    driverOptions(self, 'Tribes')

#configures the driver options of web driver chrome
def driverOptions(self, inputData):
    #checks the type of print wants to make
    if inputData.lower() == 'players':
        url = path_to_players_ranking
    else:
        url = path_to_tribes_ranking

    #chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(path_to_chromedriver)
    driver.get(url % (self))
    time.sleep(2)

    # expands to the size defined
    driver.set_window_size(page_width, page_height)

    #gets the html xpath of the table to screenshot
    ele = driver.find_element("xpath", xpath_value).screenshot_as_png
    imageStream = io.BytesIO(ele)
    im = Image.open(imageStream)
    im.save(output_path + self + '/top' + inputData + '-' + today.strftime("%d_%m") + '.png')

    driver.quit()

for x in predefined_worlds:
    #creates a path for each world to save the img if doesn't exist
    if not os.path.exists(output_path + x):
        os.mkdir(output_path + x)

        #generates the printscreens
        screenshotsGenerator(x)