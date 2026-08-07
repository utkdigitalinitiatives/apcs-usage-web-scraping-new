def DigitalCampus(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # SWANK
    
    # Input the URL for the main website here
    vendorURL = 'https://digitalcampus.swankmp.net/utk334393/login?m=1'


    datePattern = re.compile('[A-z][A-z][A-z] [0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start Date needs to be in the following format: First three letters of month name, space, YYYY.')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End Date needs to be in the following format: First three letters of month name, space, YYYY.')    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userName"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/app-root/catalog-layout/mat-sidenav-container/mat-sidenav-content/main/login/div/div/form/div[1]/div[3]/div/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')    
    
    
    # Go to Reports
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/admin-layout/nav/mat-sidenav-container/mat-sidenav/div/mat-nav-list[1]/a[5]/span'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/app-root/admin-layout/nav/mat-sidenav-container/mat-sidenav/div/mat-nav-list[1]/a[5]/span').click()
    except:
        raise ReferenceError('Reports button not found. Double-check the login information; if it is correct, then update the XPATH in the code.')
    
    
    
    # Monthly Usage Data Report:
    
    
    ## From Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-5"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-input-5"]').send_keys(startDate) # First three letters of month, space, YYYY
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')
    
    
    ## To Date
    try:
        driver.find_element(By.XPATH, '//*[@id="mat-input-6"]').send_keys(endDate) # First three letters of month, space, YYYY
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')
    
    
    ## Download the Report
    try:
        driver.find_element(By.XPATH, '/html/body/app-root/admin-layout/nav/mat-sidenav-container/mat-sidenav-content/div/main/reports/div/monthly-usage-data-report/mat-card/mat-card-content/form/div[3]/button/span[2]').click()
    except:
        raise ReferenceError('Download button not found. Update the XPATH.')
    
    print('Monthly Usage Report downloaded. Wait for the Title Request report:')
    time.sleep(2) #Pause between report downloads
    
    # Title Request Report:
    
    
    ## From Date
    try:
        driver.find_element(By.XPATH, '//*[@id="mat-input-3"]').send_keys(startDate) # First three letters of month, space, YYYY
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')
    
    ## To Date
    try:
        driver.find_element(By.XPATH, '//*[@id="mat-input-4"]').send_keys(endDate) # First three letters of month, space, YYYY
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')
    
    ## Download the Report
    try:
        driver.find_element(By.XPATH, '/html/body/app-root/admin-layout/nav/mat-sidenav-container/mat-sidenav-content/div/main/reports/div/title-request-report/mat-card/mat-card-content/form/div[2]/button/span[2]').click()
    except:
        raise ReferenceError('Download button not found. Update the XPATH.')
        
    keyword = input('Once both reports appear in Downloads, type anything here to close the browser.')

    driver.close()

def DigitalCampus_Info():
    print('Input keys needed:')
    print('Start date - First three letters of month name, space, YYYY format.')
    print('End date - First three letters of month name, space, YYYY format.')