def CRC(startMonth, startYear):
    # CRC Handbook of Chemsitry and Physics
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import getpass
    
    # CRC Handbook (ChemNet)

    match startMonth:
        case 'Jan':
            endString = '1'
        case 'Feb':
            endString = '2'
        case 'Mar':
            endString = '3'
        case 'Apr':
            endString = '4'
        case 'May':
            endString = '5'
        case 'Jun':
            endString = '6'
        case 'Jul':
            endString = '7'
        case 'Aug':
            endString = '8'
        case 'Sep':
            endString = '9'
        case 'Oct':
            endString = '10'
        case 'Nov':
            endString = '11'
        case 'Dec':
            endString = '12'

    #match endMonth:
    #    case 'Jan':
    #        endString2 = '1'
    #    case 'Feb':
    #        endString2 = '2'
    #    case 'Mar':
    #        endString2 = '3'
    #    case 'Apr':
    #        endString2 = '4'
    #    case 'May':
    #        endString2 = '5'
    #    case 'Jun':
    #        endString2 = '6'
    #    case 'Jul':
    #        endString2 = '7'
    #    case 'Aug':
    #        endString2 = '8'
    #    case 'Sep':
    #        endString2 = '9'
    #    case 'Oct':
    #        endString2 = '10'
    #    case 'Nov':
    #        endString2 = '11'
    #    case 'Dec':
    #        endString2 = '12'
    
    # Input the URL for the main website here
    vendorURL = 'https://support.chemnetbase.com/faces/reports/Counter.xhtml'
    
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
        driver.find_element(By.XPATH, '//*[@id="logonForm:j_idt15"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="logonForm:j_idt20"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="logonForm:j_idt23"]').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')
    
    
    # Choose all Applications
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="appSelectAllBtn"]')))
        driver.find_element(By.XPATH, '//*[@id="appSelectAllBtn"]').click()
    except:
        raise ReferenceError('Select All button not found. Update the XPATH.')


    
    # Choose Custom Date option
    try:
        driver.find_element(By.XPATH, '//*[@id="j_idt79_label"]').click()
        print('Choose Custom from the drop-down (last option in the list). The code will continue shortly.')
        time.sleep(10)
    except:
        raise ReferenceError('Date dropdown not found. Update the XPATH.')


    # Select the Dates:

    ## Start Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counterDateFrom_input"]')))
        driver.find_element(By.XPATH, '//*[@id="counterDateFrom_input"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counterDateFrom"]/div/div[1]/div/select')))
        select = Select(driver.find_element(By.XPATH, '//*[@id="counterDateFrom"]/div/div[1]/div/select'))
        select.select_by_visible_text(str(startYear))
    except:
        raise ReferenceError('Year not found. The first year present is 2016 and the last year is current year. If your year is in that range, update the XPATH.')

    ## Start Month

    monthStart = '//*[@id="counterDateFrom"]/div/div[2]/a[' + endString + ']'
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, monthStart)))
        driver.find_element(By.XPATH, monthStart).click()
    except:
        raise ReferenceError('Month not found. Update the XPATH.')

    ## End Year

    print('Select the To year and month manually. The code will continue shortly.')
    time.sleep(15)  
    
    #try:

        #driver.find_element(By.XPATH, '//*[@id="counterDateTo"]').click()
        #WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counterDateTo"]/div/div[1]/div/select')))
        #select = Select(driver.find_element(By.XPATH, '//*[@id="counterDateTo"]/div/div[1]/div/select'))
        #select.select_by_visible_text(str(endYear))
    #except:
    #    raise ReferenceError('Year not found. The first year present is 2016 and the last year is current year. If your year is in that range, update the XPATH.')

    ## End Month

    #monthEnd = '//*[@id="counterDateTo"]/div/div[2]/a[' + endString2 + ']'
    #try:
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, endMonth)))
    #    driver.find_element(By.XPATH, endMonth).click()
    #except:
    #    raise ReferenceError('Month not found. Update the XPATH.')


    
    # Reveal the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="goBtn"]')))
        driver.find_element(By.XPATH, '//*[@id="goBtn"]').click()
    except:
        raise ReferenceError('Go button not found. Update the XPATH.')
    

    # Press the Export Button
    #try:
    #    button = driver.find_element(By.XPATH, '//*[@id="j_idt102"]')
    #except ReferenceError:
    #    print("element not found")
    #else:        
    #    print("element exists")
    #    try:
    #        driver.find_element(By.XPATH, '//*[@id="counterForm"]/div[1]/a[1]').click()
    #    except ReferenceError:
    #        print('export not done')
    #    else:
    #        print("export done")
  

    
    # Manually download the report
    
    print('Use the logos above the table to download the data.')
    print('')
    print('')
    keyword = input('When you are finished, type anything here to close the browser.')

    driver.close()


def CRC_Info():
    print('Keys needed:')
    print('Start month - First three letters of name only.')
    print('Start year - YYYY format.')
    print('')
    print('The Custom Date drop-down must be clicked manually. Then, the To date must be input manually.')
    print('Once the code finishes running, manually download the report by clicking on the logo matching your preferred download method.')
    