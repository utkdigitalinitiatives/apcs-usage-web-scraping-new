def IGI(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass



    # Input the URL for the main website here
    vendorURL = 'https://www.igi-global.com/gateway/login/?returnurl=%2fgateway%2flibrarian-tools%2fcounter-reports%2f'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucGenericLogin_txtUsername"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucGenericLogin_txtUsername"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucGenericLogin_txtPassword"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucGenericLogin_lnkLogin"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlInstitutionEntities"]'))) #To ensure the webpage loads before trying

    
    # Download Report - Platform Master Report (PR)

    ## This is chosen by default.


    ## Change the Reporting Period Start Date

    try:
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_pnlContainer"]/div[7]/div[1]').click()
    except:
        raise ReferenceError('Reporting Period tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')


    ## Change the Reporting Period End Date   
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')


    ## Download to Excel
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')   


    print('PR Report downloaded. Wait for next report...')
    time.sleep(5)
    

    # Download Report - Platform Usage (PR_P1)

    ## Choose the Report Type

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))
        select.select_by_visible_text('Platform Usage')
    except:
        raise ReferenceError('Report Type dropdown not found. Update the XPATH.')  


    ## Change the Reporting Period Start Date

    try:
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_pnlContainer"]/div[7]/div[1]').click()
    except:
        raise ReferenceError('Reporting Period tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')


    ## Change the Reporting Period End Date   
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')


    ## Download to Excel
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')


    print('PR_P1 Report downloaded. Wait for next report...')
    time.sleep(5)




    # Download Report - Title Master Report (TR)

    ## Choose the Report Type

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))
        select.select_by_visible_text('Title Master Report')
    except:
        raise ReferenceError('Report Type dropdown not found. Update the XPATH.')  


    ## Change the Reporting Period Start Date

    try:
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_pnlContainer"]/div[7]/div[1]').click()
    except:
        raise ReferenceError('Reporting Period tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')


    ## Change the Reporting Period End Date   
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')


    ## Download to Excel
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')


    print('TR Report downloaded. Wait for next report...')
    time.sleep(5)



    # Download Report - Book Usage by Access Type (TR_B3)

    ## Choose the Report Type

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))
        select.select_by_visible_text('Book Usage by Access Type')
    except:
        raise ReferenceError('Report Type dropdown not found. Update the XPATH.')  


    ## Change the Reporting Period Start Date

    try:
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_pnlContainer"]/div[7]/div[1]').click()
    except:
        raise ReferenceError('Reporting Period tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')


    ## Change the Reporting Period End Date   
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')


    ## Download to Excel
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')


    print('TR_B3 Report downloaded. Wait for next report...')
    time.sleep(5)
        


    # Download Report - Journal Usage by Access Type (TR_J3)

    ## Choose the Report Type

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))
        select.select_by_visible_text('Journal Usage by Access Type')
    except:
        raise ReferenceError('Report Type dropdown not found. Update the XPATH.')  


    ## Change the Reporting Period Start Date

    try:
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_pnlContainer"]/div[7]/div[1]').click()
    except:
        raise ReferenceError('Reporting Period tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')


    ## Change the Reporting Period End Date   
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')


    ## Download to Excel
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')


    print('TR_J3 Report downloaded. Wait for next report...')
    time.sleep(5)



    # Download Report - Multimedia Item Requests (IR_M1)

    ## Choose the Report Type

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_ddlReports"]'))
        select.select_by_visible_text('Multimedia Item Requests')
    except:
        raise ReferenceError('Report Type dropdown not found. Update the XPATH.')  


    ## Change the Reporting Period Start Date

    try:
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_pnlContainer"]/div[7]/div[1]').click()
    except:
        raise ReferenceError('Reporting Period tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtStartDate"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date box not found. Update the XPATH.')


    ## Change the Reporting Period End Date   
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').clear()
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_txtEndDate"]').send_keys(endDate)
    except:
        raise ReferenceError('End date box not found. Update the XPATH.')


    ## Download to Excel
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_cphMain_cphSection_ucCounter_lnkViewReportExcel"]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')


    keyword = input('IR_M1 Report downloaded. Once it is done, type anything here to close the browser.')    


    driver.close()


def IGI_Info():
    print('Keys needed:')
    print('Start Date - The format needs to be full month, space, DD, comma, space, YYYY. Include the 0 on the date if using a single digit day. Example: October 31, 2024 or June 04, 2021')
    print('End Date - Same format as the start date.')
    print('')
    print('This will automatically download the following reports: PR, PR_P1, TR, TR_B3, TR_J3, IR_M1.')


        
