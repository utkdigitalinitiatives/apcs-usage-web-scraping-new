def Flipster(startMonth, startYear, endMonth, endYear):
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
    # Flipster


    yearString = re.compile('[0-9][0-9][0-9][0-9]')

    if yearString.fullmatch(str(startYear)) == None:
        raise SyntaxError('Starting year must be in YYYY format.')
    elif yearString.fullmatch(str(endYear)) == None:
        raise SyntaxError('Ending year must be in YYYY format.')

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    if any(startMonth in x  for x in months) == False:
        raise SyntaxError('Full month names are required for this function.')
    elif any(endMonth in x  for x in months) == False:
        raise SyntaxError('Full month names are required for this function.')
    
    
    # Input the URL for the main website here
    vendorURL = 'https://eadmin.ebscohost.com/eadmin/login.aspx?ReturnUrl=%2feadmin%2f'

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)

    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="UserName"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="UserName"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="Submit"]').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')   


    
    # Go to the Reports and Statistics tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="custServiceHeader_toolbar_lnkReports"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="custServiceHeader_toolbar_lnkReports"]').click()
    except:
        raise ReferenceError('Reports and Statistics tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')


    # Go to the Flipster Usage Reports
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="LibUsageReportItem"]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="LibUsageReportItem"]/a').click()
    except:
        raise ReferenceError('Flipster Usage Reports button not found. Update the XPATH.')


    # Download Reports - Platform Usage (PR1)

    ## Change Report Type

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Definitions"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="Definitions"]'))
        select.select_by_visible_text('Platform Usage Report')
    except:
        raise ReferenceError('Report Type dropdown not found. Update the XPATH.')

    
    ## Choose Start Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startYears"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="startYears"]'))
        select.select_by_visible_text(str(startYear))
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')


    
    ## Choose Start Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startMonths"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="startMonths"]'))
        select.select_by_visible_text(startMonth)
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')

   
    
    ## Choose End Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endYears"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="endYears"]'))
        select.select_by_visible_text(str(endYear))
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')



    ## Choose End Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endMonths"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="endMonths"]'))
        select.select_by_visible_text(endMonth)
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')



    ## Create Report for Download
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="exportReport"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="exportReport"]').click()
    except:
        raise ReferenceError('Create Report button not found. Update the XPATH.')


    print('PR1 report downloading. Wait for next report...')
    time.sleep(5)


    # Download Reports - Title Usage (TR1)

    ## Change Report Type

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Definitions"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="Definitions"]'))
        select.select_by_visible_text('Title Usage Report')
    except:
        raise ReferenceError('Report Type dropdown not found. Update the XPATH.')


    ## Choose Start Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startYears"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="startYears"]'))
        select.select_by_visible_text(str(startYear))
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')
        

    ## Choose Start Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startMonths"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="startMonths"]'))
        select.select_by_visible_text(startMonth)
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')


    ## Choose End Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endYears"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="endYears"]'))
        select.select_by_visible_text(str(endYear))
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')


    ## Choose End Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endMonths"]'))) #To ensure the webpage loads before filling out the form
        select = Select(driver.find_element(By.XPATH, '//*[@id="endMonths"]'))
        select.select_by_visible_text(endMonth)
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')



    ## Create Report for Download
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="exportReport"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="exportReport"]').click()
    except:
        raise ReferenceError('Create Report button not found. Update the XPATH.')


    keyword = input('TR1 report downloading. When it appears in Downloads, type anything to close the browser.')


    driver.close()
    

def Flipster_Info():
    print('Keys needed:')
    print('Start month - Full month name needed.')
    print('Start year - YYYY format.')
    print('End month - Full month name needed.')
    print('End year - YYYY format.')
    print('')
    print('Reports will not download if the date range requested is longer than 12 months.')







