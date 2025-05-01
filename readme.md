# Emotion Detection Model

This project is a machine learning-based emotion detection system that classifies text into different emotions. It uses a neural network built with TensorFlow and Keras, and the model is trained on a labeled dataset of text and emotions.

## Features
- Preprocesses text data using tokenization and padding.
- Encodes emotion labels into numerical format using `LabelEncoder`.
- Trains a neural network model to classify text into emotions.
- Predicts the emotion of user-inputted text.

## How It Works
1. **Data Preprocessing**:
   - The text data is tokenized and converted into sequences.
   - Sequences are padded to ensure uniform input length.
   - Emotion labels are encoded into numerical format and converted to one-hot encoding.

2. **Model Training**:
   - A Sequential neural network is built with an embedding layer, a flattening layer, and dense layers.
   - The model is trained using the `categorical_crossentropy` loss function and the Adam optimizer.

3. **Prediction**:
   - The trained model predicts the emotion of a given text input.
   - The predicted label is decoded back into its original emotion label.

## File Structure
- `emotions.ipynb`: Jupyter Notebook containing the code for data preprocessing, model training, and prediction.
- `train.txt`: Dataset file containing text and corresponding emotion labels (not included here).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/emotion-detection.git
   cd emotion-detection