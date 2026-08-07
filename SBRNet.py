def SBRNet():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Mergent Online:

    # Input the URL for the main website here
    vendorURL = 'https://libguides.utk.edu/databases/283'

    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    
    # Go to Usage Reporting
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/footer/div/div/div[1]/ul/li[8]/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="form"]/footer/div/div/div[1]/ul/li[8]/a').click()
    except:
        raise ReferenceError('Usage Reporting page not found. Double-check the login information; if it is correct, then update the XPATH.')
  
    
    ## Input the Password
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="p_lt_ctl04_pageplaceholder_p_lt_WebPartZone2_ZoneMain_LoginForm_viewBiz_LoginPassword_txtText"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="p_lt_ctl04_pageplaceholder_p_lt_WebPartZone2_ZoneMain_LoginForm_viewBiz_LoginPassword_txtText"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="p_lt_ctl04_pageplaceholder_p_lt_WebPartZone2_ZoneMain_LoginForm_viewBiz_btnOK"]').click()        
    except:
        raise TimeoutError('Password box not found. Update the XPATH in the code.') 



    print('Usage will need to be recorded and/or downloaded one month at a time. Downloads are done via right-clicking the table.')
        
    keyword = input('When you are done, type anything here to close the browser.')


    driver.close()


def SBRNet_Info():
    print('No input keys needed.')
    print('')
    print('The login needs a NetID to function, but will work without one only if run on campus or with a VPN.')
    print('All usage will need to be recorded one month at a time and downloaded in a six-month chunk, both manually.')