def PubMed():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # PubMed
    
    # Input the URL for the main website here
    vendorURL = 'https://www.ncbi.nlm.nih.gov/projects/linkout/libHld/login.cgi'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[2]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[2]/input').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[2]/td[2]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[3]/td/input[3]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Go to Usage Statistics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/p[2]/a[3]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="content"]/p[2]/a[3]').click()
    except:
        raise ReferenceError('Usage Statistics page not found. Double-check the login information; if it is correct, then update the XPATH.')
    
    
    # Change the Breakdown to Monthly

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tabcontent"]/form/p/select[1]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="tabcontent"]/form/p/select[1]'))
        select.select_by_visible_text('Monthly')
    except:
        raise ReferenceError('Breakdown dropdown not found. Update the XPATH.')
    
    # Update the Usage Data
    try:
        driver.find_element(By.XPATH, '//*[@id="tabcontent"]/form/p/input').click()
    except:
        raise ReferenceError('Update button not found. Update the XPATH.')
        
    time.sleep(2) 
    
    
    # Export to CSV
    try:
        driver.find_element(By.XPATH, '//*[@id="main-content"]/article/p/a[2]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')
        
    keyword = input('When you are finished, type anything here to close the browser.')


    driver.close()


def PubMed_Info():
    print('No input keys needed.')