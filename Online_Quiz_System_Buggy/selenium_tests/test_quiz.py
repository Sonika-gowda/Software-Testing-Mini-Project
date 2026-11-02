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

    # Wait for first question
    question = wait.until(
        EC.visibility_of_element_located((By.ID, "questionText"))
    )

    print("Question:", question.text)

    # Select Stack
    options = driver.find_elements(By.CLASS_NAME, "option")

    for option in options:
        if option.text.strip() == "Stack":
            option.click()
            break

    # Submit answer and navigate through remaining questions
    for i in range(10):
        next_button = driver.find_element(By.ID, "nextBtn")
        next_button.click()

        if i < 9:
            wait.until(
                lambda d: d.find_element(By.ID, "questionNumber").text
                != f"Question {i + 1} of 10"
            )

    # Wait for result page
    wait.until(
        EC.visibility_of_element_located((By.ID, "resultPage"))
    )

    print("\nANSWER REVIEW:")
    print(driver.find_element(By.ID, "reviewContainer").text)

    print("Test completed. Check whether Stack was marked correct.")

finally:
    driver.quit()