def JazzDiscography():
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
    vendorURL = 'https://lordisco-com.utk.idm.oclc.org/tjd/CoverFrame'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)


    print('Access the website using your UTK login, including any two-factor authentication. The code will start after logging in.')
    time.sleep(25)

#    try:
#        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div/form/table/tbody/tr[1]/td[2]/input'))) #To ensure the webpage loads before trying
#        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/form/table/tbody/tr[1]/td[2]/input').send_keys(username)
#        driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(password)
#        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/form/table/tbody/tr[4]/td/input[1]').click()
#    except:
#        raise ReferenceError('Login webpage not found. If the code timed out before you were able to login, increase the timer. If the webpage never appeared, double-check the URL; if it is correct, then update the XPATH in the code.')


    # Go to My Preferences
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bottomButtons"]/a[1]/div'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="bottomButtons"]/a[1]/div').click()
    except:
        raise ReferenceError('My Preferences tab not found. If the URL did not load to the main page post-login, edit the URL or the code. Otherwise, update the XPATH.')

        
    # Input the password
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr/td/form/input[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/form/input[1]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/form/input[2]').click()
    except:
        raise ReferenceError('Login webpage not found. Update the XPATH in the code.')


    keyword = input('Usage by month is at the bottom of this page. Usage will need to be input into NonCounter_Usage_Compilation_Updated and saved manually. When you are done, type anything here to close the browser.')


    driver.close()

def JazzDiscography_Info():
    print('No keys needed.')
    print('')
    print('The website must be accessed via your UTK login, including any two-factor authentication.')
    print('After the code finishes running, usage will need to be saved and recorded manually.')