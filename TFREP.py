def TFREP(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # T&F - REP Platform
    
    # Input the URL for the main website here
    vendorURL = 'http://subs.sams.tf.semcs.net/'
    
    yearPattern = re.compile('[0-9][0-9][0-9][0-9]')

    if yearPattern.fullmatch(str(startYear)) == None:
        raise SyntaxError('Start Year must be in YYYY format.')
    elif yearPattern.fullmatch(str(endYear)) == None:
        raise SyntaxError('End Year must be in YYYY format.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login_form"]/input[2]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Go to the COUNTER 4 Reports
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/ul/li[2]/ul/li[2]/span'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[2]/ul/li[2]/ul/li[2]/span').click()
    except:
        raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH in the code.')
    
    
    # Manually click on COUNTER 4
    print('Click the COUNTER 4 Button.')
    time.sleep(7)
    
    #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/ul/li[2]/ul/li[2]/ul/li[2]/a'))) #Checking if the dropdown is open
    #driver.find_element(By.XPATH, '/html/body/div[2]/ul/li[2]/ul/li[2]/ul/li[2]').click()
    
    
    # Set the Dates:
    
    ## Start Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter_from_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="counter_from_month"]'))
        select.select_by_visible_text(startMonth) # Full month name
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')
    
    ## Start Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="counter_from_year"]'))
        select.select_by_visible_text(str(startYear)) # YYYY format
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')
    
    
    ## End Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="counter_to_month"]'))
        select.select_by_visible_text(endMonth) # Full month name
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')
    
    ## End Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="counter_to_year"]'))
        select.select_by_visible_text(str(endYear)) # YYYY format
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')
    
    # Select the Reports to Download:
    
    reports = ['BR1: Number of Successful Title Requests by Month and Title',
               'BR2: Number of Successful Section Requests by Month and Title', 
               #'BR3: Access Denied to Content Items by Month, Title and Category', 
               #'BR4: Access Denied to Content items by Month, Platform and Category',
               #'BR5: Total Searches by Month and Title',
               #'CR1: Consortium Report 1',
               #'CR2: Consortium Report 2',
               'DB1: Total Searches, Result Clicks and Record Views by Month and Database',
               #'DB2: Access Denied by Month, Database and Category',
               'PR1: Total Searches, Result Clicks and Record Views by Month and Platform']

    
    for report in reports:
        try:
            select = Select(driver.find_element(By.XPATH, '//*[@id="counter_report"]'))
            select.select_by_visible_text(report)
        except:
            raise ReferenceError('Report not found. Double-check the report name and update the name and/or XPATH.')

        reportName = report[0:3]
    
        # Generate Report
        driver.find_element(By.XPATH, '//*[@id="run_report_container"]/input').click()

        if reportName == 'PR1':
            keyword = input('All reports downloaded. Type anything here to close the browser.')

            driver.close()
        else:
            print(reportName, ' report downloaded. Please wait for the next report...')
            time.sleep(2)


def TFREP_Info():
    print('Input keys needed:')
    print('Start month - Full name required.')
    print('Start year - YYYY format.')
    print('End month - Full name required.')
    print('End year - YYYY format.')
    print('')
    print('The website has many report types that can be downloaded. Check the list in the underlying code, and comment out any unwanted reports.')