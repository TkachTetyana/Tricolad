from _pytest.fixtures import fixture
from playwright.sync_api import sync_playwright

from Trikolad import Trikolad


@fixture
def get_playwright():
    with sync_playwright() as p:
        yield p

@fixture
def trikolad(get_playwright):
    tl = Trikolad(get_playwright)
    yield tl
    tl.close()