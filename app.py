import streamlit as st
import joblib
import numpy as np


st.sidebar.title('Введите значения для каждого признака')
f1 = st.sidebar.number_input('Время, затраченное на этап "Продувка"')
f2 = st.sidebar.number_input('Доля O2 в отх. газах (медиана)')
f3 = st.sidebar.number_input('Доля H2 в отх. газах (медиана)')
f4 = st.sidebar.number_input('Доля СО2 в отх. газах')
f5 = st.sidebar.number_input('Марка заданная')
f6 = st.sidebar.number_input('Доля СО2 в отъ. газах (стандартное отклонение)')
f7 = st.sidebar.number_input('Направление разливки')
f8 = st.sidebar.number_input('Доля О2 в отх. газах (суммарное значение)')
f9 = st.sidebar.number_input('Время, затраченное на этап "Обрыв горловины"')
f10 = st.sidebar.number_input('Температура чугуна')



l = np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10], dtype = "float32").reshape(1, -1)
model = joblib.load("model.pkl")
pred = model.predict(l)

temp = np.round(pred[0][0])
c = pred[0][1]

st.write('Температура: ', temp)
st.write('Содержание углерода: ', c)

