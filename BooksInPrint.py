def BooksInPrint():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass

    # Books In Print

    # Input the URL for the main website here
    vendorURL = 'https://www.booksinprint.com/'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)


    # Clear the Cookies
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-close-btn-container"]/button'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button').click()
    except:
        raise ReferenceError('Cookies pop-up not found. If one did not appear, remove this piece of the code. If the website did not appear, update the URL. Otherwise, update the XPATH.')

    
    # Go to the Administrator tab
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BipAccountLink"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="BipAccountLink"]').click()
    except:
        raise ReferenceError('Administrator tab not found. Update the XPATH.')

    #try:
    #    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="myAccountLink"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="myAccountLink"]').click()
    #except:
    #raise ReferenceError('Account Settings button not found. Update the XPATH.')

    # Log in
    #try:
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="adminUID"]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="adminUID"]').send_keys(username)
    #    driver.find_element(By.XPATH, '//*[@id="adminPWD"]').send_keys(password)
    #    driver.find_element(By.XPATH, '//*[@id="btnCheckAdminCredentials"]').click()
    #except:
    #    raise ReferenceError('Login pop-up not found. Update the XPATH in the code.')
    
    print('Log in using the Admin User Authentication pop-up and the username and password credentials stored on KeePass. The code will continue shortly.')
    time.sleep(25)

    
    # Go to the Monthly Usage Statistic Reports
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divContainer"]/div/div/a[1]/span'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="divContainer"]/div/div/a[1]/span').click()
    except:
        raise ReferenceError('Monthly Usage Statistic Reports button not found. Update the XPATH.')


    keyword = input("Each month's data is stored in a separate link on this tab and should be input into the NonCounter_Usage_Compilation_Updated report. When you are done, type anything here to close the browser.")

    driver.close()

def BooksInPrint_Info():
    print('No keys needed.')
    print('')
    print('Logging in will need to be done manually.')
    print('Usage is stored in separate links for each month, and will need to be combined and recorded manually once the code finishes running.')