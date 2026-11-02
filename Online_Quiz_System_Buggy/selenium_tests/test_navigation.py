from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://localhost:8000")

    # Enter student name
    driver.find_element(By.ID, "studentName").send_keys("Test Student")

    # Start quiz
    driver.find_element(
        By.CSS_SELECTOR, "#loginForm button[type='submit']"
    ).click()

    # Wait for Question 1
    wait.until(
        EC.visibility_of_element_located((By.ID, "questionText"))
    )

    # Select Stack
    options = driver.find_elements(By.CLASS_NAME, "option")

    for option in options:
        if option.text.strip() == "Stack":
            option.click()
            break

    print("Selected answer: Stack")

    # Click Next
    driver.find_element(By.ID, "nextBtn").click()

    wait.until(
        lambda d: "2" in d.find_element(
            By.ID, "questionNumber"
        ).text
    )

    print("Navigated to Question 2")

    # Click Previous
    driver.find_element(By.ID, "previousBtn").click()

    wait.until(
        lambda d: "1" in d.find_element(
            By.ID, "questionNumber"
        ).text
    )

    print("Returned to Question 1")

    # Check whether Stack remains selected
    selected_options = driver.find_elements(
        By.CSS_SELECTOR, ".option.selected"
    )

    if selected_options and selected_options[0].text.strip() == "Stack":
        print("Test Result: PASS - Answer was retained.")
    else:
        print("BUG FOUND: Previously selected answer was cleared.")
        print("Test Result: FAIL")

finally:
    driver.quit()