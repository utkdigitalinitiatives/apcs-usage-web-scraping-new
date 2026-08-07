def ReferenceShelf(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    # Salem Press
    
    # Input the URL for the main website here
    vendorURL = 'https://online.salempress.com/home.do'


    monthPattern = re.compile('[A-z][A-z][A-z]')
    yearPattern = re.compile('[0-9][0-9][0-9][0-9]')

    if monthPattern.fullmatch(startMonth) == None:
        raise SyntaxError('Start month must be the first three letters of the month name only.')
    elif monthPattern.fullmatch(endMonth) == None:
        raise SyntaxError('End month must be the first three letters of the month name only.')

    if yearPattern.fullmatch(str(startYear)) == None:
        raise SyntaxError('Start year must be in YYYY format.')
    elif yearPattern.fullmatch(str(endYear)) == None:
        raise SyntaxError('End year must be in YYYY format.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    
    # Click on the Login Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="getActivationAdminstratorPopup"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="getActivationAdminstratorPopup"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Manually Input the Username and Password
    
    print('Log into the website using the login information in KeePass.')
    print('')
    print('The code will continue shortly.')
    time.sleep(20) #Allowing time to log in
    
    
    # Go to the Usage Reports
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="saReportDivId"]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="saReportDivId"]/a').click()
    except:
        raise ReferenceError('Usage Reports button not found. Double-check the login information; if it is correct, increase the sleep timer.')
    
    
    # Choose a Date Range:
    
    ## Start Date
    
    
    ### Open the Date Range
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startDate1"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="startDate1"]').click()
    except:
        raise ReferenceError('Date Range not found. Update the XPATH.')
    

    
    ### Year
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
        select.select_by_visible_text(str(startYear)) #YYYY
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')



    
    ### Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
        select.select_by_visible_text(startMonth) #First three letters of month only
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')
    
    
    
    ### Done Button
    try:
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/button[2]').click()
    except:
        raise ReferenceError('Done button not found. Update the XPATH.')
    
    
    ## End Date
    
    
    ### Open the Date Range
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endDate1"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="endDate1"]').click()
    except:
        raise ReferenceError('Date Range not found. Update the XPATH.')
    


        
    ### Year
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
        select.select_by_visible_text(str(endYear)) #YYYY
    except:
        raise ReferenceError('End year not found. Update the XPATH.')

    
    ### Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
        select.select_by_visible_text(endMonth) #First three letters of month only
    except:
        raise ReferenceError('End month not found. Update the XPATH.')
    

    
    
    ### Done Button
    try:
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/button[2]').click()
    except:
        raise ReferenceError('Done button not found. Update the XPATH.')
    
    
    
    
    # Download Reports:
    
    options = ['Platform Report 1', 'Book Report 2', 'Book Report 3', 'Book Report 4']
    
    for report in options:
    
        # Change the type to the report name
        try:
            select = Select(driver.find_element(By.XPATH, '//*[@id="type"]'))
            select.select_by_visible_text(report)
            
            # Then Download Report
            driver.find_element(By.XPATH, '//*[@id="reportGeneratorFormBtn"]').click()
            if report == 'Book Report 4':
                keyword = input('All reports downloaded. Type anything here to close the browser.')

                driver.close()
            else:
                print(report, 'downloaded. Wait for next report:')
                time.sleep(2)
        except:
            raise ReferenceError('Report not found. Update the XPATH.')

def ReferenceShelf_Info():
    print('Input keys needed:')
    print('Start month - First three letters of month name.')
    print('Start year - YYYY format.')
    print('End month - First three letters of month name.')
    print('End year - YYYY format.')
    print('')
    print('Logging in will need to be done manually.')