<img src="https://github.com/NathanielBirhanu/cancer_detector/blob/main/DALL%C2%B7E%202024-12-30%2022.31.15%20-%20A%20healthcare%20professional%20interacting%20with%20a%20medical%20interface%2C%20analyzing%20tumor%20data%20on%20a%20screen.%20The%20scene%20is%20focused%20on%20a%20person%20in%20a%20lab%20coat%20looki.webp" width="800" height= "500">


# Breast Cancer Prediction System

## Introduction
Breast cancer is a critical health issue that affects millions globally, with early and accurate diagnosis being key to reducing its impact. This project offers a simple, user-friendly solution for predicting whether a breast tumor is benign or malignant based on user-inputted characteristics. By combining a responsive frontend form with a Flask-based machine learning backend, this system empowers users and healthcare professionals with real-time predictions to aid in decision-making.

## 🎯 Objective
To create a lightweight and accessible web application that takes tumor characteristics as input, processes them through a machine learning model, and provides accurate predictions for breast cancer classification.

---

## 💡 Features

### Web-Based Input Form
- Intuitive and responsive form to collect tumor characteristics such as mean, standard error, and worst-case values.
- Organized sections for improved usability, making it easy to input data step-by-step.

### Flask-Integrated Machine Learning
- A backend powered by Flask to process user inputs.
- Real-time predictions using a pre-trained machine learning model hosted on the server.

### Real-Time Results
- Submit tumor data and instantly receive a classification of benign or malignant.
- Designed for quick and straightforward results.


---

## 🔍 Problem Overview
Breast tumors fall into two main categories:

- **Benign Tumors**: Non-cancerous growths that pose a lower risk but require monitoring.
- **Malignant Tumors**: Cancerous growths that demand immediate medical intervention.

Traditional diagnostic methods often rely on subjective visual analysis, which can be prone to errors. This project aims to support the diagnostic process by offering data-driven insights with greater accuracy.

---

## 🛠️ Project Approach

### **Frontend**
#### Technologies Used:
- **HTML5**, **CSS3** for structure and styling.
- **JavaScript** for interactivity and form validation.

#### Design Philosophy:
- Grouped inputs into logical sections (Mean, Standard Error, and Worst Features).
- Used a responsive layout with Flexbox for clean, side-by-side input organization.

### **Backend**
#### Framework: Flask
- A lightweight and powerful Python web framework for handling input data and serving predictions.

### **Model**
In this project, we use a **Logistic Regression** model to classify breast tumors as benign or malignant. Logistic Regression is a powerful yet simple algorithm that works well for binary classification problems like this one. It provides interpretable results and performs efficiently even on relatively small datasets.

### Key Steps:

#### Data Preprocessing:
- We clean the data, handle missing values, and normalize features for better model performance.
- We also split the data into training and test sets to evaluate the model's performance on unseen data.

#### Model Building:
- We implemented a Logistic Regression model using Scikit-learn to classify tumors based on their characteristics.
- To improve accuracy, we experimented with feature selection to remove irrelevant components and reduce dimensionality, preventing overfitting.

#### Evaluation:
- We evaluated the model using common metrics such as accuracy on both the training and test datasets.


#### Workflow:
1. User submits tumor characteristics via the form.
2. Flask backend processes the data and applies the model for prediction.
3. The result is returned to the user in real-time.

---

## 📊 Dataset
This system utilizes the Breast Cancer Wisconsin (Diagnostic) Dataset, a widely recognized dataset containing tumor characteristics, including:

- **Mean**, **Standard Error**, and **Worst-Case Values** for features like radius, texture, area, smoothness, and compactness.
- **Binary Labels**:
  - `0`: Benign
  - `1`: Malignant

---

## 📈 Performance
The machine learning model, trained using Logistic Regression, achieved:

- **Training Accuracy**: 98%
- **Test Accuracy**: 95%

These metrics demonstrate the model's ability to generalize well and provide reliable predictions.

---
