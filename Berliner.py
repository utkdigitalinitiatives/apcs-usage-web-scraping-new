def Berliner():
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
    vendorURL = 'https://institutions.digitalconcerthall.com/user/log_in'
    
    ## Store the vendor's username and password here
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')


    datePattern = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    # Log into the website
    driver.get(vendorURL)
    

    # Input the username and password, then log in
    try:
        driver.find_element(By.XPATH, '//*[@id="user_username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="user_password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login_form"]/div/div[4]/button').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    print('Input the Start date and the End date. The code will resume by clicking the Update button in a few seconds.')
    time.sleep(15)
    
    
    # Click the Update button
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="institution-statistics-from-to"]/div[3]/button')))
        driver.find_element(By.XPATH, '//*[@id="institution-statistics-from-to"]/div[3]/button').click() 
    except:
        raise ReferenceError('Update button not found. Double-check the XPATH in the code.')
    
    
    print('After the visuals appear on screen, scroll down and press the CSV button to export the data.')
    keyword = input('When the CSV finishes downloading, type anything here to close the browser.')

    driver.close()

def Berliner_Info():
    print('No keys needed.')
    print('')
    print('The start date and end date must be input manually. After that, the data must also be exported manually.')