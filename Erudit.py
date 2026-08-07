def Erudit(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Erudit
    
    # Input the URL for the main website here
    vendorURL = 'https://www.erudit.org/en/account/login/'

    yearString = re.compile('[0-9][0-9][0-9][0-9]')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    if any(startMonth in x  for x in months) == False:
        raise SyntaxError('Full month names are required for this function.')
    elif any(endMonth in x  for x in months) == False:
        raise SyntaxError('Full month names are required for this function.')


    if yearString.fullmatch(str(startYear)) == None:
        raise SyntaxError('Starting year must be in YYYY format.')
    elif yearString.fullmatch(str(endYear)) == None:
        raise SyntaxError('Ending year must be in YYYY format.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="submit-id-submit"]').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')        
    
    
    # Click on the My Account tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-nav"]/li[3]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="main-nav"]/li[2]/a').click()
    except:
        raise ReferenceError('About tab not found. Update the XPATH.')
    
    # Click on Dashboard
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-nav"]/li[2]/ul/li[1]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="main-nav"]/li[2]/ul/li[1]/a').click()
    except:
        raise ReferenceError('Statistics button not found. Update the XPATH.')


    # Click on Statistics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dashboard-home"]/div[3]/nav/ul/li[2]/a/span'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="dashboard-home"]/div[3]/nav/ul/li[2]/a/span').click()
    except:
        raise ReferenceError('Statistics button not found. Update the XPATH.')  
    
    # Download Journal Requests Report (TR_J1)
    
    
    
    ## Start Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_counter_r5_trj1-month_start"]'))) #This time, no need to wait for a buffer period
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_trj1-month_start"]'))
        select.select_by_visible_text(startMonth) #Full month names
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')
    
    ## Start Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_trj1-year_start"]'))
        select.select_by_visible_text(str(startYear)) #YYYY format
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')
    
    ## End Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_trj1-month_end"]'))
        select.select_by_visible_text(endMonth) #Full month names
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')
    
    ## End Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_trj1-year_end"]'))
        select.select_by_visible_text(str(endYear)) #YYYY format
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')
    
    ## Download the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="counter_r5_trj1-submit"]').click()
    except:
        raise ReferenceError('Submit button not found. Update the XPATH.')


    print('TR_J1 Downloaded.')

    # Download Journal Usage by Access Type Report (TR_J3)

    #try:
    #    driver.find_element(By.XPATH, '//*[@id="statistics"]/div[3]/main/div/div/ul/li[2]/a').click()
    #except:
    #    raise ReferenceError('TR_J3 button not found. Update the XPATH.')

    print('Click the TR_J3 button if you want to download any other reports. Otherwise, close the browser.')
    time.sleep(5)
    
    ## Start Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_counter_r5_trj3-month_start"]'))) #This time, no need to wait for a buffer period
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_trj3-month_start"]'))
        select.select_by_visible_text(startMonth) #Full month names
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')
    
    ## Start Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_trj3-year_start"]'))
        select.select_by_visible_text(str(startYear)) #YYYY format
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')
    
    ## End Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_trj3-month_end"]'))
        select.select_by_visible_text(endMonth) #Full month names
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')
    
    ## End Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_trj3-year_end"]'))
        select.select_by_visible_text(str(endYear)) #YYYY format
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')
    
    ## Download the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="counter_r5_trj3-submit"]').click()
    except:
        raise ReferenceError('Submit button not found. Update the XPATH.')

    print('TR_J3 Downloaded.')


    # Download Journal Article Requests Report (IR_A1)
    
    print('Click the IR_A1 button if you want to download the Item Report. Otherwise, close the browser.')
    time.sleep(5)

    #try:
    #    driver.find_element(By.XPATH, '//*[@id="statistics"]/div[3]/main/div/div/ul/li[3]/a').click()
    #except:
    #    raise ReferenceError('IR_A1 button not found. Update the XPATH.')
    
    ## Start Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_counter_r5_ira1-month_start"]'))) #This time, no need to wait for a buffer period
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_ira1-month_start"]'))
        select.select_by_visible_text(startMonth) #Full month names
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')
    
    ## Start Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_ira1-year_start"]'))
        select.select_by_visible_text(str(startYear)) #YYYY format
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')
    
    ## End Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_ira1-month_end"]'))
        select.select_by_visible_text(endMonth) #Full month names
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')
    
    ## End Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="id_counter_r5_ira1-year_end"]'))
        select.select_by_visible_text(str(endYear)) #YYYY format
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')
    
    ## Download the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="counter_r5_ira1-submit"]').click()
    except:
        raise ReferenceError('Submit button not found. Update the XPATH.')  

    print('IR_A1 downloaded.')
    
    
    keyword = input('When the reports finish downloading, type anything here to close the browser.')

    driver.close()


def Erudit_Info():
    print('Input keys needed:')
    print('Start Month: Full month name needed')
    print('Start Year: YYYY format')
    print('End Month: Full month name needed')
    print('End Year: YYYY format')
    print('')
    print('If downloading any other reports besides the TR_J1, then you must manually move to those pages by clicking their buttons. TR_J3 will run before IR_A1.')