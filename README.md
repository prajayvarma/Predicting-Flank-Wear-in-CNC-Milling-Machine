# Predicting-Flank-Wear-in-CNC-Milling-Machine

Predicting Flank Wear in CNC Milling Machines : This project focuses on predicting flank wear in CNC milling tools using machine learning techniques. We analyze sensor data and machining parameters to build a simple yet effective model that can estimate tool wear and potentially help in predictive maintenance.

👥 Team Members

Chinthala Prajay Varma (230003018)

Jaajimoggala Ramaraju (230003018)

Banoth Santhosh (230003014)

🧩 Project Overview

The goal is to build a data-driven model to estimate the flank wear (VB) of cutting tools during CNC milling operations. By analyzing sensor readings (like spindle vibration and motor current) along with machining parameters such as feed rate, depth of cut, and time, we aim to predict how worn a tool is — without direct physical inspection.

📁 Dataset Summary

We worked with data from 109 machining runs, split into:

Training data: 52 runs

Testing data: 57 runs

Each run includes:

Sensor Readings

Spindle Motor Current (DC)

Vibration (VIB)

Machining Parameters

Feed Rate

Depth of Cut

Time

Target Variable

VB (Flank Wear)

🔍 Methodology

We tried two different data preprocessing strategies (called Score 1 and Score 2) to prepare input features before training our model.

🧪 Score 1: Simple Averaging

For each run, we took the mean of all 9000 sensor data points for DC and VIB.

Added feed rate and depth of cut as additional features.

Final features: DC, VIB, Feed, DOC

🧪 Score 2: Trimmed Mean

To reduce noise, we removed the lowest and highest 1000 values from each sensor's data.

Then took the mean of the remaining 7000 points.

Used time instead of feed & DOC.

Final features: DC, VIB, Time

🤖 Model Training & Evaluation

We used a Linear Regression model in MATLAB for simplicity and interpretability.

Tool: fitlm() function in MATLAB

Evaluation Metric: Root Mean Square Error (RMSE)

MATLAB snippet for model evaluation: { predictions_test = predict(lrModel, X_test); rmse_test = sqrt(mean((y_test - predictions_test).^2)); }

To visualize performance, we plotted actual vs. predicted VB values.
