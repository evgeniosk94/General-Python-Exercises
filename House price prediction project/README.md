# 🏠 Bangalore Home Price Prediction App

This is a simple machine learning web application that predicts housing prices in Bangalore based on user input (location, square footage, number of bedrooms, and bathrooms). It consists of an end-to-end pipeline from data cleaning to web-based predictions.

---

## 📂 Project Structure

```
.
├── 01_eda_cleaning.ipynb       # Data cleaning and EDA notebook
├── cleaned_data.csv            # Cleaned dataset (generated)
├── src/
│   └── main.py                 # Trains model and generates columns.json
├── app/
│   ├── server.py               # Flask backend API
│   ├── app.html                # Frontend interface
│   ├── app.js                  # Frontend JS logic
│   ├── app.css                 # Stylesheet
│   └── artifacts/
│       └── columns.json        # Model metadata (needs to be pasted here)
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

Follow these steps to run the full project:

### 1. 📊 Generate the Cleaned Dataset
First, run the notebook `01_eda_cleaning.ipynb` to preprocess the raw housing data and generate:
```
cleaned_data.csv
```
This file is required by the model training script in the next step.

---

### 2. 🛠️ Train the Model and Generate `columns.json`
From the `src` folder, run:

```bash
python main.py
```

This will:
- Train the machine learning model on the cleaned dataset
- Generate `columns.json`, which includes metadata like location names

---

### 3. 📁 Move `columns.json` to the Correct Folder
Copy the `columns.json` file from the `src` directory and paste it into:

```
app/artifacts/
```

This step is crucial for the server to load location data properly.

---

### 4. 🖥️ Run the Flask Server
Navigate to the `app` folder and run:

```bash
python server.py
```

This will start a Flask backend server on `http://127.0.0.1:5000`.

---

### 5. 🌐 Launch the Frontend App
Open `app.html` (located in the `app` folder) **in a browser**. This HTML file communicates with the Flask server to:
- Populate location dropdown dynamically
- Send prediction inputs
- Display estimated housing prices

---

## ⚙️ Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

Ensure you're using a **virtual environment**. You can create one like this:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

---

## 📌 Important Notes

- Make sure the Flask server (`server.py`) is running before opening `app.html`, otherwise location loading and predictions won't work.
- Do **not** forget to move the `columns.json` to the `artifacts/` folder as the app depends on it for input validation.
- This app is for educational/demo purposes and uses a simple linear regression model — performance may vary in real-world cases.

---

## 📬 Contact
Feel free to reach out if you have questions or suggestions!

---

## 📄 License
This project is open-source and free to use under the MIT License.