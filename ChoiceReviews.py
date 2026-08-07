def ChoiceReviews(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass

    # Choice Reviews


    datePattern = re.compile('[A-z][A-z][A-z], [0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start date string must be in the following format: First three letters of month, comma, space, YYYY. Ex: Jan, 2025')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End date string must be in the following format: First three letters of month, comma, space, YYYY. Ex: Jan, 2025')

    
    # Input the URL for the main website here
    vendorURL = 'https://choicereviews.org/login?loginFrom=https%3A%2F%2Fchoicereviews.org%2F'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="_submit"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    # Go to the Usage Statistics button
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="js-navigation-menu"]/li[4]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="js-navigation-menu"]/li[4]/a').click()
    except:
        raise ReferenceError('Admin tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    print('Click on the Page View Data button that appears in the admin tab.')
    time.sleep(5)



    # Change the Start Data
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from-time"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="from-time"]').clear()
        driver.find_element(By.XPATH, '//*[@id="from-time"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date tab not found. Update the XPATH.')


    # Change the End Data
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to-time"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="to-time"]').clear()
        driver.find_element(By.XPATH, '//*[@id="to-time"]').send_keys(endDate)
    except:
        raise ReferenceError('End date tab not found. Update the XPATH.')


    # Download Page View Data
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="testtest"]/div[1]/div[2]/div/div/div/div[3]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="testtest"]/div[1]/div[2]/div/div/div/div[3]/div/a[1]').click()
    except:
        raise ReferenceError('Download button not found. Update the XPATH.')



    
    keyword = input('Report downloading; it will take a few seconds to appear in downloads. When you are done, type anything here to close the browser.')

    driver.close()

def ChoiceReviews_Info():
    print('Keys needed:')
    print('Start date - First three letters of month name, comma, space, YYYY is required. Example: Jan, 2025')
    print('End date - Same format as the start date. Example: Jun, 2025')
    print('')
    print('The usage tab will have to be clicked manually after logging in.')


    