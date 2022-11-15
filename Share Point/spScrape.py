from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from xlwt import Workbook
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
import time
from spApplicantInfo import*
from Paste import*

#Login Credentials
username = 'stran@advantechglobal.org'
password = 'steventran2022$'
query = '(system OR network OR systems) AND (administrator OR admin OR validate OR validation OR validator) AND (test OR testing OR tested OR tester OR troubleshooting OR troubleshoot OR troubleshot) AND (ACAS OR SCAP OR LAN OR LANs) AND (STIGs OR STIG OR a&a OR authentication OR authorization OR access OR assurance OR compliance OR implementaqtion) AND (putty OR winscp OR securecrt) AND (cyber OR security) AND (windows OR unix)'

#Start runtime timer
start = time.time()

def countdown(t):
    while t != 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Time left: " + timer, end="\r")
        time.sleep(1)
        t -= 1
        
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
    actions.send_keys(Keys.DOWN)
    actions.send_keys(Keys.UP)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    
    content = []
    i = 0
    repeat = False
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
             
            if ':x:' in url:
                text = 'EXCEL FILE'
            elif 'Intvw%20Checklist' in url:
                for x in range(4):
                    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    time.sleep(0.25)
                actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
                text = paste()
            else:
                for x in range(3):
                    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    time.sleep(0.25)
                actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
                text = paste()
            
            content.append(text)
            driver.close()
            # inputting content into google language processor
            # Samuel and Joey try to figure out how to get this part to work
            # driver.get("https://cloud.google.com/natural-language")
            # driver.find_element(By.CLASS_NAME, "inputs reset")
            # driver.send_keys(content)
            # driver.find_element(By.CLASS_NAME, "inputs reset").click()

            # once you figure that out try to extract the names, emails, numbers into excel
            driver.switch_to.window(tabs[0])

        else:
            #No New Tab
            time.sleep(1)# Prevents the url check from checking before the link is changed
            url = driver.current_url
            urls.append(url)
            print(str(i + 1) + ": " + url)
            
            if 'msg' in url:
                print('HIT MSG-----------')
                actions.send_keys(Keys.TAB)
                actions.send_keys(Keys.TAB)
                actions.perform()
                for x in range(10):
                    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
                text = paste()
                driver.find_elements(By.CLASS_NAME, 'ms-Button-icon')[20].click()     
            elif 'html' in url:
                print('HIT HTML-----------')
                actions.send_keys(Keys.TAB)
                actions.send_keys(Keys.TAB)
                actions.perform()
                for x in range(10):
                    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
                text = paste()
                driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/div[4]/div/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div[3]/div[6]/button/span/i').click()
            else:
                try:
                    driver.find_elements(By.CLASS_NAME, 'ms-Button-menuIcon')[4].click()
                    driver.find_element(By.NAME, 'Open in browser').click()
                    time.sleep(1)
                    driver.switch_to.window(driver.window_handles[1])
                    for x in range(10):
                        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                        actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
                    text = paste()

                    driver.close()
                    driver.switch_to.window(tabs[0])
                except:
                    text = 'INVALID FILE'
            
            content.append(text)
            actions.send_keys(Keys.ESCAPE)
            actions.perform()
                
        #Checks if the last two urls are the same
        if (len(urls) > 1) and (urls[-1] == urls[-2]):
            print('---------------REPEATING LINK ALERT!---------------') # Don't worry about this the following code will fix it and continue
            if repeat:
                break
            repeat = True
            countdown(3) # Wait for the page to load (need tweaking)
            # Reintialize the pointer to the next element
            content.pop()
            urls.pop()
            driver.find_element(By.CLASS_NAME, 'root-125').click()
            actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.RETURN)
            actions.perform()
            continue
        else:
            repeat = False

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
    s1.write(row, 0, 'URL')
    s1.write(row, 1, 'File Type')
    s1.write(row, 2, 'File Name')
    s1.write(row, 3, 'URL - Names')
    s1.write(row, 4, 'Content - Names')
    s1.write(row, 5, 'Content - Email')
    s1.write(row, 6, 'Content - Phone')

    wb.save('spScrape_' + date.today().strftime("%m_%d_%Y") + '.csv')
    row += 1    

    #Populate parallel arrays
    #content array initialized in line 70
    links = []
    ftypes = []
    fnames = []
    spacyNameUrl = [] #2D array (each url has list of names)
    spacyNameContent = []
    spacyEmail = []
    spacyPhone = []
    while len(urls) != 0:
        print('REMAINING: ' + str(len(urls)))
        links.append(urls[0])
        filetype = 'OTHER'
        filename = ''
        if(':w:' in urls[0]):
            filetype = 'Word'
            filename = urls[0].split('file=')[1].split('&action')[0].replace('%20', ' ').replace('%23', '#').replace('%5B', ' ').replace('%5D', ' ').replace('-', ' ').replace('_', ' ').replace('.', ' ').replace('(', ' ').replace(')', ' ')
        elif ':x:' in urls[0]:
            filetype = 'Excel'
            filename = urls[0].split('file=')[1].split('&action')[0].replace('%20', ' ').replace('%23', '#').replace('%5B', ' ').replace('%5D', ' ').replace('-', ' ').replace('_', ' ').replace('.', ' ').replace('(', ' ').replace(')', ' ')
        else: #WORK IN PROGRESS (getting file name of OTHER file types)
            filename = urls[0].split('.aspx?')[1].split('&q=')[0].replace('%20', ' ').replace('%23', '#').replace('%5B', ' ').replace('%5D', ' ').replace('-', ' ').replace('_', ' ').replace('.', ' ').replace('(', ' ').replace(')', ' ').replace('%2F', ' ').replace('%2B', ' ').replace('%2E', ' ').replace('%5F', ' ').replace('%2D', ' ')
        ftypes.append(filetype)
        fnames.append(filename)
        spacyNameUrl.append(name_scrape(filename))
        spacyNameContent.append(name_scrape(content[0]))
        spacyEmail.append(email_scrape(content[0]))
        spacyPhone.append(phone_scrape(content[0]))
        del urls[0]
        del content[0]

    #Print to Excel
    while len(links) != 0:
        if 'AllItems.aspx?q=' in links[0]: #If link is not main Sharepoint page, print
            del links[0]
            del ftypes[0]
            del fnames[0]
            del spacyNameUrl[0]
            del spacyNameContent[0]
            del spacyEmail[0]
            del spacyPhone[0]
            continue

        s1.write(row, 0, links[0])
        s1.write(row, 1, ftypes[0])
        s1.write(row, 2, fnames[0])
    # Remove dupes from excel sheet






        #Print spacyNameUrl
        snu = ''
        spacyNameUrl[0] = [*set(spacyNameUrl[0])]
        while(len(spacyNameUrl[0]) != 0):
            #Manual Filter
            snu += spacyNameUrl[0][0].replace('Intvw Checklist', '').replace('RESUMES', '') + ', '
            del spacyNameUrl[0][0]
        snu = snu[:-2]
        s1.write(row, 3, snu)

        #Print spacyNameContent
        snc = ''
        spacyNameContent[0] = [*set(spacyNameContent[0])]
        while(len(spacyNameContent[0]) != 0):
            if 'Jacquelyn Fraser' not in spacyNameContent[0][0]:
                snc += spacyNameContent[0][0] + ', '
            del spacyNameContent[0][0]
        snc = snc[:-2]
        s1.write(row, 4, snc)

        #Print spacyEmail
        se = ''
        spacyEmail[0] = [*set(spacyEmail[0])]
        while(len(spacyEmail[0]) != 0):
            #Manual Filter
            if 'ptoro' not in spacyEmail[0][0] and 'cbrown' not in spacyEmail[0][0] and 'fraser' not in spacyEmail[0][0] and 'no_reply' not in spacyEmail[0][0]:
                se += spacyEmail[0][0] + ', '
            del spacyEmail[0][0]
        se = se[:-2]
        s1.write(row, 5, se)

        #Print spacyPhone
        sp = ''
        spacyPhone[0] = [*set(spacyPhone[0])]
        while(len(spacyPhone[0]) != 0):
            #Manual Filter
            if count_ints(spacyPhone[0][0]) == 10 or count_ints(spacyPhone[0][0]) == 11:
                sp += spacyPhone[0][0] + ', '
            del spacyPhone[0][0]
        sp = sp[:-2]
        s1.write(row, 6, sp)

        del links[0]
        del ftypes[0]
        del fnames[0]
        del spacyNameUrl[0]
        del spacyNameContent[0]
        del spacyEmail[0]
        del spacyPhone[0]
        row += 1

    wb.save('spScrape_(' + str(row - 1) + 'apps)_' + date.today().strftime("%m_%d_%Y") + '.csv')

bot(username, password, query)

#Record and ouput runtime
end = time.time()
print('PROGRAM RUNTIME: ' + str(end - start))
