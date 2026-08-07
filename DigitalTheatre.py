def DigitalTheatre(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    import pandas as pd
    import time
    import re
    import getpass
    # Digital Theatre+


    dateString = re.compile('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')

    if dateString.fullmatch(str(startDate)) == None:
        raise SyntaxError('Starting date must be in MMDDYYYY format.')
    elif dateString.fullmatch(str(endDate)) == None:
        raise SyntaxError('Ending date must be in MMDDYYYY format.')
    
    
    # Input the URL for the main website here
    vendorURL = 'https://edu.digitaltheatreplus.com/'

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

#    try:
#        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/form/div[3]/input'))) #To ensure the webpage loads before filling out the form
#        driver.find_element(By.XPATH, '//*[@id="session_email"]').send_keys(username)
#        driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys(password)
#        driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/form/div[3]/input').click()
#    except:
#        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')       


    # Go to the COUNTER 5 reports tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layout"]/footer/div[2]/div[4]/div[2]/ul/li[2]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="layout"]/footer/div[2]/div[4]/div[2]/ul/li[2]/a').click()
    except:
        raise ReferenceError('COUNTER 5 button not found. Update the XPATH.')


    # Choose the Full UT Knoxville Account
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="report-customer-id-button"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="report-customer-id-button"]').click()
    except:
        raise ReferenceError('Organisation ID dropdown not found. Update the XPATH.')


    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="report-customer-id-option-ab32a514-df74-4469-a2c3-c8ec8178ab31"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="report-customer-id-option-ab32a514-df74-4469-a2c3-c8ec8178ab31"]').click()
    except:
        raise ReferenceError('Organisation ID dropdown not found. Update the XPATH.')


    # Select Start Date
    try:
        driver.find_element(By.XPATH, '//*[@id="report-start-date"]').send_keys(str(startDate))
    except:
        raise ReferenceError('Start Date box not found. Update the XPATH.')


    # Select End Date
    try:
        driver.find_element(By.XPATH, '//*[@id="report-end-date"]').send_keys(str(endDate))
    except:
        raise ReferenceError('End Date box not found. Update the XPATH.')
    

    # Select Report Types

    ## Comment out any report types that are not needed.


    try:
        driver.find_element(By.XPATH, '//*[@id="PR"]/div[1]').click() #Platform Master Report (PR)
        driver.find_element(By.XPATH, '//*[@id="PR_P1"]/div[1]').click() #Platform Usage Report (PR_P1)
        driver.find_element(By.XPATH, '//*[@id="IR_M1"]/div[1]').click() #Multimedia Item Requests (IR_M1)
        driver.find_element(By.XPATH, '//*[@id="DR"]/div[1]').click() #Database Master Report (DR)
        driver.find_element(By.XPATH, '//*[@id="DR_D1"]/div[1]').click() #Database Search and Item Usage (DR_D1)
    except:
        raise ReferenceError('Report boxes not found. Update the XPATH.')


    # Download the report files

    try:
        driver.find_element(By.XPATH, '//*[@id="main"]/form/div[5]/button/span[2]').click()
    except:
        raise ReferenceError('Download button not found. If no report boxes were checked, check their XPATH. Otherwise, update the button XPATH.')


    
    keyword = input('Reports downloading. Multiple reports may take a few seconds to finish downloading and will download into one ZIP folder. When the report or ZIP folder appears in Downloads, type anything here to close the browser.')


    driver.close()


def DigitalTheatre_Info():
    print('Keys needed:')
    print('Start Date - MMDDYYYY format. No spaces or special characters.')
    print('End Date - MMDDYYYY format. No spaces or special characters.')






    

