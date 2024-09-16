import uuid
from pydoc import importfile
from playwright.sync_api import sync_playwright
import re

def test_web_shop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://tricolad.com.ua/")
        rnd = uuid.uuid4().hex
        page.locator("li").filter(has_text="Шоколад кондитерський").get_by_role("link").click()
        page.get_by_role("link", name="Чорний").nth(1).click()
        page.locator("div:nth-child(2) > .descr > .cart-add").click()
        page.get_by_text("Продовжити покупки").click()
        page.get_by_role("link", name="Упакування, сервірування").click()
        page.get_by_role("link", name="Коробки").nth(1).click()
        page.get_by_role("heading", name="Коробки для цукерок та плиток").get_by_role("link").click()
        page.locator("div:nth-child(2) > .descr > .cart-add").click()
        page.get_by_role("row", name="Новорічна. Коробка для 9").get_by_role("spinbutton").click()
        page.get_by_role("row", name="Шоколад чорний 55% (C501/J),").get_by_role("spinbutton").fill("5")
        page.get_by_text("Оформити замовлення Продовжити покупки").click()
        page.locator("li").filter(has_text="Інгредієнти кондитерські").get_by_role("link").click()
        page.get_by_role("heading", name="Начинки та пасти").get_by_role("link").click()
        page.get_by_role("heading", name="Паста фісташкова").get_by_role("link").click()
        page.locator("div:nth-child(3) > .descr > .cart-add").click()
        page.get_by_role("row", name="Фісташкова паста натуральна").locator("span").click()
        page.wait_for_timeout(5000)
        page.locator("#cart_popup").get_by_text("Оформити замовлення").click()
        page.get_by_label("Ваше прізвище та ім'я *").fill("Tester Test"+rnd)
        page.get_by_label("По батькові *").fill("Testovych"+rnd)
        page.get_by_label("Email *").fill("test"+rnd+"@test.tset")
        page.get_by_label("Телефон *").fill("0668301083")
        page.get_by_label("Місто *").fill("Дніпро")
        page.get_by_label("Доставка").select_option("19281")
        page.get_by_label("Примітка до замовлення").fill("Самовивіз")
        page.get_by_label("Контактні дані інші необхідні контактні дані для доставки").fill(
            "Дніпро, пр. О.Поля, 66")
        page.wait_for_timeout(1000)
        #page.locator(".purch-btn").click(force=True)
        page.wait_for_timeout(1000)
        page.get_by_role("heading", name="Замовлення №").click()
        #page.pause()
        browser.close()