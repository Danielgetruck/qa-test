from playwright.sync_api import sync_playwright
import time
import pyautogui

def main():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       page = browser.new_page()
       
       page.evaluate("document.documentElement.requestFullscreen()")
       
       try:
           print("Starting login process...")
           page.goto('https://platform-dev.getruck.co.il/login/')
           page.set_viewport_size({"width": 1920, "height": 1080})
           
           email_input = page.locator('input[type="email"]')
           if email_input:
               email_input.fill('jafora@getruck.co')
           
           password_input = page.locator('input[type="password"]')
           if password_input:
               password_input.fill('Jafor2024')
           
           login_button = page.locator('button[type="submit"]')
           if login_button:
               login_button.click()
           
           time.sleep(5)

           workspace_selector = page.locator('div._selected-workspace_1uq4u_680')
           if workspace_selector.count() > 0:
               workspace_selector.click()
               time.sleep(1)
               
               production_env = page.locator('div._navigation-item_14udl_17:has-text("אמת")')
               if production_env.count() > 0:
                   production_env.click()
                   time.sleep(2)
           
           try:
               page.get_by_text("תכנון חדש").click()
           except:
               try:
                   page.get_by_role("button", name="תכנון חדש").click()
               except:
                   page.locator('button:has-text("תכנון חדש"):visible').click()
           
           time.sleep(1)
           
           name_input = page.locator('input[data-test-id="CreatePlan-Modal-Ul-Input"]')
           if name_input:
               name_input.fill("דניאל")

           date_picker = page.locator('div[data-test-id="CreatePlanModal-Ul-DatePicker-picker"]')
           if date_picker:
               date_picker.click()
               time.sleep(2)
               date_element = page.get_by_text("27").first
               page.wait_for_timeout(500)
               date_element.dblclick(delay=100)
               time.sleep(1)
           
           branch_element = page.locator('span._item_6wn44_1 span:has-text("סניף 20")')
           if branch_element.count() > 0:
               branch_element.first.click()
               time.sleep(1)
               
               branch_30_selector = 'span._item_6wn44_1:has-text("סניף 30")'
               branch_30 = page.locator(branch_30_selector)
               if branch_30.count() > 0:
                   branch_30.first.click()
           
           create_button = page.locator('button[data-test-id="CreatePlanModal-NewButton"]')
           if create_button.count() > 0:
               create_button.first.click()
               time.sleep(1)
               
           sync_button = page.locator('button[data-test-id="Button"]:has-text("סנכרון")')
           if sync_button.count() > 0:
               sync_button.click()
               current_x, current_y = pyautogui.position()
               pyautogui.moveTo(current_x + 75, current_y)
               time.sleep(20)
               
               close_sync_button = page.locator('button[data-test-id="Button"]:has-text("סגור")')
               if close_sync_button.count() > 0:
                   close_sync_button.click()

           search_container = page.locator('div._container_1epzx_1')
           search_input = search_container.locator('input[type="text"]')
           if search_input.count() > 0:
               search_input.click()
               search_input.fill("תל אביב")

           close_button = page.locator('button[data-test-id="Button"]:has-text("סגור")')
           if close_button.count() > 0:
               close_button.click()

           workspace_tab = page.locator('li._tab-info_w1s1r_15:has-text("לוח עבודה")')
           if workspace_tab.count() > 0:
               workspace_tab.click()
               time.sleep(2)

           add_route_button = page.locator('button.btn-secondary_3y7iw_70:has(span.icon-add)')
           if add_route_button.count() > 0:
               add_route_button.click()
               time.sleep(1)

           driver_dropdown = page.locator('div._dropdown_1job3_706')
           if driver_dropdown.count() > 0:
               driver_dropdown.click()
               time.sleep(2)
               
               first_driver = page.locator('div._option_x9mpz_1').first
               if first_driver.count() > 0:
                   first_driver.click()
               time.sleep(1)
               
           time.sleep(10)  # המתנה סופית לפני סגירה
           print("Closing browser...")
           browser.close()
           
       except Exception as e:
           print(f"Main error: {e}")
           browser.close()

if __name__ == '__main__':
   main()