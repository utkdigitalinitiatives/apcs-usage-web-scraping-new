def Kanopy(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Kanopy

    # Input the URL for the main website here
    vendorURL = 'https://www.kanopy.com/en/ut/login'

    datePattern = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Starting date must be in MM/DD/YYYY format.')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('Ending date must be in MM/DD/YYYY format.')

    startMonth = int(startDate[0:2])
    startDay = int(startDate[3:5])
    startYear = startDate[6:10]

    endMonth = int(endDate[0:2])
    endDay = int(endDate[3:5])
    endYear = endDate[6:10]


    match startMonth:
        case 1:
            endString = 'January'
        case 2:
            endString = 'February'
        case 3:
            endString = 'March'
        case 4:
            endString = 'April'
        case 5:
            endString = 'May'
        case 6:
            endString = 'June'
        case 7:
            endString = 'July'
        case 8:
            endString = 'August'
        case 9:
            endString = 'September'
        case 10:
            endString = 'October'
        case 11:
            endString = 'November'
        case 12:
            endString = 'December'
            
    match endMonth:
        case 1:
            endString2 = 'January'
        case 2:
            endString2 = 'February'
        case 3:
            endString2 = 'March'
        case 4:
            endString2 = 'April'
        case 5:
            endString2 = 'May'
        case 6:
            endString2 = 'June'
        case 7:
            endString2 = 'July'
        case 8:
            endString2 = 'August'
        case 9:
            endString2 = 'September'
        case 10:
            endString2 = 'October'
        case 11:
            endString2 = 'November'
        case 12:
            endString2 = 'December'
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[3]/form/div[1]/input'))) #To ensure the webpage loads before trying
        print('Close the privacy pop-up that appears on the screen.')
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="main-content"]/div[3]/form/div[1]/input').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="main-content"]/div[3]/form/div[2]/input').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="main-content"]/div[3]/form/button').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Go to Analytics
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/main/div[1]/ul/li[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[3]/main/div[1]/ul/li[2]').click()
    except:
        raise ReferenceError('Analytics link not found. Double-check the login information and update if necessary. If correct, update the XPATH in the code.')
    
    
    # Click on Videos
    try:
        WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-area"]/div/div/div[1]/div/div[1]/div/div/a[3]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="content-area"]/div/div/div[1]/div/div[1]/div/div/a[3]').click()
    except:
        raise ReferenceError('Videos button not found. Update the XPATH.')
    
    
    
    # Show All Entries
    try:
        WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="DataTables_Table_0_length"]/label/select'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0_length"]/label/select'))
        select.select_by_visible_text('All')
    except:
        raise ReferenceError('Entries dropdown not found. Update the XPATH.')
    
    
    # Set the Date Range
    
    try:
        driver.find_element(By.XPATH, '//*[@id="date_start"]').click()
    except:
        raise ReferenceError('Start Date range dropdown not found. Update the XPATH.')

    try:    
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="date_start_root"]/div/div/div/div/div[1]/select[1]'))) #To ensure the webpage loads before trying
    
    ## Start Date - Year

        select = Select(driver.find_element(By.XPATH, '//*[@id="date_start_root"]/div/div/div/div/div[1]/select[1]'))
        select.select_by_visible_text(startYear) #YYYY format
    except:
        raise ReferenceError('Unable to change start year. Update the XPATH for the year.')
    
    ## Start Date - Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="date_start_root"]/div/div/div/div/div[1]/select[2]'))
        select.select_by_visible_text(endString) #Full month format
    except:
        raise ReferenceError('Unable to change start month. Update the XPATH for the month.')
    ## Start Date - Day
    
    
    ######### WARNING ##############
    
    ## USING THIS FORMAT, THE EXACT DAY'S XPATH MUST BE LISTED BELOW
    
    
    # To change the date properly, find a seven-day calendar and find the location of the date on it. The row is the tr[] number, the column is the td[] number.
    ## Example: If the 1st of the month is on a Thursday, it would be in row 1, column 5. Then, the 30th would be row 5, column 6.
    ### Those numbers are the only thing that needs to change for this to work properly.


    #### THE FOLLOWING MUST BE UPDATED EACH YEAR WITH THE NEW CALENDAR ####

    rowStart = 1
    match startMonth:
        case 1:
            colStart = 5
        case 2:
            colStart = 1
        case 3:
            colStart = 1
        case 4:
            colStart = 4
        case 5:
            colStart = 6
        case 6:
            colStart = 2
        case 7:
            colStart = 4
        case 8:
            colStart = 7
        case 9:
            colStart = 3
        case 10:
            colStart = 5
        case 11:
            colStart = 1
        case 12:
            colStart = 3

    for i in range(1, startDay):
        if colStart == 7:
            colStart = 0
            rowStart += 1
        colStart += 1
        
    
    try:
        driver.find_element(By.XPATH, '//*[@id="date_start_table"]/tbody/tr['+str(rowStart)+']/td['+str(colStart)+']/div').click()
    except:
        raise ValueError('The date could not be found. Double-check the XPATH for the date input.')
    
    
    
    
    try:
        driver.find_element(By.XPATH, '//*[@id="date_end"]').click()
    except:
        raise ReferenceError('End Date range dropdown not found. Update the XPATH.')
    
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="date_end_root"]/div/div/div/div/div[1]/select[1]'))) #To ensure the webpage loads before trying
    
    
    ## End Date - Year
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="date_end_root"]/div/div/div/div/div[1]/select[1]'))
        select.select_by_visible_text(endYear) #YYYY format
    except:
        raise ReferenceError('Unable to change end year. Update the XPATH.')
    
    ## End Date - Month
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="date_end_root"]/div/div/div/div/div[1]/select[2]'))
        select.select_by_visible_text(endString2) #Full month format
    except:
        raise ReferenceError('Unable to change end month. Update the XPATH.')
    
    ## End Date - Day
    
    
    ######### WARNING ##############
    
    ## USING THIS FORMAT, THE EXACT DAY'S XPATH MUST BE LISTED BELOW
    
    # See above for finding correct answer.

    
    
    
    #### THE FOLLOWING MUST BE UPDATED EACH YEAR WITH THE NEW CALENDAR ####

    rowStart = 1
    match endMonth:
        case 1:
            colStart = 5
        case 2:
            colStart = 1
        case 3:
            colStart = 1
        case 4:
            colStart = 4
        case 5:
            colStart = 6
        case 6:
            colStart = 2
        case 7:
            colStart = 4
        case 8:
            colStart = 7
        case 9:
            colStart = 3
        case 10:
            colStart = 5
        case 11:
            colStart = 1
        case 12:
            colStart = 3

    for i in range(1, endDay):
        if colStart == 7:
            colStart = 0
            rowStart += 1
        colStart += 1

    try:
        driver.find_element(By.XPATH, '//*[@id="date_end_table"]/tbody/tr['+str(rowStart)+']/td['+str(colStart)+']/div').click()
    except:
        raise ValueError('The date could not be found. Double-check the XPATH for the date input.')
    
    
    # Export to Excel
    try:
        driver.find_element(By.XPATH, '//*[@id="DataTables_Table_0_wrapper"]/div[1]/label/a').click()
    except:
        raise ReferenceError('Export button not found. Update the XPATH.')

    keyword = input('When the report download finishes, type anything here to close the browser.')

    driver.close()


def Kanopy_Info():
    print('Input keys needed:')
    print('Start Date: MM/DD/YYYY format.')
    print('End Date: MM/DD/YYYY format.')
    print('')
    print('A privacy pop-up will appear on the login screen, and it needs to be closed manually.')
    print('This code is specifically designed for the 2026 calendar year, as the website requires a very specific format for picking dates. The year will need to be updated each year for usage gathering.')