def MGG():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    import pandas as pd
    import time
    import re
    import getpass
    # MGG Online


    # Input the URL for the main website here
    vendorURL = 'https://www.mgg-online.com/'

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)




    # Go to the Login page
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div[2]/div[1]/button[1]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[2]/div[1]/button[1]').click()
    except:
        raise ReferenceError('Login button not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')


    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="login-username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="modal-bg"]/div/footer/button[1]/span[2]').click()
    except:
        raise ReferenceError('Login page not found. Update the XPATH in the code.')   

        

    # Go to My Account
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div[2]/div[2]/div[1]/a[3]/span[2]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[2]/div[1]/a[3]/span[2]').click()
    except:
        raise ReferenceError('My Account button not found. Double-check the login information; if correct, increase the code wait timer or update the XPATH.')

    # Then Admin
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account-logged-in"]/nav/ul/li[6]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="account-logged-in"]/nav/ul/li[6]/a').click()
    except:
        raise ReferenceError('Admin button not found. Update the XPATH.')

    # Then Usage Statistics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inst-admin-subview"]/div/div[2]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="inst-admin-subview"]/div/div[2]/a').click()
    except:
        raise ReferenceError('Usage statistics button not found. Update the XPATH.')


    # Choose UT Knoxville
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lrfi-d94dbd23-13fb-4012-9944-60294128d6ff"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="lrfi-d94dbd23-13fb-4012-9944-60294128d6ff"]').click()
    except:
        raise ReferenceError('Usage statistics button not found. Update the XPATH.')


    # Select the DR_D1 TSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lrf-5/DR_D1/tsv"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="lrf-5/DR_D1/tsv"]').click()
    except:
        raise ReferenceError('DR_D1 button not found. Update the XPATH.')


    print('Input the date range you are looking for, then press download to get the usage report.')

    keyboard = input('When you are done, type anything here to close the browser.')


    driver.close()


def MGG_Info():
    print('No keys needed.')
    print('')
    print('After the code finishes, the dates will need to be input manually, then data will be downloaded manually.')
          



    