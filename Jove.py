def Jove():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    from datetime import date
    import getpass


    # Input the URL for the main website here
    vendorURL = 'https://app.jove.com/auth/signin'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="vector-layout_main"]/div[1]/div/div[1]/div/form/div[3]/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    # Go to My JoVE

    #time.sleep(5)
    
    #try:
    #    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/header/div[3]/div/div/div/span'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/header/div[3]/div/div/div/span').click()
    #except:
    #    raise ReferenceError('Admin button not found. Double-check the login information; if correct, update the XPATH.')

    print('Click the UT Libraries button, then click on the My JoVE button. The code will continue shortly.')
    time.sleep(12)


    #try:
    #    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/button[2]'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/button[2]').click()
    #except:
    #    raise ReferenceError('My JoVE link not found. Update the XPATH.')


    # Go to Counter & Usage Statistics
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="vector-layout_main"]/div[1]/div/div[3]/div[1]/div[2]/a[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="vector-layout_main"]/div[1]/div/div[3]/div[1]/div[2]/a[2]').click()
    except:
        raise ReferenceError('Usage statistics button not found. Update the XPATH.')



    print('COUNTER usage is stored in the Counter Reports tab on the webpage that just appeared. Manually download from there.')

    keyword = input('When you are done, type anything here to close the browser.')
        

    driver.close()
    

def Jove_Info():
    print('No keys needed.')
    print('')
    print('Accessing the admin page will need to be done manually.')
    print('Usage is stored in a second tab, which will open at the end of the code. After this tab opens, the rest must be done manually.')