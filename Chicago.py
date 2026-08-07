def Chicago():
    # Chicago Manual of Style
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    import math
    import getpass

    # Input the URL for the main website here
    vendorURL = 'http://reports.chicagomanualofstyle.com/inst/inst.html'
    
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
        driver.find_element(By.XPATH, '//*[@id="inst-user"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="inst-pwd"]').send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="submitBtn"]').click()
    except:
        raise ReferenceError('Login page not found. Double-check the URL in the code. If it is correct, then update the XPATH.')

    
    # Web Scrape the Tables

    try:
        table_XPath = '//*[@id="main"]/div/div/div[1]/'
        
        ## On this website, each year is put into its own table. The [1] above represents the current year, [2] is last year, etc. all the way back to 2010.
        ## If looking at past years, change the [1] accordingly.
        
        
        ##CHANGE THE NUMBER OF ROWS BELOW
        num_rows = 8
        ##The number of rows should be the number of finished months in the date range you are scraping, plus 2 per year (one for the title at the top of the year, one for the Calendar YTD information at the bottom of the year).
            ##Note: 2010 only starts in September. The current month will not be in the data, but needs to be included in the count.
        
        num_cols = 2
        
        
        table = []
        for row in range(1,num_rows + 1): ##The end of the range should be the number of rows, plus 1 due to Python formatting.
        
        
            row_XPath = table_XPath + 'div[' + str(row) + ']'
            row_data = []
            if math.remainder(row, num_rows) == 1: #The first row, which will be used for column titles
                row_data = ['Publisher', 'The University of Chicago Press']
            else:
                for col in range(1, num_cols + 1):
                    text = driver.find_element(by='xpath', value=row_XPath + '/div[' + str(col) + ']').text
                    row_data.append(text)
            table.append(row_data)
            
        df = pd.DataFrame(table)
    except:
        raise ReferenceError('Usage data not found. Double-check the login information in the code. If it is correct, update the table web-scraping code.')
    
    df
    
    
    df.to_excel('Chicago-DB.xlsx', index = False)

    keyword = input('When the Excel file appears in the Python function list, type anything here to close the browser.')

    driver.close()


def Chicago_Info():
    print('No keys needed.')
    print('')
    print('The underlying code will need to be updated depending on the window of time you are downloading. Use the comments shown in the code to make the necessary changes.')
    print('The report will download as an Excel file appearing in the Jupyter Notebook List to the left of the screen.')