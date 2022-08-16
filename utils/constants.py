from datetime import date

"""Paths"""
#Path to generate the folders and .png's
output_path = "output/"

#Path to enter on player ranking
path_to_players_ranking = 'https://%s.tribalwars.com.pt/guest.php?screen=ranking&mode=player'

#Path to enter on tribe ranking
path_to_tribes_ranking = 'https://%s.tribalwars.com.pt/guest.php?screen=ranking&mode=ally'

#Xpath path for the table with the data of the players/tribe top ranking
xpath_value = '//*[@id="content_value"]/tbody/tr/td/table[2]/tbody/tr/td[2]'

#path for obtain the opened worlds
stats_path = 'https://www.tribalwars.com.pt/page/stats'

#xpath path for the list of opened worlds currently
xpath_worlds_value = '//*[@id="stats"]/div[3]/div[3]/div[10]/div[2]/aside/div[2]/ul'

"""Another utils"""

#variable for naming files
today = date.today()

#page_size
page_width = 1920
page_height = 1090

#Dictionary for replace strings
replaceStrings = {"Mundo ": "pt", "Clássico ": "ptc", "Casual ": "ptp", "Speed 1": ''}



