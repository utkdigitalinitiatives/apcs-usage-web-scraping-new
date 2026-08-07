def WRDS():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Mergent Online:

    # Input the URL for the main website here
    vendorURL = 'https://wrds-www.wharton.upenn.edu/'

    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    

    print("WARNING: This code function requires two-factor authentication via Alexander's phone. If Alexander is not running this code, you will need to let him know you are running this before doing so. Otherwise, the code will not work.")

    keyword = input('If Alexander is running this code, or if he is aware of this code being ran, input anything here to continue.')
    
    # Log into the website
    driver.get(vendorURL)
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_header_username"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_header_username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="id_header_password"]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/nav/div[1]/div[1]/div/div[2]/div/form/div/div[3]/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    

    print('Pausing for two-factor authentication...')

    time.sleep(15)
    
    
    # Go to WRDS REP TOOLS
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li/div/a[2]'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/nav/div[2]/div[1]/ul/li/div/a[2]').click()
    except:
        raise ReferenceError('WRDS REP TOOLS page not found. Double-check the login information; if it is correct, then update the XPATH.')
  
    
    ## Go to the Usage Report
    #try:
    #    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-body"]/div[2]/div/div[2]/section/section[2]/div/div[2]/div[1]/div/ul/li'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="main-body"]/div[2]/div/div[2]/section/section[2]/div/div[2]/div[1]/div/ul/li').click()        
    #except:
    #    raise TimeoutError('Usage report not found. Update the XPATH in the code.') 



    print('Scroll down to the WRDS Usage Report in the Reports and Analytics section. Click there to see usage.')
    print('Usage will need to be recorded and/or downloaded one month at a time.')
        
    keyword = input('When you are done, type anything here to close the browser.')

    driver.close()


def WRDS_Info():
    print('No input keys needed.')
    print('')
    print("The login uses two-factor authentication from Alexander's phone, so be prepared for this in advance of running this code.")
    print('The usage page will need to be clicked manually. From there, all usage will need to be recorded and/or downloaded manually, one month at a time.')