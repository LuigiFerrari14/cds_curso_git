import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    return pd.read_csv('data/processed/bikes_completed.csv')


def main():
    df = load_data


if __name__ == '__main__':
    main()




df = load_data()

st.dataframe(df)