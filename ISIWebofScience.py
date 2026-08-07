def ISIWebofScience(startMonth, startYear, endMonth, endYear):
    # ISI Web of Science
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import datetime
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    import getpass
    
    # Input the URL for the main website here
    vendorURL = 'https://access.clarivate.com/login?app=wurs'
    
    
    
    # Set the Current OS for surfing the web
    ## Will likely be Edge, but can change to Chrome or FireFox if necessary
    driver = webdriver.Edge()
    
    username = getpass.getpass('Enter the Username Here:')
    password = getpass.getpass('Enter the Password Here:')

    
    
    # Log into the website
    driver.get(vendorURL)
    
    # Input the username and password, then log in
    
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-0"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').clear()
        driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').clear()
        driver.find_element(By.XPATH, '//*[@id="mat-input-1"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="signIn-btn"]').click()
    except:
        raise ReferenceError('Login webpage not found. Double-check the URL; if it is correct, then update the XPATH in the code.')
    
    
    
    # Go to the Counter Reports tab
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="counter-reports-tab"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="counter-reports-tab"]').click()
    except:
        raise ReferenceError('Counter Reports tab not found. Update the XPATH.')



    # Download Reports - PR_P1
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/div/app-counter-report/div/mat-card/mat-card-content/button[2]/span[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/div/app-counter-report/div/mat-card/mat-card-content/button[2]/span[2]').click()
    except:
        raise ReferenceError('PR_P1 button not found. Update the XPATH.')
    
    
    # Change the Date Range to Custom
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-5"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-5"]').click()
    except:
        raise ReferenceError('Date Range dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-26"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-option-26"]').click()
    except:
        raise ReferenceError('Custom option not found. Update the XPATH.')


    beginningStartXPath = '//*[@id="mat-option-'

    startDate = datetime(startYear, startMonth, 1)
    currentDate = datetime(datetime.now().year, datetime.now().month, 1)

    delta = relativedelta(currentDate, startDate)

    deltaDate = delta.months + delta.years * 12


    if deltaDate > 36:
        raise ValueError('Usage is only available for the last three years.')
    elif deltaDate == 0:
        raise ValueError('Usage is not available for the current month.')


    match deltaDate:
        case 36:
            beginningEndXPath = '26"]'
        case 35:
            beginningEndXPath = '27"]'
        case 34:
            beginningEndXPath = '28"]'
        case 33:
            beginningEndXPath = '29"]'
        case 32:
            beginningEndXPath = '30"]'
        case 31:
            beginningEndXPath = '31"]'
        case 30:
            beginningEndXPath = '32"]'
        case 29:
            beginningEndXPath = '33"]'
        case 28:
            beginningEndXPath = '34"]'
        case 27:
            beginningEndXPath = '35"]'
        case 26:
            beginningEndXPath = '36"]'
        case 25:
            beginningEndXPath = '37"]'
        case 24:
            beginningEndXPath = '38"]'
        case 23:
            beginningEndXPath = '39"]'
        case 22:
            beginningEndXPath = '40"]'
        case 21:
            beginningEndXPath = '41"]'
        case 20:
            beginningEndXPath = '42"]'
        case 19:
            beginningEndXPath = '43"]'
        case 18:
            beginningEndXPath = '44"]'
        case 17:
            beginningEndXPath = '45"]'
        case 16:
            beginningEndXPath = '46"]'
        case 15:
            beginningEndXPath = '47"]'
        case 14:
            beginningEndXPath = '48"]'
        case 13:
            beginningEndXPath = '49"]'
        case 12:
            beginningEndXPath = '50"]'
        case 11:
            beginningEndXPath = '51"]'
        case 10:
            beginningEndXPath = '52"]'
        case 9:
            beginningEndXPath = '53"]'
        case 8:
            beginningEndXPath = '54"]'
        case 7:
            beginningEndXPath = '55"]'
        case 6:
            beginningEndXPath = '56"]'
        case 5:
            beginningEndXPath = '57"]'
        case 4:
            beginningEndXPath = '58"]'
        case 3:
            beginningEndXPath = '59"]'
        case 2:
            beginningEndXPath = '60"]'
        case 1:
            beginningEndXPath = '61"]'

            


    beginningXPath = beginningStartXPath + beginningEndXPath
    
    # Change the Beginning Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-6"]/div'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-6"]/div').click()
    except:
        raise ReferenceError('Beginning Date dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, beginningXPath))) #To ensure the webpage loads before trying//*[@id="mat-option-26"]
        driver.find_element(By.XPATH, beginningXPath).click()
    except:
        raise ReferenceError('Beginning Date not found. Update the XPATH.')


    
    endStartXPath = '//*[@id="mat-option-'

    endDate = datetime(endYear, endMonth, 1)
    currentDate = datetime(datetime.now().year, datetime.now().month, 1)

    delta = relativedelta(currentDate, endDate)

    deltaDate = delta.months + delta.years * 12


    if deltaDate > 36:
        raise ValueError('Usage is only available for the last three years.')
    elif deltaDate == 0:
        raise ValueError('Usage is not available for the current month.')


    match deltaDate:
        case 36:
            endEndXPath = '62"]'
        case 35:
            endEndXPath = '63"]'
        case 34:
            endEndXPath = '64"]'
        case 33:
            endEndXPath = '65"]'
        case 32:
            endEndXPath = '66"]'
        case 31:
            endEndXPath = '67"]'
        case 30:
            endEndXPath = '68"]'
        case 29:
            endEndXPath = '69"]'
        case 28:
            endEndXPath = '70"]'
        case 27:
            endEndXPath = '71"]'
        case 26:
            endEndXPath = '72"]'
        case 25:
            endEndXPath = '73"]'
        case 24:
            endEndXPath = '74"]'
        case 23:
            endEndXPath = '75"]'
        case 22:
            endEndXPath = '76"]'
        case 21:
            endEndXPath = '77"]'
        case 20:
            endEndXPath = '78"]'
        case 19:
            endEndXPath = '79"]'
        case 18:
            endEndXPath = '80"]'
        case 17:
            endEndXPath = '81"]'
        case 16:
            endEndXPath = '82"]'
        case 25:
            endEndXPath = '83"]'
        case 14:
            endEndXPath = '84"]'
        case 13:
            endEndXPath = '85"]'
        case 12:
            endEndXPath = '86"]'
        case 11:
            endEndXPath = '87"]'
        case 10:
            endEndXPath = '88"]'
        case 9:
            endEndXPath = '89"]'
        case 8:
            endEndXPath = '90"]'
        case 7:
            endEndXPath = '91"]'
        case 6:
            endEndXPath = '92"]'
        case 5:
            endEndXPath = '93"]'
        case 4:
            endEndXPath = '94"]'
        case 3:
            endEndXPath = '95"]'
        case 2:
            endEndXPath = '96"]'
        case 1:
            endEndXPath = '97"]'


    endXPath = endStartXPath + endEndXPath

    # Change the Ending Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-8"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-8"]').click()
    except:
        raise ReferenceError('Ending Date dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, endXPath))) #To ensure the webpage loads before trying//*[@id="mat-option-26"]
        driver.find_element(By.XPATH, endXPath).click()
    except:
        raise ReferenceError('Ending Date not found. Update the XPATH.')



    # Generate the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/app-report-dialog-date-selection/div[2]/div[2]/button'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/app-report-dialog-date-selection/div[2]/div[2]/button').click()
    except:
        raise ReferenceError('Generate button not found. Update the XPATH.')   


    print('PR_P1 Downloading. Wait for next report...')
    time.sleep(5)



    # Close the Box
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/app-report-dialog-date-selection/div[1]/mat-icon'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/app-report-dialog-date-selection/div[1]/mat-icon').click()
    except:
        raise ReferenceError('Close button not found. Update the XPATH.')   
    



    # Download Reports - DR_D1
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/div/app-counter-report/div/mat-card/mat-card-content/button[4]/span[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/div/app-counter-report/div/mat-card/mat-card-content/button[4]/span[2]').click()
    except:
        raise ReferenceError('DR_D1 button not found. Update the XPATH.')
    
    
    # Change the Date Range to Custom
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-13"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-13"]').click()
    except:
        raise ReferenceError('Date Range dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-106"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-option-106"]').click()
    except:
        raise ReferenceError('Custom option not found. Update the XPATH.')


    beginningStartXPath = '//*[@id="mat-option-'

    startDate = datetime(startYear, startMonth, 1)
    currentDate = datetime(datetime.now().year, datetime.now().month, 1)

    delta = relativedelta(currentDate, startDate)

    deltaDate = delta.months + delta.years * 12


    if deltaDate > 36:
        raise ValueError('Usage is only available for the last three years.')
    elif deltaDate == 0:
        raise ValueError('Usage is not available for the current month.')


    match deltaDate:
        case 36:
            beginningEndXPath = '106"]'
        case 35:
            beginningEndXPath = '107"]'
        case 34:
            beginningEndXPath = '108"]'
        case 33:
            beginningEndXPath = '109"]'
        case 32:
            beginningEndXPath = '110"]'
        case 31:
            beginningEndXPath = '111"]'
        case 30:
            beginningEndXPath = '112"]'
        case 29:
            beginningEndXPath = '113"]'
        case 28:
            beginningEndXPath = '114"]'
        case 27:
            beginningEndXPath = '115"]'
        case 26:
            beginningEndXPath = '116"]'
        case 25:
            beginningEndXPath = '117"]'
        case 24:
            beginningEndXPath = '118"]'
        case 23:
            beginningEndXPath = '119"]'
        case 22:
            beginningEndXPath = '120"]'
        case 21:
            beginningEndXPath = '121"]'
        case 20:
            beginningEndXPath = '122"]'
        case 19:
            beginningEndXPath = '123"]'
        case 18:
            beginningEndXPath = '124"]'
        case 17:
            beginningEndXPath = '125"]'
        case 16:
            beginningEndXPath = '126"]'
        case 15:
            beginningEndXPath = '127"]'
        case 14:
            beginningEndXPath = '128"]'
        case 13:
            beginningEndXPath = '129"]'
        case 12:
            beginningEndXPath = '130"]'
        case 11:
            beginningEndXPath = '131"]'
        case 10:
            beginningEndXPath = '132"]'
        case 9:
            beginningEndXPath = '133"]'
        case 8:
            beginningEndXPath = '134"]'
        case 7:
            beginningEndXPath = '135"]'
        case 6:
            beginningEndXPath = '136"]'
        case 5:
            beginningEndXPath = '137"]'
        case 4:
            beginningEndXPath = '138"]'
        case 3:
            beginningEndXPath = '139"]'
        case 2:
            beginningEndXPath = '140"]'
        case 1:
            beginningEndXPath = '141"]'

            


    beginningXPath = beginningStartXPath + beginningEndXPath
    
    
    # Change the Beginning Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-15"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-15"]').click()
    except:
        raise ReferenceError('Beginning Date dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, beginningXPath))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, beginningXPath).click()
    except:
        raise ReferenceError('Beginning Date not found. Update the XPATH.')

    
    endStartXPath = '//*[@id="mat-option-'

    endDate = datetime(endYear, endMonth, 1)
    currentDate = datetime(datetime.now().year, datetime.now().month, 1)

    delta = relativedelta(currentDate, endDate)

    deltaDate = delta.months + delta.years * 12

    if deltaDate > 36:
        raise ValueError('Usage is only available for the last three years.')
    elif deltaDate == 0:
        raise ValueError('Usage is not available for the current month.')


    match deltaDate:
        case 36:
            endEndXPath = '142"]'
        case 35:
            endEndXPath = '143"]'
        case 34:
            endEndXPath = '144"]'
        case 33:
            endEndXPath = '145"]'
        case 32:
            endEndXPath = '146"]'
        case 31:
            endEndXPath = '147"]'
        case 30:
            endEndXPath = '148"]'
        case 29:
            endEndXPath = '149"]'
        case 28:
            endEndXPath = '150"]'
        case 27:
            endEndXPath = '151"]'
        case 26:
            endEndXPath = '152"]'
        case 25:
            endEndXPath = '153"]'
        case 24:
            endEndXPath = '154"]'
        case 23:
            endEndXPath = '155"]'
        case 22:
            endEndXPath = '156"]'
        case 21:
            endEndXPath = '157"]'
        case 20:
            endEndXPath = '158"]'
        case 19:
            endEndXPath = '159"]'
        case 18:
            endEndXPath = '160"]'
        case 17:
            endEndXPath = '161"]'
        case 16:
            endEndXPath = '162"]'
        case 25:
            endEndXPath = '163"]'
        case 14:
            endEndXPath = '164"]'
        case 13:
            endEndXPath = '165"]'
        case 12:
            endEndXPath = '166"]'
        case 11:
            endEndXPath = '167"]'
        case 10:
            endEndXPath = '168"]'
        case 9:
            endEndXPath = '169"]'
        case 8:
            endEndXPath = '170"]'
        case 7:
            endEndXPath = '171"]'
        case 6:
            endEndXPath = '172"]'
        case 5:
            endEndXPath = '173"]'
        case 4:
            endEndXPath = '174"]'
        case 3:
            endEndXPath = '175"]'
        case 2:
            endEndXPath = '176"]'
        case 1:
            endEndXPath = '177"]'


    endXPath = endStartXPath + endEndXPath


    # Change the Ending Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-17"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-17"]').click()
    except:
        raise ReferenceError('Ending Date dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, endXPath))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, endXPath).click()
    except:
        raise ReferenceError('Ending Date not found. Update the XPATH.')



    # Generate the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/app-report-dialog-date-selection/div[2]/div[2]/button'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/app-report-dialog-date-selection/div[2]/div[2]/button').click()
    except:
        raise ReferenceError('Generate button not found. Update the XPATH.') 

    print('DR_D1 Downloading. Wait for next report...')
    time.sleep(5)


    # Close the Box
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/app-report-dialog-date-selection/div[1]/mat-icon'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-1"]/div/div/app-report-dialog-date-selection/div[1]/mat-icon').click()
    except:
        raise ReferenceError('Close button not found. Update the XPATH.')   
    





    

    # Download Reports - PR
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/div/app-counter-report/div/mat-card/mat-card-content/button[1]/span[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/div/app-counter-report/div/mat-card/mat-card-content/button[1]/span[2]').click()
    except:
        raise ReferenceError('PR button not found. Update the XPATH.')
    
    
    # Change the Date Range to Custom
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-21"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-21"]').click()
    except:
        raise ReferenceError('Date Range dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-186"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-option-186"]').click()
    except:
        raise ReferenceError('Custom option not found. Update the XPATH.')


    beginningStartXPath = '//*[@id="mat-option-'

    startDate = datetime(startYear, startMonth, 1)
    currentDate = datetime(datetime.now().year, datetime.now().month, 1)

    delta = relativedelta(currentDate, startDate)

    deltaDate = delta.months + delta.years * 12


    if deltaDate > 36:
        raise ValueError('Usage is only available for the last three years.')
    elif deltaDate == 0:
        raise ValueError('Usage is not available for the current month.')


    match deltaDate:
        case 36:
            beginningEndXPath = '186"]'
        case 35:
            beginningEndXPath = '187"]'
        case 34:
            beginningEndXPath = '188"]'
        case 33:
            beginningEndXPath = '189"]'
        case 32:
            beginningEndXPath = '190"]'
        case 31:
            beginningEndXPath = '191"]'
        case 30:
            beginningEndXPath = '192"]'
        case 29:
            beginningEndXPath = '193"]'
        case 28:
            beginningEndXPath = '194"]'
        case 27:
            beginningEndXPath = '195"]'
        case 26:
            beginningEndXPath = '196"]'
        case 25:
            beginningEndXPath = '197"]'
        case 24:
            beginningEndXPath = '198"]'
        case 23:
            beginningEndXPath = '199"]'
        case 22:
            beginningEndXPath = '200"]'
        case 21:
            beginningEndXPath = '201"]'
        case 20:
            beginningEndXPath = '202"]'
        case 19:
            beginningEndXPath = '203"]'
        case 18:
            beginningEndXPath = '204"]'
        case 17:
            beginningEndXPath = '205"]'
        case 16:
            beginningEndXPath = '206"]'
        case 15:
            beginningEndXPath = '207"]'
        case 14:
            beginningEndXPath = '208"]'
        case 13:
            beginningEndXPath = '209"]'
        case 12:
            beginningEndXPath = '210"]'
        case 11:
            beginningEndXPath = '211"]'
        case 10:
            beginningEndXPath = '212"]'
        case 9:
            beginningEndXPath = '213"]'
        case 8:
            beginningEndXPath = '214"]'
        case 7:
            beginningEndXPath = '215"]'
        case 6:
            beginningEndXPath = '216"]'
        case 5:
            beginningEndXPath = '217"]'
        case 4:
            beginningEndXPath = '218"]'
        case 3:
            beginningEndXPath = '219"]'
        case 2:
            beginningEndXPath = '220"]'
        case 1:
            beginningEndXPath = '221"]'

            


    beginningXPath = beginningStartXPath + beginningEndXPath
    
    # Change the Beginning Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-23"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-23"]').click()
    except:
        raise ReferenceError('Beginning Date dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, beginningXPath))) #To ensure the webpage loads before trying//*[@id="mat-option-26"]
        driver.find_element(By.XPATH, beginningXPath).click()
    except:
        raise ReferenceError('Beginning Date not found. Update the XPATH.')


    
    endStartXPath = '//*[@id="mat-option-'

    endDate = datetime(endYear, endMonth, 1)
    currentDate = datetime(datetime.now().year, datetime.now().month, 1)

    delta = relativedelta(currentDate, endDate)

    deltaDate = delta.months + delta.years * 12


    if deltaDate > 36:
        raise ValueError('Usage is only available for the last three years.')
    elif deltaDate == 0:
        raise ValueError('Usage is not available for the current month.')


    match deltaDate:
        case 36:
            endEndXPath = '222"]'
        case 35:
            endEndXPath = '223"]'
        case 34:
            endEndXPath = '224"]'
        case 33:
            endEndXPath = '225"]'
        case 32:
            endEndXPath = '226"]'
        case 31:
            endEndXPath = '227"]'
        case 30:
            endEndXPath = '228"]'
        case 29:
            endEndXPath = '229"]'
        case 28:
            endEndXPath = '230"]'
        case 27:
            endEndXPath = '231"]'
        case 26:
            endEndXPath = '232"]'
        case 25:
            endEndXPath = '233"]'
        case 24:
            endEndXPath = '234"]'
        case 23:
            endEndXPath = '235"]'
        case 22:
            endEndXPath = '236"]'
        case 21:
            endEndXPath = '237"]'
        case 20:
            endEndXPath = '238"]'
        case 19:
            endEndXPath = '239"]'
        case 18:
            endEndXPath = '240"]'
        case 17:
            endEndXPath = '241"]'
        case 16:
            endEndXPath = '242"]'
        case 25:
            endEndXPath = '243"]'
        case 14:
            endEndXPath = '244"]'
        case 13:
            endEndXPath = '245"]'
        case 12:
            endEndXPath = '246"]'
        case 11:
            endEndXPath = '247"]'
        case 10:
            endEndXPath = '248"]'
        case 9:
            endEndXPath = '249"]'
        case 8:
            endEndXPath = '250"]'
        case 7:
            endEndXPath = '251"]'
        case 6:
            endEndXPath = '252"]'
        case 5:
            endEndXPath = '253"]'
        case 4:
            endEndXPath = '254"]'
        case 3:
            endEndXPath = '255"]'
        case 2:
            endEndXPath = '256"]'
        case 1:
            endEndXPath = '257"]'


    endXPath = endStartXPath + endEndXPath

    # Change the Ending Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-25"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-25"]').click()
    except:
        raise ReferenceError('Ending Date dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, endXPath))) #To ensure the webpage loads before trying//*[@id="mat-option-26"]
        driver.find_element(By.XPATH, endXPath).click()
    except:
        raise ReferenceError('Ending Date not found. Update the XPATH.')



    # Generate the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-dialog-2"]/div/div/app-report-dialog-date-selection/div[2]/div[2]/button'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-2"]/div/div/app-report-dialog-date-selection/div[2]/div[2]/button').click()
    except:
        raise ReferenceError('Generate button not found. Update the XPATH.')   


    print('PR Master Report Downloading. Wait for next report...')
    time.sleep(10)


    # Close the Box
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-dialog-2"]/div/div/app-report-dialog-date-selection/div[1]/mat-icon'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-2"]/div/div/app-report-dialog-date-selection/div[1]/mat-icon').click()
    except:
        raise ReferenceError('Close button not found. Update the XPATH.')  

    


    # Download Reports - DR
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/div/app-counter-report/div/mat-card/mat-card-content/button[3]/span[2]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/div/app-counter-report/div/mat-card/mat-card-content/button[3]/span[2]').click()
    except:
        raise ReferenceError('DR button not found. Update the XPATH.')
    
    
    # Change the Date Range to Custom
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-29"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-29"]').click()
    except:
        raise ReferenceError('Date Range dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-option-266"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-option-266"]').click()
    except:
        raise ReferenceError('Custom option not found. Update the XPATH.')


    beginningStartXPath = '//*[@id="mat-option-'

    startDate = datetime(startYear, startMonth, 1)
    currentDate = datetime(datetime.now().year, datetime.now().month, 1)

    delta = relativedelta(currentDate, startDate)

    deltaDate = delta.months + delta.years * 12


    if deltaDate > 36:
        raise ValueError('Usage is only available for the last three years.')
    elif deltaDate == 0:
        raise ValueError('Usage is not available for the current month.')


    match deltaDate:
        case 36:
            beginningEndXPath = '266"]'
        case 35:
            beginningEndXPath = '267"]'
        case 34:
            beginningEndXPath = '268"]'
        case 33:
            beginningEndXPath = '269"]'
        case 32:
            beginningEndXPath = '270"]'
        case 31:
            beginningEndXPath = '271"]'
        case 30:
            beginningEndXPath = '272"]'
        case 29:
            beginningEndXPath = '273"]'
        case 28:
            beginningEndXPath = '274"]'
        case 27:
            beginningEndXPath = '275"]'
        case 26:
            beginningEndXPath = '276"]'
        case 25:
            beginningEndXPath = '277"]'
        case 24:
            beginningEndXPath = '278"]'
        case 23:
            beginningEndXPath = '279"]'
        case 22:
            beginningEndXPath = '280"]'
        case 21:
            beginningEndXPath = '281"]'
        case 20:
            beginningEndXPath = '282"]'
        case 19:
            beginningEndXPath = '283"]'
        case 18:
            beginningEndXPath = '284"]'
        case 17:
            beginningEndXPath = '285"]'
        case 16:
            beginningEndXPath = '286"]'
        case 15:
            beginningEndXPath = '287"]'
        case 14:
            beginningEndXPath = '288"]'
        case 13:
            beginningEndXPath = '289"]'
        case 12:
            beginningEndXPath = '290"]'
        case 11:
            beginningEndXPath = '291"]'
        case 10:
            beginningEndXPath = '292"]'
        case 9:
            beginningEndXPath = '293"]'
        case 8:
            beginningEndXPath = '294"]'
        case 7:
            beginningEndXPath = '295"]'
        case 6:
            beginningEndXPath = '296"]'
        case 5:
            beginningEndXPath = '297"]'
        case 4:
            beginningEndXPath = '298"]'
        case 3:
            beginningEndXPath = '299"]'
        case 2:
            beginningEndXPath = '300"]'
        case 1:
            beginningEndXPath = '301"]'

            


    beginningXPath = beginningStartXPath + beginningEndXPath
    
    # Change the Beginning Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-31"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-31"]').click()
    except:
        raise ReferenceError('Beginning Date dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, beginningXPath))) #To ensure the webpage loads before trying//*[@id="mat-option-26"]
        driver.find_element(By.XPATH, beginningXPath).click()
    except:
        raise ReferenceError('Beginning Date not found. Update the XPATH.')


    
    endStartXPath = '//*[@id="mat-option-'

    endDate = datetime(endYear, endMonth, 1)
    currentDate = datetime(datetime.now().year, datetime.now().month, 1)

    delta = relativedelta(currentDate, endDate)

    deltaDate = delta.months + delta.years * 12


    if deltaDate > 36:
        raise ValueError('Usage is only available for the last three years.')
    elif deltaDate == 0:
        raise ValueError('Usage is not available for the current month.')


    match deltaDate:
        case 36:
            endEndXPath = '302"]'
        case 35:
            endEndXPath = '303"]'
        case 34:
            endEndXPath = '304"]'
        case 33:
            endEndXPath = '305"]'
        case 32:
            endEndXPath = '306"]'
        case 31:
            endEndXPath = '307"]'
        case 30:
            endEndXPath = '308"]'
        case 29:
            endEndXPath = '309"]'
        case 28:
            endEndXPath = '310"]'
        case 27:
            endEndXPath = '311"]'
        case 26:
            endEndXPath = '312"]'
        case 25:
            endEndXPath = '313"]'
        case 24:
            endEndXPath = '314"]'
        case 23:
            endEndXPath = '315"]'
        case 22:
            endEndXPath = '316"]'
        case 21:
            endEndXPath = '317"]'
        case 20:
            endEndXPath = '318"]'
        case 19:
            endEndXPath = '319"]'
        case 18:
            endEndXPath = '320"]'
        case 17:
            endEndXPath = '321"]'
        case 16:
            endEndXPath = '322"]'
        case 25:
            endEndXPath = '323"]'
        case 14:
            endEndXPath = '324"]'
        case 13:
            endEndXPath = '325"]'
        case 12:
            endEndXPath = '326"]'
        case 11:
            endEndXPath = '327"]'
        case 10:
            endEndXPath = '328"]'
        case 9:
            endEndXPath = '329"]'
        case 8:
            endEndXPath = '330"]'
        case 7:
            endEndXPath = '331"]'
        case 6:
            endEndXPath = '332"]'
        case 5:
            endEndXPath = '333"]'
        case 4:
            endEndXPath = '334"]'
        case 3:
            endEndXPath = '335"]'
        case 2:
            endEndXPath = '336"]'
        case 1:
            endEndXPath = '337"]'


    endXPath = endStartXPath + endEndXPath

    # Change the Ending Date
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-select-value-33"]'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-select-value-33"]').click()
    except:
        raise ReferenceError('Ending Date dropdown not found. Update the XPATH.')

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, endXPath))) #To ensure the webpage loads before trying//*[@id="mat-option-26"]
        driver.find_element(By.XPATH, endXPath).click()
    except:
        raise ReferenceError('Ending Date not found. Update the XPATH.')



    # Generate the Report
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-dialog-3"]/div/div/app-report-dialog-date-selection/div[2]/div[2]/button'))) #To ensure the webpage loads before trying
        driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-3"]/div/div/app-report-dialog-date-selection/div[2]/div[2]/button').click()
    except:
        raise ReferenceError('Generate button not found. Update the XPATH.')   
    
    
    
        

    keyword = input('DR Master Report downloading. Once it appears in Downloads, type anything here to close the browser.')  


def ISIWebofScience_Info():
    print('Input keys needed:')
    print('Start month: A number from 1-12.')
    print('Start year: Can only go back a maximum of 3 years from the current date.')
    print('End month: A number from 1-12.')
    print('End year: Can only go back a maximum of 3 years from the current date.')
    print('')
    print('This code downloads the following reports: PR_P1, DR_D1, PR, DR.')