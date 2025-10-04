# 🔐 Phishing Website Detection Using Random Forest

This project is a machine learning-based solution for detecting phishing websites using a **Random Forest classifier**. It helps users determine whether a given website is legitimate or potentially malicious by analyzing specific features extracted from the URL and page metadata.

---

## 🚀 Features

- Detects phishing websites using a trained Random Forest model
- Accepts user input for prediction (from CSV file, form, or script)
- Lightweight and easy to deploy
- Cleanly structured and documented

---

## 📁 Project Structure

```
phishing_detection/
├── dataset/                # Contains the phishing dataset (CSV)
├── model/                  # Stores the trained Random Forest model (e.g., .pkl file)
├── main.py                 # Main script to run predictions
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/phishing_detection.git
cd phishing_detection
pip install -r requirements.txt
```

> 💡 Make sure you’re using a virtual environment for best practice.

---

## ▶️ How to Run

After installing the required packages, run the main script:

```bash
python phish_app.py
```

> Replace `phish_app.py` with the name of your script that performs prediction using the trained model.

---

## 📊 Algorithm Used

- **Random Forest Classifier**  
  A powerful ensemble method that builds multiple decision trees and merges them to improve accuracy and control overfitting.

---

## 🧠 Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- (Optional) Flask — if building a web interface

---

## 📦 Requirements

Install required libraries with:

```bash
pip install -r requirements.txt
```

Typical packages used:

```
scikit-learn
pandas
numpy
```

---

## 📌 Dataset

You can use datasets like:

- [Phishing Websites Dataset from UCI](https://archive.ics.uci.edu/ml/datasets/Phishing+Websites)
- Or any labeled CSV dataset with phishing indicators

---

## 👨‍💻 Author

**Abdifatah Adam**  
[GitHub](https://github.com/ENG-duurgal)  


---

## 📜 License

This project is open-source and free to use for educational purposes.
