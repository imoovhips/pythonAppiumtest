from appium import webdriver
from selenium.webdriver.common.by import By

# путь к нашему приложению:
# /Users/imoovhips/PycharmProjects/pythonAppium/app/preprod-0.46.4.0.apk

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "emulator-5554",
    "app": "/Users/imoovhips/PycharmProjects/pythonAppium/app/2gis.apk",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

# com.android.permissioncontroller:id/permission_allow_foreground_only_button

driver.implicitly_wait(5)

driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
driver.quit()