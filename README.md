# fish-image-classification

# 🐟 Multiclass Fish Image Classification

## 📌 Project Overview

This project focuses on building a **Deep Learning–based image classification system** that can identify different species of fish from images. The solution uses **Convolutional Neural Networks (CNN)** and **Transfer Learning with pre-trained models** to improve classification accuracy.

The trained model is deployed using a **Streamlit web application** that allows users to upload a fish image and get the predicted fish category with a confidence score.

---

# 🎯 Problem Statement

Fish species classification is an important task in **marine biology, fisheries management, and the seafood industry**. Manual identification of fish species can be time-consuming and error-prone.

The goal of this project is to develop an **automated system that classifies fish images into multiple categories using deep learning techniques**.

---

# 🧠 Skills & Technologies Used

* Python
* Deep Learning
* TensorFlow / Keras
* Convolutional Neural Networks (CNN)
* Transfer Learning
* Image Processing
* Model Evaluation
* Streamlit
* GitHub

---

# 🏗️ Project Workflow

## 1️⃣ Data Collection

The dataset contains images of different fish species organized into folders where each folder represents a class.

Example structure:

```
data/
 ├── train/
 ├── test/
 └── val/
```

---

## 2️⃣ Data Preprocessing

The following preprocessing steps were applied:

* Resize images to **224 × 224**
* Normalize pixel values
* Convert images to RGB format

---

## 3️⃣ Data Augmentation

To improve model generalization and prevent overfitting:

* Random rotation
* Random zoom
* Horizontal flipping

---

## 4️⃣ Model Development

Two approaches were used:

### Baseline Model

A **CNN model built from scratch**.

### Transfer Learning Models

Five pre-trained models were used:

* VGG16
* ResNet50
* MobileNet
* InceptionV3
* EfficientNetB0

Pre-trained models were initialized with **ImageNet weights** and fine-tuned on the fish dataset.

---

## 5️⃣ Model Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Training history (accuracy and loss) was also visualized to analyze model performance.

---

## 6️⃣ Model Selection

The model with the **highest validation accuracy** was selected as the final model and saved as a `.h5` file.

```
best_model.h5
```

---

# 🚀 Streamlit Deployment

A **Streamlit web application** was built to allow users to:

* Upload a fish image
* Predict fish species
* Display prediction confidence

Run the application using:

```
streamlit run app.py
```

---

# 📂 Project Structure

```
fish-image-classification
│
├── app.py
├── best_model.h5
├── requirements.txt
├── README.md
│
├── notebooks
│   └── training.ipynb
│
├── models
│   └── saved_models
│
└── screenshots
    └── streamlit_output.png
```

---

# 📦 Requirements

Install dependencies using:

```
pip install -r requirements.txt
```

Example requirements:

```
tensorflow
streamlit
numpy
pillow
scikit-learn
matplotlib
```

---

# 📊 Model Prediction Example

Upload a fish image in the Streamlit app.

Output example:

```
Predicted Fish: Sea Bass
Confidence: 94.7%
```

---

# 💡 Business Use Cases

* Fish species identification
* Marine biodiversity research
* Fisheries monitoring
* Seafood industry automation

---

# 🔮 Future Improvements

* Improve dataset size
* Apply advanced augmentation
* Use ensemble models
* Deploy as a cloud API
