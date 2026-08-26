def Diabetes(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass

    vendorURL = 'https://sitemaster.diabetesjournals.org/admin/login.aspx'

    startYear = int(startDate[-4:])
    endYear = int(endDate[-4:])

    if startYear < 2023:
        raise ValueError('Usage is only available from January 2023 onwards.')
        
    if startYear < 2025 and endYear >= 2025:
        raise ValueError('Usage timeframes can not span across 2025. Usage before January 2025 is COUNTER 5 only, while usage starting in January 2025 is COUNTER 5.1 only.')

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
        driver.find_element(By.XPATH, '//*[@id="txtUser"]').send_keys(username)
    except:
        raise ReferenceError('Login page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
        
    driver.find_element(By.XPATH, '//*[@id="txtPassword"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="bSignIn"]').click()


    # Pick the COUNTER Report Button based on the date

    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Tab10"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="Tab10"]').click()
        except:
            raise TimeoutError('COUNTER R5 Reports button not found. Check the login information and update if necessary. If the login is correct, then update the XPATH in the code.')

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Tab13"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="Tab13"]').click()
        except:
            raise TimeoutError('COUNTER R5.1 Reports button not found. Check the login information and update if necessary. If the login is correct, then update the XPATH in the code.')



    # Select Start and End Dates


    ## Start Date
    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_ddlfromDateRange"]'))) #To ensure the webpage loads before trying
            select = Select(driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_ddlfromDateRange"]'))
            select.select_by_visible_text(startDate)
        except:
            raise ReferenceError('Start date dropdown not found. Update the XPATH.')

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_ddlfromDateRange"]'))) #To ensure the webpage loads before trying
            select = Select(driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_ddlfromDateRange"]'))
            select.select_by_visible_text(startDate)
        except:
            raise ReferenceError('Start date dropdown not found. Update the XPATH.')



    ## End Date
    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_ddltoDateRange"]'))) #To ensure the webpage loads before trying
            select = Select(driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_ddltoDateRange"]'))
            select.select_by_visible_text(endDate)
        except:
            raise ReferenceError('End date dropdown not found. Update the XPATH.')

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_ddltoDateRange"]'))) #To ensure the webpage loads before trying
            select = Select(driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_ddltoDateRange"]'))
            select.select_by_visible_text(endDate)
        except:
            raise ReferenceError('End date dropdown not found. Update the XPATH.')



    # Download Reports

    ## IR_M1
    
    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_rptCounterReportChildren_0_btnDownloadTsvCounterReport_1"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_rptCounterReportChildren_0_btnDownloadTsvCounterReport_1"]').click()
        except:
            raise ReferenceError('IR_M1 report button not found. Update the XPATH.')  

        print('IR_M1 downloading. Wait for next report...')
        time.sleep(7)

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_rptCounterReportChildren_0_btnDownloadTsvCounterReport_1"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_rptCounterReportChildren_0_btnDownloadTsvCounterReport_1"]').click()
        except:
            raise ReferenceError('IR_M1 report button not found. Update the XPATH.')  

        print('IR_M1 downloading. Wait for next report...')
        time.sleep(7)        




    ## PR
    
    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_btnDownloadTsvCounterReport_1"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_btnDownloadTsvCounterReport_1"]').click()
        except:
            raise ReferenceError('PR report button not found. Update the XPATH.')  

        print('PR downloading. Wait for next report...')
        time.sleep(7)

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_btnDownloadTsvCounterReport_1"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_btnDownloadTsvCounterReport_1"]').click()
        except:
            raise ReferenceError('PR report button not found. Update the XPATH.')  

        print('PR downloading. Wait for next report...')
        time.sleep(7)     



    ## PR_P1
    
    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_rptCounterReportChildren_1_btnDownloadTsvCounterReport_0"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_rptCounterReportChildren_1_btnDownloadTsvCounterReport_0"]').click()
        except:
            raise ReferenceError('PR report button not found. Update the XPATH.')  

        print('PR_P1 downloading. Wait for next report...')
        time.sleep(7)

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_rptCounterReportChildren_1_btnDownloadTsvCounterReport_0"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_rptCounterReportChildren_1_btnDownloadTsvCounterReport_0"]').click()
        except:
            raise ReferenceError('PR report button not found. Update the XPATH.')  

        print('PR_P1 downloading. Wait for next report...')
        time.sleep(7)    



    ## TR
    
    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_btnDownloadTsvCounterReport_2"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_btnDownloadTsvCounterReport_2"]').click()
        except:
            raise ReferenceError('TR report button not found. Update the XPATH.')  

        print('TR downloading. Wait for next report...')
        time.sleep(7)

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_btnDownloadTsvCounterReport_2"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_btnDownloadTsvCounterReport_2"]').click()
        except:
            raise ReferenceError('TR report button not found. Update the XPATH.')  

        print('TR downloading. Wait for next report...')
        time.sleep(7)    



    ## TR_B3
    
    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_rptCounterReportChildren_2_btnDownloadTsvCounterReport_2"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_rptCounterReportChildren_2_btnDownloadTsvCounterReport_2"]').click()
        except:
            raise ReferenceError('TR_B3 report button not found. Update the XPATH.')  

        print('TR_B3 downloading. Wait for next report...')
        time.sleep(7)

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_rptCounterReportChildren_2_btnDownloadTsvCounterReport_2"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_rptCounterReportChildren_2_btnDownloadTsvCounterReport_2"]').click()
        except:
            raise ReferenceError('TR_B3 report button not found. Update the XPATH.')  

        print('TR_B3 downloading. Wait for next report...')
        time.sleep(7)  




    ## TR_J3
    
    if startYear < 2025:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_rptCounterReportChildren_2_btnDownloadTsvCounterReport_5"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR5ReportsContent_rptCounterReport_rptCounterReportChildren_2_btnDownloadTsvCounterReport_5"]').click()
        except:
            raise ReferenceError('TR_J3 report button not found. Update the XPATH.')  

        keyboard = input('TR_J3 downloading. When you are done, type anything here to close the browser.')

    else:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_rptCounterReportChildren_2_btnDownloadTsvCounterReport_5"]'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="AdminMainContent_ucCounterR51ReportsContent_rptCounterReport_rptCounterReportChildren_2_btnDownloadTsvCounterReport_5"]').click()
        except:
            raise ReferenceError('TR_J3 report button not found. Update the XPATH.')  

        keyboard = input('TR_J3 downloading. When you are done, type anything here to close the browser.')


    driver.close()

def Diabetes_Info():
    print('Keys needed:')
    print('Start date - Must be in this format: full name of the month all in lowercase, dash, YYYY. Ex: april-2024 or october-2025')
    print('End date - Same format as the start date.')
    print('')
    print('This vendor stores COUNTER 5 and COUNTER 5.1 usage across specific date ranges. COUNTER 5 is only available up to December 2024. COUNTER 5.1 is only available starting in January 2025.')
    print('')
    print('This code will download the following reports regardless of COUNTER type: IR_M1, PR, PR_P1, TR, TR_B3, TR_J3.')
    