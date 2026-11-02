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

    # Correct answers according to the original JavaScript
    answers = [
        "Queue",
        "CSS",
        "SELECT",
        "HTTP",
        "Linux",
        "<a>",
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
    percentage = driver.find_element(By.ID, "percentage").text

    print("Final Score:", score)
    print("Displayed Percentage:", percentage)

    score_value = int(score.split("/")[0])
    expected_percentage = (score_value / 10) * 100

    print("Expected Percentage:", expected_percentage, "%")

    actual_percentage = float(percentage.replace("%", ""))

    if actual_percentage != expected_percentage:
        print("BUG FOUND: Percentage calculation is incorrect.")
        print("Test Result: FAIL")
    else:
        print("Percentage calculation is correct.")
        print("Test Result: PASS")

finally:
    driver.quit()