def WBEncyc(startMonth):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # World Book Encyclopedia

    # Input the URL for the main website here
    vendorURL = 'https://www.worldbookonline.com/myaccount/home?tu=/myaccount/login'
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    
    # Log into the website
    driver.get(vendorURL)
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="default"]/div[4]/div[1]/div[1]/div/form/table/tbody/tr[1]/td[2]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="default"]/div[4]/div[1]/div[1]/div/form/table/tbody/tr[1]/td[2]/input').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="default"]/div[4]/div[1]/div[1]/div/form/div/input').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Go to Usage
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/ul/li[9]/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div/div[3]/ul/li[9]/a').click()
    except:
        raise ReferenceError('Usage page not found. Double-check the login information; if it is correct, then update the XPATH.')
  
    
    # Select the Start Month
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="availableMonths"]'))) #This time, no need to wait for a buffer period
        select = Select(driver.find_element(By.XPATH, '//*[@id="availableMonths"]'))
        select.select_by_visible_text(startMonth) #Full month names, comma, space, YYYY
    except:
        print('Start month not found. Check to see if the start month is in the following format:')
        print('Full month name, comma, space, YYYY.')
        raise ReferenceError('Update the start month format if your input start month does not match this format. If the start month is in the proper format, Update the XPATH.')

    ## Save as a CSV
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="interior"]/div[4]/div[2]/table/tbody/tr[1]/td/button[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="interior"]/div[4]/div[2]/table/tbody/tr[1]/td/button[1]').click()        
    except:
        raise TimeoutError('Save As button not found. Update the XPATH in the code.') 


    ## Choose the CSV
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="usageDownloadPopup"]/input[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="usageDownloadPopup"]/input[2]').click()      
    except:
        raise TimeoutError('CSV button not found. Update the XPATH in the code.') 


    ## Download Report
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="usageDownloadButton"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="usageDownloadButton"]').click()        
    except:
        raise TimeoutError('Download button not found. Update the XPATH in the code.') 

     

        
    keyword = input('Once the report appears in Downloads, type anything here to close the browser.')

    driver.close()


def WBEncyc_Info():
    print('Input keys needed:')
    print('Start month: full month name, comma, space, YYYY format. Example: January, 2024')
    print('')
    print('Usage will always download usage for the month before, the month of, and the year after the start month provided. Start months can go back as far as January 2018.')