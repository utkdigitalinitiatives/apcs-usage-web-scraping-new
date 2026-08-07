def ATArchitecture(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re

    
    # Input the URL for the main website here
    vendorURL = 'https://aplust.net/area-privada/biblioteca-digital/'

    datePattern = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Starting date must be in the following format: MM/DD/YYYY')

    if datePattern.fullmatch(endDate) == None:
        raise SyntaxError('Ending date must be in the following format: MM/DD/YYYY')

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    
    # Log into the website
    driver.get(vendorURL)


    # Go to My Account
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="carrito_cabecero"]/p/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="carrito_cabecero"]/p/a[1]').click()
    except:
        raise ReferenceError('My account button not found. Update the XPATH.')


    # Go to My Statistics
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mainContent"]/div/div/div/p[6]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/div/p[6]/a').click()
    except:
        raise ReferenceError('My statistics button not found. Update the XPATH.')
    

    # Input the admin password
    print('Once the password box appears, input the password found on KeePass. The code will continue shortly.')
    time.sleep(20)


    # Set the Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="start_date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date not found. If the login failed, then update the password in the code. Otherwise, update the XPATH.')


    # Set the End Date
    try:
        driver.find_element(By.XPATH, '//*[@id="end_date"]').send_keys(endDate)
    except:
        raise ReferenceError('End date not found. Update the XPATH.')


    # Update with the Search button
    try:
        driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/div[2]/div/form[1]/button').click()
    except:
        raise ReferenceError('Search button not found. Update the XPATH.')


    # Export to Excel
    try:
        driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/div[2]/div/form[3]/button').click()
    except:
        raise ReferenceError('Export to Excel button not found. Update the XPATH.')

    
    keyword = input('When the usage file finishes downloading, type any key to close the window.')

    driver.close()


def ATArchitecture_Info():
    print('Keys needed:')
    print('Start date - in MM/DD/YYYY format.')
    print('End date - in MM/DD/YYYY format.')
    print('')
    print('The code tends to take a long time to run; it will likely time out somewhere in the middle of running. This tends to occur when the password is needed. Everything after that will need to be done manually.')
    