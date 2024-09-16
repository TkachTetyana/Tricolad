import uuid
from playwright.sync_api import Playwright, sync_playwright
class Trikolad:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context=self.browser.new_context()
        self.page = self.context.new_page()
    def open(self):
        self.page.goto('https://tricolad.com.ua/')
        self.pause(1000)
        return self

    def select_product_category(self, category_name):
        self.page.locator("li").filter(has_text=category_name).get_by_role("link").click()
        return self

    def select_position_by_link(self, name:str):
        self.page.get_by_role("link", name=name).nth(1).click()
        return self

    def select_position_by_heading(self, name: str):
        self.page.get_by_role("heading", name=name).get_by_role("link").click()
        return self
    def select_position_by_row(self, name: str):
        self.page.get_by_role("row", name=name).get_by_role("spinbutton").click()
        return self

    def fill_position_by_row(self, name: str, count:int):
        self.page.get_by_role("row", name=name).get_by_role("spinbutton").fill(str(count))
        return self

    def press_continue_buying_button(self):
        self.page.get_by_text("Продовжити покупки").click()
        return self

    def add_to_cart(self,level):
        self.page.locator("div:nth-child("+str(level)+") > .descr > .cart-add").click()
        return self
    def fill_person_data(self):
        rnd = uuid.uuid4().hex
        self.page.get_by_label("Ваше прізвище та ім'я *").fill("Tester Test" + rnd)
        self.page.get_by_label("По батькові *").fill("Testovych" + rnd)
        self.page.get_by_label("Email *").fill("test" + rnd + "@test.tset")
        self.page.get_by_label("Телефон *").fill("0668301083")
        self.page.get_by_label("Місто *").fill("Дніпро")
        self.page.get_by_label("Доставка").select_option("19281")
        self.page.get_by_label("Примітка до замовлення").fill("Самовивіз")
        self.page.get_by_label("Контактні дані інші необхідні контактні дані для доставки").fill(
            "Дніпро, пр. О.Поля, 66")
        return self

    def make_order(self):
        self.page.locator("#cart_popup").get_by_text("Оформити замовлення").click()
        self.fill_person_data()
        self.pause(1000)
        self.page.locator(".purch-btn").click(force=True)
        self.pause(1000)

    def remove_from_cart(self, name:str):
        self.page.get_by_role("row", name=name).locator("span").click()
        self.page.wait_for_timeout(1000)
        return self

    def check_order(self):
        self.page.get_by_role("heading", name="Замовлення №").click()
        return self

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def pause(self, msp=1000):
        self.page.wait_for_timeout(msp)
        return self