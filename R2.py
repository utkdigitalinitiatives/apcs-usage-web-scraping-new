def R2():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # R2 Digital Library

    keyword = input('WARNING: This code will only gather the entire 2026 year, not a specific date range. If a specific date range is needed, then interrupt the code. If all of 2026 is good, then type anything here to continue.')
    
    # Input the URL for the main website here
    vendorURL = 'https://www.r2library.com/'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-user"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="login-user"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="form0"]/div[2]/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    print('If a popup appears at this point, close it. If not, then wait a few seconds for the code to continue.')
    time.sleep(7)
    
    # Go to the Admin tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav-main"]/ul/li[5]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="nav-main"]/ul/li[5]/a').click()
    except:
        raise ReferenceError('Admin tab not found. Double-check the login information; if it is correct, then update the XPATH in the code.')
    
    
    # Then go to the COUNTER Reports
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[3]/div[2]/ul[4]/li[4]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="container"]/div[3]/div[2]/ul[4]/li[4]/a').click()
    except:
        raise ReferenceError('COUNTER Report tab not found. Update the XPATH.')
    
    # Each report is on its own page, and will need to be web-scraped individually.
    
    webpageXPATH = ['//*[@id="content"]/ul/li[1]/a', '//*[@id="content"]/ul/li[2]/a', '//*[@id="content"]/ul/li[3]/a']
    
    
    ## In order: Book Requests, Book Access Denied, Platform Usage
    
    
    # Gather the data:
        
    for webpage in webpageXPATH:

        driver.get('https://www.r2library.com/Admin/CounterReport/Index/3508?Period=Last30Days')

        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, webpage))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, webpage).click()
        except:
            raise ReferenceError('Webpage not found. Double-check the XPATH in the webpageXPATH list.')
        
        
        # Change the date range to 2024 entire year:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ReportQuery_Period"]'))) #To ensure the webpage loads before trying
            select = Select(driver.find_element(By.XPATH, '//*[@id="ReportQuery_Period"]'))
            select.select_by_visible_text('2026 entire year')
        except:
            raise ReferenceError('Date range not found. Make sure the year in the code is the current year; if it is, then update the XPATH.')

        print('Click the Run Report button. The code will continue shortly.')
        time.sleep(7)
        
        
        
        ## NOTE: If a specific date range is necessary, comment out the code below and manually set the dates. The calendar format on this webpage does not allow automatic month selection.
        #time.sleep(10) #To set the date range manually
        
        
        # Run the Report
        driver.find_element(By.XPATH, '//*[@id="report-filters"]/table/tbody/tr[3]/td[2]/button')
        
        
        # Web Scrape the Table
        try:
            table_XPath = '//*[@id="content"]/div[2]/table/tbody/'
            num_rows = len(driver.find_elements(by='xpath', value=table_XPath + 'tr')) + 1
            num_cols = len(driver.find_elements(by='xpath', value=table_XPath + 'tr[2]/td')) + 1
            
            table = []
            for row in range(1,num_rows):
                    row_data = []
                    for col in range(1, num_cols):
                        if row in range(4, num_rows, 2) and col == 1:
                            text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row - 1}]/td[{col}]').text
                        elif row in range(4, num_rows, 2) and col != 1:
                            text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row}]/td[{col - 1}]').text
                        else:
                            text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row}]/td[{col}]').text
                        row_data.append(text)
                    table.append(row_data)
                
            df = pd.DataFrame(table)
            
            # Clean up the scraped table
            df = df.rename(columns = {0: 'ISBN', 1: 'Total', 2: 'Metric_Type', 3: 'Reporting_Period_Total',
                                      4: 'Jan-2026', 5: 'Feb-2026', 6: 'Mar-2026', 7: 'Apr-2026', 8: 'May-2026', 9: 'Jun-2026', 10: 'Jul-2026', 11: 'Aug-2026', 12: 'Sep-2026', 13: 'Oct-2026', 14: 'Nov-2026', 15: 'Dec-2026'})
            
            # If there are more months or fewer months in the year as of the running of this code, add or remove columns from the list above. 
            ## All date columns follow the same format: first three letters of month, hyphen, YYYY.
            
            
            # Export to a TSV file
            if webpage == '//*[@id="content"]/ul/li[1]/a':
                df.to_csv('R2-BR1-Usage.tsv', sep = '\t', index = False)
            elif webpage == '//*[@id="content"]/ul/li[2]/a':
                df.to_csv('R2-BR2-Usage.tsv', sep = '\t', index = False)
            else:
                df.to_csv('R2-PR1-Usage.tsv', sep = '\t', index = False)
        
            time.sleep(2) #Time before moving to the next webpage
        
            if webpage == '//*[@id="content"]/ul/li[1]/a':
                print('Book Requests Done')
            elif webpage == '//*[@id="content"]/ul/li[2]/a':
                print('Book Access Denied Done')
            else:
                print('Platform Usage Done')
        except:
            raise ReferenceError('Report download failed. Double-check the XPATH for scraping the table.')

    keyword = input('All reports done. Type in anything here to close the browser.')


    driver.close()


def R2_Info():
    print('No input keys needed.')