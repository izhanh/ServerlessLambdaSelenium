import webdriverFunctions

# Main

def seleniumTest(event, context):
    driver = webdriverFunctions.getChromeDriver()

    webdriverFunctions.navigate(driver, 'https://www.google.com/')
    body = "Headless Chrome Initialized, Page title: [{}]".format(webdriverFunctions.getDriverTitle(driver))
    print(body)

    response = {
        "statusCode": 200,
        "body": body
    }

    print(webdriverFunctions.getDriverVersion(driver))
    webdriverFunctions.saveScreenshot(driver, "success.png")
    webdriverFunctions.closeDriverSession(driver)

    print(response)
    return response

seleniumTest("", "")