def Chadwyck(fromDate, toDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    # ProQuest - Chadwyck Healy
    
    # Input the URL for the main website here
    vendorURL = 'https://myusage.chadwyck.com/stats/stats.cgi?UID=utenknox#'
    
    datePattern = re.compile('[A-z][A-z][A-z] [0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(fromDate) == None:
        raise SyntaxError('The from date must be in the following format: first three letters of month name, space, YYYY.')
    elif datePattern.fullmatch(toDate) == None:
        raise SyntaxError('The to date must be in the following format: first three letters of month name, space, YYYY.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    driver.get(vendorURL)
    
    # The Login must be done manually.

    print('Log into the website using the username and login info in KeePass.')
    print('')
    print('Once logged in, close the cookie preferences pop-up (if one appears) and wait for the code to continue.')
    
    
    time.sleep(20) #Time to log into the website
    
    
    
    # Select the Date Range:
    
    ## From Date

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/p/table/tbody/tr[1]/td[1]/select[1]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/p/table/tbody/tr[1]/td[1]/select[1]'))
        select.select_by_visible_text(fromDate) # First three letters of the month, space, YYYY
    except:
        raise ReferenceError('From date dropdown not found. Increase the timer if you need more time to login. If you were able to log in, update the XPATH.')
    
    ## To Date

    try:
        select = Select(driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/p/table/tbody/tr[1]/td[1]/select[2]'))
        select.select_by_visible_text(toDate) # First three letters of the month, space, YYYY
    except:
        raise ReferenceError('To date dropdown not found. Update the XPATH.')
    
    # Select Monthly as the summary type:

    try:
        driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/p/table/tbody/tr[6]/td/input[2]').click()
    except:
        raise ReferenceError('Summary button not found. Update the XPATH.')
    
    # Select all Statistics

    try:
        driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/p/table/tbody/tr[11]/td/p[1]/input').click()
    except:
        raise ReferenceError('All Statistics button not found. Update the XPATH.')
    
    # Change the Format to display in Excel

    try:
        driver.find_element(By.XPATH, '/html/body/form/p[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/input[3]').click()
    except:
        raise ReferenceError('Format display button not found. Update the XPATH.')
    
    # Show Statistics
    try:
        driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td/table/tbody/tr/td/p/table/tbody/tr[13]/td/input').click()
    except:
        raise ReferenceError('Show Statistics button not found. Update the XPATH.')
        
    keyword = input('When the report appears in Downloads, type anything here to close the browser.')

    driver.close()


def Chadwyck_Info():
    print('Input keys needed:')
    print('From date - First three letters of month name, space, YYYY format.')
    print('To date - First three letters of month name, space, YYYY format.')
    print('')
    print('The login must be done manually.')