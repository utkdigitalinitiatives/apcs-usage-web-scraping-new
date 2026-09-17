def Elsevier(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    from datetime import datetime
    import getpass



    startingPointYear = datetime.now().year

    numClicksStart = startingPointYear - startYear
    numClicksEnd = startingPointYear - endYear

    if numClicksStart < 0 or numClicksStart > 5:
        raise ValueError('Usage is only stored for the last five calendar years up to the current year. Your starting year falls outside of this range.')
    if numClicksEnd < 0 or numClicksEnd > 5:
        raise ValueError('Usage is only stored for the last five calendar years up to the current year. Your ending year falls outside of this range.')

    match startMonth:
        case 'January':
            startString = '1'
        case 'February':
            startString = '2'
        case 'March':
            startString = '3'
        case 'April':
            startString = '4'
        case 'May':
            startString = '5'
        case 'June':
            startString = '6'
        case 'July':
            startString = '7'
        case 'August':
            startString = '8'
        case 'September':
            startString = '9'
        case 'October':
            startString = '10'
        case 'November':
            startString = '11'
        case 'December':
            startString = '12'

    match endMonth:
        case 'January':
            endString = '1'
        case 'February':
            endString = '2'
        case 'March':
            endString = '3'
        case 'April':
            endString = '4'
        case 'May':
            endString = '5'
        case 'June':
            endString = '6'
        case 'July':
            endString = '7'
        case 'August':
            endString = '8'
        case 'September':
            endString = '9'
        case 'October':
            endString = '10'
        case 'November':
            endString = '11'
        case 'December':
            endString = '12'

    

    # Input the URL for the main website here
    vendorURL = 'https://admintool.elsevier.com'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)

    # Click the Get Started Button
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="about"]/form/div[2]/button/span/span'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="about"]/form/div[2]/button/span/span').click()
    except:
        raise ReferenceError('Get started button not found. Double-check the URL; if it is correct, then update the XPATH in the code.')

    # Clear the Cookies
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    except:
        raise ReferenceError('Accept all cookies button not found. If one did not appear, comment out this code block in the code. Otherwise, update the XPATH.')

    ## Username
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bdd-email"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="bdd-email"]').send_keys(username)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="bdd-elsPrimaryBtn"]').click()
    except:
        raise ReferenceError('Username webpage not found. Update the XPATH.')

    ## Password
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bdd-password"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="bdd-password"]').send_keys(password)
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="bdd-elsPrimaryBtn"]').click()
    except:
        raise ReferenceError('Password box not found. Double-check the username; if it is correct, then update the XPATH.')


    # Go to the Product Insights for your organization link
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/section/h2/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="page-content"]/div[2]/section/h2/a[1]').click()
    except:
        raise ReferenceError('Product Insights button not found. Double-check the password; if it is correct, then update the XPATH.')      

    vendorURL2 = 'https://e-pic.elsevier.com/dashboard'

    driver.get(vendorURL2)



    print('A cookies or survey pop-up should appear on the first tab. Close that pop-up. There may also be a login button for EPIC on this page as well; if so, that needs to be clicked manually. If neither appear on the first page, wait for the code to continue.')
    time.sleep(15)
    
    # Click the COUNTER COP5.1 Reports button
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tile_COP51React"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="tile_COP51React"]').click()
    except:
        raise ReferenceError('COUNTER COP5.1 Button not found. If the code continued before you were able to log in, increase the wait timer in the code. Otherwise, update the XPATH to this button.')   


    keyword = input('All reports can be run from this page, and will appear for download at the bottom of the page. When you are finished, type anything here to close the window.')

    
    
    

def Elsevier_Info():
    print('Keys needed:')
    print('Start month - The full name of the month is needed.')
    print('Start year - YYYY format.')
    print('End month - The full name of the month is needed.')
    print('End year - YYYY format.')
    print('')
    print('The code will move to a second webpage in the middle. All work will remain on the first tab that opens, not the second one that opens after the code starts.')
    print('')
    print('After moving to this second page, the code will require you to close a pop-up or two (it can vary depending on the run).')
    print('Once the code finishes, all reports will need to be requested and downloaded manually.')