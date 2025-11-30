import time
import random
from playwright.sync_api import sync_playwright

def manual_otp_input():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        app = browser.new_page()
        mail = browser.new_page()
        
        email = f"test{random.randint(1000,9999)}@mailinator.com"
        print(f"Email: {email}")
        
        app.goto('https://desktop.labamu.co.id/landing')
        app.click('text=Login with Email')
        app.fill('input[type="email"]', email)
        app.check('input[type="checkbox"]')
        app.click('button[type="submit"]')
        print("✅ OTP requested")
        
        time.sleep(5)
        mail.goto(f'https://www.mailinator.com/v4/public/inboxes.jsp?to={email.split("@")[0]}')
        mail.click('tr:first-child')
        time.sleep(5)
        
        print("=" * 50)
        print("Copy OTP from Email by click detail email")
        print("=" * 50)

        otp = input("Enter OTP from email: ").strip()
        
        inputs = app.query_selector_all('input[type="tel"]')
        for i, char in enumerate(otp):
            if i < len(inputs):
                inputs[i].fill(char)
                inputs[-1].press('Enter')
        
        print(f"✅ OTP {otp} inputted")
        time.sleep(5)
        browser.close()

manual_otp_input()