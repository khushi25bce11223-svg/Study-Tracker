# StudyTracker 

## 📗 Project Overview 

StudyTracker is a simple and effective Python-based tool that helps students to track their study routine. It allows users to add subjects, their important tasks, record daily hours, and view overall progress. The project helps to improve time management , productivity, grading and also encourages consistency.

## ⭐ Features

- Add and manage multiple subjects
- Record daily study time for each subjects
- View total hours spent on each subject
- Persistent data storage using JSON
- Simple, menu-driven console interface

## 🛠️ Technologies Used

- Python 3
- JSON (for data storae )
- Built-in OS and File Handling modules

  ## 📩 Installation Steps
  
  1. Clone the repository:
     '''bash
     git clone
  https://github.com/yourusername/StudyTracker.git

## HOW TO RUN THE PROJECT

1. Run the script
2. The program menu will allow to:
       - Add Subject
       - Log Study Time
       - View  Progress
       - Save and Exit
## 🧪 Instruction For Testing 

1. Test Adding a Subject
   - Select Add Subject
   - Enter a subject name (example: Computer Science)
   - Go to View Progress
   - Confirm the newly added subject is displayed or not

2. Test Logging Study Time
   - Select Log Study Time
   - Enter hours studied (example:3)
   - Open View Progress
   - Verify hours updated correctly

3. Test Data Saving and Loading
   - Add subjects and log hours
   - Choose Save and Exit
   - Run the program again
   - Ensure previously saved data loads from data.json

4. Test Invalid Inputs
   - Enter letters instead of numbers -> Program should display an error
   - Add an already existing subject -> Should show a warning
   - Log hours for a non-existing subject -> Should show "Subject jnot found"

5. Test Menu Navigation
   - Navigate every option in the menu
   - Ensure there are no crashes
   - Verify outputs match expected behaviour
     

  
