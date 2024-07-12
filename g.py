from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from data import writedict_csv

url = 'https://ipindiaonline.gov.in/eregister/Application_View.aspx'
temp = []
wd = webdriver.Chrome()



for i in range(701):
    wd.get(url)
    try:
        wd.find_element(By.XPATH,'//*[@id="rdb_0"]').click()

        wd.find_element(By.XPATH,'//*[@id="applNumber"]').send_keys(str(1000000+ i))
        
        while (wd.find_element(By.XPATH,'//*[@id="captcha1"]').get_attribute('value') == ''):
            print()
            wd.find_element(By.XPATH,'//*[@id="captcha1"]').click()
        time.sleep(5)
        
        break

        wd.find_element(By.XPATH,'//*[@id="btnView"]').click()
        
        WebDriverWait(wd,2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="SearchWMDatagrid_ctl03_lnkbtnappNumber1"]')))
    #'//*[@id="SearchWMDatagrid_ctl03_lnkbtnappNumber1"]'
        wd.find_element(By.XPATH,'//*[@id="SearchWMDatagrid_ctl03_lnkbtnappNumber1"]').click()
    #//*[@id="lblappdetail"]/table[2]/tbody/tr[1]/td[1]/b/font
        a = wd.find_element(By.XPATH,'//*[@id="lblappdetail"]/table[2]/tbody/tr[1]/td[1]/b/font').get_attribute('innerHTML')
    #//*[@id="lblappdetail"]/table[2]/tbody/tr[2]/td[1]/font[2]/b
        b = wd.find_element(By.XPATH,'//*[@id="lblappdetail"]/table[2]/tbody/tr[2]/td[1]/font[2]/b').get_attribute('innerHTML')
    #'//*[@id="lblappdetail"]/table[4]/tbody/tr')
        l = wd.find_elements(By.XPATH,'//*[@id="lblappdetail"]/table[@style="font-size=larger; background-color:mintcream;"]/tbody/tr/td[2]')
        #if wd.find_elements(By.XPATH,'//*[@id="lblappdetail"]/table[3]/tbody/tr/td[2]')
        #l = wd.find_elements(By.XPATH,'//*[@id="lblappdetail"]/table[3]/tbody/tr/td[2]')
        #l = wd.find_elements(By.XPATH,'//*[@id="lblappdetail"]/table[4]/tbody/tr/td[2]')
        #l = wd.find_elements(By.XPATH,'//*[@id="lblappdetail"]/table[5]/tbody/tr/td[2]')
        #
        for i in range(len(l)):
            x = l[i].get_attribute('innerHTML')
            if '<br>' in x:
                x.replace('<br>','')
            temp.append(x)
    
        temp.append(a)
        temp.append(b)
        break
        try:
            w = writedict_csv(temp)
        except PermissionError:
            pass
        
        
        temp = []
        
        
    
    except selenium.common.exceptions.UnexpectedAlertPresentException as s:
        pass


    
    
    
    
        
            

    
       
        
    
        
        

