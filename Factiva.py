def Factiva():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Factiva

    # Input the URL for the main website here
    vendorURL = 'http://global.factiva.com'
    
    
    
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
        driver.find_element(By.XPATH, '//*[@id="password-form-item"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="signin-btn"]').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')        
    
    # Go to the Usage Reports
    
    
    ## Click on the Gear
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dj_header-wrap"]/ul[2]/li/a')))
        driver.find_element(By.XPATH, '//*[@id="dj_header-wrap"]/ul[2]/li/a').click()
    except:
        raise ReferenceError('Options tab not found. Update the XPATH.')
    time.sleep(0.5) # To allow the dropdown options to appear\
    
    #then Click on Account
    try:
        driver.find_element(By.XPATH, '//*[@id="dj_header-wrap"]/ul[2]/li/div/ul/li[6]/a').click()
    except:
        raise ReferenceError('Account tab not found. Update the XPATH.')
    time.sleep(0.5) # Again allowing dropdown options to appear
    
    #then Click on Usage Reports
    try:
        driver.find_element(By.XPATH, '//*[@id="dj_header-wrap"]/ul[2]/li/div/ul/li[6]/ul/li[2]/a').click()
    except:
        raise ReferenceError('Usage Reports tab not found. Update the XPATH.')
    
    # Click the Support button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/a[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[1]/a[2]').click()
    except:
        raise ReferenceError('Support button not found. Update the XPATH.')


        
    
    # The rest must be done manually

    print('On the webpage that just appeared, go to the ADMINISTRATION button. Then, go to the View Reports button under the COUNTER 5 section. The reports can be downloaded from the link after this.')
    print('')
    print('')
    keyword = input('When you are finished downloading reports, type anything here to close the browser.')

    driver.close()


def Factiva_Info():
    print('No input keys needed.')
    print('')
    print('Once the code finishes running, all future steps to download the usage reports on the new page that appears must be done manually.')