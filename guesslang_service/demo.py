import guesslang
import pandas as pd
import streamlit as st


@st.cache(hash_funcs={guesslang.Guess: id})
def get_guesslang():
    return guesslang.Guess()

col1, col2 = st.columns(2)
with col1:
    code = st.text_area("Code", "", height=500)

with col2:
    guess = get_guesslang()
    result_list = guess.probabilities(code) 
    df = pd.DataFrame((result_list), columns=["Langauage", "Prob"])
    st.table(df)
    

