def Ancestry(startDate, numMonths, email):

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.edge.options import Options
    import pandas as pd
    import numpy as np
    import time
    import re
    from datetime import date, datetime, timedelta
    from dateutil.relativedelta import relativedelta


    # Input the URL for the main website here
    vendorURL = 'http://ancestrylibrary.proquest.com/alereports'

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
    elif dateCheck + relativedelta(months = numMonths - 1) >= datetime.today():
        raise ValueError('Your date range goes past the current month. Reduce the number of months or change the start date.')


    if email.endswith('@utk.edu') == False and email.endswith('@tennessee.edu') == False:
        raise ValueError('Make sure the data is sent to a @utk.edu or a @tennessee.edu email.')
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    # Log into the website
    driver.get(vendorURL)
    

    # Clear the cookies pop-up
    try:
        time.sleep(3)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    except:
        raise ReferenceError('Popup not found. If one did not appear in the browser, then comment out the lines of code above. Otherwise, update the XPATH.')
    
    # Fill all of the information on the website:

    
    ## Report Type
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="reportid"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.ID, 'reportid'))
        select.select_by_visible_text('Counter Database Report 1')
    except:
        raise ReferenceError('Report Type dropdown not found. Double-check the website URL and fix if necessary. If the URL is correct, then update the XPATH in the code.')
    
    
    ## Delivery Method
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="deliverMethod"]'))) #The webpage buffers for a second after making the Report Type decision
        select = Select(driver.find_element(By.ID, 'deliverMethod'))
        select.select_by_visible_text('Email report now')
    except:
        raise ReferenceError('Delivery method not found. Update the XPATH in the code.')
    
    
    ## Usage Period: Start Date
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="counterDateFrom"]'))) #The webpage buffers for a second after making the Delivery Method decision too
        select = Select(driver.find_element(By.ID, 'counterDateFrom'))
        select.select_by_visible_text(startDate)
    except:
        raise ReferenceError('Start Date dropdown not found. Update the XPATH in the code.')
    
    
    ## Usage Period: Number of Months
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="months"]/select'))) #This time, no need to wait for a buffer period
        select = Select(driver.find_element(By.XPATH, '//*[@id="months"]/select'))
        select.select_by_visible_text(str(numMonths))
    except:
        raise ReferenceError('Number of months dropdown not found. Update the XPATH in the code.')
    

    ## Select the CSV Button
    try:
        driver.find_element(By.XPATH, '//*[@id="formUsage"]/table[7]/tbody/tr/td[1]/table[1]/tbody/tr[9]/td/input[2]').click()  
    except:
        raise ReferenceError('CSV button not found. Update the XPATH in the code.')


    ## Enter the email
    try:
        driver.find_element(By.XPATH, '//*[@id="formUsage"]/table[7]/tbody/tr/td[1]/table[1]/tbody/tr[11]/td/input').send_keys(email)
    except:
        raise ReferenceError('Email input box not found. Update the XPATH in the code.')    


    # Send the email

    try:
        driver.find_element(By.XPATH, '//*[@id="formUsage"]/table[7]/tbody/tr/td[1]/table[2]/tbody/tr/td/input').click()
    except:
        ReferenceError('Create Report button not found. Update the XPATH in the code.')

    keyword = input('When you are finished, type anything here to close the browser.')

    driver.close()

def Ancestry_Info():
    print('Keys Needed:')
    print('Start Date - First three letters of month, space, YYYY format.')
    print('Number of Months - An integer between 1 and 12. The number of months can not exceed the current month.')
    print('Email - To send the CSV to.')

