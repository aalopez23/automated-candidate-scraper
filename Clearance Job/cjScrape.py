#Authors: Noah Jaungue, Steven Tran, Henry Luu, Jonathan Nguyen, Antonio Lopez

from encodings import search_function
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from xlwt import Workbook
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

start = time.time()
random.seed(None, 2)
def delay():
    return random.randint(3,6)

#USER INPUTS
#Logins: (Ptage92121, Advantech2022$) // (cba92037, g#M8q2qQ)

username = 'cba92037'
password = 'g#M8q2qQ'
query = 'Collect, process and analyze construction program data to present current and forecasted schedule and financial information in the form of reports, data tables and graphs combined within presentations or reports. Conduct data analytics using proprietary systems, exported data, complicated multi-sheet Excel documents, Pivot tables, timelines, trends, and interdependencies for leadership and stakeholders to incorporate into decision-making process. Distribute output reports to leadership and operations groups utilizing multiple tools including email, SharePoint, and Flank Speed to ensure outbound communication is effective and timely. Maintain, update, and improve complicated Excel documents to adjust for new projects, change in project grouping, modification to client business rules and gov’t financial fiscal year changes. Calculate Work in Progress (WIP) totals to compare with plan (budget), Schedule Performance Index, Cost Performance Index, in addition to several KPIs utilizing data collected from multiple systems and sources and populate tables and forms to present to the client, including Requests for Information, Proposed Changes, Project Modifications, Cost and Time Growth. Create Excel Queries to automate client’s needs to expedite dynamic report and filtration processes to locate anomalies and manage by exception any errors that surface. Review with Project Controls personnel any changes to project forecasts and completion times to advice and adjust Excel systems to correctly calculate Cost Growth, Time Growth and other KPIs and parameters.'
search_type = False #----TRUE = Boolean, FALSE = Intellisearch----

def bot(username, password, query):
    #Create Driver
    options = Options()
    options.add_argument('--incognito')
    options.binary_location = '/Applications/Google Chrome.app'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    
    #Open Clearance Jobs
    driver.get('https://www.clearancejobs.com/login')
    time.sleep(delay())
    
    #Login
    fields = driver.find_elements(By.CLASS_NAME, 'el-input__inner')
    fields[0].send_keys(username)
    time.sleep(delay())
    fields[1].send_keys(password)
    time.sleep(delay())
    driver.find_element(By.CLASS_NAME, 'btn-submitForm').click()
    time.sleep(delay())

    #Boolean Search Page, w/ Query
    if search_type:
        driver.get('https://www.clearancejobs.com/resumes/advanced-search/boolean')
    else:
        driver.get('https://www.clearancejobs.com/resumes/advanced-search/')


    time.sleep(delay())
    driver.find_element(By.CLASS_NAME, 'cj-textarea__inner').send_keys(query)
    time.sleep(delay())
    time.sleep(20) #Extra Time to Input Location
    driver.find_element(By.CLASS_NAME, 'btn-info').click()
    time.sleep(delay())

    #Change to 50 per page
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/div/span').click()
    
    time.sleep(delay())
    driver.find_element(By.XPATH, '//*[text()="50 per page"]').click()
    time.sleep(10)

    #Create Workbook
    wb = Workbook()
    row = 0
    s1 = wb.add_sheet('S1')
    s1.write(row, 0, "URL")
    s1.write(row, 1, "Name")
    s1.write(row, 2, "Phone Number")
    s1.write(row, 3, "E-Mail")
    s1.write(row, 4, "Title")
    s1.write(row, 5, "Clearance")
    s1.write(row, 6, "YOE")
    s1.write(row, 7, "Relocation?")
    s1.write(row, 8, "Salary")
    s1.write(row, 9, "Highest Degree")
    s1.write(row, 10, "Military Branch")
    s1.write(row, 11,"Ideal Locations")
    s1.write(row, 12,"Last Profile Update")
    row += 1

    #Call wbPush() for each CJ page
    sum = 0
    while row >= 0:
        row = pagePush(driver, wb, s1, row)
        sum += row

    wb.save('cjScrape_(' + str(sum) + 'apps)_' + date.today().strftime("%m_%d_%Y") + '.csv')


