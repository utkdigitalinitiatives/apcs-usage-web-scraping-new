def LDC():
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
    vendorURL = 'https://catalog.ldc.upenn.edu/login'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')


    
    # Log into the website
    driver.get(vendorURL)

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="spree_user_login"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="spree_user_login"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="spree_user_password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="submit_form"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    # Go to the Downloads tab
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="org-members"]/fieldset/a[6]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="org-members"]/fieldset/a[6]').click()
    except:
        raise ReferenceError('Downloads tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')


    keyword = input('Usage will need to be downloaded and tracked manually. When you are done, type anything to close the browser.')

    driver.close()


def LDC_Info():
    print('No keys needed.')