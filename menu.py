import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#retrieves the current date for up-to-date menu 
def date_now():
    date = datetime.datetime.now()
    final = date.strftime("%-m-%-d-%Y")
    return final

def get_menu(meal, hall):
    """
    :param meal: represents what meal of the day the user is looking for (Breakfast, Lunch, Dinner)
    :param hall: gets the menu of whichever dining hall is selected (banRighHall, jeanRoyceHall, or leonardHall)
    """

    url = 'https://www.queensu.ca/food/eat-now/todays-menu'
    driver = webdriver.Chrome()
    driver.get(url)


    button = driver.find_element(By.ID, hall)
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()

    date_value = date_now()
    # Wait until the input element with the specific value is present
    wait = WebDriverWait(driver, 10)
    date_radio_button = wait.until(EC.presence_of_element_located((By.XPATH, f"//input[@name='selDate'][@value='{date_value}']")))

    #Click the parent label of the input element
    date_button = date_radio_button.find_element(By.XPATH, "./..")
    #driver.execute_script("arguments[0].scrollIntoView();", parent_label)
    date_button.click()

    wait = WebDriverWait(driver, 10)
    meal_radio_button = wait.until(EC.presence_of_element_located((By.XPATH, f"//input[@name='mealPeriod'][@value='{meal}']")))
    meal_label = meal_radio_button.find_element(By.XPATH, "./..")
    #driver.execute_script("arguments[0].scrollIntoView();", meal_label)
    meal_label.click()


    time.sleep(3)

    foods = driver.find_elements(By.CLASS_NAME, "menuItemHeader")

    list = "\n".join([food.text for food in foods])

    return list

if __name__ == "__main__":
    menu = get_menu("Breakfast", "leonardHall")
    print(menu)