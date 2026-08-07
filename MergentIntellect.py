def MergentIntellect(startDate, endDate):
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
    vendorURL = 'https://www.mergentintellect.com/index.php/login/index/admin'

    datePattern = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start date must be in MM/DD/YYYY format.')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End date must be in MM/DD/YYYY format.')
    
    
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
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    
    
    # Go to the Administration Page
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="profile_link"]/div'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="profile_link"]/div').click()
    except:
        raise ReferenceError('Administration page not found. Double-check the login information; if it is correct, then update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user_admin_link"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="user_admin_link"]').click()
    except:
        raise ReferenceError('Administration page link not found. Update the XPATH.')    
    
    
    # Change to the Detailed Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ddl_report_type_wrap"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ddl_report_type_wrap"]').click()
    except:
        raise ReferenceError('Report Type button not found. Update the XPATH.')

    print('Select "Detailed" from the Report Type dropdown that appeared.')
    time.sleep(5)
    
      
    ## Start Date
    try:
        driver.find_element(By.XPATH, '//*[@id="startdate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="startdate"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')

    
    ## End Date
    try:
        driver.find_element(By.XPATH, '//*[@id="enddate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="enddate"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')
    
    
    ## Select all Report Columns
    
    try:
        driver.find_element(By.XPATH, '//*[@id="allTo2"]').click()
    except:
        raise ReferenceError('All Reports Column button (>>) not found. Update the XPATH.')

    
    ## Change Report Output to CSV:
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ddl_report_format_wrap"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ddl_report_format_wrap"]').click()
    except:
        raise ReferenceError('Report Type button not found. Update the XPATH.')

    print('Choose "CSV" from the Report Format dropdown that appeared.')
    time.sleep(5)
    
    
    # Generate Report
    try:
        driver.find_element(By.XPATH, '//*[@id="btnGenerateReport"]').click()
    except:
        raise ReferenceError('Generate button not found. Update the XPATH.')


    # Finish the Download
    print('Download the file or input an email to send the report to.')

        
    keyword = input('When you are done, type anything here to close the browser.')


    driver.close()

def MergentIntellect_Info():
    print('Input keys needed:')
    print('Start date - MM/DD/YYYY format.')
    print('End date - MM/DD/YYYY format.')
    print('')
    print('The website contains two dropdowns that must be clicked on manually. Then, the report must be downloaded manually.')