from urllib.request import urlopen
from link_finder import LinkFinder
import csv

def write_format1(games,arcade_name,file,arcade_id):
    #create database for games
    #arcade_id, arcade_name, game1
    #arcade_id, arcade_name, game2
    #...
    for game in games:
        line = [str(arcade_id), arcade_name, game]
        writer = csv.writer(file, delimiter='|')
        writer.writerow(line)
        #file.write(line+'\n')

def write_format2_helper(list):
    #to concatenate a list of string
    output = ''
    if len(list) == 1:
        return output
    #get rid of the first element which is the tag for this list
    for i in range(1,len(list)):
        if(len(list[i].strip())==0):
            #pass the empty line
            continue
        output += list[i]+','
    return output

def write_format2(arcade_name,profile,file,arcade_id):
    #create the database for arcades
    contact_number = write_format2_helper(profile[0])
    address = write_format2_helper(profile[1])
    open_time = write_format2_helper(profile[2])
    information = write_format2_helper(profile[3])

    line = [str(arcade_id), arcade_name, contact_number, address, open_time, information]
    writer = csv.writer(file, delimiter = '|')
    writer.writerow(line)


def gather_information(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder()
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.get_games(),finder.get_arcade_name(),finder.get_profile()
