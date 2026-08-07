def NexisUni(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    from datetime import datetime
    import getpass
        
    # Input the URL for the main website here
    vendorURL = 'https://accountinsights.lexisnexis.com/'

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')

    if startMonth < 1 or startMonth > 12:
        raise ValueError('Start month must be between 1 and 12.')
    if startYear < 2023:
        raise ValueError('Usage is not available for years prior to 2023.')
    
    # Log into the website
    driver.get(vendorURL)

    # Input the username and password, then log in
    
    ## Separate webpages for this website
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userid"]'))) #To ensure the webpage loads before trying, and it is a long load
        driver.find_element(By.XPATH, '//*[@id="userid"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="signInSbmtBtn"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="next"]').click()
    except:
        raise ReferenceError('Second login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    # Exit the Tutorial Page

    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btn_QT_Back"]'))) #Another long load here
        driver.find_element(By.XPATH, '//*[@id="btn_QT_Back"]').click()
    except:
        raise ReferenceError('Tutorial page not found. Double-check login information. If logged in and this page did not appear, comment out this code. Otherwise, update the XPATH.')


    # Go to the Usage Page

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav-usage-report"]')))
        driver.find_element(By.XPATH, '//*[@id="nav-usage-report"]').click()
    except:
        raise ReferenceError('Usage page not found. Update the XPATH.')


    # Change the Start Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startMonth"]/div/div')))
        driver.find_element(By.XPATH, '//*[@id="startMonth"]/div/div').click()
    except:
        raise ReferenceError('Start Month dropdown not found. Update the XPATH.')

    startPathA = '//*[@id="startDate_'

    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    startID = currentMonth - startMonth + (12 * (currentYear - startYear))

    fullStartPath = startPathA + str(startID) + '"]'

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, fullStartPath)))
        driver.find_element(By.XPATH, fullStartPath).click()
    except:
        raise ReferenceError('Start Month not found. If the list opened properly, then update the month XPATH. Otherwise, update the dropdown XPATH.')


    # Change the End Month
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endMonth"]/div/div')))
        driver.find_element(By.XPATH, '//*[@id="endMonth"]/div/div').click()
    except:
        raise ReferenceError('End Month dropdown not found. Update the XPATH.')

    startPathA = '//*[@id="startDate_'

    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    startID = currentMonth - startMonth + (12 * (currentYear - startYear))
    endID = currentMonth - endMonth + (12 * (currentYear - endYear))


    fullStartPath = startPathA + str(startID) + '"]'
    fullEndPath = startPathA + str(endID) + '"]'


    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, fullEndPath)))
        driver.find_element(By.XPATH, fullEndPath).click()
    except:
        raise ReferenceError('End Month not found. If the list opened properly, then update the month XPATH. Otherwise, update the dropdown XPATH.')
        


    # Download the Usage Report
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnDownload"]'))) #Another long load here
        driver.find_element(By.XPATH, '//*[@id="btnDownload"]').click()
        driver.find_element(By.XPATH, '//*[@id="btnDownload"]').click()
        driver.find_element(By.XPATH, '//*[@id="btnDownload"]').click()
        driver.find_element(By.XPATH, '//*[@id="btnDownload"]').click()
        driver.find_element(By.XPATH, '//*[@id="btnDownload"]').click()
        driver.find_element(By.XPATH, '//*[@id="btnDownload"]').click()
    except:
        raise ReferenceError('Download button not found. Update the XPATH.')



    keyword = input('The Download button may take some more clicks to actually download the report. When the report appears in Downloads, type anything here to close the browser.')

    driver.close()


def NexisUni_Info():
    print('Input keys needed:')
    print('Start month - A number between 1 and 12.')
    print('Start year - YYYY format. Usage is not available before 2023.')
    print('End month - A number between 1 and 12.')
    print('End year - YYYY format. Usage is not available before 2023.')

