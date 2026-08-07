def Paratext():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Eight Centuries
    
    # Input the URL for the main website here
    vendorURL = 'https://public.paratext.com/customer/account/account-login.php'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginform"]/form/div[1]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="loginform"]/form/div[1]/input').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="loginform"]/form/div[2]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginform"]/form/button').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')
    
    
    # Go to the Usage Statistics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[5]/div/div/div[2]/div/div[2]/div[1]/div[2]/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[5]/div/div/div[2]/div/div[2]/div[1]/div[2]/a[1]').click()
    except:
        raise ReferenceError('Usage Statistics link not found. Update the XPATH.')

    
    
    
    print('Use the new webpage that opens to download the COUNTER report.')
    print('')
    print('')
    keyword = input('When you are finished, type anything here to close the browser.')

    driver.close()


def Paratext_Info():
    print('No input keys needed.')
    print('')
    print('The code will automatically open a second webpage. This page will need to be filled out manually to access usage statistics.')