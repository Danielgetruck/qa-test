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
           
           print("Entering login credentials...")
           email_input = page.locator('input[type="email"]')
           if email_input:
               email_input.fill('jafora@getruck.co')
           
           password_input = page.locator('input[type="password"]')
           if password_input:
               password_input.fill('Jafor2024')
           
           print("Attempting to login...")
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
               else:
                   print("לא נמצאה סביבת אמת")
           else:
               print("לא נמצא בורר סביבות עבודה")
           
           try:
               page.get_by_text("תכנון חדש").click()
           except:
               try:
                   page.get_by_role("button", name="תכנון חדש").click()
               except:
                   page.locator('button:has-text("תכנון חדש"):visible').click()
           
           time.sleep(1)
           
           try:
               print("Attempting to fill name field...")
               name_input = page.locator('input[data-test-id="CreatePlan-Modal-Ul-Input"]')
               if name_input:
                   name_input.fill("דניאל")
                   print("Successfully filled name field")
           except Exception as e:
               print(f"Error filling name field: {e}")

           try:
               print("Attempting to work with date picker...")
               date_picker = page.locator('div[data-test-id="CreatePlanModal-Ul-DatePicker-picker"]')
               if date_picker:
                   date_picker.click()
                   time.sleep(2)
                   
                   try:
                       date_element = page.get_by_text("27").first
                       page.wait_for_timeout(500)
                       date_element.dblclick(delay=100)
                   except Exception as e:
                       print(f"Error selecting date: {e}")

               time.sleep(1)
               
           except Exception as e:
               print(f"Error with date picker: {e}")
           
           try:
               print("Attempting to open branch dropdown...")
               branch_element = page.locator('span._item_6wn44_1 span:has-text("סניף 20")')
               print(f"Number of branch elements found: {branch_element.count()}")
               
               if branch_element.count() > 0:
                   print("Attempting single click on סניף 20")
                   
                   try:
                       branch_element.first.click()
                   except Exception as e:
                       try:
                           page.evaluate("""(element) => {
                               const event = new MouseEvent('click', {
                                   'view': window,
                                   'bubbles': true,
                                   'cancelable': true
                               });
                               element.dispatchEvent(event);
                           }""", branch_element.first)
                       except Exception as js_e:
                           print(f"Failed to click: {js_e}")
                   
                   time.sleep(1)
                   
                   try:
                       branch_30_selector = 'span._item_6wn44_1:has-text("סניף 30")'
                       branch_30 = page.locator(branch_30_selector)
                       
                       if branch_30.count() > 0:
                           branch_30.first.click()
                           print("Successfully selected branch 30")
                       else:
                           print("Could not find branch 30")
                   except Exception as select_e:
                       print(f"Error selecting branch 30: {select_e}")
               else:
                   print("No branch 20 element found")
               
           except Exception as e:
               print(f"Error with branch selection: {e}")
           
           try:
               print("Attempting to click 'צור חדש' button...")
               create_button = page.locator('button[data-test-id="CreatePlanModal-NewButton"]')
               
               if create_button.count() > 0:
                   create_button.first.click()
                   print("Successfully clicked 'צור חדש' button")
               else:
                   print("Could not find 'צור חדש' button")
               
               time.sleep(1)
           except Exception as e:
               print(f"Error clicking 'צור חדש' button: {e}")
               
           try:
               print("Attempting to click sync button...")
               sync_button = page.locator('button[data-test-id="Button"]:has-text("סנכרון")')
               if sync_button.count() > 0:
                   sync_button.click()
                   print("Successfully clicked sync button")
                   
                   current_x, current_y = pyautogui.position()
                   pyautogui.moveTo(current_x + 75, current_y)
                   
                   time.sleep(20)
               else:
                   print("Could not find sync button")
           except Exception as e:
               print(f"Error clicking sync button: {e}")

           try:
               print("Attempting to click and fill search input...")
               search_container = page.locator('div._container_1epzx_1')
               search_input = search_container.locator('input[type="text"]')
               
               if search_input.count() > 0:
                   search_input.click()
                   search_input.fill("תל אביב")
                   print("Successfully filled search input")
               else:
                   print("Could not find search input")
           except Exception as e:
               print(f"Error with search input: {e}")

           try:
               print("Attempting to click close button...")
               close_button = page.locator('button[data-test-id="Button"]:has-text("סגור")')
               if close_button.count() > 0:
                   close_button.click()
                   print("Successfully clicked close button")
               else:
                   print("Could not find close button")
           except Exception as e:
               print(f"Error clicking close button: {e}")
           
           time.sleep(5)
           
       except Exception as e:
           print(f"Main error: {e}")

       # הדפדפן לא נסגר
       while True:
           time.sleep(1)

if __name__ == '__main__':
   main()