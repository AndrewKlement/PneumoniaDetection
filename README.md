# PneumoniaDetection

**Analyzing CNN and Transformer Models in Detecting Pneumonia from Chest X-Rays**

This repository contains the code and resources used in our research project comparing the performance of Convolutional Neural Networks (CNNs) and Transformer-based models in detecting pneumonia from chest X-ray images.

## 📌 Project Overview

Pneumonia is a serious infection that affects millions globally. Automated detection using deep learning on chest X-rays has shown great potential in improving diagnosis efficiency. In this project, we explore and evaluate the effectiveness of various CNN and Transformer architectures for binary classification of pneumonia presence.

## 👥 Authors

- Andrew Klement  
- Kevin Aprilian
- Alexander Agung
- Rilo Chandra Pradana

## 🧠 Models Used

We experimented with several deep learning models, including:

### Convolutional Neural Networks (CNNs)
- DenseNet121
- ResNet50

### Transformer-Based Models
- ViT-B/16 (Vision Transformer)
- Swin-T (Shifted Window Transformer)

## 📊 Evaluation Metrics

To compare models, we used the following performance metrics:
- Accuracy
- Precision
- Recall
- F1-Score

<a href="https://github.com/AndrewKlement/PneumoniaDetection/blob/main/Screenshot%202025-11-06%20083244.png" target="_blank">
        <img src='https://github.com/AndrewKlement/PneumoniaDetection/blob/main/Screenshot%202025-11-06%20083244.png' width='650px' alt='image missing' /> </a>

## 📊 Training & Validation Loss Graph
<a href="https://github.com/AndrewKlement/PneumoniaDetection/blob/main/metrics.png" target="_blank">
        <img src='https://github.com/AndrewKlement/PneumoniaDetection/blob/main/metrics.png' width='650px' alt='image missing' /> </a>

## 📁 Dataset
We used the [Chest X-Ray Images (Pneumonia) dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia), publicly available on Kaggle. It contains over 5,000 labeled chest X-ray images (Normal vs Pneumonia).

Note: Dataset is not included in this repository due to size. Please download it manually and place it in the appropriate folder.
