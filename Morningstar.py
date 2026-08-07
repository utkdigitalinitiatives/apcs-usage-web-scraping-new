def Morningstar(year):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Mergent Online:

    # Input the URL for the main website here
    vendorURL = 'https://research.morningstar.com/ic/admin/sign-in'

    datePattern = re.compile('[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(str(year)) == None:
        raise SyntaxError('Year must be in YYYY format.')

    if year < 2023:
        raise ValueError('Usage is only available starting in 2023.')
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Email"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    
    
    # Go to Usage Reports
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="site-nav__usage-reports"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="site-nav__usage-reports"]').click()
    except:
        raise ReferenceError('Usage Reports page not found. Double-check the login information; if it is correct, then update the XPATH.')
  
    
    
    # Change to Counter: Searches and Sessions
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/div/div/main/div/div/div/div/div[2]/nav/ul/li[3]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div[2]/div/div/main/div/div/div/div/div[2]/nav/ul/li[3]/a').click()
    except:
        raise ReferenceError('Searches and Sessions button not found. Update the XPATH.')


    ## Select the Year
    if year != 2026:
        startPath = '//*[@id="start-of-content"]/main/div/div/div/div/div[2]/div/div/ul/li['
    
        match year:
            case 2025:
                endPath = '2]/a/div/div/div/div[2]/span'
            case 2024:
                endPath = '3]/a/div/div/div/div[2]/span'
    
        xPath = startPath + endPath
        
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xPath))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, xPath).click()
        except:
            raise ReferenceError('Year not found. Update the XPATH.')

    keyword = input('Click the Excel button to export the data. When the report appears in Downloads, type anything here to close the browser.')




    driver.close()

def Morningstar_Info():
    print('Input keys needed:')
    print('Year - YYYY format.')
    print('')
    print('The report will need to be exported manually.')