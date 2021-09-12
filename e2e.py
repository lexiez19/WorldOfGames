import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Utils import SCORES_FILE_NAME


#
# def test_scores_service():
#     browser = webdriver.Chrome(executable_path="C:/Users/almogr/PycharmProjects/Class-Lessons/Lesson 4 - "
#                                                "02-07-2021/chromedriver_win32/chromedriver.exe")
#     # browser.get("http://127.0.0.1:5000/")
#     browser.get("http://www.walla.co.il")
#     return
#     # print("This URL is in test_scores_function", base_url)

def test_scores_service():
    # score = int(SCORES_FILE_NAME)
    score = 35
    if 1 < score < 1000:
        print(True)
        return True
    else:
        print(False)
        return False


def main_function():
    if test_scores_service():
        print("Result is True, Exit Code is 0")
        sys.exit(0)
    else:
        print("Result is False, Exit Code is -1")
        sys.exit(-1)


main_function()
