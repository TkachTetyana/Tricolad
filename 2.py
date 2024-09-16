import uuid
from pydoc import importfile

from playwright.sync_api import sync_playwright, expect
import re
from playwright_stealth import stealth_sync


def test_negative_badurl():
    with (sync_playwright() as p):
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        stealth_sync(page)

        page.goto("https://tricolad.com.ua/aktsijnij-tovar/c210")
        assert  page.url=="https://tricolad.com.ua/aktsijnij-tovar/c210", "товар не знайдено"

        page.goto("https://tricolad.com.ua/aktsijnij-tovar/c210"+"test")
        page.wait_for_timeout(5000)
        assert page.get_by_role("heading", name="Помилка 404. Сторінку не знайдено").is_visible(),
        "помилка 404 не знайдена"

def test_negative_zabuv_parol():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://tricolad.com.ua/")
        page.get_by_role("link", name="Забули пароль?").click()
        page.get_by_label("Email *").click()
        page.get_by_label("Email *").fill("t.tkach@i.ua")
        page.get_by_role("button", name="Нагадати").click()
        page.wait_for_timeout(5000)
        page.get_by_text("Помилка. Перевірте правильність заповнення полів або спробуйте пізніше").click()

        context.close()
        browser.close()




        
         # page.get_by_role("link", name="Реєстрація").click()
        # page.get_by_label("Ваше ім'я *").fill("Tetyana")
        # page.get_by_label("Email *").fill("t.tkach@i.ua")
        # page.get_by_label("Пароль *").fill("12345")
        # page.get_by_label("Телефон").fill("0668301083")
        # page.get_by_label("Контактні дані").fill("Dnipro")
        # page.pause()
        # page.get_by_role("button", name="Продовжити").click()
        # page.get_by_text("Дякуємо за реєстрацію. На Ваш email").click()

        # page.get_by_text("Укр", exact=True).click()
        # page.get_by_role("link", name="Рус").click()

        context.close()
        browser.close()

