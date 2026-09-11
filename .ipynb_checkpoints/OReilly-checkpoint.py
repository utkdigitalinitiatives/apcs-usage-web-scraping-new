def OReilly(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    # O'Reilly for Higher Education

    if startYear < 2025:
        raise ValueError('Usage is only available from January 2025 onwards.')
        
    if endYear < startYear:
        raise ValueError('The usage can not end later than its starting month.')


    match startMonth:
        case 'Jan':
            startMonthString = 1
        case 'Feb':
            startMonthString = 2
        case 'Mar':
            startMonthString = 3
        case 'Apr':
            startMonthString = 4
        case 'May':
            startMonthString = 5
        case 'Jun':
            startMonthString = 6
        case 'Jul':
            startMonthString = 7
        case 'Aug':
            startMonthString = 8
        case 'Sep':
            startMonthString = 9
        case 'Oct':
            startMonthString = 10
        case 'Nov':
            startMonthString = 11
        case 'Dec':
            startMonthString = 12


    match endMonth:
        case 'Jan':
            endMonthString = 1
        case 'Feb':
            endMonthString = 2
        case 'Mar':
            endMonthString = 3
        case 'Apr':
            endMonthString = 4
        case 'May':
            endMonthString = 5
        case 'Jun':
            endMonthString = 6
        case 'Jul':
            endMonthString = 7
        case 'Aug':
            endMonthString = 8
        case 'Sep':
            endMonthString = 9
        case 'Oct':
            endMonthString = 10
        case 'Nov':
            endMonthString = 11
        case 'Dec':
            endMonthString = 12


    match str(startYear):
        case '2025':
            startYearString = 2
        case '2026':
            startYearString = 3

    match str(endYear):
        case '2025':
            endYearString = 2
        case '2026':
            endYearString = 3
            
    
    # Input the URL for the main website here
    vendorURL = 'https://learning.oreilly.com/home/'

    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()


    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)

    
    # Input the username

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="main"]/div/section/div/form/button').click()
    except:
        raise ReferenceError('Username page not found. Double-check the URL; if it is correct, then update the XPATH in the code.')   



    # Then the password

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="main"]/div/section/section/section/div/form/div[3]/button').click()
    except:
        raise ReferenceError('Password page not found. Update the XPATH in the code.')   


    print('Make sure the page is in full screen before continuing.')
    time.sleep(7)
    
    
    # Go to the Admin button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="orm-global-site-header"]/div/div[3]/nav/ul/li[1]/button'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="orm-global-site-header"]/div/div[3]/nav/ul/li[1]/button').click()
    except:
        raise ReferenceError('Admin button not found. Was the browser in full screen? If so, update the XPATH in the code.')


    # Then Click Insights
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="popover-admin"]/ul/li[1]/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="popover-admin"]/ul/li[1]/a').click()
    except:
        raise ReferenceError('Insights button not found. Update the XPATH in the code.')    


    # Open the dropdown for the Activity Trends Time Period
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="insights-panel"]/section[2]/div[1]/div[2]/div/div[1]/div'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="insights-panel"]/section[2]/div[1]/div[2]/div/div[1]/div').click()
    except:
        raise ReferenceError('Time Period dropdown for the Activity Trend section of usage not found. Update the XPATH in the code.')   


    # Choose Custom Range
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="_r_1q_"]/li[4]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="_r_1q_"]/li[4]').click()
    except:
        raise ReferenceError('Custom Range selection not found. Update the XPATH in the code.')  


    # Select Start Month
    startMonthXPath = r'//*[@id="insights-panel"]/section[2]/div[1]/div[2]/div/div[3]/div['+startYearString+']/ul/li['+startMonthString+']'
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, startMonthXPath))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, startMonthXPath).click()
    except:
        raise ReferenceError('Selected start month not found. Update the XPATH in the code.')  

    
    # Select End Month
    endMonthXPath = r'//*[@id="insights-panel"]/section[2]/div[1]/div[2]/div/div[3]/div['+endYearString+']/ul/li['+endMonthString+']'
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, endMonthXPath))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, endMonthXPath).click()
    except:
        raise ReferenceError('Selected end month not found. Update the XPATH in the code.') 


    # Click Apply
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="insights-panel"]/section[2]/div[1]/div[2]/div/div[3]/div[4]/button[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="insights-panel"]/section[2]/div[1]/div[2]/div/div[3]/div[4]/button[2]').click()
    except:
        raise ReferenceError('Apply button not found. Update the XPATH in the code.') 

    
    # Click the Download Button
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="insights-panel"]/section[2]/div[1]/div[2]/div/a'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="insights-panel"]/section[2]/div[1]/div[2]/div/a').click()
    except:
        raise ReferenceError('Download button not found. Update the XPATH in the code.') 
    

    keyword = input('When the download appears, type anything here to close the browser.')

    driver.close()


def OReilly_Info():
    print('Input keys needed:')
    print('Start month - First three letters of the month name only.')
    print('Start year - YYYY format.')
    print('End month - First three letters of the month name only.')
    print('End year - YYYY format.')







    