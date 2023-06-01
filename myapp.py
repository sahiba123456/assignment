import streamlit as st
import pandas as pd
 
st.header("Area Chart")
 
data = {"a":[23, 12, 78, 4, 54], "b":[0, 13 ,88, 51, 3], 
"c":[45, 2, 46, 67, 56]}
 
df = pd.DataFrame(data)
df
st.area_chart(df)
