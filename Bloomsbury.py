def Bloomsbury(startDate, endDate):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass
    # Bloomsbury

    # Input the URL for the main website here
    vendorURL = 'https://sams-sigma.com/app/login?publisherId=74'

    datePattern = re.compile('[A-z][A-z][A-z] [0-9][0-9][0-9][0-9]')

    
    if datePattern.fullmatch(startDate) == None:
        raise SyntaxError('Start Date needs to be in the following format: First three letters of month name, space, YYYY.')
    elif datePattern.fullmatch(endDate) == None:
        raise SyntaxError('End Date needs to be in the following format: First three letters of month name, space, YYYY.')      
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()

    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    
    # Log into the website
    driver.get(vendorURL)
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/form/div/div/div[4]/input[1]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    # Switch to the University of Tennessee, Knoxville account
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/ul/li[1]/div/div[2]/div/div/span'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/ul/li[1]/div/div[2]/div/div/span').click()
    except:
        raise ReferenceError('Account dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-0-1"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-0-1"]/a/div').click()
    except:
        raise ReferenceError('UT Knoxville tab not found. Double-check the login information; if it is correct, then update the XPATH.')


    # Go to Reports
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div[3]/div/div/div[5]/div/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div[3]/div/div/div[5]/div/a').click()
    except:
        raise ReferenceError('Reports button not found. Double-check the login information; if it is correct, then update the XPATH.')


    # Go to the COUNTER button
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/a').click()
    except:
        raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')


    # Select the Report - DR Database Master Report
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    except:
        raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-2-0"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-2-0"]/a/div').click()
    except:
        raise ReferenceError('DR report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
        driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    except:
        raise TimeoutError('Download report button not found. Update the XPATH in the code.') 


    print('DR downloading. Click on Download under Report link once the button appears. The next report will download shortly.')
    time.sleep(35)


    # Go to the COUNTER button
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a').click()
    except:
        raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')  


    # Select the Report - DR_D1 Database Search and Item Usage
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    except:
        raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-5-1"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-5-1"]/a/div').click()
    except:
        raise ReferenceError('DR_D1 report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
        driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    except:
        raise TimeoutError('Download report button not found. Update the XPATH in the code.') 


    print('DR_D1 downloading. Click on Download under Report link once the button appears. The next report will download shortly.')
    time.sleep(35)

     
    # Go to the COUNTER button
    #try:
    #    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a'))) #To ensure the webpage loads before trying, it takes a while
    #    driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a').click()
    #except:
    #    raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')  


    # Select the Report - IR Item Master Report
    #try:
    #    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
    #    driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    #except:
    #    raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    #try:
    #    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-8-3"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
    #    driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-8-3"]/a/div').click()
    #except:
    #    raise ReferenceError('IR report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    #try:
    #    driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
    #    driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    #except:
    #    raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    #try:
    #    driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
    #    driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
    #    driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    #except:
    #    raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    #try:
    #    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    #except:
    #    raise TimeoutError('Download report button not found. Update the XPATH in the code.') 


    #print('IR downloading. Click on Download under Report link once the button appears. The next report will download shortly.')
    #time.sleep(10)


    # Go to the COUNTER button
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a').click()
    except:
        raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')
    
    
    # Select the Report - IR_M1 Multimedia Item Requests
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    except:
        raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-8-4"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-8-4"]/a/div').click()
    except:
        raise ReferenceError('IR_M1 report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
        driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    except:
        raise TimeoutError('Download report button not found. Update the XPATH in the code.') 


    print('IR_M1 downloading. Click on Download under Report link once the button appears. The next report will download shortly.')
    time.sleep(35)


    # Go to the COUNTER button
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a').click()
    except:
        raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')  


    # Select the Report - PR Platform Master Report
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    except:
        raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-11-5"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-11-5"]/a/div').click()
    except:
        raise ReferenceError('PR report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
        driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    except:
        raise TimeoutError('Download report button not found. Update the XPATH in the code.') 


    print('PR downloading. Click on Download under Report link once the button appears. The next report will download shortly.')
    time.sleep(35)    
    

    # Go to the COUNTER button
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a').click()
    except:
        raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')


    # Select the Report - PR_P1 Platform Master Report
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    except:
        raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-14-6"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-14-6"]/a/div').click()
    except:
        raise ReferenceError('PR report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
        driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    except:
        raise TimeoutError('Download report button not found. Update the XPATH in the code.') 


    print('PR_P1 downloading. Click on Download under Report link once the button appears. The next report will download shortly.')
    time.sleep(35)       






    # Go to the COUNTER button
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a').click()
    except:
        raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')  


    # Select the Report - TR Title Master Report
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    except:
        raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-17-7"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-17-7"]/a/div').click()
    except:
        raise ReferenceError('TR report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
        driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    except:
        raise TimeoutError('Download report button not found. Update the XPATH in the code.') 


    print('TR downloading. Click on Download under Report link once the button appears. The next report will download shortly.')
    time.sleep(25)        


    


    # Go to the COUNTER button
    #try:
    #    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a'))) #To ensure the webpage loads before trying, it takes a while
    #    driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a').click()
    #except:
    #    raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')  


    # Select the Report - TR_B1 Book Requests Excluding OA_Gold
    #try:
    #    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
    #    driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    #except:
    #    raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    #try:
    #    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-23-8"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
    #    driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-23-8"]/a/div').click()
    #except:
    #    raise ReferenceError('TR_B1 report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    #try:
    #    driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
    #    driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    #except:
    #    raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    #try:
    #    driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
    #    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
    #    driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
    #    driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    #except:
    #    raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    #try:
    #    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
    #    driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    #except:
    #    raise TimeoutError('Download report button not found. Update the XPATH in the code.') 


    #print('TR_B1 downloading. Click on Download under Report link once the button appears. The next report will download shortly.')
    #time.sleep(25)        


    # Go to the COUNTER button
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/ul/li[6]/ul/li[3]/a').click()
    except:
        raise ReferenceError('COUNTER button not found. Double-check the login information; if it is correct, then update the XPATH.')  


    # Select the Report - TR_B3 Book Usage by Access Type
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="publisher-counter-report-type"]/div/span').click()
    except:
        raise ReferenceError('Report dropdown not found. Double-check the login information; if it is correct, then update the XPATH.')       


    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-select-choices-row-20-10"]/a/div'))) #To ensure the webpage loads before trying, it takes a while
        driver.find_element(By.XPATH, '//*[@id="ui-select-choices-row-20-10"]/a/div').click()
    except:
        raise ReferenceError('TR_B3 report button not found. Double-check the login information; if it is correct, then update the XPATH.')   

    
    # Input the Start Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="start-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="start-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="start-date"]').send_keys(startDate)
    except:
        raise ReferenceError('Start date input box not found. Update the XPATH.')


    # Input the End Date
    
    try:
        driver.find_element(By.XPATH, '//*[@id="end-date"]').click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="end-date"]'))) #This time, no need to wait for a buffer period
        driver.find_element(By.XPATH, '//*[@id="end-date"]').send_keys(endDate)
        driver.find_element(By.XPATH, '//*[@id="report-extension"]').click()
    except:
        raise ReferenceError('End date input box not found. Update the XPATH.')

        

    ## Download the report
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div/div/div/div[3]/div/div/div/div[3]/ui-view/div/div/div/form/div/div[9]/div/div/input').click()        
    except:
        raise TimeoutError('Download report button not found. Update the XPATH in the code.') 

   
    
    keyword = input('TR_B3 downloading. Once the report is downloaded, type anything here to close the browser.')

    driver.close()


def Bloomsbury_Info():
    print('Input keys needed:')
    print('Start month: First three letters of month name, space, YYYY format.')
    print('End month: First three letters of month name, space, YYYY format.')
    print('')
    print('This code downloads the following reports: DR, DR_D1, IR_M1, PR, PR_P1, TR, TR_B3.')