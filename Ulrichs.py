def Ulrichs():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Ulrich's
    
    # Input the URL for the main website here
    vendorURL = 'https://clientcenter.serialssolutions.com/CC/Login/Default.aspx'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="_login__login_UserName"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="_login__login_UserName"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="_login__login_Password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="_login__login_LoginButton"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Go to the Usage Statistics Website:
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_cphCCMain__ManagmentLinkview_dlHeader_ctl00_dlLinkViewItems_ctl01_dlLinks_ctl05_hlLink"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ctl00_cphCCMain__ManagmentLinkview_dlHeader_ctl00_dlLinkViewItems_ctl01_dlLinks_ctl05_hlLink"]').click()
    except:
        raise ReferenceError('Usage Statistics website not found. Double-check the login information; if it is correct, then update the XPATH.')

    
    # Then go to the Reports tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ReportLink"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="ReportLink"]').click()
    except:
        raise ReferenceError('Reports tab not found. Update the XPATH.')

    
    # Then the Total Searches tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="TotalSearchesHref"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="TotalSearchesHref"]').click()
    except:
        raise ReferenceError('Total Searches tab not found. Update the XPATH.')   
    
    
    
    # The report must be downloaded manually from here.
    
    print('The rest of the report must be downloaded manually.')

    keyword = input('When you are done, type anything here to close the browser.')

    driver.close()


def Ulrichs_Info():
    print('No input keys needed.')
    print('')
    print('Once the code stops running, all future steps must be done manually.')