import streamlit as st
import joblib
import numpy as np

f1 = st.number_input('Введите значение признака 1')
f2 = st.number_input('Введите значение признака 2')
f3 = st.number_input('Введите значение признака 3')
f4 = st.number_input('Введите значение признака 4')
f5 = st.number_input('Введите значение признака 5')
f6 = st.number_input('Введите значение признака 6')
f7 = st.number_input('Введите значение признака 7')
f8 = st.number_input('Введите значение признака 8')
f9 = st.number_input('Введите значение признака 9')
f10 = st.number_input('Введите значение признака 10')


l = np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10], dtype = "float32").reshape(1, -1)
model = joblib.load("model.pkl")
pred = model.predict(l)

temp = np.round(pred[0][0])
c = pred[0][1]

st.write('Температура: ', temp)
st.write('Содержание углерода: ', c)

st.write(l)