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
file_name = "Action Tracker Historical "


#Resources
driver_path = rf"C:\Users\{user_}\Eaton\CRDS RWD MCB Haina Plant - Documents\Data management\Python\msedgedriver.exe"
url = "https://app.powerbi.com/groups/be617f5d-66b5-4cfb-a9c5-4981efdbceee/reports/3aacb03b-adb4-489c-b1be-bc6d618718f0/ReportSectionfc183199feb2108949d4?ctid=d6525c95-b906-431a-b926-e9b51ba43cc4"
xpath_visual = "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div[1]/div/report/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[3]/transform/div/div[2]/div"
xpath_three_dots = "/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/div/div[1]/div/report/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[3]/transform/div/visual-container-header/div/div/div/visual-container-options-menu/visual-header-item-container/div/button/i"
xpath_export_1 = "/html/body/div[3]/div[3]/div/ng-component/pbi-menu/button[3]/span"
xpath_export_2 = "/html/body/div[3]/div[3]/div/mat-dialog-container/export-data-dialog/mat-dialog-actions/button[1]"

#
driver = webdriver.Edge(executable_path = driver_path)
driver.get(url)
# driver.minimize_window()

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

os.rename(rf"C:\Users\{user_}\Downloads\Action Tracker Historical.xlsx" , rf"C:\Users\{user_}\Eaton\CRDS RWD MCB Haina Plant - Documents\Data management\PBI Dashboard\PBIX File\Posted in workspace\MCB - Other Metrics\CI\Action Tracker\Action Tracker Historical\{file_name} {today_}.xlsx")

print("Done! ✅")