from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date
import time
import os


#Get user name
user_ = os.getlogin()
print(user_)

#Get the current date in correct format
today = date.today()
today_ = today.strftime('%m-%d-%Y')
file_name = "Aging data "

#Resources
driver_path = rf"C:\Users\{user_}\Eaton\CRDS RWD MCB Haina Plant - Documents\Data management\Python\msedgedriver.exe"
url = "https://app.powerbi.com/groups/be617f5d-66b5-4cfb-a9c5-4981efdbceee/reports/9fbe302d-b7b5-46f5-b61c-bef7adadbdbf/ReportSectiondc8f1378e786b816b3a2?ctid=d6525c95-b906-431a-b926-e9b51ba43cc4&filter=Reports%2FReportGuid%20eq%20%279fbe302d-b7b5-46f5-b61c-bef7adadbdbf%27"
xpath_visual = "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div[1]/div/report/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[2]/transform/div/div[2]/div/visual-modern/div"
xpath_three_dots = "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div[1]/div/report/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[2]/transform/div/visual-container-header/div/div/div/visual-container-options-menu/visual-header-item-container/div/button/i"
xpath_export_1 = "/html/body/div[3]/div[3]/div/ng-component/pbi-menu/button[3]/span"
xpath_export_2 = "/html/body/div[3]/div[3]/div/mat-dialog-container/export-data-dialog/mat-dialog-actions/button[1]"

#
driver = webdriver.Edge(executable_path = driver_path)
driver.get(url)

#
print("Starting driver")
time.sleep(25)

button = driver.find_element(by=By.XPATH, value = xpath_visual)
button.click()
time.sleep(10)

button = driver.find_element(by=By.XPATH, value = xpath_three_dots)
button.click()
time.sleep(10)

button = driver.find_element(by=By.XPATH, value = xpath_export_1)
button.click()
time.sleep(10)

button = driver.find_element(by=By.XPATH, value = xpath_export_2)
button.click()
time.sleep(10)

os.rename(rf"C:\Users\{user_}\Downloads\data.xlsx" , rf"C:\Users\{user_}\Eaton\CRDS RWD MCB Haina Plant - Documents\Data management\PBI Dashboard\PBIX File\Posted in workspace\MCB - Other Metrics\CI\Programa Kaizen y Segerencia\Aging historical data\{file_name} {today_}.xlsx")

print("Done! ✅")