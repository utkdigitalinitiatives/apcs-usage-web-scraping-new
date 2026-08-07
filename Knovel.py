def Knovel():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # Knovel
    
    # Input the URL for the main website here
    vendorURL = 'https://commander.knovel.com/login'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="login-username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')


    #print('The eserials@utk.edu email contains a two-factor authentication code that will need to be typed in. The code will automatically continue in 30 seconds.')
    #time.sleep(10)

    # Go to Administration
    #try:
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar_accordion"]/li/a'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '//*[@id="sidebar_accordion"]/li/a').click()
    #except:
    #    raise ReferenceError('Administration button not found. Double-check the login information; if it is correct, then update the XPATH in the code.')

    #time.sleep(3)
    # Then Reports
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar_accordion"]/li/ul/li[3]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="sidebar_accordion"]/li/ul/li[3]').click()
    except:
        raise ReferenceError('Reports button not found. Update the XPATH.')

    time.sleep(3)
    # Then View
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar_accordion"]/li/ul/li[3]/div/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="sidebar_accordion"]/li/ul/li[3]/div/a[1]').click()
    except:
        raise ReferenceError('View Reports button not found. Update the XPATH.')
    
    
    # Download Reports
    
    ## Each report has its own download button on this page. 
    
    ### Comment out any reports below that should not be downloaded.
    
    
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inner_sel_customer_monthlyactivityreport_xls"]/a'))) #To ensure the webpage loads before trying
    
    try:
        # Montly Activity Report
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_monthlyactivityreport_xls"]/a').click()
        
        # Montly Usage Report
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_monthlyusagereport_xls"]/a').click()
        
        # Counter 4: Record Views (DB1)
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_counterdb1recordviews_xls"]/a').click()
        
        # Counter 4: Turnaways (DB2)
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_counterdb2turnaways_xls"]/a').click()
        
        # Counter 5: Search and Item Usage (DR_D1)
        driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_counterdrd1searchanditemusage_xls"]/a').click()
        
        # Counter 5: Database Access Denied (DR_D2)
       # driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_counterdrd2databaseaccessdenied_xls"]/a').click()
        
        # Counter 4: Total Searches (PR1)
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_counterpr1totalsearches_xls"]/a').click()
        
        # Counter 5: Platform Usage (PR_P1)
        driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_counterprp1platformusage_xls"]/a').click()
        
        # Pending Content Removals
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_pendingcontentremovals_xls"]/a').click()
        
        # My Subscription New Resources
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_mysubscriptionnewresources_xls"]/a').click()
        
        # Corrosion Activity Report
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_corrosionactivityreport_xls"]/a').click()
        
        # Monthly Activity Report Aggregated
        #driver.find_element(By.XPATH, '//*[@id="inner_sel_customer_monthlyactivityreportaggregated_xls"]/a').click()
    except:
        raise ReferenceError('At least one report was not found. Double-check the report XPATH.')
    
    
    
    keyword = input('When the files finish downloading, type any key.')

    driver.close()

def Knovel_Info():
    print('No input keys needed.')
    print('')
    print('Knovel offers several COUNTER and non-COUNTER reports. Each will need to be commented in or out in the underlying code depending on which ones you want to download.')
    print('Report Types:')
    print('Monthly Activity (NC), Monthly Usage (NC), DB1, DB2, DR_D1, DR_D2, PR1, PR_P1')
    print('These reports will automatically contain the last 12 months usage from the current month.')