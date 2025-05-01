import streamlit as st
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten 

# Load and preprocess the dataset
@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv('train.txt', sep=";")
    data.columns = ['Text', "Emotions"]
    return data

# Train the model
@st.cache(allow_output_mutation=True)
def train_model():
    data = load_data()
    text = data['Text'].tolist()
    labels = data['Emotions'].tolist()

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(text)

    sequences = tokenizer.texts_to_sequences(text)
    max_length = max([len(seq) for seq in sequences])
    padded_sequences = pad_sequences(sequences, maxlen=max_length)

    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(labels)
    one_hot_labels = keras.utils.to_categorical(labels)

    xtrain, x_test, y_train, y_test = train_test_split(padded_sequences, one_hot_labels, test_size=0.2)

    model = Sequential()
    model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=128, input_length=max_length))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(units=len(one_hot_labels[0]), activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(xtrain, y_train, epochs=2, batch_size=32, validation_data=(x_test, y_test))

    return model, tokenizer, label_encoder, max_length

# Streamlit app
st.title("Emotion Detection App")
st.write("Enter a sentence to predict its emotion.")

# Input text
input_text = st.text_input("Enter your text here:")

# Load model and tokenizer
model, tokenizer, label_encoder, max_length = train_model()

if st.button("Predict Emotion"):
    if input_text.strip():
        # Preprocess input text
        input_sequence = tokenizer.texts_to_sequences([input_text])
        padded_input_sequence = pad_sequences(input_sequence, maxlen=max_length)

        # Predict emotion
        prediction = model.predict(padded_input_sequence)
        predicted_label = label_encoder.inverse_transform([np.argmax(prediction[0])])

        # Display result
        st.write(f"Predicted Emotion: **{predicted_label[0]}**")
    else:
        st.write("Please enter some text to predict.")