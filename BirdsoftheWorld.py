def BirdsoftheWorld():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    
    # Birds of the World
    
    # Input the URL for the main website here
    vendorURL = 'https://secure.birds.cornell.edu/cassso/login?service=https%3A%2F%2Fbirdsoftheworld.org%2Flogin%2Fcas'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-user-name"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="input-user-name"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="form-submit"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    # Try to Access the Vendor Portal

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div[2]')))
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[2]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[2]/div[2]/div[3]/nav[1]/ul/li[1]/a').click()
    except:
        raise ReferenceError('Vendor Portal not found. Update the XPATH.')
        

    
    # Download the Page View Metrics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[1]/div[3]/div[1]/div/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div[3]/div[1]/div/a').click()
    except:
        raise ReferenceError('Metrics webpage not found. Did you click on the Vendor Portal button? If so, then update the Page View Metrics XPATH.')
    
    keyword = input('When the report download finishes, type anything here to close the browser.')

    driver.close()


def BirdsoftheWorld_Info():
    print('No keys needed.')