def Gale(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass


    datePattern = re.compile('[0-9][0-9][0-9][0-9]-[0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start date string must be in the following format: YYYY-MM')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End date string must be in the following format: YYYY-MM')
    
    vendorURL = 'https://admin.gale.com/galeadmin/login.gale'

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
        driver.find_element(By.XPATH, '//*[@id="user"]').send_keys(username)
    except:
        raise ReferenceError('Login page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
        
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login"]').click()
    
    # Go to the knox61277 Tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="formHomePage:results:0:viewEditLink"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="formHomePage:results:0:viewEditLink"]').click()
    except:
        raise TimeoutError('Account tab not found. Check the login information and update if necessary. If the login is correct, then update the XPATH in the code.')

    # Then go to the Reports tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="reports"]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="reports"]/a').click()
    except:
        raise TimeoutError('Reports button not found. Update the XPATH in the code.')


    # Then click View Usage Reports
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="reports:View_Usage_Reports"]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="reports:View_Usage_Reports"]/a').click()
    except:
        raise TimeoutError('View Usage Reports button not found. Update the XPATH in the code.')    

    # Move to the second tab

    vendorURL2 = 'https://admin.gale.com/galeadmin/login.gale?target=usageAuth&redirect_uri=https%3A//gale.siqcloud.online/auth/login/callback/gale-token&next=http%3A//gale.siqcloud.online/p/2/dashboard%3Forganization%3Dlocation%253Aknox61277%26begin_date%3D2025-03%26end_date%3D2025-03%26report_type%3DDashboard'
    driver.get(vendorURL2)


    # Input the username and password, then log in

    try:
        driver.find_element(By.XPATH, '//*[@id="user"]').send_keys(username)
    except:
        raise ReferenceError('Login page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
        
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login"]').click()


    print('Select the account whose reports you want from the dropdown in the top-right corner of the original page (do NOT use the second tab that appears). Account 61277 is chosen by default.')

    time.sleep(10)
    
    # Platform Report

    ## Click on the Counter Button
    try:
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-counter-master"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-counter-master"]').click()
    except:
        raise TimeoutError('Counter button not found. Update the XPATH in the code.')   


    ## Then the Platform Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[3]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[3]/div/a[1]').click()
    except:
        raise TimeoutError('Platform button not found. Update the XPATH in the code.') 


    ## Input the Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_begin_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').send_keys(startDate)
    except:
        raise TimeoutError('Start date not found. Update the XPATH in the code.') 


    ## Input the End Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').send_keys(endDate)
    except:
        raise TimeoutError('End date not found. Update the XPATH in the code.') 

    
    ## Run the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loadGridButton"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="loadGridButton"]').click()
    except:
        raise TimeoutError('Run Report button not found. Update the XPATH in the code.')       

    
    ## Download the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a').click()
    except:
        raise TimeoutError('Download button not found. Update the XPATH in the code.')  

    ## Choose CSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]').click()
    except:
        raise TimeoutError('CSV option not found. Update the XPATH in the code.') 

    print('Platform Report downloaded. Wait for next report...')
    time.sleep(3)


    # Database Report

    ## Click on the Counter Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-counter-master"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-counter-master"]').click()
    except:
        raise TimeoutError('Counter button not found. Update the XPATH in the code.')   


    ## Then the Platform Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[3]/div/a[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[3]/div/a[2]').click()
    except:
        raise TimeoutError('Database button not found. Update the XPATH in the code.') 


    ## Input the Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_begin_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').send_keys(startDate)
    except:
        raise TimeoutError('Start date not found. Update the XPATH in the code.') 


    ## Input the End Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').send_keys(endDate)
    except:
        raise TimeoutError('End date not found. Update the XPATH in the code.') 

    ## Run the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loadGridButton"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="loadGridButton"]').click()
    except:
        raise TimeoutError('Run Report button not found. Update the XPATH in the code.')       

    ## Download the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a').click()
    except:
        raise TimeoutError('Download button not found. Update the XPATH in the code.')   

    ## Choose CSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]').click()
    except:
        raise TimeoutError('CSV option not found. Update the XPATH in the code.')

    print('Database Report downloaded. Wait for next report...')
    time.sleep(3)

    # Title Report

    ## Click on the Counter Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-counter-master"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-counter-master"]').click()
    except:
        raise TimeoutError('Counter button not found. Update the XPATH in the code.')   


    ## Then the Platform Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[3]/div/a[3]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[3]/div/a[3]').click()
    except:
        raise TimeoutError('Title button not found. Update the XPATH in the code.') 


    ## Input the Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_begin_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').send_keys(startDate)
    except:
        raise TimeoutError('Start date not found. Update the XPATH in the code.') 


    ## Input the End Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').send_keys(endDate)
    except:
        raise TimeoutError('End date not found. Update the XPATH in the code.') 

    ## Random Click
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-form"]/div/div[10]'))) #To ensure the webpage loads before trying
    driver.find_element(By.XPATH, '//*[@id="counter-form"]/div/div[10]').click()


    ## Run the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loadGridButton"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="loadGridButton"]').click()
    except:
        raise TimeoutError('Run Report button not found. Update the XPATH in the code.')       

    ## Download the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a').click()
    except:
        raise TimeoutError('Download Report button not found. Update the XPATH in the code.')
    
    ## Choose CSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]').click()
    except:
        raise TimeoutError('CSV option not found. Update the XPATH in the code.')


    print('Title Report downloaded. Wait for next report...')
    time.sleep(3)

    
    # TR_B3 - Book Usage by Access Type

    ## Click on the Counter Standard Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-counter-standard"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-counter-standard"]').click()
    except:
        raise TimeoutError('Counter Standard button not found. Update the XPATH in the code.')   


    ## Then the Title Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-title"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-title"]').click()
    except:
        raise TimeoutError('Title button not found. Update the XPATH in the code.') 


    ## Then the TR_B3 Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[4]/div/div[3]/div/a[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[4]/div/div[3]/div/a[2]').click()
    except:
        raise TimeoutError('TR_B3 button not found. Update the XPATH in the code.') 


    ## Input the Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_begin_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').send_keys(startDate)
    except:
        raise TimeoutError('Start date not found. Update the XPATH in the code.') 


    ## Input the End Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').send_keys(endDate)
    except:
        raise TimeoutError('End date not found. Update the XPATH in the code.') 

    ## Run the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loadGridButton"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="loadGridButton"]').click()
    except:
        raise TimeoutError('Run Report button not found. Update the XPATH in the code.')       

    ## Download the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a').click()
    except:
        raise TimeoutError('Download button not found. Update the XPATH in the code.')   

    ## Choose CSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]').click()
    except:
        raise TimeoutError('CSV button not found. Update the XPATH in the code.')


    print('TR_B3 downloaded. Wait for next report...')
    time.sleep(3)

    # TR_J3 - Journal Usage by Access Type

    ## Click on the Counter Standard Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-counter-standard"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-counter-standard"]').click()
    except:
        raise TimeoutError('Counter Standard button not found. Update the XPATH in the code.')   


    ## Then the Title Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-title"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-title"]').click()
    except:
        raise TimeoutError('Title button not found. Update the XPATH in the code.') 


    ## Then the TR_J3 Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[4]/div/div[3]/div/a[4]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[4]/div/div[3]/div/a[4]').click()
    except:
        raise TimeoutError('TR_J3 button not found. Update the XPATH in the code.') 


    ## Input the Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_begin_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').send_keys(startDate)
    except:
        raise TimeoutError('Start date not found. Update the XPATH in the code.') 


    ## Input the End Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').send_keys(endDate)
    except:
        raise TimeoutError('End date not found. Update the XPATH in the code.') 

    ## Run the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loadGridButton"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="loadGridButton"]').click()
    except:
        raise TimeoutError('Run Report button not found. Update the XPATH in the code.')       

    ## Download the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a').click()
    except:
        raise TimeoutError('Download button not found. Update the XPATH in the code.')   

    ## Choose CSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]').click()
    except:
        raise TimeoutError('CSV option not found. Update the XPATH in the code.')


    print('TR_J3 downloaded. Wait for next report...')
    time.sleep(3)


    # DR_D1 - Database Search and Item Usage

    ## Click on the Counter Standard Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-counter-standard"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-counter-standard"]').click()
    except:
        raise TimeoutError('Counter Standard button not found. Update the XPATH in the code.')   


    ## Then the Database Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-database"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-database"]').click()
    except:
        raise TimeoutError('Database button not found. Update the XPATH in the code.') 


    ## Then the DR_D1 Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[4]/div/div[2]/div/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="topnav-menu-content"]/ul/li[4]/div/div[2]/div/a').click()
    except:
        raise TimeoutError('DR_D1 button not found. Update the XPATH in the code.') 


    ## Input the Start Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_begin_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_begin_date"]').send_keys(startDate)
    except:
        raise TimeoutError('Start date not found. Update the XPATH in the code.') 


    ## Input the End Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_date"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').clear()
        driver.find_element(By.XPATH, '//*[@id="id_end_date"]').send_keys(endDate)
    except:
        raise TimeoutError('End date not found. Update the XPATH in the code.') 

    ## Run the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loadGridButton"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="loadGridButton"]').click()
    except:
        raise TimeoutError('Run Report button not found. Update the XPATH in the code.')       

    ## Download the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/a').click()
    except:
        raise TimeoutError('Download button not found. Update the XPATH in the code.')   

    ## Choose CSV
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-right-panel"]/div/div[1]/div[1]/div/a[1]').click()
    except:
        raise TimeoutError('CSV option not found. Update the XPATH in the code.')


    keyword = input('All reports downloaded. Input anything here to close the browser.')

    if keyword != '':
        driver.close()

def Gale_Info():
    print('Keys Needed:')
    print('startDate: YYYY-MM format.')
    print('endDate: YYYY-MM format.')
    print('')
    print('The code downloads the following reports: PR, DR, TR, TR_B3, TR_J3, DR_D1.')
    print('This code will work for either account. The account must be chosen manually.')
    print('NOTE: This page will automatically open a second tab. All usage is on the FIRST tab that appears, even after this second tab opens.')