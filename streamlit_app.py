import streamlit as st
import joblib
import numpy as np


st.sidebar.title('Введите значения для каждого признака')
f1 = st.sidebar.number_input('Время, затраченное на этап "Продувка"')
f2 = st.sidebar.number_input('Доля O2 в отх. газах (медиана)')
f3 = st.sidebar.number_input('Доля H2 в отх. газах (медиана)')
f4 = st.sidebar.number_input('Доля СО2 в отх. газах')
f5 = st.sidebar.text_input('Марка заданная')
f6 = st.sidebar.number_input('Доля СО2 в отъ. газах (стандартное отклонение)')
f7 = st.sidebar.text_input('Направление разливки')
f8 = st.sidebar.number_input('Доля О2 в отх. газах (суммарное значение)')
f9 = st.sidebar.number_input('Время, затраченное на этап "Обрыв горловины"')
f10 = st.sidebar.number_input('Температура чугуна')



l = np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]).reshape(1, -1)
model1 = joblib.load("cb_temp.pkl")
model2 = joblib.load("cb_c.pkl")
pred_t = model1.predict(l)
pred_c = model2.predict(l)

temp = np.round(pred_t[0])
c = pred_c[0]

st.write('Температура: ', temp)
st.write('Содержание углерода: ', c)

