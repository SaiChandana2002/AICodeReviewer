 AI-Driven Python Code Reviewer

📌 Overview

An intelligent Python code review tool built with Streamlit and Google Gemini AI. This application reviews Python scripts, detects bugs, logical errors, and suggests improvements along with clear explanations.

✨ Features

🤖 Advanced AI Code Analysis: Powered by Google Gemini 1.5 Pro for in-depth Python code evaluation.

🐛 Bug Identification & Solutions: Spots issues in the code and recommends optimized fixes.

📖 Insightful Explanations: Provides detailed reasoning behind each identified issue and its solution.

🎨 Intuitive UI: Clean and user-friendly interface built using Streamlit.

⚙️ Installation

🔹 Prerequisites

Python 3.7 or higher must be installed.

🔹 Install Dependencies

Run the following command to install all required libraries:

pip install -r requirements.txt

🚀 Usage

📥 Clone the repository or copy the project files.

▶️ Launch the Streamlit app:

python -m streamlit run app.py

✍️ Input your Python code in the text area.

🔄 Click the Review button.

✅ Receive:

🔍 Detailed Bug Report

🛠 Suggested Fixed Code

📚 Clear Explanations


🔧 Configuration

Integrate your Google Gemini API key by updating the configuration:

ai.configure(api_key="YOUR_API_KEY")


📁 Project Structure

/ai_code_reviewer
│── app.py               # Main Streamlit application
│── README.md            # Documentation
└── requirements.txt      # Dependency list

🤝 Contributing

Feel free to fork the repository, suggest improvements, or submit pull requests.
