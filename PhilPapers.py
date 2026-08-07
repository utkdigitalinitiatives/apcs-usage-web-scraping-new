def PhilPapers():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    # PhilPapers

    # Input the URL for the main website here
    vendorURL = 'https://philpapers.org/institution/5790/?accessKey=aTYQyInClvntss9RNPre'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    
    # Log into the website
    driver.get(vendorURL)


    # Go to Usage statistics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentContainer"]/div[2]/span[6]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="contentContainer"]/div[2]/span[6]/a').click()
    except:
        raise ReferenceError('Usage statistics tab not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    # Export usage to Excel
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="contentContainer"]/div[3]/a[1]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="contentContainer"]/div[3]/a[1]').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH in the code.')


    print('All usage will be downloaded, so specific periods will need to be cleaned up in the downloaded Excel file.')

    keyboard = input('When the report appears in Downloads, type anything here to close the browser.')

    driver.close()


def PhilPapers_Info():
    print('No keys needed.')