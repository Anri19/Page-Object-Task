from Pages.main_page import MainPage
from Pages.login_page import LoginPage

#link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    # page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = page.go_to_login_page()
    login_page.should_be_login_page() # Здесь выполняются все тесты с login_page

# def test_guest_should_be_login_url(browser):
#     #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#  #   page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#     page.should_be_login_url()

# def test_guest_should_be_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#  #   page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#     page.should_be_login_form()
    
# def test_guest_should_be_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#  #   page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#     page.should_be_register_form()  

def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# def test_guest_should_be_login_url(broser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_url()

# def test_guest_should_be_login_form(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_form()

# def test_guest_should_be_register_form(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_register_form()     

#ПЕРВЫЙ ВАРИАНТ
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     browser.get(link)
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()

#ВТОРОЙ ВАРИАНТ
# def go_to_login_page(browser):
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()

# def test_guest_can_go_to_login_page(browser): 
#    browser.get(link) 
#    go_to_login_page(browser) 