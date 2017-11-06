# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:34:53 2017

@author: Yi (Robin) Fan
"""

import os
from helper import *


#parameters set up
url_head = 'https://zenius-i-vanisher.com/v5.2/arcade.php?id='
game_file_path = os.path.join('db_game.csv')
arcade_file_path = os.path.join('db_arcade.csv')
game_file = open(game_file_path,'w+')
arcade_file = open(arcade_file_path,'w+')
game_file.write('Arcade_ID|Arcade_Name|Game\n')
arcade_file.write('Arcade_ID|Arcade_Name|Contact Number|Address|Open Time|Information\n')


#main
for i in range (4244): #manually binary search lol!
    #i is the id in url. treated as arcade_id here
    print(i)
    url = url_head + str(i)
    games,arcade_name,profile = gather_information(url)
    #print(arcade_name,games)
    #print(profile)
    write_format1(games,arcade_name,game_file,i)
    write_format2(arcade_name,profile,arcade_file,i)
game_file.close()
arcade_file.close()
