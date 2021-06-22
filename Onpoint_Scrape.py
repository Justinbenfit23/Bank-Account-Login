import os
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from dotenv import load_dotenv
from os.path import join, dirname
from oauth2client.service_account import ServiceAccountCredentials
import sys, subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gspread'])
import gspread
from bs4 import BeautifulSoup
import urllib.request


chrome_driver_path = '/Users/Justin/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

dotenv_path = join(dirname(__file__), 'login.env')
load_dotenv(dotenv_path)
BANK_USERNAME = os.environ.get("BANK_USERNAME")
BANK_PASSWORD = os.environ.get("BANK_PASSWORD")

driver.get('https://secure.onpointcu.com/opccuonline_42/uux.aspx#/login')

driver.find_element_by_xpath('//*[@id="fldUsername"]').send_keys(BANK_USERNAME)
driver.find_element_by_xpath('//*[@id="fldPassword"]').send_keys(BANK_PASSWORD)
def login():
    driver.find_element_by_xpath('//*[@id="userLinks"]/button').click()
login()

time.sleep(2)

def two_factor_auth():
    if (driver.current_url == 'https://secure.onpointcu.com/opccuonline_42/uux.aspx#/login/mfa/targets'):
        driver.find_element_by_xpath('//*[@id="ember1501"]').click()
two_factor_auth()

time.sleep(30)

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/Justin/Desktop/Onpoint_Project/credentials.json",scope)
client = gspread.authorize(creds)


gc = gspread.service_account(filename= "/Users/Justin/Desktop/Onpoint_Project/credentials.json")

sh = gc.open("Onpoint Test")

access_code = sh.sheet1.get('D1')
values = ','.join(map(str, access_code))

driver.find_element_by_xpath('//*[@id="tacEntry"]').send_keys(values[2:8])

time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-inner"]/div[4]/form/div[2]/button[1]').click()

time.sleep(10)

def check_register():
    if (driver.current_url == 'https://secure.onpointcu.com/opccuonline_42/uux.aspx#/landingPage'):
        pass 
    else:
        driver.find_element_by_xpath('//*[@id="ember1598"]').click()
check_register()

time.sleep(5)
Balance_1 = driver.find_elements_by_xpath('//*[@id="ember2133"]/dd')



"""url = urllib.request.urlopen("https://secure.onpointcu.com/opccuonline_42/uux.aspx#/landingPage").read()
soup = BeautifulSoup(url,'lxml')
Balance_1 = soup.findall('dd')"""
print(Balance_1)




"""sh.sheet1.update('D2',Balance_1)"""







        




        
    
    


