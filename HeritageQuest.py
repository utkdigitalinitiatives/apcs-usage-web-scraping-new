def HeritageQuest(startDate, numMonths):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    from datetime import date, datetime, timedelta
    from dateutil.relativedelta import relativedelta
    # HeritageQuest
    
    # Input the URL for the main website here
    vendorURL = 'https://www.heritagequestonline.com/localadminweb/hqousagereport/do/report?pid=2843'

    datePattern = re.compile('[A-z][A-z][A-z] [0-9][0-9][0-9][0-9]')

    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Starting date must be in the following format: First three letters of month, a space, YYYY')

    months = startDate[0:3]

    match months:
        case 'Jan':
            endString = 1
        case 'Feb':
            endString = 2
        case 'Mar':
            endString = 3
        case 'Apr':
            endString = 4
        case 'May':
            endString = 5
        case 'Jun':
            endString = 6
        case 'Jul':
            endString = 7
        case 'Aug':
            endString = 8
        case 'Sep':
            endString = 9
        case 'Oct':
            endString = 10
        case 'Nov':
            endString = 11
        case 'Dec':
            endString = 12

    dateCheck = datetime(int(startDate[4:8]), endString, 1)
    

    if numMonths.is_integer() == False or numMonths > 12:
        raise SyntaxError('The number of months must be an integer between 1 and 12.')
    elif dateCheck + relativedelta(months = numMonths) >= datetime.today():
        raise ValueError('Your date range goes past the current month. Reduce the number of months or change the start date.')

    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    driver.get(vendorURL)

    print('Close the cookies popup, then wait for the code to continue.')
    time.sleep(5)
    
    # Change the Report Type to COUNTER
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="reportid"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="reportid"]'))
        select.select_by_visible_text('Counter Database Report 1') #The only COUNTER report on offer through Heritage Quest
    except:
        raise ReferenceError('Report Type box not found. Update the XPATH.')

    time.sleep(2) #Wait for the webpage to buffer
    
    # Change the Delivery Method to Download now
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="deliverMethod"]'))
        select.select_by_visible_text('Download now')
    except:
        raise ReferenceError('Delivery Method box not found. If this error occurred while the webpage was still buffering, increase the sleep timer in the code. Otherwise, update the XPATH.')

    time.sleep(2) #Wait for the webpage to buffer
    
    # Change the Usage Period:
    
    ## Start Date
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="counterDateFrom"]'))
        select.select_by_visible_text(startDate)
    except:
        raise ReferenceError('Delivery Method box not found. If this error occurred while the webpage was still buffering, increase the sleep timer in the code. Otherwise, update the XPATH.')        
    
    
    ## Number of Months
    try:
        select = Select(driver.find_element(By.XPATH, '//*[@id="months"]/select'))
        select.select_by_visible_text(str(numMonths)) #Maximum of 12, even if the start date is more than 12 months ago. Current month is included.
    except:
        raise ReferenceError('Number of months box not found. Update the XPATH.')
    
    
    # Create the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="formUsage"]/table[7]/tbody/tr/td[1]/table[2]/tbody/tr/td/input').click()
    except:
        raise ReferenceError('Generate report button not found. Update the XPATH.')

    
    keyword = input('When the download appears, type anything here to close the browser.')

    driver.close()


def HeritageQuest_Info():
    print('Input keys needed:')
    print('Start date - First three days of the month, space, YYYY format')
    print('Months since start date - A number between 1 and 12. The current month can be included in the range.')
    print('')
    print('When the page appears, the pop-up must be closed manually. The report will then download automatically.')