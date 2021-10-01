import streamlit as st
from PIL import Image
import base64
import pandas as pd
import numpy as np



def main():
    img = Image.open("web_logo1.png")
    st.set_page_config(page_title='Concrete Compressive Strength Prediction App', page_icon=img, layout='wide')

    hide_menu_style = """
            <style>
            #MainMenu {visibility:hidden; }
            footer {visibility:hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    st.error("Application in progress....coming soon...!!!")

    st.title("Concrete Compressive Strength Prediction App")
    image=Image.open("concrete_png.png")
    st.image(image,use_column_width=True)

    st.write("""
    This App predicts the Compressive Strength of Concrete, reducing the wait time, labour and human error.

    **Python Libraries Used : ** streamlit, pandas, numpy, sklearn
    
    
    """)
    st.write("**Dataset : ** Data is obtained from Kaggle.")

    df = pd.read_csv('concrete.csv',sep=';')

    def convert_df(df):
        return df.to_csv().encode('utf-8')
    
    csv = convert_df(df)

    st.download_button(
        "Download Data as CSV",
        csv,
        "cement_data.csv",
        "text/csv",
        key='concrete-cement-compressive-strength'
    )


if __name__ == '__main__':
    main() 

