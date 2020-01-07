from bs4 import BeautifulSoup
from pymongo import MongoClient
import os
import requests
from selenium import webdriver
import selenium
import time
import re
import pprint


#Starter Page



client = MongoClient()
database = client['2k_db_2']   # Database name
collections = database['player_data']

#function that gets all of the pages of the site that I want to scrape
def get_pages(): 

    page = 'https://2kmtcentral.com/20/players'
    

    page_lst = []
    counter = 1
    
    #insert the orignal link to the fron of the list
    page_lst.insert(0, 'https://2kmtcentral.com/20/players')
    while counter < 40:
        page_lst.append(page + '/' + 'page/' +str(counter))
        counter+=1
    return page_lst    

#function that gets all of the player links from the 
def get_player_links():
    player_list = []

    for i in get_pages():
        webpage = requests.get(i)
        soup = BeautifulSoup(webpage.text,'html.parser')
        for tag in soup.find_all('a',class_='name box-link'):
            link = tag['href']
            player_list.append(link)

    return player_list

def scrape():
    for p in get_player_links():
        sub_page = requests.get(p)
        sub_soup = BeautifulSoup(sub_page.text, 'html.parser')

        try:
        #get name of player
            find_name = sub_soup.find_all('h1')
            name = find_name[0].get_text()

            
            #get the theme type
            try:
                find_theme = sub_soup.find_all('div',class_='col-xs-4 no-padding')
                theme = find_theme[0].get_text(strip = True).strip('Theme')
            except:
                theme = 000
            
            #get postion
            try:
                find_position = sub_soup.find_all('div',class_='col-xs-4 no-padding')
                postion = find_position[1].get_text(strip = True).strip('Position')
            except:
                postion = 000
                
            try:
            #get height
                find_height = sub_soup.find_all('div',class_='col-xs-4 no-padding')
                height = find_position[3].get_text(strip = True).strip('Height')
            except:
                height = 000


            #get weight
            try:
                find_weight = sub_soup.find_all('div',class_='col-xs-4 no-padding')
                weight = find_position[4].get_text(strip = True).strip('Weight')
            except:
                weight = 000

            
            #get age
            try:
                find_age = sub_soup.find_all('div',class_='col-xs-4 no-padding')
                age = find_position[5].get_text(strip = True).strip('Age')
            except:
                age = 000

            #get team
            try: 
                find_team = sub_soup.find_all('div',class_='col-xs-6 no-padding')
                team = find_team[0].get_text(strip = True).strip('Team')
            except:
                team = 000
            
            #get school 
            try: 
                find_school = sub_soup.find_all('div',class_='col-xs-6 no-padding')
                school = find_team[1].get_text(strip = True).strip('From') 
            except:
                school = 000
            
            #get overall rating
            try:
                find_overall = sub_soup.find_all('h4',class_='attribute-header')
                overall = find_overall[0].get_text(strip = True).strip('Overall')
            except:
                overall = 000

            #get outside scoring section neeed to parse later 
            try:
                find_outside_scoring = sub_soup.find_all('section',class_='outside_scoring')
                outside_scoring = find_outside_scoring[0].get_text(strip = True)
            except:
                outside_scoring = 000
                
            #get inside section 
            try:
                find_inside_scoring = sub_soup.find_all('section',class_='inside_scoring')
                inside_scoring = find_inside_scoring[0].get_text(strip = True)
            except:
                inside_scoring = 000

            #get athleticism section
            try:
                find_athleticism = sub_soup.find_all('section',class_='athleticism')
                athleticism = find_athleticism[0].get_text(strip = True)
            except:
                athleticism = 000

            #get playmaking section
            try:
                find_playmaking = sub_soup.find_all('section',class_='playmaking')
                playmaking = find_playmaking[0].get_text(strip = True)
            except:
                playmaking = 000

            #get defending section
            try:
                find_defending = sub_soup.find_all('section',class_='defending')
                defending = find_defending[0].get_text(strip = True)
            except:
                defending = 000

            #get rebounding section
            try:
                find_rebounding = sub_soup.find_all('section',class_='rebounding')
                rebounding = find_rebounding[0].get_text(strip = True)
            except:
                rebounding = 000

            collections.insert_one({'Player_Name':name, 'Theme_Type':theme, 'Postion':postion, 'Height':height, 'Weight':weight, 'Age':age,'team':team, 'School':school, 'Overall':overall, 'Outside_Scoring':outside_scoring, 'inside_scoring':inside_scoring, 'athleticism':athleticism, 'playmaking':playmaking,'defending':defending, 'rebounding':rebounding})
        except:
            continue
        
        
        
if __name__ == "__main__":
    scrape()
    print('Done!')