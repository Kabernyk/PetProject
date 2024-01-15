#!/usr/bin/python

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    webkit = playwright.webkit

    browser = webkit.launch()
    page = browser.new_page()

    url = 'http://localhost'
    page.goto(url)

    title = page.title()
    page.screenshot(path='shot.png')
    print(title)