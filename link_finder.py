# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:04:43 2017

@author: Yi (Robin) Fan
"""

from html.parser import HTMLParser

class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()
        #flags for parsing html
        self.trFlag=False
        self.tdFlag=False
        self.strongFlag=False
        self.dataFlag=False
        self.arcade_nameFlag = False #this is for the name of the arcade_name

        #flags for parsing information, address, open_time, contact_number
        self.h2_select = False
        self.h2_parse_Info = False
        self.h2_parse_Open = False
        self.h2_parse_Addr = False
        self.h2_parse_Ctct = False

        #the information we ned
        self.arcade_name = ''
        self.games = set()
        self.information = list()
        self.open_time = list()
        self.address = list()
        self.contact_number = list()

    def h2_deflag(self):
        self.h2_parse_Info = False
        self.h2_parse_Addr = False
        self.h2_parse_Ctct = False
        self.h2_parse_Open = False

    def handle_data(self, data):
        if self.dataFlag:
            self.games.add(data)

        if self.arcade_nameFlag:
            self.arcade_name = data

        #set up parsing flag for information, address, contact and opening times
        #this part should above the code used for actually parsing these information
        if self.h2_select:
            if data == "Information":
                self.h2_deflag()
                self.h2_parse_Info = True

            elif data == "Contact Number":
                self.h2_deflag()
                self.h2_parse_Ctct = True

            elif data == "Address":
                self.h2_deflag()
                self.h2_parse_Addr = True

            elif data == "Opening Times":
                self.h2_deflag()
                self.h2_parse_Open = True
            else:
                self.h2_deflag()
                
        #actually parse the Information
        if self.h2_parse_Info:
            self.information.append(data)
        if self.h2_parse_Open:
            self.open_time.append(data)
        if self.h2_parse_Addr:
            self.address.append(data)
        if self.h2_parse_Ctct:
            self.contact_number.append(data)


    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        #parse the games
        if tag == 'tr' and len(attrs)==0:
            self.trFlag = True
        if tag == 'td' and len(attrs)==1:
            (attribute, value) = attrs[0]
            if attribute == 'class' and value == 'top':
                self.tdFlag = True
        if tag == 'strong' and len(attrs) == 0:
            self.strongFlag = True
            if self.trFlag and self.tdFlag and self.strongFlag:
                self.dataFlag = True

        #parse the name of the arcade_name
        if tag == 'h1':
            self.arcade_nameFlag = True

        #parse the information, address, contact, opening times
        if tag == 'h2':
            self.h2_select = True



    def handle_endtag(self, tag):
        #parse the games
        if tag =='strong':
            self.trFlag=False
            self.tdFlag=False
            self.strongFlag=False
            self.dataFlag=False

        #parse the name of the loation
        if  tag == 'h1':
            self.arcade_nameFlag = False

        #parse the information, address, contact, opening times
        if tag == 'h2':
            self.h2_select = False


    def get_games(self):
        return self.games

    def get_arcade_name(self):
       return self.arcade_name

    def get_information(self):
        return self.information

    def get_address(self):
        return self.address

    def get_open_time(self):
        return self.open_time

    def get_contact_number(self):
        return self.contact_number

    def get_profile(self):
        return [self.contact_number,self.address,self.open_time,self.information]

    def error(self, message):
        pass
