import time
import io
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from utils import constants as cons


def replace_all(text, dic):
  #function to change certain words using a dictionary
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
  
#generates the images for the worlds
def getRanking(self, inputData):
  # function that configs the driver to obtain the table with player and tribe rankings
  
    #checks the type of print wants to make
    if inputData.lower() == 'players':
        url = cons.path_to_players_ranking
    else:
        url = cons.path_to_tribes_ranking

    #chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url % (self))
    time.sleep(2)

    # expands to the size defined
    driver.set_window_size(cons.page_width, cons.page_height)

    #gets the html xpath of the table to screenshot
    ele = driver.find_element("xpath", cons.xpath_value).screenshot_as_png
    imageStream = io.BytesIO(ele)
    im = Image.open(imageStream)
    im.save(cons.output_path + self + '/top' + inputData + '-' + cons.today.strftime("%d_%m") + '.png')

    driver.quit()


#gets available worlds that are currently open

# gets the list of the current online worlds
def getOpenWorldsList():
  # function that obtains all available worlds still open
  #chrome options
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(cons.stats_path)
  time.sleep(2)


  # gets the html xpath of the div with the worlds available
  ele = driver.find_element("xpath", cons.xpath_worlds_value).text

  #replaces the strings for the certain domain
  output = (replace_all(ele, cons.replaceStrings)).split("\n")
  #remove speed worls that became empty strings
  output.remove('')

  driver.quit()
  print("List of current available worlds was successfully obtained.")
  return output


for x in getOpenWorldsList():
  #creates a path for each world to save the img if doesn't exist
  if not os.path.exists(cons.output_path + x):
    print("Creating the paths for saving the images...")
    os.mkdir(cons.output_path + x)

  print("\nStarting the screenshots - World " + x)
  #generates the printscreens
  
  #starts the playerRanking
  getRanking(x, 'Players')
  print("Screenshot of the Players Ranking from the server " + x + " taken and saved sucessfully!")
  #starts the tribeRanking
  getRanking(x, 'Tribes')
  print("Screenshot of the Tribes Ranking from the server " + x + " taken and saved sucessfully!")

print("\nScript sucessfully Stoped! Thanks for using me :D")