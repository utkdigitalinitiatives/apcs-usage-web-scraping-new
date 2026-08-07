def Ambrose():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    
    # Input the URL for the main website here
    vendorURL = 'https://www.ambrosevideo.com/log-in'
    
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
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    except:
        raise ReferenceError('Login page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
        
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="jm-maincontent"]/div[1]/form/fieldset/div[3]/div/button').click()
    
    
    
    # Click on the Usage Statistics Button on the left side of the screen
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="jm-maincontent"]/div[1]/div[1]/ul/li[4]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="jm-maincontent"]/div[1]/div[1]/ul/li[4]/a').click()
    except:
        raise TimeoutError('Usage statistics button not found. Check the login information and fix if necessary. If it is correct, then update the XPATH in the code.')
    
    # Click on the Request Selected Statistics button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btn-confirm"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="btn-confirm"]').click()
    except:
        raise ReferenceError('Request Selected Statistics button could not be found. Update the XPATH in the code, then try again.')
    

    # The pop-up that appears must be manually clicked on to work.
    print('Click on the Request Reports button to finish downloading.')
    print('')
    print('')
    keyword = input('When you are finished, type anything here to close the browser.')

    driver.close()

def Ambrose_Info():
    print('No Inputs Needed.')
    print('The Request Reports button that appears after the code runs must be clicked manually to download reports.')