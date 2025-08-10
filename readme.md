# Quiz Game V2

A simple, console-based quiz game in Python, featuring a clean separation of logic, data, and user interface — perfect for demonstrating object-oriented programming (OOP).

##  Project Structure

- `data.py` — Contains the question data set (e.g., a list of question-and-answer pairs).  
- `question_model.py` — Defines the `Question` class to represent each quiz item.  
- `quiz_brain.py` — Contains the `QuizBrain` class which manages quiz progression, scoring, and logic.  
- `ui.py` — Handles user interaction: displaying questions, accepting input, and showing results.

##  Features

- **OOP design**: Encapsulates quiz logic within classes for maintainability and clarity.  
- **Progressive quiz flow**: Asks one question at a time and updates the score dynamically.  
- **Clear separation of concerns**: Logic, data, and UI are modularized for ease of maintenance and future expansion.  

##  Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/Thunderer9506/Quiz_Game-V2.git
   cd Quiz_Game-V2
2. Ensure you have Python installed (preferably version 3.x).

3. Run the quiz:

 ```bash
python main.py
```
    - The game will ask questions one by one.

    - Input your answer when prompted.

    - At the end, your final score will be displayed.

## How It Works
- data.py` provides the raw quiz questions.

- `question_model.py` defines objects to store questions and answers neatly.

- `quiz_brain.py` uses these objects to manage the quiz flow — tracking which question you're on, checking answers, and tallying your score.

- `ui.py` interacts with you (the player), displaying questions and interpreting your inputs.

## Customization Ideas
- Add more questions to `data.py` or pull them from an external source (CSV, JSON, API).

- Enhance the UI for better user experience (e.g., colored text, timed questions).

- Support multiple quiz categories or difficulty levels.

- Expand question types (e.g., multiple choice, fill-in-the-blank).

## License
This project is free to use and modify — feel free to fork and build upon it!
