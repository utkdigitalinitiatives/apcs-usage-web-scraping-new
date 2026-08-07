def Scientific():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Scientific.Net
    
    # Input the URL for the main website here
    vendorURL = 'https://idp.scientific.net/login'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    
    
    # Log into the website
    driver.get(vendorURL)
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idp-auth-email"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="idp-auth-email"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="idp-auth-password"]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/sc-root/main/ng-component/div/p-card/div/div/form/p-button[1]/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Go to the Library tab
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/a').click()
    except:
        raise ReferenceError('Library tab not found. Double-check the login information; if it is correct, then update the XPATH.')
        
    # Go to the COUNTER 5 Reports
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[3]/div/ul/li[4]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div/ul/li[4]/a').click()
    except:
        raise ReferenceError('COUNTER Reports button not found. Update the XPATH.')
    
    # Change Export type to XLSX
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/form/div/div[2]/span[4]/label'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div/form/div/div[2]/span[4]/label').click()
    except:
        raise ReferenceError('Export type button not found. Update the XPATH.')
    
    # Then Export Reports:
    try:
        ## TR_J1 (Journal Requests)
        #driver.find_element(By.XPATH, '//*[@id="report-list"]/tbody/tr[2]/td[4]/a').click()
        
        ## TR_J2 (Journal Access Denied)
        #driver.find_element(By.XPATH, '//*[@id="report-list"]/tbody/tr[3]/td[4]/a').click()
        
        ## TR_J3 (Journal Usage by Access Type)
        driver.find_element(By.XPATH, '//*[@id="report-list"]/tbody/tr[4]/td[4]/a').click()
        
        ## TR_J4 (Journal Requests by YOP)
        #driver.find_element(By.XPATH, '//*[@id="report-list"]/tbody/tr[5]/td[4]/a').click()
        
        ## TR_B1 (Book Requests)
        #driver.find_element(By.XPATH, '//*[@id="report-list"]/tbody/tr[6]/td[4]/a').click()
        
        ## TR_B2 (Book Access Denied)
        #driver.find_element(By.XPATH, '//*[@id="report-list"]/tbody/tr[7]/td[4]/a').click()

        ## TR_B3 (Book Access Denied)
        driver.find_element(By.XPATH, '//*[@id="report-list"]/tbody/tr[8]/td[4]/a').click()
    except:
        raise ReferenceError('At least one report not exported. Update the XPATH.')
        

    # Go to the TR
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="open-form"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="open-form"]').click()
    except:
        raise ReferenceError('TR open button not found. Update the XPATH.')
        

    # Load the TR
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="title-report"]/button[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="title-report"]/button[1]').click()
    except:
        raise ReferenceError('TR load button not found. Update the XPATH.')
        

    keyword = input('When all reports appear in Downloads, type anything here to close the browser.')

    driver.close()


def Scientific_Info():
    print('No input keys needed.')
    print('')
    print('The code auto-downloads the following reports: TR, TR_J3, TR_B3.')
    print('The TR_J1, TR_J2, TR_B1, TR_B2, and TR_J4 are also available. These can be downloaded manually, or the underlying code can automate gathering them.')
    print('All reports automatically contain all usage for the current calendar year, divided up by month. Any other dates will need to be chosen manually.')