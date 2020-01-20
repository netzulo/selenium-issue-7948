from selenium.webdriver.remote.webelement import WebElement


def poc():
    try:
        ele = WebElement()
    except:
        pass
    raise Exception("if printed, you can't reproduce this behaviour")
