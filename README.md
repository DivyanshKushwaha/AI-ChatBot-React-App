# Chatbot with Google Gemini API and SQL Integration  

This project is an AI-powered chatbot that uses **Google Gemini API** for intelligent responses and integrates with a **SQL database** to retrieve product and supplier information.  

## 🚀 Features  

- Natural language understanding with **Google Gemini API**  
- Fetches products by **brand** from the database  
- Retrieves suppliers by **category**  
- Handles **common greetings** and responses  
- Uses **React.js (Material UI) for frontend** and **Flask for backend**  

## 🛠️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-repo/chatbot-project.git
cd chatbot-project
```
### 2️⃣ Backend Setup
- Install Dependencies
```bash

cd backend
pip install -r requirements.txt
```
- Configure Environment Variables
- Create a .env file inside backend/ and add:
    - GEMINI_API_KEY=your_google_gemini_api_key
    - DB_HOST=your_database_host
    - DB_NAME=your_database_name
    - DB_USER=your_database_username
    - DB_PASSWORD=your_database_password



- Run Flask Server
``` bash
python app.py
```
### 3️⃣ Frontend Setup
- Install Dependencies
```bash
cd frontend
npm install
```

- Start React App
``` bash
npm start
```

## 🎯 Usage
- Start typing your query in the chat window.
- Example queries:
    - 🛒 "List products of brand Apple"
    - 🏢 "Which supplier provides Laptops?"
- The chatbot will fetch relevant data from the database and respond accordingly.


## 📝 Notes
- Ensure your Google Gemini API key is valid.
- The Flask backend must be running before starting the React frontend.
- Keep your .env file secure and do not share credentials.