def Naxos(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Naxos

    # Input the URL for the main website here
    vendorURL = 'http://www.naxosmusiclibrary.com/home.asp?rurl=%2Fdefault%2Easp'

    yearFormat = re.compile('[0-9][0-9][0-9][0-9]')

    if yearFormat.fullmatch(str(startYear)) == None:
        raise SyntaxError('Start Year must be in YYYY format.')
    elif yearFormat.fullmatch(str(endYear)) == None:
        raise SyntaxError('End Year must be in YYYY format.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)


    # Close the Cookies pop-up
    #try:
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cmpwelcomebtnsave"]/a'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="cmpwelcomebtnsave"]/a').click()
    #except:
    #    raise ReferenceError('Cookies pop-up not found. If a pop-up did not appear, then remove these lines. Otherwise, update the XPATH in the code.')    


    print('Close the cookies pop-up that appears.')
    time.sleep(7)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentarea"]/div/main/section/div[1]/div/div[2]/form/div[1]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="contentarea"]/div/main/section/div[1]/div/div[2]/form/div[1]/input').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="contentarea"]/div/main/section/div[1]/div/div[2]/form/div[2]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="contentarea"]/div/main/section/div[1]/div/div[2]/form/div[4]/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')



    # Go to the My Account Setting page
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menubar-1"]/li[3]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="menubar-1"]/li[3]/a').click()
    except:
        raise ReferenceError('My Account page not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    # Go to the My Account webpage
    driver.get('https://www.naxosmusiclibrary.com/account')

    time.sleep(3)
    
    # Then go to the Usage Statistics webpage
    driver.get('https://www.naxosmusiclibrary.com/statistics')
    time.sleep(3)


    # Naxos Music Library
    # Set the Date Range
    
    ## Start Date - Month
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/div/select[1]')))
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/div/select[1]'))
        select.select_by_visible_text(startMonth) # Full month name
    except:
        raise ReferenceError('Start Month dropdown not found. Double-check the URLs leading to this page; if correct, update the XPATH.')
    
    
    ## Start Date - Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/div/select[2]'))
        select.select_by_visible_text(str(startYear)) # YYYY format
    except:
        raise ReferenceError('Start Year dropdown not found. Update the XPATH.')
    
    
    ## End Date - Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/div/select[1]'))
        select.select_by_visible_text(endMonth) # Full month name
    except:
        raise ReferenceError('End Month dropdown not found. Update the XPATH.')
    
    ## End Date - Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/div/select[2]'))
        select.select_by_visible_text(str(endYear)) # YYYY format
    except:
        raise ReferenceError('End Year dropdown not found. Update the XPATH.')


    ## Set the Time Zone
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[2]/div/select'))
        select.select_by_visible_text('UTC+5') # No spaces here
    except:
        raise ReferenceError('Time Zone dropdown not found. Update the XPATH.')
    
    
    # Click Submit
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[2]/button').click()
    except:
        raise ReferenceError('Submit button not found. Update the XPATH.')
    
    # Export the findings to Excel
    try:
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[3]/div/div[1]/p[1]/a/span')))
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[3]/div/div[1]/p[1]/a/span').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')

    print('Music Library report downloading. The Jazz report will download soon.')
    time.sleep(7)




    
    # Move to Naxos Music Library Jazz
    try:
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div/ul/li[2]/button')))
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/ul/li[2]/button').click()
    except:
        raise ReferenceError('Jazz Library button not found. Update the XPATH.')

    
    # Set the Date Range
    
    ## Start Date - Month
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/div/select[1]')))
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/div/select[1]'))
        select.select_by_visible_text(startMonth) # Full month name
    except:
        raise ReferenceError('Start Month dropdown not found. Double-check the URLs leading to this page; if correct, update the XPATH.')
    
    
    ## Start Date - Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[1]/div/select[2]'))
        select.select_by_visible_text(str(startYear)) # YYYY format
    except:
        raise ReferenceError('Start Year dropdown not found. Update the XPATH.')
    
    
    ## End Date - Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/div/select[1]'))
        select.select_by_visible_text(endMonth) # Full month name
    except:
        raise ReferenceError('End Month dropdown not found. Update the XPATH.')
    
    ## End Date - Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/div/select[2]'))
        select.select_by_visible_text(str(endYear)) # YYYY format
    except:
        raise ReferenceError('End Year dropdown not found. Update the XPATH.')


    ## Set the Time Zone
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[2]/div/select'))
        select.select_by_visible_text('UTC+5') # No spaces here
    except:
        raise ReferenceError('Time Zone dropdown not found. Update the XPATH.')
    
    
    # Click Submit
    try:
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[2]/div[2]/button').click()
    except:
        raise ReferenceError('Submit button not found. Update the XPATH.')
    
    # Export the findings to Excel
    try:
        WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[3]/div/div[1]/p[1]/a/span')))
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div[3]/div/div[1]/p[1]/a/span').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')

   

    keyword = input('Jazz report downloading. When the report appears in Downloads, type anything here to close the browser.')


    driver.close()


def Naxos_Info():
    print('Input keys needed:')
    print('Start month - Full month name needed.')
    print('Start year - YYYY format.')
    print('End month - Full month name needed.')
    print('End year - YYYY format.')
    print('')
    print('The cookies pop-up that appears on the login screen needs to be closed manually.')