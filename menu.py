import time
import datetime
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def date_now():
    """Retrieves the current date formatted for the URL."""
    return datetime.datetime.now().strftime("%-m-%-d-%Y")

def setup_driver(headless=True):
    """Initializes the Selenium WebDriver with optional headless mode."""
    options = Options()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('window-size=1920x1080')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
    driver = webdriver.Chrome(options=options)
    return driver


def get_menu(driver, meal, hall):
    """
    Fetches the menu for a specific meal and dining hall.
    
    :param driver: Selenium WebDriver instance.
    :param meal: Meal type (Breakfast, Lunch, Dinner).
    :param hall: Dining hall identifier.
    :return: Menu list as a string or None if not available.
    """
    try:
        driver.get('https://www.queensu.ca/food/eat-now/todays-menu')

        button = driver.find_element(By.ID, hall)
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

        date_value = date_now()
        date_radio_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//input[@name='selDate'][@value='{date_value}']")))
        date_radio_button.find_element(By.XPATH, "./..").click()

        meal_radio_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//input[@name='mealPeriod'][@value='{meal}']")))
        meal_radio_button.find_element(By.XPATH, "./..").click()
    
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "menuItemHeader")))
        foods = driver.find_elements(By.CLASS_NAME, "menuItemHeader")

        return "\n".join(food.text for food in foods)
    
    except Exception as e:
        logging.error(f"Error fetching menu for {hall}: {e}")
        return

def main():
    logging.basicConfig(level=logging.INFO)
    driver = setup_driver()
    try:
        menu = get_menu(driver, "Dinner", "leonardHall")
        if menu:
            print(menu)
        else:
            print("Menu not available.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
