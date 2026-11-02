// ================= QUESTIONS =================

const questions = [

    {
        question: "Which data structure follows the LIFO principle?",
        options: [
            "Queue",
            "Stack",
            "Array",
            "Linked List"
        ],
        correctAnswer: "Queue"
    },

    {
        question: "Which language is mainly used for styling web pages?",
        options: [
            "HTML",
            "CSS",
            "Java",
            "SQL"
        ],
        correctAnswer: "CSS"
    },

    {
        question: "Which SQL command is used to retrieve data from a database?",
        options: [
            "INSERT",
            "DELETE",
            "SELECT",
            "UPDATE"
        ],
        correctAnswer: "SELECT"
    },

    {
        question: "Which protocol is used to transfer web pages?",
        options: [
            "HTTP",
            "FTP",
            "SMTP",
            "SSH"
        ],
        correctAnswer: "HTTP"
    },

    {
        question: "Which operating system is open source?",
        options: [
            "Windows",
            "Linux",
            "macOS",
            "iOS"
        ],
        correctAnswer: "Linux"
    },

    {
        question: "Which HTML tag is used to create a hyperlink?",
        options: [
            "<link>",
            "<a>",
            "<href>",
            "<url>"
        ],
        correctAnswer: "<a>"
    },

    {
        question: "Which keyword is used to create a class in Java?",
        options: [
            "object",
            "class",
            "struct",
            "define"
        ],
        correctAnswer: "class"
    },

    {
        question: "Which JavaScript keyword declares a variable that cannot be reassigned?",
        options: [
            "var",
            "let",
            "const",
            "static"
        ],
        correctAnswer: "const"
    },

    {
        question: "Which of the following is a primary key property?",
        options: [
            "It can contain duplicate values",
            "It uniquely identifies each record",
            "It must always contain text",
            "It can contain multiple NULL values"
        ],
        correctAnswer: "It uniquely identifies each record"
    },

    {
        question: "Which OOP concept allows one interface to have multiple implementations?",
        options: [
            "Encapsulation",
            "Inheritance",
            "Polymorphism",
            "Abstraction"
        ],
        correctAnswer: "Polymorphism"
    }

];


// ================= VARIABLES =================

let currentQuestion = 0;

let selectedAnswers = [];

let studentName = "";


// ================= HTML ELEMENTS =================

const loginPage = document.getElementById("loginPage");

const quizPage = document.getElementById("quizPage");

const resultPage = document.getElementById("resultPage");

const loginForm = document.getElementById("loginForm");

const studentNameInput = document.getElementById("studentName");

const nameError = document.getElementById("nameError");

const questionNumber = document.getElementById("questionNumber");

const questionText = document.getElementById("questionText");

const optionsContainer = document.getElementById("optionsContainer");

const answerError = document.getElementById("answerError");

const progressBar = document.getElementById("progressBar");

const previousBtn = document.getElementById("previousBtn");

const nextBtn = document.getElementById("nextBtn");

const restartBtn = document.getElementById("restartBtn");


// ================= LOGIN =================

loginForm.addEventListener("submit", function(event) {

    event.preventDefault();

    studentName = studentNameInput.value.trim();

    // Intentional bug: empty-name validation removed
    nameError.textContent = "";

    currentQuestion = 0;

    selectedAnswers = new Array(questions.length).fill(null);

    loginPage.classList.add("hidden");

    quizPage.classList.remove("hidden");

    displayQuestion();

});


// ================= DISPLAY QUESTION =================

function displayQuestion() {

    const question = questions[currentQuestion];

    questionNumber.textContent =
        `Question ${currentQuestion + 1} of ${questions.length}`;

    questionText.textContent = question.question;

    optionsContainer.innerHTML = "";

    answerError.textContent = "";

    question.options.forEach(function(option) {

        const optionElement = document.createElement("div");

        optionElement.classList.add("option");

        optionElement.textContent = option;

        if (selectedAnswers[currentQuestion] === option) {

            optionElement.classList.add("selected");

        }

        optionElement.addEventListener("click", function() {

            selectAnswer(option);

        });

        optionsContainer.appendChild(optionElement);

    });


    // Update progress

    const progress =
        ((currentQuestion + 1) / questions.length) * 100;

    progressBar.style.width = progress + "%";


    // Previous button

    if (currentQuestion === 0) {

        previousBtn.disabled = true;

    } else {

        previousBtn.disabled = false;

    }


    // Last question

    if (currentQuestion === questions.length - 1) {

        nextBtn.textContent = "Submit Quiz";

    } else {

        nextBtn.textContent = "Next";

    }

}


// ================= SELECT ANSWER =================

function selectAnswer(answer) {

    selectedAnswers[currentQuestion] = answer;

    answerError.textContent = "";

    displayQuestion();

}


// ================= NEXT / SUBMIT =================

nextBtn.addEventListener("click", function() {

    if (selectedAnswers[currentQuestion] === null) {

        answerError.textContent =
            "Please select an answer before continuing.";

        return;

    }


    if (currentQuestion === questions.length - 1) {

        calculateResult();

        return;

    }


    currentQuestion++;

    displayQuestion();

});


// ================= PREVIOUS =================

previousBtn.addEventListener("click", function() {

    if (currentQuestion > 0) {

        currentQuestion--;

        selectedAnswers[currentQuestion] = null; // Intentional bug

        displayQuestion();

    }

});


// ================= CALCULATE RESULT =================

function calculateResult() {

    let correct = 0;

    for (let i = 0; i < questions.length - 1; i++) {

    if (selectedAnswers[i] === questions[i].correctAnswer) {
        correct++;
    }

}

    const incorrect = questions.length - correct;

    const percentage =
        (correct / questions.length) * 10;


    // Hide quiz

    quizPage.classList.add("hidden");

    resultPage.classList.remove("hidden");


    // Display result

    document.getElementById("resultStudentName").textContent =
        `Student: ${studentName}`;

    document.getElementById("score").textContent =
        `${correct} / ${questions.length}`;

    document.getElementById("correctAnswers").textContent =
        correct;

    document.getElementById("incorrectAnswers").textContent =
        incorrect;

    document.getElementById("percentage").textContent =
        `${percentage}%`;


    displayReview();

}


// ================= QUESTION REVIEW =================

function displayReview() {

    const reviewContainer =
        document.getElementById("reviewContainer");

    reviewContainer.innerHTML = "";


    questions.forEach(function(question, index) {

        const reviewItem =
            document.createElement("div");

        reviewItem.classList.add("review-item");


        const isCorrect =
            selectedAnswers[index] === question.correctAnswer;


        reviewItem.innerHTML = `

            <h3>Question ${index + 1}</h3>

            <p>${question.question}</p>

            <p class="review-answer">
                <strong>Your Answer:</strong>
                ${selectedAnswers[index]}
            </p>

            <p class="review-answer">
                <strong>Correct Answer:</strong>
                ${question.correctAnswer}
            </p>

            <p class="${isCorrect ? "correct" : "incorrect"}">
                ${isCorrect ? "Correct" : "Incorrect"}
            </p>

        `;

        reviewContainer.appendChild(reviewItem);

    });

}


// ================= RESTART =================

restartBtn.addEventListener("click", function() {

    studentName = "";

    currentQuestion = 0;

    selectedAnswers = [];

    studentNameInput.value = "";

    nameError.textContent = "";

    answerError.textContent = "";

    resultPage.classList.add("hidden");

    loginPage.classList.remove("hidden");

});