def Minerva():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Minerva Medica

    # Input the URL for the main website here
    vendorURL = 'https://www.minervamedica.it/en/login.php?mode=1222'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Click the Try Again button to get past cookie check
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Content"]/p[2]/a/span/span'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="Content"]/p[2]/a/span/span').click()
    except:
        raise ReferenceError('Cookie popup not found. If one did not appear, comment out this chunk of code. Otherwise, update the XPATH.')
    
    # Go to the Corporate Account tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mybutton3"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mybutton3"]').click()
    except:
        raise ReferenceError('Corporate Account tab not found. Update the XPATH.')
    
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form2"]/input[3]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="form2"]/input[1]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="pwd2"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="form2"]/input[3]').click()
    except:
        raise ReferenceError('Login page not found. Update the XPATH.')
    
    
    # Go to the Subscription Department page by manually clicking on it
    print('Click on the "Contact Subscription Department" button under "YOUR SUBSCRIPTIONS". The code will continue running shortly.')
    time.sleep(10) # Allows time to click the button
    
    # Then the usage statistics page
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Content"]/p[7]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="Content"]/p[7]/a').click()
    except:
        raise ReferenceError('Usage statistics page not found. If the timer is too short, increase the time in the underlying code.')
        
    
    # Then the Global Statistics page
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="Content"]/p[21]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="Content"]/p[21]/a').click()
    except:
        raise ReferenceError('Global Statistics page not found. Update the XPATH.')
    

    # Web Scrape the Table
    try:
        table_XPath = '//*[@id="Content"]/table[2]/tbody/'
        num_rows = len(driver.find_elements(by='xpath', value=table_XPath + 'tr')) + 1
        num_cols = len(driver.find_elements(by='xpath', value=table_XPath + 'tr[3]/td')) + 1
        
        table = []
        for row in range(3, num_rows, 2):
                row_data = []
                for col in range(1, num_cols):
                    text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row}]/td[{col}]').text
                    row_data.append(text)
                table.append(row_data)
            
        df = pd.DataFrame(table)
        
        
        # Clean up the scraped table
        df = df.rename(columns = {0: 'Year', 1: 'Sessions', 2: 'Pageviews'})
        
        
        # Export to a TSV file
        df.to_csv('Minerva-DB.tsv', sep = '\t', index = False)
    except:
        raise ReferenceError('Statistics file not exported. Double-check the XPATH and table format.')

    keyword = input('When the TSV appears in the folder, type anything here to close the browser.')

    driver.close()

def Minerva_Info():
    print('No input keys needed.')
    print('')
    print('In the middle of running the code, the Subscription Department page will need to be manually clicked on.')