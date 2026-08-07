def TheatreRecord():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Theatre Record
    
    # Input the URL for the main website here
    vendorURL = 'https://www.theatrerecord.com/login'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')

    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[1]/form/input[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/form/input[1]').send_keys(username)
        driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/form/input[2]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/form/input[3]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')

    
    # Go to the Account Dropdown

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="account"]').click()
    except:
        raise ReferenceError('Account button not found. Double-check the login information; if it is correct, then update the XPATH in the code.')


    # Then My Account

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account"]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="account"]/div/a[1]').click()
    except:
        raise ReferenceError('My Account option not found. Update the XPATH in the code.')

    time.sleep(7)

    # Web Scrape the Statistics:
    try:
        table_XPath = '/html/body/main/div/section/article/div[6]/table/tbody/'
        num_rows = len(driver.find_elements(by='xpath', value=table_XPath + 'tr')) + 1
        num_cols = len(driver.find_elements(by='xpath', value=table_XPath + 'tr[2]/td')) + 1
        
        table = []
        for row in range(2,num_rows):
                row_data = []
                for col in range(1, num_cols):
                    text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row}]/td[{col}]').text
                    row_data.append(text)
                table.append(row_data)
            
        df = pd.DataFrame(table)
        
        # Clean up the scraped table
        df = df.rename(columns = {0: 'Year', 1: 'Logins', 2: 'Issues Viewed'})
        
        # Export to a TSV file
        df.to_csv('TheatreRecord-DB.tsv', sep = '\t', index = False)

        keyword = input('When the TSV appears in the Python file list, type anything here to close the browser.')

        driver.close()
        
    except:
        raise ReferenceError('Report not downloaded. Double-check the table XPATH.')


def TheatreRecord_Info():
    print('No input keys needed.')