from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

base_url = "https://www.vieclamtot.com"

def test_eight_components():
    driver = webdriver.Chrome(
        #full size
        
    )

    # driver.get(base_url + "/viec-lam-huyen-binh-chanh-tp-ho-chi-minh/101804298.htm")
    driver.get(base_url + "/viec-lam-quan-tan-binh-tp-ho-chi-minh/103218327.htm")
    # wait until class name is loaded
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sc-ifAKCX")))

    show_phone_number_btn = driver.find_element(by=By.CLASS_NAME, value="sc-ifAKCX")
    if (show_phone_number_btn): 
        show_phone_number_btn.click()

        # get phone number
        phone_number = show_phone_number_btn.text

        print(phone_number)

        driver.quit()
        print("Test passed")

    # quit if response 410
    if (driver.find_elements(by=By.CLASS_NAME, value="NotFound_notFoundWrapper__2_cFc")):
        driver.quit()
        print("NOT FOUND")
        return


if __name__ == "__main__":
    test_eight_components()