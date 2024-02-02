import streamlit as st
import pandas as pd

st.title("Sistema de Recomendación")

df = pd.read_csv("dataset_stream.csv")
df.dropna(inplace=True)

if st.checkbox("🌮Restaurantes mexicanos en USA"):
    st.write(df)

col1,col2,col3,col4 = st.columns([3,3,3,3])

df1 = df[(df["Stars"]==1)&(df["State"]=="AZ")][["State","Name","Address","City"]]
df_ = df[(df["Stars"]==2)&(df["State"]=="AZ")][["State","Name","Address","City"]]
df_1 = df[(df["Stars"]==3)&(df["State"]=="AZ")][["State","Name","Address","City"]]
df_2 = df[(df["Stars"]==4)&(df["State"]=="AZ")][["State","Name","Address","City"]]
df_3 = df[(df["Stars"]==5)&(df["State"]=="AZ")][["State","Name","Address","City"]]
df_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="AZ")][["State","Name","Address","City"]]
df2 = df[(df["Stars"]==1)&(df["State"]=="CA")][["State","Name","Address","City"]]
df1_ = df[(df["Stars"]==2)&(df["State"]=="CA")][["State","Name","Address","City"]]
df1_1 = df[(df["Stars"]==3)&(df["State"]=="CA")][["State","Name","Address","City"]]
df1_2 = df[(df["Stars"]==4)&(df["State"]=="CA")][["State","Name","Address","City"]]
df1_3 = df[(df["Stars"]==5)&(df["State"]=="CA")][["State","Name","Address","City"]]
df1_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="CA")][["State","Name","Address","City"]]
df3 = df[(df["Stars"]==1)&(df["State"]=="FL")][["State","Name","Address","City"]]
df2_ = df[(df["Stars"]==2)&(df["State"]=="FL")][["State","Name","Address","City"]]
df2_1 = df[(df["Stars"]==3)&(df["State"]=="FL")][["State","Name","Address","City"]]
df2_2 = df[(df["Stars"]==4)&(df["State"]=="FL")][["State","Name","Address","City"]]
df2_3 = df[(df["Stars"]==5)&(df["State"]=="FL")][["State","Name","Address","City"]]
df2_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="FL")][["State","Name","Address","City"]]
df4 = df[(df["Stars"]==1)&(df["State"]=="PA")][["State","Name","Address","City"]]
df3_ = df[(df["Stars"]==2)&(df["State"]=="PA")][["State","Name","Address","City"]]
df3_1 = df[(df["Stars"]==3)&(df["State"]=="PA")][["State","Name","Address","City"]]
df3_2 = df[(df["Stars"]==4)&(df["State"]=="PA")][["State","Name","Address","City"]]
df3_3 = df[(df["Stars"]==5)&(df["State"]=="PA")][["State","Name","Address","City"]]
df3_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="PA")][["State","Name","Address","City"]]
df5 = df[(df["Stars"]==1)&(df["State"]=="MO")][["State","Name","Address","City"]]
df4_ = df[(df["Stars"]==2)&(df["State"]=="MO")][["State","Name","Address","City"]]
df4_1 = df[(df["Stars"]==3)&(df["State"]=="MO")][["State","Name","Address","City"]]
df4_2 = df[(df["Stars"]==4)&(df["State"]=="MO")][["State","Name","Address","City"]]
df4_3 = df[(df["Stars"]==5)&(df["State"]=="MO")][["State","Name","Address","City"]]
df4_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="MO")][["State","Name","Address","City"]]
df6 = df[(df["Stars"]==1)&(df["State"]=="IN")][["State","Name","Address","City"]]
df5_ = df[(df["Stars"]==2)&(df["State"]=="IN")][["State","Name","Address","City"]]
df5_1 = df[(df["Stars"]==3)&(df["State"]=="IN")][["State","Name","Address","City"]]
df5_2 = df[(df["Stars"]==4)&(df["State"]=="IN")][["State","Name","Address","City"]]
df5_3 = df[(df["Stars"]==5)&(df["State"]=="IN")][["State","Name","Address","City"]]
df5_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="IN")][["State","Name","Address","City"]]
df7 = df[(df["Stars"]==1)&(df["State"]=="TN")][["State","Name","Address","City"]]
df6_ = df[(df["Stars"]==2)&(df["State"]=="TN")][["State","Name","Address","City"]]
df6_1 = df[(df["Stars"]==3)&(df["State"]=="TN")][["State","Name","Address","City"]]
df6_2 = df[(df["Stars"]==4)&(df["State"]=="TN")][["State","Name","Address","City"]]
df6_3 = df[(df["Stars"]==5)&(df["State"]=="TN")][["State","Name","Address","City"]]
df6_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="TN")][["State","Name","Address","City"]]
df8 = df[(df["Stars"]==1)&(df["State"]=="LA")][["State","Name","Address","City"]]
df7_ = df[(df["Stars"]==2)&(df["State"]=="LA")][["State","Name","Address","City"]]
df7_1 = df[(df["Stars"]==3)&(df["State"]=="LA")][["State","Name","Address","City"]]
df7_2 = df[(df["Stars"]==4)&(df["State"]=="LA")][["State","Name","Address","City"]]
df7_3 = df[(df["Stars"]==5)&(df["State"]=="LA")][["State","Name","Address","City"]]
df7_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="LA")][["State","Name","Address","City"]]
df9 = df[(df["Stars"]==1)&(df["State"]=="NV")][["State","Name","Address","City"]]
df8_ = df[(df["Stars"]==2)&(df["State"]=="NV")][["State","Name","Address","City"]]
df8_1 = df[(df["Stars"]==3)&(df["State"]=="NV")][["State","Name","Address","City"]]
df8_2 = df[(df["Stars"]==4)&(df["State"]=="NV")][["State","Name","Address","City"]]
df8_3 = df[(df["Stars"]==5)&(df["State"]=="NV")][["State","Name","Address","City"]]
df8_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="NV")][["State","Name","Address","City"]]
df10 = df[(df["Stars"]==1)&(df["State"]=="ID")][["State","Name","Address","City"]]
df9_ = df[(df["Stars"]==2)&(df["State"]=="ID")][["State","Name","Address","City"]]
df9_1 = df[(df["Stars"]==3)&(df["State"]=="ID")][["State","Name","Address","City"]]
df9_2 = df[(df["Stars"]==4)&(df["State"]=="ID")][["State","Name","Address","City"]]
df9_3 = df[(df["Stars"]==5)&(df["State"]=="ID")][["State","Name","Address","City"]]
df9_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="ID")][["State","Name","Address","City"]]
df11 = df[(df["Stars"]==1)&(df["State"]=="NJ")][["State","Name","Address","City"]]
df10_ = df[(df["Stars"]==2)&(df["State"]=="NJ")][["State","Name","Address","City"]]
df10_1 = df[(df["Stars"]==3)&(df["State"]=="NJ")][["State","Name","Address","City"]]
df10_2 = df[(df["Stars"]==4)&(df["State"]=="NJ")][["State","Name","Address","City"]]
df10_3 = df[(df["Stars"]==5)&(df["State"]=="NJ")][["State","Name","Address","City"]]
df10_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="NJ")][["State","Name","Address","City"]]
df12 = df[(df["Stars"]==1)&(df["State"]=="DE")][["State","Name","Address","City"]]
df11_ = df[(df["Stars"]==2)&(df["State"]=="DE")][["State","Name","Address","City"]]
df11_1 = df[(df["Stars"]==3)&(df["State"]=="DE")][["State","Name","Address","City"]]
df11_2 = df[(df["Stars"]==4)&(df["State"]=="DE")][["State","Name","Address","City"]]
df11_3 = df[(df["Stars"]==5)&(df["State"]=="DE")][["State","Name","Address","City"]]
df11_4 = df[(df["Valoracion"]=="Muy bueno")&(df["State"]=="DE")][["State","Name","Address","City"]]
if col1.checkbox("Arizona"):
    if col1.button("AZ⭐"):
        st.write("Peores restaurantes 👎",df1.head())
    if col1.button("AZ⭐⭐"):
        st.write("Restaurantes 2 ⭐",df_.head())
    if col1.button("AZ⭐⭐⭐"):
        st.write("Restaurantes 3 ⭐",df_1.head())
    if col1.button("AZ⭐⭐⭐⭐"):
        st.write("Restaurantes 4 ⭐",df_2.head())
    if col1.button(" AZ⭐⭐⭐⭐⭐ "):
        st.write("Restaurantes 5 ⭐",df_3.head())
    if col1.button("AZ✅"):
        st.write(" Mejores restaurantes 👍 ",df_4.head())
