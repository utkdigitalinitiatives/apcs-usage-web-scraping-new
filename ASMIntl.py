def ASMIntl(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    
    vendorURL = 'https://c5live.mpsinsight.com/asm/login'

    datePattern = re.compile('[0-9][0-9]-[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start date string must be in the following format: MM-YYYY')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End date string must be in the following format: MM-YYYY')

    ## Store the vendor's username and password here
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    # Log into the website
    driver.get(vendorURL)
    
    
    # Input the username and password, then log in

    try:
        driver.find_element(By.XPATH, '/html/body/app-root/div/app-astm-login/div/div/div[2]/form/div[1]/input').send_keys(username)
    except:
        raise ReferenceError('Login page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
        
    driver.find_element(By.XPATH, '/html/body/app-root/div/app-astm-login/div/div/div[2]/form/div[2]/input').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/app-root/div/app-astm-login/div/div/div[2]/form/button').click()
    
    # Go to Usage Reports
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="headingProcessing"]/h5/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="headingProcessing"]/h5/a').click()
    except:
        raise TimeoutError('Usage Reports page not found. Check the login information and update if necessary. If the login is correct, then update the XPATH in the code.')

    

    # Run Reports
    
    reportList = ['TR - Title Master Report', #'TR_B1 - Book Requests (Excluding OA_Gold)', 'TR_B2 - Book Access Denied', 
                  'TR_B3 - Book Usage by Access Type', 'DR - Database Master Report', 'DR_D1 - Database Search and Item Usage', 'PR - Platform Master Report', 'PR_P1 - Platform Usage']
    xpathStart = '//*[@id="report"]/ss-multiselect-dropdown/div/div/a['

    for report in range(len(reportList)):
        match report:
            case 0:
                end = '2]'
            #case 1:
            #    end = '3]'
            #case 2:
            #    end = '4]'
            case 1:
                end = '5]'
            case 2:
                end = '6]'
            case 3:
                end = '8]'
            case 4:
                end = '10]'
            case 5:
                end = '11]' #If this does not work, add /span/span[2] to all

        reportXPath = xpathStart + end


        # Select the report dropdown
        #try:
        #    time.sleep(2) #Because the webpage needs to buffer
        #    driver.find_element(By.XPATH, '//*[@id="report"]/ss-multiselect-dropdown/div').click()
        #except:
        #    raise ReferenceError('Dropdown button not found. Update the XPATH.')

        # Select the report
        if report == 0:
            print('Open the Select Report list by clicking on the dropdown.')
            time.sleep(4)
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, reportXPath)))
            driver.find_element(By.XPATH, reportXPath).click()
        except:
            raise ReferenceError('Report XPATH not found. Is the XPATH correct? If not, update the start and/or the match function.')

                # Set Start Date
        if report == 0:
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="year-month3"]')))
                driver.find_element(By.XPATH, '//*[@id="year-month3"]').send_keys(startDate)
            except:
                raise TimeoutError('Start date box not found. Update the XPATH.')
    
        # Set End Date
        if report == 0:
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="year-month4"]')))
                driver.find_element(By.XPATH, '//*[@id="year-month4"]').send_keys(endDate)
            except:
                raise TimeoutError('End date box not found. Update the XPATH.') 

        # Export as TSV
        driver.find_element(By.XPATH, '//*[@id="page-content111"]/div/div/form/div[2]/button[3]').click()

        if report == 5:
            keyword = input('All reports downloaded. Type anything here to close the browser.')
            driver.close()
            
        else:
            print('Report downloaded. Click the Select Report list dropdown, then wait for the next report.')
            time.sleep(7)



def ASMIntl_Info():
    print('Keys Needed:')
    print('startDate: MM-YYYY format.')
    print('endDate: MM-YYYY format.')
    print('')
    print('The report list will need to be clicked for each report downloaded.')
    print('The reports this code will auto-download can be adjusted by going into the code. By default, it downloads the TR, TR_B3, DR, DR_D1, PR, PR_P1.')