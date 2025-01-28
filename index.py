from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.evaluate("document.documentElement.requestFullscreen()")
        
        try:
            print("Starting login process...")
            page.goto('https://platform-dev.getruck.co.il/login/')
            page.set_viewport_size({"width": 1920, "height": 1080})
            
            # Login
            email_input = page.locator('input[type="email"]')
            if email_input:
                email_input.fill('jafora@getruck.co')
            
            password_input = page.locator('input[type="password"]')
            if password_input:
                password_input.fill('Jafor2024')
            
            login_button = page.locator('button[type="submit"]')
            if login_button:
                login_button.click()
            
            # Wait for login to complete and page to load
            page.wait_for_timeout(5000)

            # Select workspace
            workspace_selector = page.locator('div._selected-workspace_1uq4u_680')
            if workspace_selector.count() > 0:
                workspace_selector.click()
                page.wait_for_timeout(1000)
                
                production_env = page.locator('div._navigation-item_14udl_17:has-text("אמת")')
                if production_env.count() > 0:
                    production_env.click()
                    page.wait_for_timeout(2000)
            
            # Keep browser open
            while True:
                time.sleep(1)
            
        except Exception as e:
            print(f"Main error: {e}")
            browser.close()

if __name__ == '__main__':
    main()
    