from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("http://localhost:8000")

    # Login
    driver.find_element(By.ID, "studentName").send_keys("Test Student")

    driver.find_element(
        By.CSS_SELECTOR, "#loginForm button[type='submit']"
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "questionText"))
    )

    # Answer all questions using their configured correct answers.
    # This deliberately uses the application's answer key.

    answers = [
        "Queue",
        "CSS",
        "SELECT",
        "HTTP",
        "Linux",
        "href",
        "class",
        "const",
        "It uniquely identifies each record",
        "Polymorphism"
    ]

    for index, answer in enumerate(answers):
        options = driver.find_elements(By.CLASS_NAME, "option")

        for option in options:
            if option.text.strip() == answer:
                option.click()
                break

        driver.find_element(By.ID, "nextBtn").click()

        if index < 9:
            wait.until(
                lambda d, expected=index + 2:
                d.find_element(By.ID, "questionNumber").text
                == f"Question {expected} of 10"
            )

    # Wait for results
    wait.until(
        EC.visibility_of_element_located((By.ID, "resultPage"))
    )

    score = driver.find_element(By.ID, "score").text

    print("Score:", score)

    if score == "9 / 10":
        print("BUG FOUND: Last question was excluded from scoring.")
        print("Test Result: FAIL")
    else:
        print("Unexpected score. Inspect the answer review.")

    print("\nAnswer Review:")
    print(driver.find_element(By.ID, "reviewContainer").text)

finally:
    driver.quit()