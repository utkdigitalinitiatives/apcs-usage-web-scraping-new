def Intelex():
    # Intelex Past Masters
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    
    # Input the URL for the main website here
    vendorURL = 'http://www.nlx.com/customer'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sushi_customer_id"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="sushi_customer_id"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="sushi_requestor_id"]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/form/input[4]').click()
    except:
        raise ReferenceError('Login page not found. Check the URL; if correct, then update the XPATH.')
    
    
    # Go to the Web Stats
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="masthead-navbar-cs"]/li[2]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="masthead-navbar-cs"]/li[2]/a').click()
    except:
        raise ReferenceError('Web stats tab not found. Double-check the login information. If correct, then update the XPATH.')
    
    
    # Then go to the COUNTER webpage
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div[2]/ul/li[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/ul/li[1]/a').click()
    except:
        raise ReferenceError('COUNTER Webpage not found. Update the XPATH.')
    
    
    # Then export to CSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div[2]/p[2]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/p[2]/a').click()
    except:
        raise ReferenceError('CSV export button not found. Update the XPATH.')

    keyword = input('When the report appears in Downloads, type anything here to close the browser.')


    driver.close()

    
def Intelex_Info():
    print('No input keys or manual steps needed.')