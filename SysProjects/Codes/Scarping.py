from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
import timeit
import time
import csv
from urllib3 import request

serv: Service = Service(binary_path)
job_title:str = 'Python Developer'.replace(' ', '%20')
location:str = 'German'.replace(' ', '%20')
num_of_pages: int = 1
url:str = f'''https://www.linkedin.com/jobs/search?keywords={job_title}&location={location}&geoId=103644278&trk=public_jobs_jobs-search-bar_search\-submit&position=1&pageNum={num_of_pages}'''

Xpath: str = ''
outer_selector: str = 'base-serp-page'
inner_selector: str = 'ul li h3'

file_name: str = f'report_{location.replace('%20','_')}.csv'
file_header: list[str]= ['number', 'Job Tilte', 'Company Name', 'Location', 'Registered Time', 'Employment Type', 'Seniority Level']
driver = webdriver.Chrome(service=serv, keep_alive=True)
driver.maximize_window()
t1 = timeit.default_timer()
driver.get(url)
# time.sleep(10)
# itirator = driver.find_elements(By.CSS_SELECTOR, '#main-content > section.two-pane-serp-page__results-list > ul')
# print(len(itirator[0]))

with open(file_name, 'w', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(file_header)
    time.sleep(5)
    for i in range (1, 26):
        
        section = driver.find_element(By.XPATH, f'//*[@id="main-content"]/section[2]/ul/li[{i}]/div/a').click()
        time.sleep(5) 
        details = driver.find_element(By.CSS_SELECTOR, '.two-pane-serp-page__detail-view')
        title_ = details.find_element(By.TAG_NAME, 'h2').text

        spans = details.find_elements(By.TAG_NAME, 'span')

        comp_name = spans[0].find_element(By.TAG_NAME, 'a').text
        loc_ = spans[1].text
        reg_time =spans[2].text

        emp_type = details.find_element(By.CSS_SELECTOR, 'div.details-pane__content.details-pane__content--show > div > section.core-section-container.my-3.description > div > ul > li:nth-child(2) > span').text
        seni_lvl = details.find_element(By.CSS_SELECTOR, 'div.details-pane__content.details-pane__content--show > div > section.core-section-container.my-3.description > div > ul > li:nth-child(1) > span').text
        # decription =details.find_element(By.CSS_SELECTOR, 'div.details-pane__content.details-pane__content--show > div > section.core-section-container.my-3.description > div > div > section > div')
        # describe_ = decription.text
        writer.writerow([i, title_, comp_name, loc_, reg_time, emp_type, seni_lvl])
t2 = timeit.default_timer()
print(f'Data fetch in {t2-t1} s')
    
    
driver.quit()