#Push applicant data (50 apps) from one CJ page, push to Workbook
def pagePush(driver, wb, s1, row):
    listURL = driver.current_url
    #Retrieve all applicant URLs
    apps = driver.find_elements(By.CLASS_NAME, 'resume-search-candidate-card-desktop__name')
    pg = 0
    urls = []

    while(pg < len(apps)):
        print(apps[pg].get_attribute('href'))
        urls.append(apps[pg].get_attribute('href'))
        pg += 1
    print('# of Applicants: ' + str(len(apps)))

    #Loop through apps
    pg = 0
    while(pg < len(apps)):
        #Open applicant page
        print('---------- READING: ' + str(row) + ' ----------')
        print('URL: ' + urls[pg])
        driver.get(urls[pg])
        time.sleep(random.randint(6,8))

        #Get list of desired info [url, name, phone, email, title, clearance, YOE, relo, salary, degree, branch, ideal locations, last update]
        s1.write(row, 0, urls[pg])
        try: #NAME
            name = driver.find_element(By.CLASS_NAME, 'profile-name').text
            print(name)
            s1.write(row, 1, name)
        except:
            print('No Name')
        try: #PHONE
            phone = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[4]/div/div[2]/div/div[4]/div/div[2]/span').text
            if phone == 'No mobile phone':
                phone = ''
            print(phone)
            s1.write(row, 2, phone)
        except:
            print('EXCEPT: No mobile phone')
        try: #EMAIL
            email = driver.find_elements(By.CLASS_NAME, 'cj-data-field__value')[14].text
            print(email)
            s1.write(row, 3, email)
        except:
            print('EXCEPT: No Email')
        try: #TITLE
            title = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[3]/span').text
            print(title)
            s1.write(row, 4, title)
        except:
            print("EXCEPT: No Title")    
        try: #CLEARANCE
            clear = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div/div[1]/span').text
            print(clear)
            s1.write(row, 5, clear)
        except:
            print("EXCEPT: No Clearance")
        try: #YEARS OF EXPERIENCE
            yoe = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[2]/div/div[2]/div/div[1]/div/div[2]/span').text
            print(yoe)
            s1.write(row, 6, yoe)
        except:
            print("EXCEPT: No YOE")
        try: #RELOCATION
            relo = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[5]/div/div[2]/div/div[1]/div/div[2]/span').text
            print(relo)
            s1.write(row, 7, relo)
        except:
            print("EXCEPT: No Relocation Preference")
        try: #SALARY
            salary = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div[2]/span').text
            print(salary)
            s1.write(row, 8, salary)
        except:
            print("EXCEPT: No Salary")      
        try: #HIGHEST DEGREE
            degree = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div/div[2]/div[1]/div[5]/div/div[2]/span').text
            print(degree)
            s1.write(row, 9, degree)
        except:
            print("EXCEPT: No Highest Degree")
        try: #MILITARY BRANCH
            branch = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div/div[2]/div[1]/div[7]/div/div[2]/span').text
            print(branch)
            s1.write(row, 10, branch)
        except:
            print("EXCEPT: No Military Branch")
        try: #IDEAL LOCATIONS
            location = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[5]/div/div[2]/div/div[3]/div/div[2]/span').text
            print(location)
            s1.write(row, 11, location)
        except:
            print("EXCEPT: No Ideal Locations")
        try: #LAST UPDATE
            update = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div[5]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            print(update)
            s1.write(row, 12, update)
        except:
            print("EXCEPT: No Last Update")                                                                                                        
        wb.save('cjScrape22_' + date.today().strftime("%m_%d_%Y") + '.csv')

        pg += 1
        row += 1

    #Move to next page of applicants, using URL substring
    last = int(listURL[-1])
    last += 1
    listURL = listURL[0: len(listURL) - 1] + str(last)
    driver.get(listURL)
    time.sleep(10)

    #Check if last page
    if len(apps) < 50:
        row = -1
    return row

bot(username, password, query)

#Record and ouput runtime
end = time.time()
print('PROGRAM RUNTIME: ' + str(end - start))