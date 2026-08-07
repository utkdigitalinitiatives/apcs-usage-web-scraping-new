def ExactEditions():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    
    vendorURL = 'https://login.exacteditions.com/login'

    ## Store the vendor's username and password here
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    # Log into the website
    driver.get(vendorURL)
    
    # Click on the username button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="show-username"]')))
        driver.find_element(By.XPATH, '//*[@id="show-username"]').click()
    except:
        raise ReferenceError('username button not found. Update the XPATH.')

        
    # Input the username and password, then log in

    try:
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
    except:
        raise ReferenceError('Login page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
        
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login-ee"]/div/div[2]/div/div[2]/section/form[1]/div[5]/div[2]/button').click()
    
    # Go to the Account tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]').click()
    except:
        raise TimeoutError('Account tab not found. Check the login information and update if necessary. If the login is correct, then update the XPATH in the code.')

    # Then select Account
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[2]/ul/li[1]/a').click()
    except:
        raise TimeoutError('Account button not found. Update the XPATH in the code.')


    # Choose the Usage Statistics button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="preferences"]/div[2]/div[2]/ul[1]/li[3]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="preferences"]/div[2]/div[2]/ul[1]/li[3]/a').click()
    except:
        raise TimeoutError('Usage Statistics button not found. Update the XPATH in the code.')    


    # View the Page Views Details
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="stats"]/div[2]/div/h4/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="stats"]/div[2]/div/h4/a[1]').click()
    except:
        raise TimeoutError('Top Page Views Details button not found. Update the XPATH in the code.')   

    
    # Web Scrape the Table
    try:
        table_XPath = '//*[@id="stats"]/div[3]/div/table/tbody/'
        num_rows = len(driver.find_elements(by='xpath', value=table_XPath + 'tr')) + 1
        num_cols = len(driver.find_elements(by='xpath', value=table_XPath + 'tr[1]/td')) + 1
        
        table = []
        for row in range(1, num_rows):
                row_data = []
                for col in range(1, num_cols):
                    text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row}]/td[{col}]').text
                    row_data.append(text)
                table.append(row_data)
            
        df = pd.DataFrame(table)
        
        
        # Clean up the scraped table
        df = df.rename(columns = {0: 'Jan', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May', 5: 'Jun', 6: 'Jul', 7: 'Aug', 8: 'Sep', 9: 'Oct', 10: 'Nov', 11: 'Dec'})
        
        
        # Export to a TSV file
        df.to_csv('ExactEditions-DB.tsv', sep = '\t', index = False)
    except:
        raise ReferenceError('Statistics file not exported. Double-check the XPATH and table format.')
    

    keyword = input('Once the TSV appears in the Python list, input anything here to close the browser.')

    driver.close()


def ExactEditions_Info():
    print('No keys needed.')
    print('The report will download as a TSV appearing in the Jupyter Notebook List to the left of the screen.')