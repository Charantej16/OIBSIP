🧮 BMI Calculator Project

A simple GUI-based BMI Calculator built using Python and Tkinter that calculates Body Mass Index (BMI), classifies health status, and stores user data in a CSV file.

This project is suitable for internships, mini-projects, and academic submissions.

📌 Features

🖥️ User-friendly Graphical Interface (GUI)
⚖️ BMI calculation using height & weight
🏷️ Automatic health category detection
📁 Stores records in CSV file
🔒 Error handling for invalid inputs

🛠️ Technologies Used

Python 3
Tkinter (GUI)
CSV Module (Data Storage)
OS Module (File Handling)

📂 Project Structure

BMI_CALCULATOR/
│
├── bmi_gui.py        # Main GUI application
├── bmi_data.csv      # Stores BMI records
└── README.md         # Project documentation

⚙️ How It Works

User enters:

Name
Weight (kg)
Height (cm)
BMI is calculated using:
BMI = weight / (height * height)
Health category is identified automatically
Data is saved into bmi_data.csv
Result is displayed on the screen

📊 BMI Categories
BMI Range	Health Category
< 18.5-Underweight
18.5 – 24.9-Normal
25 – 29.9-Overweight
≥ 30-Obese

▶️ How to Run the Application

python bmi_gui.py

📁 CSV Data Storage

All user BMI records are saved in bmi_data.csv in the following format:
Name,Weight,Height,BMI,Category

🚀 Future Enhancements

Add BMI history visualization (charts)
Export data to Excel
Add age & gender-based analysis
Improve UI design

🎓 Conclusion

This project demonstrates Python GUI development, file handling, and basic health-related calculations, making it ideal for internship evaluation and academic submission.
