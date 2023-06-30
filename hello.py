import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_a_success_login(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://practicetestautomation.com/practice-test-login/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "username").send_keys(
            "student"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "Password123"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click()  # klik tombol submit
        time.sleep(1)

        # validasi
        # Get the current URL
        current_url = browser.current_url

        # Define the expected URL
        expected_url = "https://practicetestautomation.com/logged-in-successfully/"

        # Check if the expected URL is included in the current URL
        self.assertIn(expected_url, current_url)

    def test_a_failed_login_with_empty_username(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://practicetestautomation.com/practice-test-login/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "username").send_keys(
            " "
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            "Password123"
        )  # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click()  # klik tombol submit
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.ID, "error").text

        self.assertEqual(response_message, "Your username is invalid!")

    def test_a_failed_login_with_empty_password(self):
       # steps
        browser = self.browser  # buka web browser
        browser.get("https://practicetestautomation.com/practice-test-login/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "username").send_keys(
            "student"
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            " "
        )  # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click()  # klik tombol submit
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.ID, "error").text

        self.assertEqual(response_message, "Your password is invalid!")

    def test_a_failed_login_with_empty_username_and_password(self):
        # steps
        browser = self.browser  # buka web browser
        browser.get("https://practicetestautomation.com/practice-test-login/")  # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "username").send_keys(
            " "
        )  # isi username
        time.sleep(1)
        browser.find_element(By.ID, "password").send_keys(
            " "
        )  # isi password
        time.sleep(1)
        browser.find_element(By.ID, "submit").click()  # klik tombol submit
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.ID, "error").text

        self.assertEqual(response_message, "Your username is invalid!")

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
