def test_exist_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary"), "Кнопка добавления в корзину отсутствует"
