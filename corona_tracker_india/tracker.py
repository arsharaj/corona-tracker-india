# Author - Arsharaj Chauhan
# Corona-Tracker-India
# Copyright (C) 2020  Arsharaj Chauhan

import datetime
from requests import get
from bs4 import BeautifulSoup
from tabulate import tabulate
import os

def track_corona_india():
    """
        Fetches the data from the internet and write it into the text file
        that is stored locally in a well tabulated format.
    """
    try:    
        # Getting the today's date
        today = datetime.date.today()

        # Defining the data-file
        filename = 'corona-data/' + str(today) + '-data.txt'

        # Opening the datafile
        try:
            datafile = open(filename, "w")
        except FileNotFoundError:
            os.mkdir("corona-data")
            print("Creating a folder named corona-data")
            datafile = open(filename, "w")
        except:
            print("An error occured.")
            print("Report to the maintainer.")

        # Getting the html file
        corona_web_url = 'https://www.mohfw.gov.in/'
        html_text = get(corona_web_url).text
        html_text = BeautifulSoup(html_text, 'html.parser')

        # Writing the title of the source
        datafile.write("Title : MoHFW"+ "\n")

        # Gathering all the meta-site data
        raw_data = html_text.find_all('div', class_= "site-meta")
        for data in raw_data[:3]:
            datafile.write(data.get_text().strip() + "\n")
        datafile.write("\n\n")

        # Getting the site stats data
        datafile.write("Statistics : \n")
        raw_data = html_text.find("div", class_="site-stats-count").ul.find_all('li')
        table = []
        for data in raw_data[:-1]:
            table.append([data.find('span').get_text(),data.strong.get_text()])
        datafile.write(tabulate(table,tablefmt="pretty"))
        datafile.write("\n\n")

        # Getting the data statewise
        datafile.write("COVID-19 Statewise Status : \n\n")
        raw_data = html_text.find("div", class_ = "data-table").table

        # Fetching the data from the headers
        table_headers = raw_data.thead.tr.find_all("th")
        headers = []
        for head in table_headers:
            headers.append(head.get_text().strip())

        # Fetching the table body
        table_body = raw_data.tbody.find_all("tr")
        table = []
        for state in table_body[:-2]:
            mini_table = []
            for data in state.find_all('td'):
                mini_table.append(data.get_text().strip())
            table.append(mini_table)
        datafile.write(tabulate(table,headers,tablefmt="fancy_grid"))
        datafile.write("\n")
        datafile.write("Total number of confirmed cases : " + table_body[-2].find_all('td')[1].get_text().strip())
        datafile.close()
        print("All the data is fetched into the corona-data folder ..")
    except ConnectionError:
        print("Network Problem..")
        print("Try to checkout your internet connection")
    except:
        print("\n")
    return