def Covidence():
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
    # Merative CareNotes
    
    # Input the URL for the main website here
    vendorURL = 'https://app.covidence.org/reviews/active'

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/form/div[3]/input'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="session_email"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="session_password"]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/form/div[3]/input').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')        



    print('Click on the JH button in the top right corner, then click on University of Tennessee at Knoxville. The code will continue shortly.')
    time.sleep(10)



    # Go to the Research Insights Dashboard
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/section/div[2]/div/button'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/section/div[2]/div/button').click()
    except:
        raise ReferenceError('Research Insights dashboard button not found. Update the XPATH.')


    print('Record the Reviews Created Over Time in the NonCounter Usage Update or on a separate Excel file, split up by month. Scrolling over each bar will show the raw count.')

    keyword = input('When you are done, type anything here to close the browser.')

    driver.close()


def Covidence_Info():
    print('No keys needed.')
    print('')
    print('The admin profile page will need to be accessed manually after logging in.')
    print('The usage will need to be recorded into Excel separately, as Covidence only offers usage in charts instead of raw tables. This usage will appear on a second tab.')
    print('')
    print('Only the last 12 months of usage are available at any time.')