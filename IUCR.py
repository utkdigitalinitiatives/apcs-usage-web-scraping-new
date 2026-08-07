def IUCR(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # IUCR
    
    # Input the URL for the main website here
    vendorURL = 'http://journals.iucr.org/services/usagereports.html'

    monthPattern = re.compile('[A-z][A-z][A-z]')
    yearPattern = re.compile('[0-9][0-9][0-9][0-9]')

    if monthPattern.fullmatch(startMonth) == None:
        raise SyntaxError('Start month should be the first three letters only.')
    elif monthPattern.fullmatch(endMonth) == None:
        raise SyntaxError('End month should be the first three letters only.')

    if yearPattern.fullmatch(str(startYear)) == None:
        raise SyntaxError('Start year should be in YYYY format.')
    elif yearPattern.fullmatch(str(endYear)) == None:
        raise SyntaxError('End year should be in YYYY format.')
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/form/table/tbody/tr[1]/td[2]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="main"]/form/table/tbody/tr[1]/td[2]/input').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="main"]/form/table/tbody/tr[2]/td[2]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="main"]/form/table/tbody/tr[3]/td[2]/input').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')        
    
    
    # Proceed past the Not Secure page
    
    #try:
    #    time.sleep(2)
        #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="proceed-button"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="proceed-button"]').click()
    #except:
    #    raise ReferenceError('Not secure page not found. If this did not appear, then update the login information or comment out the code chunk if login worked. Otherwise, update the XPATH.')
    

    # Click on Usage Data button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account"]/ul/li[2]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="account"]/ul/li[2]/a').click()
    except:
        raise ReferenceError('Usage Data button not found. Update the XPATH.')
    
    
    
    
    # Adjust the Dates
    
    
    ## Start Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/select'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/select'))
        select.select_by_visible_text(startMonth) #First three letters of the month only
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')
    
    ## Start Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[3]/select'))
        select.select_by_visible_text(str(startYear)) #YYYY
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')
    
    
    ## End Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[5]/select'))
        select.select_by_visible_text(endMonth) #First three letters of the month only
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')
    
    
    ## End Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[1]/td[6]/select'))
        select.select_by_visible_text(str(endYear)) #YYYY
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')

    
    
    
    # Choose Reports
    
    ## If any of these are not necessary, comment out those lines.
    
    
    
    ## Journal Report 1: Number of Successful Full-Text Article Requests by Month and Journal.
    
    ###### THIS ONE STARTS CLICKED BY DEFAULT
    
    #try:
        #driver.find_element(By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[2]/td[1]/input').click()
    #except:
    #    raise ReferenceError('JR1 Report button not found. Update the XPATH.')
        
    ## Journal Report 1 GOA: Number of Successful Gold Open Access Full-Text Article Requests by Month and Journal.

    #try:
        #driver.find_element(By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[3]/td[1]/input').click()
    #except:
    #    raise ReferenceError('JR1-GOA Report button not found. Update the XPATH.')
    
    ## Journal Report 2: Access Denied to Full-Text Articles by Month, Journal and Category.

    #try:
    #    driver.find_element(By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[4]/td[1]/input').click()
    #except:
    #    raise ReferenceError('JR2 Report button not found. Update the XPATH.')
    
    ## 	Journal Report 5: Number of Successful Full-Text Article Requests by Year-of-Publication.

    #try:
    #    driver.find_element(By.XPATH, '//*[@id="usageform"]/table/tbody/tr/td[1]/table/tbody/tr[5]/td[1]/input').click()
    #except:
    #    raise ReferenceError('JR5 Report button not found. Update the XPATH.')
    
    
    # Download the article(s)
    try:
        driver.find_element(By.XPATH, '//*[@id="usagedownload"]').click()
    except:
        raise ReferenceError('Download button not found. Update the XPATH.')

    print('These HTML files will need to be copied into Excel manually.')
    keyword = input('When you are done, type anything here to close the browser.')


    driver.close()


def IUCR_Info():
    print('Input keys needed:')
    print('Start month - First three letters only.')
    print('Start year - YYYY format')
    print('End month - First three letters only.')
    print('End year - YYYY format')
    print('')
    print('')
    print('IUCR offers the following reports: JR1, JR1-GOA, JR2, JR5. The JR1 will download automatically.')
    print('If you want to download a report, uncomment its code chunk in the underlying code. If you do not want to download a report, comment it out using "#" before each line.')
    print('')
    print('The usage data will need to be copied from the website file created upon download to Excel manually.')