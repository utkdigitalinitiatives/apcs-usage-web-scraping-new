def MEMSO(reportYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Medieval and Early Modern Sources Online (MEMSO)

    # Input the URL for the main website here
    vendorURL = 'https://tannerritchie.com/stats/'

    yearPattern = re.compile('[0-9][0-9][0-9][0-9]')

    if yearPattern.fullmatch(str(reportYear)) == None:
        raise SyntaxError('Year must be in YYYY format.')
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/form/table/tbody/tr[1]/td[2]/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[1]/div/form/table/tbody/tr[1]/td[2]/input').send_keys(username)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/form/table/tbody/tr[2]/td[2]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="plain"]/form/table/tbody/tr[3]/td/input').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    
    
    
    
    webpagePaths = ['//*[@id="plain"]/ul[2]/li[2]/a', '//*[@id="plain"]/ul[2]/li[3]/a', '//*[@id="plain"]/ul[2]/li[4]/a', '//*[@id="plain"]/ul[2]/li[5]/a']
    
    for path in webpagePaths:
        try:
            # Go to Statistics Home
            driver.get('https://tannerritchie.com/stats/institution.php?i=29')
        
            
            # Go to the report webpage
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, path))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, path).click()
            
            
            # Change the Year
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yearSelector"]'))) #The webpage buffers for a second after making the Report Type decision
            select = Select(driver.find_element(By.XPATH, '//*[@id="yearSelector"]'))
            select.select_by_visible_text(str(reportYear))  # Years in YYYY format, or can click All years
            
            
            # Download to CSV
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yearSelectorForm"]/button'))) #To ensure the webpage loads before trying
            driver.find_element(By.XPATH, '//*[@id="yearSelectorForm"]/button').click()
    
            print('Report Downloaded. Please wait...')
            time.sleep(3)
        except:
            raise ReferenceError('A report has failed to download. Double-check the XPATHs for both the webpages and their individual parts.')
        
    keyword = input('All reports have downloaded. Type anything here to close the browser.')


    driver.close()


def MEMSO_Info():
    print('Input keys needed:')
    print('Year - YYYY format. The report will download all data for this year.')
    print('')
    print('This code will download multiple reports into separate CSVs. The exit input will only appear once all reports have been downloaded.')