if col2.checkbox("California"):
    if col2.button("CA⭐"):
        st.write(" Peores restaurantes 👎 ",df2.head())
    if col2.button("CA⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df1_.head())
    if col2.button("CA⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df1_1.head())
    if col2.button("CA⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df1_2.head())
    if col2.button("CA⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df1_3.head())
    if col2.button("CA✅"):
        st.write(" Mejores restaurantes 👍 ",df1_4.head())
if col3.checkbox("Florida"):
    if col3.button("FL⭐"):
        st.write(" Peores restaurantes 👎 ",df3.head())
    if col3.button("FL⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df2_.head())
    if col3.button("FL⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df2_1.head())
    if col3.button("FL⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df2_2.head())
    if col3.button("FL⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df2_3.head())
    if col3.button("FL✅"):
        st.write(" Mejores restaurantes 👍",df2_4.head())
if col4.checkbox("Pensilvania"):
    if col4.button("PA⭐"):
        st.write(" Peores restaurantes 👎 ",df4.head())
    if col4.button("PA⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df3_.head())
    if col4.button("PA⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df3_1.head())
    if col4.button("PA⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df3_2.head())
    if col4.button("PA⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df3_3.head())
    if col4.button("PA✅"):
        st.write(" Mejores restaurantes 👍 ",df3_4.head())
if col1.checkbox("Missouri"):
    if col1.button("MO⭐"):
        st.write(" Peores restaurantes 👎 ",df5.head())
    if col1.button("MO⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df4_.head())
    if col1.button("MO⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df4_1.head())
    if col1.button("MO⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df4_2.head())
    if col1.button("MO⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df4_3.head())
    if col1.button("MO✅"):
        st.write(" Mejores restaurantes 👍 ",df4_4.head())
if col2.checkbox("Indiana"):
    if col2.button("IN⭐"):
        st.write(" Peores restaurantes 👎 ",df6.head())
    if col2.button("IN⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df5_.head())
    if col2.button("IN⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df5_1.head())
    if col2.button("IN⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df5_2.head())
    if col2.button("IN⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df5_3.head())
    if col2.button("IN✅"):
        st.write(" Mejores restaurantes 👍 ",df5_4.head())
if col3.checkbox("Tennessee"):
    if col3.button("TN⭐"):
        st.write(" Peores restaurantes 👎 ",df7.head())
    if col3.button("TN⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df6_.head())
    if col3.button("TN⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df6_1.head())
    if col3.button("TN⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df6_2.head())
    if col3.button("TN⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df6_3.head())
    if col3.button("TN✅"):
        st.write(" Mejores restaurantes 👍 ",df6_4.head())
if col4.checkbox("Luisiana"):
    if col4.button("LA⭐"):
        st.write(" Peores restaurantes  👎",df8.head())
    if col4.button("LA⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df7_.head())
    if col4.button("LA⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df7_1.head())
    if col4.button("LA⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df7_2.head())
    if col4.button("LA⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df7_3.head())
    if col4.button("LA✅"):
        st.write(" Mejores restaurantes 👍 ",df7_4.head())
if col1.checkbox("Nevada"):
    if col1.button("NV⭐"):
        st.write(" Peores restaurantes 👎 ",df9.head())
    if col1.button("NV⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df8_.head())
    if col1.button("NV⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df8_1.head())
    if col1.button("NV⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df8_2.head())
    if col1.button("NV⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df8_3.head())
    if col1.button("NV✅"):
        st.write(" Mejores restaurantes 👍 ",df8_4.head())
if col2.checkbox("Idaho"):
    if col2.button("ID⭐"):
        st.write(" Peores restaurantes 👎 ",df10.head())
    if col2.button("ID⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df9_.head())
    if col2.button("ID⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df9_1.head())
    if col2.button("ID⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df9_2.head())
    if col2.button("ID⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df9_3.head())
    if col2.button("ID✅"):
        st.write(" Mejores restaurantes 👍 ",df9_4.head())
if col3.checkbox("Nueva Jersey"):
    if col3.button("NJ⭐"):
        st.write(" Peores restaurantes 👎 ",df11.head())
    if col3.button("NJ⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df10_.head())
    if col3.button("NJ⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df10_1.head())
    if col3.button("NJ⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df10_2.head())
    if col3.button("NJ⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df10_3.head())
    if col3.button("NJ✅"):
        st.write(" Mejores restaurantes 👍 ",df10_4.head())
if col4.checkbox("Delaware"):
    if col4.button("DE⭐"):
        st.write(" Peores restaurantes 👎 ",df12.head())
    if col4.button("DE⭐⭐"):
        st.write(" Restaurantes 2 ⭐ ",df11_.head())
    if col4.button("DE⭐⭐⭐"):
        st.write(" Restaurantes 3 ⭐ ",df11_1.head())
    if col4.button("DE⭐⭐⭐⭐"):
        st.write(" Restaurantes 4 ⭐ ",df11_2.head())
    if col4.button("DE⭐⭐⭐⭐⭐"):
        st.write(" Restaurantes 5 ⭐ ",df11_3.head())
    if col4.button("DE✅"):
        st.write(" Mejores restaurantes 👍 ",df11_4.head())
