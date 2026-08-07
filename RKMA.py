def RKMA():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    import pandas as pd
    import time
    # RKMA
    
    # Input the URL for the main website here
    vendorURL = 'http://www.rkma.com/utk/usageStats/'
    
    
    driver = webdriver.Edge()
    
    
    # Log into the website
    driver.get(vendorURL)
    
    
    
    # Web Scrape the Monthly Usage Statistics Table
    try:
        table_XPath = '/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/'
        num_rows = len(driver.find_elements(by='xpath', value=table_XPath + 'tr')) + 1
        num_cols = len(driver.find_elements(by='xpath', value=table_XPath + 'tr[2]/td')) + 1
        
        table = []
        for row in range(2,num_rows):
                row_data = []
                for col in range(1, num_cols):
                    text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row}]/td[{col}]').text
                    row_data.append(text)
                table.append(row_data)
            
        df = pd.DataFrame(table)
        
        # Clean up the scraped table
        df = df.rename(columns = {0: 'Month', 1: 'Views'})
        
        # Export to a TSV file
        df.to_csv('RKMA-DB.tsv', sep = '\t', index = False)
    except:
        raise ReferenceError('Data table not found. Update the XPATH.')

    keyword = input('When the TSV appears in the folder, type anything here to close the browser.')

    driver.close()

def RKMA_Info():
    print('No input keys needed.')
    print('')
    print('This code only works at UTK. The VPN does not work to access this.')