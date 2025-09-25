# 🌱 Plant Leaf Disease Detection  

A deep learning–based project for **plant disease classification** using image recognition. The system leverages **Convolutional Neural Networks (CNNs)** trained on a dataset of healthy and diseased plant leaves to accurately detect plant diseases.  

---

## 📖 Table of Contents  

- [Introduction](#introduction)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Dataset](#dataset)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Model Training](#model-training)  
- [Model Deployment](#model-deployment)  
- [Dependencies](#dependencies)  
- [Troubleshooting](#troubleshooting)  
- [Contributors](#contributors)  
- [License](#license)  

---

## 🌟 Introduction  

This project applies **deep learning** techniques to detect and classify plant diseases from leaf images. Early detection helps farmers and researchers prevent crop loss and improve yield.  

It includes:  
- Scripts for training and testing CNN models.  
- Pre-trained models in `.h5` and `.json` format.  
- Example image testing scripts.  
- A simple HTML template for UI integration.  

---

## 🚀 Features  

- Image-based plant disease detection.  
- Pre-trained CNN models for faster testing.  
- Easy-to-run scripts for training and evaluation.  
- Option to test with custom images.  
- Extensible for additional plant species/diseases.  

---

## 📂 Project Structure  

Final-Pro/
│
├── Training.py # Script to train the CNN model
├── leaf.py # Script for leaf disease detection
├── Example1.py / Example2.py ... # Example usage scripts
├── model.json # Model architecture
├── model.h5 # Pre-trained model weights
├── Templates/ # HTML template for UI integration
├── Dataset/ # Dataset of plant leaves (not included in repo)
└── README.md # Documentation


---

## 🌱 Dataset  

- The project expects a dataset of **plant leaf images** organized by category:

Dataset/
├── Healthy/
├── Diseased/
└── ...

- You can use datasets from sources like:  
- [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)  
- Custom collected leaf images  

---

## 🛠️ Installation  

1. Clone the repository:  
 ```bash
 git clone https://github.com/PavanRasipogula/Final-Pro.git
 cd Final-Pro
Install dependencies:

pip install -r requirements.txt
▶️ Usage
Run Leaf Detection Script
python leaf.py
Test with Pre-trained Model
python Example1.py
Train a New Model
python Training.py


#🧠 Model Training

The CNN is defined in Training.py.

By default, it trains on images from the Dataset/ folder.

After training, it saves:

model.json → model architecture

model.h5 → model weights

You can adjust hyperparameters (epochs, batch size, learning rate) inside the script.

## Model Deployment

A Templates/ folder contains a basic HTML interface.

You can integrate the trained model into a Flask or Django backend to serve predictions via web.

Deployment options:

Local Flask/Django server

Docker container

Cloud platforms like Heroku, AWS, or GCP

📚 Dependencies

The project requires:

Python 3.7+

TensorFlow / Keras

NumPy

OpenCV

Matplotlib

Flask (for web integration)

Install them manually if requirements.txt is not available:

👥 Contributors

Pavan Kumar – Author & Maintainer

📜 License

This project is licensed under the MIT License
.


---

Do you also want me to **generate a `requirements.txt` file** with the main dependencies, so that users can set up the project more easily?

