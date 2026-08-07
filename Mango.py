def Mango():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Mango Languages

    # Input the URL for the main website here
    vendorURL = 'https://org.mangolanguages.com/'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login_page"]/div/div[1]/div[1]/form/div[1]/div[3]/input').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Go to the Reports section
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="reports-nav-tab"]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="reports-nav-tab"]/a').click()
    except:
        raise ReferenceError('Reports section not found. Double-check the login information; if it is correct, then update the XPATH.')
    


    print('Fill in the date range manually, then press the download button.')
    print('')
    print('')
    keyword = input('When you are finished, type anything here to close the browser.')


    driver.close()


def Mango_Info():
    print('No input keys needed.')
    print('')
    print('Once the code stops running, input the date range and download manually.')