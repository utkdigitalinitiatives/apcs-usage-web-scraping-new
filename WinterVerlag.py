def WinterVerlag(usageYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Universitatverlag Winter GmbH


    dateString = re.compile('[0-9][0-9][0-9][0-9]')

    if dateString.fullmatch(str(usageYear)) == None:
        raise SyntaxError('Usage year must be in YYYY format.')


    XPATHYear = usageYear - 2014 + 1

    # Input the URL for the main website here
    vendorURL = 'https://journals.winter-verlag.de/'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)


    # Go to the Login page
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginBox"]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="loginBox"]/a').click()
    except:
        raise ReferenceError('Login button not found. Double-check the URL and login information; if it is correct, then update the XPATH in the code.')
        
    
    # Input the username and password, then log in

    #try:
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="quotusModalLogin"]/div/div/div[2]/form/div[1]/input'))) #To ensure the webpage loads before filling out the form
    #    driver.find_element(By.XPATH, '//*[@id="quotusModalLogin"]/div/div/div[2]/form/div[1]/input').send_keys(username)
    #    driver.find_element(By.XPATH, '//*[@id="quotusModalLogin"]/div/div/div[2]/form/div[2]/input').send_keys(password)
    #    driver.find_element(By.XPATH, '//*[@id="quotusModalLogin"]/div/div/div[2]/form/button').click()
    #except:
    #    raise ReferenceError('Login box pop-up not found. Update the XPATH in the code.')  

    # Manually Input the Username and Password
    
    print('Log into the website using the following information:')
    print('Username:', username)
    print('Password:', password)
    print('')
    print('Once logged in, the code will continue automatically.')
    time.sleep(15) #Allowing time to log in


    # Click on the Admin tab
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="primaryNavigation"]/div/div[1]/div/nav/ul[1]/li[6]/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="primaryNavigation"]/div/div[1]/div/nav/ul[1]/li[6]/a').click()
    except:
        raise ReferenceError('Admin tab not found. Update the XPATH.')


    # Click the Library dropdown
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[2]/div/button'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div/button').click()
    except:
        raise ReferenceError('Library dropdown not found. Update the XPATH.')

    time.sleep(1)

    # Then choose Hodges Library
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="instSelect"]/li/a'))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, '//*[@id="instSelect"]/li/a').click()
    except:
        raise ReferenceError('Hodges Library not found. Update the XPATH.')



    # Click the Year dropdown
    #try:
    #    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inst1"]/div[2]/div[1]/div[2]/div/button'))) #To ensure the webpage loads before filling out the form
    #    driver.find_element(By.XPATH, '//*[@id="inst1"]/div[2]/div[1]/div[2]/div/button').click()
    #except:
    #    raise ReferenceError('Year dropdown not found. Update the XPATH.')

    print('Open the Select Year dropdown at the bottom of the page. The code will continue shortly.')
    time.sleep(8)

    
    # Select the Year
    yearXPATH = r'//*[@id="statSelect"]/li['+str(XPATHYear)+']/a'
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, yearXPATH))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, yearXPATH).click()
    except:
        raise ReferenceError('Usage year not found. Usage is stored as far back as 2014 only. If the year should be available, update the XPATH.')



    # Download the JR1 - Successful Requests by Journal
    reportXPATH1 = r'//*[@id="usage_statistics_year'+str(usageYear)+'"]/div[1]/ul/li[2]/p/a'
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, reportXPATH1))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, reportXPATH1).click()
    except:
        raise ReferenceError('JR1 download button not found. Update the XPATH.')


    # Download the JR5 - Successful Requests by YOP
    reportXPATH5 = r'//*[@id="usage_statistics_year'+str(usageYear)+'"]/div[2]/ul/li[2]/p/a'
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, reportXPATH5))) #To ensure the webpage loads before filling out the form
        driver.find_element(By.XPATH, reportXPATH5).click()
    except:
        raise ReferenceError('JR5 download button not found. Update the XPATH.')


    keyboard = input('When the reports appear in Downloads, type anything here to close the browser.')


    driver.close()



def WinterVerlag_Info():
    print('Keys needed:')
    print('Usage year - YYYY format. Only usage for this year will be downloaded.')
    print('')
    print('Logging in will need to be done manually. After logging in, the usage year dropdown will need to be opened manually.')

