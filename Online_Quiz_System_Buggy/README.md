# Online Quiz System – Software Testing Mini Project

## 1. Project Overview

The **Online Quiz System** is a web-based application designed to conduct quizzes and display student results.

This project focuses on software testing using **Selenium WebDriver with Python**. The application is intentionally buggy, and automated test cases are executed to identify functional defects and verify the application's behavior.

The original application is tested without modifying its source code.

## 2. Objectives

- Understand the fundamentals of software testing.
- Perform functional testing on a web application.
- Automate test cases using Selenium WebDriver.
- Identify and document application defects.
- Verify login, quiz navigation, answer selection, and result calculations.
- Capture test execution results as evidence.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| HTML | Webpage structure |
| CSS | Application styling |
| JavaScript | Quiz functionality |
| Python | Automation scripting |
| Selenium WebDriver | Browser automation |
| Google Chrome | Browser used for testing |
| Python Virtual Environment | Dependency management |

## 4. Project Structure

```text
Software-Testing-Mini-Project/
│
└── Online_Quiz_System_Buggy/
    │
    ├── index.html
    ├── script.js
    ├── style.css
    │
    ├── selenium_tests/
    │   ├── test_login.py
    │   ├── test_quiz.py
    │   ├── test_navigation.py
    │   ├── test_results.py
    │   ├── test_percentage.py
    │   └── Screenshots
    │
    ├── venv/
    │
    └── README.md
```

## 5. Setup and Installation

### Prerequisites

- Python 3.x
- Google Chrome browser
- Visual Studio Code (optional)
- Git

### Step 1: Clone the Repository

```powershell
git clone https://github.com/Sonika-gowda/Software-Testing-Mini-Project.git
```

### Step 2: Navigate to the Project Directory

```powershell
cd Software-Testing-Mini-Project
cd Online_Quiz_System_Buggy
```

### Step 3: Create a Virtual Environment

```powershell
python -m venv venv
```

### Step 4: Activate the Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Selenium

```powershell
python -m pip install selenium
```

## 6. Running the Application

Start the local development server from the application directory:

```powershell
python -m http.server 8000
```

Open the application in Google Chrome:

```text
http://localhost:8000
```

Keep the local server running while executing the Selenium test scripts.

## 7. Executing Selenium Test Cases

Open another PowerShell terminal, navigate to the project directory, and activate the virtual environment.

Execute the test scripts individually:

```powershell
python selenium_tests\test_login.py
```

```powershell
python selenium_tests\test_quiz.py
```

```powershell
python selenium_tests\test_navigation.py
```

```powershell
python selenium_tests\test_results.py
```

```powershell
python selenium_tests\test_percentage.py
```

## 8. Bugs Identified

The following five defects were identified during automated testing:

| Bug ID | Defect Description |
|---|---|
| BUG-01 | Application allows the quiz to start without entering a student name. |
| BUG-02 | Incorrect answer key for the LIFO principle question. |
| BUG-03 | Previously selected answers are cleared when navigating to the previous question. |
| BUG-04 | The final question is excluded from score calculation. |
| BUG-05 | Percentage calculation displays an incorrect result. |

## 9. Testing Approach

The project follows this testing workflow:

1. Understand the application's functionality.
2. Identify important test scenarios.
3. Create automated test scripts using Selenium.
4. Execute test cases on the original application.
5. Observe actual application behavior.
6. Compare actual results with expected results.
7. Identify and document defects.
8. Save screenshots and test execution outputs as evidence.

## 10. Expected Outcome

The objective is to demonstrate how automated functional testing can identify defects in a web application.

The project successfully identified five defects through Selenium-based testing.

**Note:** The original application source code is intentionally kept unchanged to preserve the defects for testing and demonstration purposes.

## 11. Conclusion

This project provided practical experience in functional testing, browser automation, test case execution, defect identification, and test result analysis using Python and Selenium WebDriver.

It demonstrates how automated testing helps identify functional issues and improves software quality.

## 12. Repository

GitHub Repository:  
https://github.com/Sonika-gowda/Software-Testing-Mini-Project
