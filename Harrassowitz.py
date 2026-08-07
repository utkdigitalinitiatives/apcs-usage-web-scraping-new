def Harrassowitz():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Harrassowitz
    
    # Input the URL for the main website here
    vendorURL = 'https://www.harrassowitz-library.com/'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    
    # Go to the Login Tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginBox"]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="loginBox"]/a').click()
    except:
        raise ReferenceError('Login tab not found. Update the XPATH.')
    
    # Manually Login
    
    
    print('Log into the website using these credentials:')
    print('Email: eserials@utk.edu')
    print('Password: admin205')
    time.sleep(10)
    
    #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="quotusModalLogin"]/div/div/div[2]/form/div[1]/input'))) #To ensure the webpage loads before trying
    #driver.find_element(By.XPATH, '//*[@id="quotusModalLogin"]/div/div/div[2]/form/div[1]').send_keys(username)
    #driver.find_element(By.XPATH, '//*[@id="quotusModalLogin"]/div/div/div[2]/form/div[2]').send_keys(password)
    #driver.find_element(By.XPATH, '//*[@id="quotusModalLogin"]/div/div/div[2]/form/button').click()
    
    
    # Go to the Admin tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="primaryNavigation"]/div/div/div/nav/ul/li[6]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="primaryNavigation"]/div/div/div/nav/ul/li[6]/a').click()
    except:
        raise ReferenceError('Admin tab could not be found. If you get this message after logging in, update the XPATH.') 
  
    
    
    print('Input the year, then download the TSV files manually.')
    print('')
    print('')
    keyword = input('When you are finished, type anything here to close the browser.')    


    driver.close()

    
def Harrassowitz_Info():
    print('No input keys needed.')
    print('')
    print('Logging in must be done manually. The code will pause for 10 seconds to give time to log in.')
    print('After the code finishes running, choose Hodges Library. Select a year from the dropdown, then download the TSV files (JR1 and JR5 available).')