from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from xlwt import Workbook
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from playsound import playsound

#Login Credentials
username = 'stran@advantechglobal.org'
password = 'steventran2022$'
query = '("system administrator" OR "systems administrator" OR "IT" OR "Information Technology" OR 3c0 OR desktop OR user OR network) AND (norfolk OR virginia beach"" OR hampton OR chesapeake OR oceana OR "dam neck" OR "va beach" OR "deer creek" OR portsmouth OR "indian river" OR "great neck" OR 757)'

#Start runtime timer
start = time.time()

def countdown(t):
    while t != 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Time left: " + timer, end="\r")
        time.sleep(1)
        t -= 1
    print('The load period has ended')
        
t = 50
def bot(username, password, query):
    #Create Driver
    options = Options()
    options.binary_location = '/Applications/Google Chrome.app'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    actions = ActionChains(driver)
    driver.maximize_window()

    #Open Sharepoint
    driver.get('https://advantechgsenterprisesinc.sharepoint.com/HR/TR/RESUMES%20%20INTERVIEWS/Forms/AllItems.aspx')
    time.sleep(1)

    #Microsoft Login
    driver.find_element(By.NAME, 'loginfmt').send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(1)
    driver.find_element(By.NAME, 'passwd').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, 'idSIButton9').click()
    time.sleep(1)
    driver.find_element(By.ID, 'idSIButton9').click()    

    #Search Query
    driver.find_element(By.TAG_NAME, 'INPUT').send_keys(query)
    driver.find_element(By.TAG_NAME, 'INPUT').send_keys(Keys.RETURN)
    time.sleep(5)

    #Go to first file
    urls = []
    #Selecting the list and the not the specific element
    # Don't ask why it works but it works
    driver.find_element(By.CLASS_NAME, "root-125").click()
    actions.send_keys(Keys.DOWN)
    actions.send_keys(Keys.DOWN)
    actions.send_keys(Keys.UP)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    
    i = 0
    while(True):
        tabs = driver.window_handles
        time.sleep(3)
        if len(tabs) >= 2:
            #Base Case (There is a New Tab)
            driver.switch_to.window(tabs[1])
            time.sleep(1)
            url = driver.current_url
            urls.append(url)
            print(str(i + 1) + ": " + url)
            driver.close()
            driver.switch_to.window(tabs[0])

        else:
            #No New Tab
            time.sleep(2)# Prevents the url check from checking before the link is changed
            url = driver.current_url
            urls.append(url)
            print(str(i + 1) + ": " + url)
            actions.send_keys(Keys.ESCAPE)
            actions.perform()

        #Checks if the last url two urls are the same
        if (len(urls) > 1) and (urls[-1] == urls[-2]):
            print('---------------REPEATING LINK ALERT!---------------') # Don't worry about this the following code will fix it and continue
            playsound('mixkit-positive-notification-951.mp3')
            #urls = urls[len(urls) - 2] # Removes the last two elements from the list (NOT WORKING)
            #i -= 2 # Taking the last two elements from the counter (NOT WORKING)
            countdown(20) # Wait for the page to load (need tweaking)
            print('Wait for the load is done')
            # Reintialize the pointer to the next element
            driver.find_element(By.CLASS_NAME, "root-125").click()
            # TODO: Fix the previous two links not being recorded
            actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.UP)
            actions.send_keys(Keys.RETURN)
            actions.perform()

        if (len(urls) > 1) and (urls[-1] == urls[-2] == urls[-3]):
            break

        actions.send_keys(Keys.DOWN)
        print('DOWN')
        actions.send_keys(Keys.RETURN)
        print('RETURN')
        actions.perform()
        i += 1

    nodupes = [*set(urls)]
    print('# OF LINKS, NO DUPES: ' + str(len(nodupes)))

    #Export to Excel
    wb = Workbook()
    row = 0
    s1 = wb.add_sheet('S1')
    s1.write(row, 0, "URL")
    wb.save('spScrape_' + date.today().strftime("%m_%d_%Y") + '.csv')
    row += 1    

    while len(nodupes) != 0:
        s1.write(row, 0, nodupes[0])
        filetype = 'OTHER'
        if(':w:' in nodupes[0]):
            filetype = 'Word'
        elif ':x:' in nodupes[0]:
            filetype = 'Excel'
        s1.write(row, 1, filetype)
        del nodupes[0]
        row += 1

    wb.save('spScrape_(' + str(row - 1) + 'apps)_' + date.today().strftime("%m_%d_%Y") + '.csv')

        
        



bot(username, password, query)

#Record and ouput runtime
end = time.time()
print('PROGRAM RUNTIME: ' + str(end - start))

