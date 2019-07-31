import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                 help="Choose language: ...................")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language == "ru":
        print("\nstart chrome browser with ru language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "en":
        print("\nstart chrome browser with en language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "es":
        print("\nstart chrome browser with es language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "fr":
        print("\nstart chrome browser with fr language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "ar":
        print("\nstart chrome browser with ar language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "ca":
        print("\nstart chrome browser with ca language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "cs":
        print("\nstart chrome browser with cs language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "da":
        print("\nstart chrome browser with da language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "de":
        print("\nstart chrome browser with de language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "el":
        print("\nstart chrome browser with el language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "fi":
        print("\nstart chrome browser with fi language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "it":
        print("\nstart chrome browser with it language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "ko":
        print("\nstart chrome browser with ko language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "nl":
        print("\nstart chrome browser with nl language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "pl":
        print("\nstart chrome browser with pl language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "pt":
        print("\nstart chrome browser with pt language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "ro":
        print("\nstart chrome browser with ro language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "sk":
        print("\nstart chrome browser with sk language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "uk":
        print("\nstart chrome browser with uk language for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be normal")
    yield browser
    print("\nquit browser..")
    browser.quit()