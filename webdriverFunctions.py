import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# System folder
currentFolder = os.path.dirname(os.path.abspath(__file__))
opSys = "windows" if "windows" in platform.platform().lower() else "linux"
pathSep = "\\" if opSys == "windows" else "/"

# Specific folder things
screenshotsPath = currentFolder + pathSep + "screenshots" + pathSep
chromeBinaryPath = currentFolder + pathSep + "chrome-linux" + pathSep + "chrome"
chromedriverPath = currentFolder + pathSep + "chrome" + pathSep + "chromedriver"

# Selenium functions

def getChromeDriver():
    print("Using Chromedriver: [{}] and Chrome headless binary: [{}]".format(chromedriverPath, chromeBinaryPath))

    # Options
    options = Options()
    options.binary_location = chromeBinaryPath
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-dev-shm-usage')

    # Initialize driver
    driver = webdriver.Chrome(executable_path = chromedriverPath, chrome_options = options)
    driver.set_window_size(1600, 900)
    driver.maximize_window()

    return driver

def navigate(driver, url):
    driver.get(url)

def getDriverTitle(driver):
    return driver.title

def saveScreenshot(driver, name):
    driver.save_screenshot(screenshotsPath + name)

def closeDriverSession(driver):
    driver.close();
    driver.quit();

def getDriverVersion(driver):
    return driver.capabilities['version']