def Columbia():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass



    # Input the URL for the main website here
    vendorURL = 'http://www.columbiaonlineadmin.org/'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/form/input[3]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/form/input[3]').send_keys(username)
        driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/form/input[4]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/table[2]/tbody/tr/td[2]/form/input[5]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    
    # Go to the Searches and Sessions By Month Report
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/table[2]/tbody/tr[2]/td[1]/table[1]/tbody/tr/td/ul/li[2]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td[1]/table[1]/tbody/tr/td/ul/li[2]/a').click()
    except:
        raise ReferenceError('Searches and Sessions By Month tab not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')


    print('Fill out the start and end date in their respective boxes on the page that appears. The code will resume soon.')
    time.sleep(15)


    # Click the Filter Button
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/div[2]/table[2]/tbody/tr[4]/td/table/tbody/tr/td[6]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/div[2]/table[2]/tbody/tr[4]/td/table/tbody/tr/td[6]/input').click()
    except:
        raise ReferenceError('Filter button not found. Update the XPATH.')


    # Click the Export Report Button
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/div[2]/table[2]/tbody/tr[3]/td/table/tbody/tr/td[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[2]/td/div[2]/table[2]/tbody/tr[3]/td/table/tbody/tr/td[2]').click()
    except:
        raise ReferenceError('Export report button not found. Update the XPATH.')


    keyword = input('When the usage file finishes downloading, type any key to close the window.')

    driver.close()

def Columbia_Info():
    print('No keys needed.')
    print('')
    print('The start date and end date both need to be selected manually.')
    


