def AllAfrica(dateTextString):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import math
    import getpass 
    
    vendorURL = 'https://allafrica.com/commerce/user/manage/'

    datePattern = re.compile('[0-9][0-9][0-9][0-9]-[0-9][0-9] to [0-9][0-9][0-9][0-9]-[0-9][0-9]')

    if datePattern.fullmatch(dateTextString) == None:
        raise SyntaxError('Date string must be in the following format: YYYY-MM to YYYY-MM')


    dateStartYear = int(dateTextString[0:4])
    dateEndYear = int(dateTextString[11:15])
    dateStartMonth = int(dateTextString[5:7])
    dateEndMonth = int(dateTextString[16:18])

    monthRange = 1 + 12*(dateEndYear - dateStartYear) + (dateEndMonth - dateStartMonth)

    ## Store the vendor's username and password here
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    # Log into the website
    driver.get(vendorURL)
    
    
    # Input the username and password, then log in

    try:
        driver.find_element(By.XPATH, '//*[@id="login_username"]').send_keys(username)
    except:
        raise ReferenceError('Login page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
        
    driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div/div[1]/form/fieldset/ul/li[3]/input').click()
    
    # Click on the IP access Button on the left side of the screen
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div[1]/div[4]/ul/li/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[1]/div[4]/ul/li/a').click()
    except:
        raise TimeoutError('IP Access page not found. Check the login information and update if necessary. If the login is correct, then update the XPATH in the code.')
    
    # Input dates in the Period box
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="date-range-picker"]'))) #This step is a pop-up after the last one, so it appears before being clickable
        driver.find_element(By.XPATH, '//*[@id="date-range-picker"]').clear() #Remove pre-input date range
        driver.find_element(By.XPATH, '//*[@id="date-range-picker"]').send_keys(dateTextString)
    except:
        raise ReferenceError('Date box not found. Update the XPATH in the code.')
    
    # Display reports
    try:
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/button[1]').click()
    except:
        raise ReferenceError('Display button can not be found. Update the XPATH in the code.')


    
    # Web Scrape the Tables

    try:
        table_XPath = '/html/body/div[4]/div/div[2]/div[3]/div[2]/table/tbody/'
        
        num_rows = 5
        ##The number of rows should remain consistently at 5 as long as the report is still a COUNTER 4 styled report.
        
        num_cols = 5 + monthRange
        ##The first five columns are identifier columns, while everything after that is a month of usage.
        
        
        table = []
        for row in range(1, num_rows + 1): ##The end of the range should be the number of rows, plus 1 due to Python formatting.

            row_data = []
            if row == 1:
                for col in range(1, num_cols + 1): #Adding 1 due to Python syntax
                    text = driver.find_element(by='xpath', value=table_XPath + 'tr[' + str(row) + ']/th[' + str(col) + ']').text
                    row_data.append(text)
                table.append(row_data)
            else:
                for col in range(1, num_cols + 1): #Adding 1 due to Python syntax
                    text = driver.find_element(by='xpath', value=table_XPath + 'tr[' + str(row) + ']/td[' + str(col) + ']').text
                    row_data.append(text)
                table.append(row_data)
            
        df = pd.DataFrame(table)
    except:
        raise ReferenceError('Usage data not found. Update the table web-scraping code.')

    
    
    df.to_excel('AllAfrica-DB.xlsx', index = False)

    keyword = input('When the Excel file appears in the Python function list, type anything here to close the browser.')
    
    
    driver.close()

def AllAfrica_Info():
    print('Keys Needed:')
    print('dateTextString: YYYY-MM to YYYY-MM (must match exactly)')
    print('')
    print('The report will appear as an Excel file in the same folder as where you are running the Loading Usage Web Scraping Files code from.')