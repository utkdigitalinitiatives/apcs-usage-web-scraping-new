def NKODA(startDate, endDate):
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
    vendorURL = 'https://institutions.nkoda.com/log-in'

    datePattern = re.compile('[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start date must be in the following format: YYYY-MM-DD')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End date must be in the following format: YYYY-MM-DD')
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-onboarding/div/div/main/app-log-in/section/div[2]/div/div/div/div[1]/div[2]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/app-root/app-onboarding/div/div/main/app-log-in/section/div[2]/div/div/div/div[1]/div[2]/input').send_keys(username)
        driver.find_element(By.XPATH, '/html/body/app-root/app-onboarding/div/div/main/app-log-in/section/div[2]/div/div/div/div[2]/div[2]/input').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/app-root/app-onboarding/div/div/main/app-log-in/section/div[2]/div/div/div/div[3]/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    
    
    # Go to Usage Reports
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main/div/app-sidebar/aside/div[2]/nav/ul[4]'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/app-sidebar/aside/div[2]/nav/ul[4]').click()
    except:
        raise ReferenceError('Usage Reports page not found. Double-check the login information; if it is correct, then update the XPATH.')
  
    
    ## Input the Start Date
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[1]/div[1]/div[1]/div[1]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[1]/div[1]/div[1]/div[1]/input').clear()
        driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[1]/div[1]/div[1]/div[1]/input').send_keys(startDate)
    except:
        raise TimeoutError('Start date not found. Update the XPATH in the code.') 


    ## Input the End Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[1]/div[1]/div[1]/div[2]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[1]/div[1]/div[1]/div[2]/input').clear()
        driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[1]/div[1]/div[1]/div[2]/input').send_keys(endDate)
    except:
        raise TimeoutError('End date not found. Update the XPATH in the code.') 


    
    ## Click the Schedule CSV button
        
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[1]/div[2]/div/button'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[1]/div[2]/div/button').click()
    except:
        raise ReferenceError('Schedule CSV button not found. Update the XPATH.')


    ## Go to Scheduled Reports button 
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[2]/div/h3/span'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/app-root/app-main/div/main/app-usage-report/app-remote-report/div/div[2]/div/h3/span').click()
    except:
        raise ReferenceError('Scheduled Reports button not found. Update the XPATH.')

        
    keyword = input('The report can be downloaded from here. It may take a while and a screen refresh to appear. When you are done, type anything here to close the browser.')

    driver.close()


def NKODA_Info():
    print('Input keys needed:')
    print('Start date: YYYY-MM-DD format. The start download date will actually be one day before the input date due to a bug on the NKODA side.')
    print('End date: YYYY-MM-DD format. The end download date will actually be one day before the input date due to a bug on the NKODA side.')
    print('')
    print('The report will need to be downloaded manually. It will take a few moments and a refresh after the code finishes before the report can be downloaded.')