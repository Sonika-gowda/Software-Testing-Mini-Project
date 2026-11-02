from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pathlib import Path


# Start Chrome browser
driver = webdriver.Chrome()

try:
    # Open the locally running quiz application
    driver.get("http://localhost:8000")

    wait = WebDriverWait(driver, 10)

    # Locate the student name input
    name_input = driver.find_element(By.ID, "studentName")

    # Leave the name field empty
    name_input.clear()

    # Click the Start Quiz button
    start_button = driver.find_element(
        By.CSS_SELECTOR, "#loginForm button[type='submit']"
    )
    start_button.click()

    # Check whether the quiz page became visible
    wait.until(
        lambda d: (
            "hidden" not in d.find_element(By.ID, "quizPage").get_attribute("class")
            or d.execute_script(
                "return document.getElementById('studentName').checkValidity()"
            ) is False
            or bool(d.find_element(By.ID, "nameError").text.strip())
        )
    )

    quiz_visible = (
        "hidden" not in driver.find_element(By.ID, "quizPage").get_attribute("class")
    )

    name_error = driver.find_element(By.ID, "nameError").text.strip()

    if quiz_visible:
        print("BUG FOUND: Quiz started without entering a student name.")
        print("Test Result: FAIL")
        screenshot_path = Path(__file__).with_name("bug01_empty_name.png")
        driver.save_screenshot(str(screenshot_path))
        print(f"Screenshot saved: {screenshot_path}")
    else:
        print("Validation prevented the quiz from starting.")
        print("Test Result: PASS")
        if name_error:
            print("Validation message:", name_error)
        else:
            print("Browser's required-field validation prevented submission.")

finally:
    driver.quit()