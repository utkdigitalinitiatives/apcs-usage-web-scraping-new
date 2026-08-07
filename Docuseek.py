def Docuseek(startMonth, startYear, endMonth, endYear):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import re
    import getpass

    # Input the URL for the main website here
    vendorURL = 'https://docuseek2.com/secure/login/0/1'

    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')
    
    # Log into the website
    driver.get(vendorURL)

    
    # Input the username and password, then log in

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="form_login"]/div[4]/a').click()
    except:
        raise ReferenceError('Login page not found. Check the URL; if correct, then update the XPATH.')


    print('Make sure you are in full screen before continuing.')
    time.sleep(5)

    # Go to My Docuseek
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav_secondary"]/a[1]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="nav_secondary"]/a[1]').click()
    except:
        raise ReferenceError('My Docuseek button not found. Double-check the login information. If correct, then update the XPATH.')


    # Go to Analytics
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab4"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="tab4"]').click()
    except:
        raise ReferenceError('Analytics button not found. Update the XPATH.')


    # Download Reports


    ## Select Report Type - PR

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select_report"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="select_report"]'))
        select.select_by_visible_text('COUNTER 5.1 Platform Report (PR)')
    except:
        raise ReferenceError('Report dropdown not found. Update the XPATH.')


    ## Choose Start Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from_counter_year"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="from_counter_year"]'))
        select.select_by_visible_text(str(startYear))
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')

    ## Choose Start Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from_counter_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="from_counter_month"]'))
        select.select_by_visible_text(startMonth)
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')


    ## Choose End Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to_counter_year"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="to_counter_year"]'))
        select.select_by_visible_text(str(endYear))
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')


    ## Choose End Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to_counter_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="to_counter_month"]'))
        select.select_by_visible_text(endMonth)
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')



    ## Select the Metric Types

    try:
        driver.find_element(By.XPATH, '//*[@id="searches_platform"]').click() #Searches Platform
        driver.find_element(By.XPATH, '//*[@id="total_item_investigations"]').click() #Total Item Investigations
        driver.find_element(By.XPATH, '//*[@id="unique_item_investigations"]').click() #Unique Item Investigations
        driver.find_element(By.XPATH, '//*[@id="unique_item_requests"]').click() #Unique Item Requests
    except:
        raise ReferenceError('Metric type boxes not found. Update the XPATH.')



    ## Run the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="run_report_button"]').click()
    except:
        raise ReferenceError('Run report button not found. Update the XPATH.')   


    print('Copy this file into Excel. The code will download the next report in 30 seconds.')
    time.sleep(30)



    ## Select Report Type - PR_P1

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select_report"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="select_report"]'))
        select.select_by_visible_text('COUNTER 5.1 Platform Usage (PR_P1)')
    except:
        raise ReferenceError('Report dropdown not found. Update the XPATH.')


    ## Choose Start Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from_counter_year"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="from_counter_year"]'))
        select.select_by_visible_text(str(startYear))
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')

    ## Choose Start Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from_counter_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="from_counter_month"]'))
        select.select_by_visible_text(startMonth)
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')

    

    ## Choose End Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to_counter_year"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="to_counter_year"]'))
        select.select_by_visible_text(str(endYear))
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')



    ## Choose End Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to_counter_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="to_counter_month"]'))
        select.select_by_visible_text(endMonth)
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')





    ## Run the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="run_report_button"]').click()
    except:
        raise ReferenceError('Run report button not found. Update the XPATH.')  

    print('Copy this file into Excel. The code will download the next report in 30 seconds.')
    time.sleep(30)   




    ## Select Report Type - DR

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select_report"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="select_report"]'))
        select.select_by_visible_text('COUNTER 5.1 Database Report (DR)')
    except:
        raise ReferenceError('Report dropdown not found. Update the XPATH.')



    ## Choose Start Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from_counter_year"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="from_counter_year"]'))
        select.select_by_visible_text(str(startYear))
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')

    ## Choose Start Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from_counter_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="from_counter_month"]'))
        select.select_by_visible_text(startMonth)
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')



    ## Choose End Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to_counter_year"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="to_counter_year"]'))
        select.select_by_visible_text(str(endYear))
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')


    ## Choose End Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to_counter_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="to_counter_month"]'))
        select.select_by_visible_text(endMonth)
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')




    ## Select the Metric Types

    try:
        driver.find_element(By.XPATH, '//*[@id="total_item_investigations"]').click() #Total Item Investigations
        driver.find_element(By.XPATH, '//*[@id="unique_item_investigations"]').click() #Unique Item Investigations
        driver.find_element(By.XPATH, '//*[@id="unique_item_requests"]').click() #Unique Item Requests
        driver.find_element(By.XPATH, '//*[@id="no_license"]').click() #No License
    except:
        raise ReferenceError('Metric type boxes not found. Update the XPATH.')
        

    ## Run the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="run_report_button"]').click()
    except:
        raise ReferenceError('Run report button not found. Update the XPATH.')  

    print('Copy this file into Excel. The code will download the next report in 30 seconds.')
    time.sleep(30)    



    ## Select Report Type - IR_M1

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select_report"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="select_report"]'))
        select.select_by_visible_text('COUNTER 5.1 Multimedia Item Requests Report (IR_M1)')
    except:
        raise ReferenceError('Report dropdown not found. Update the XPATH.')


    ## Choose Start Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from_counter_year"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="from_counter_year"]'))
        select.select_by_visible_text(str(startYear))
    except:
        raise ReferenceError('Start year dropdown not found. Update the XPATH.')

    ## Choose Start Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="from_counter_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="from_counter_month"]'))
        select.select_by_visible_text(startMonth)
    except:
        raise ReferenceError('Start month dropdown not found. Update the XPATH.')


    
    ## Choose End Year

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to_counter_year"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="to_counter_year"]'))
        select.select_by_visible_text(str(endYear))
    except:
        raise ReferenceError('End year dropdown not found. Update the XPATH.')


    ## Choose End Month

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="to_counter_month"]'))) #To ensure the webpage loads before trying
        select = Select(driver.find_element(By.XPATH, '//*[@id="to_counter_month"]'))
        select.select_by_visible_text(endMonth)
    except:
        raise ReferenceError('End month dropdown not found. Update the XPATH.')





        

    ## Run the Report
    try:
        driver.find_element(By.XPATH, '//*[@id="run_report_button"]').click()
    except:
        raise ReferenceError('Run report button not found. Update the XPATH.') 

    keyboard = input('Copy this file into excel. When you are done, type anything here to close the browser.')

    driver.close()
        
def Docuseek_Info():
    print('Keys needed:')
    print('Start month - First three letters of the month name.')
    print('Start year - YYYY format.')
    print('End month - First three letters of the month name.')
    print('End year - YYYY format.')
    print('')
    print('All of the reports must be manually copied into Excel. The code will pause after downloading to the webpage to make these copies.')
    