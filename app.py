import streamlit as st
import pandas as pd
import plotly.express as px

def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Suggestions")
    Rest_Mex = load_data("dataset_rm.csv")
    menu = ["Home","States","Cities","Mexican Restaurants"]

    choice = st.sidebar.selectbox("Menu",menu)
    color = st.sidebar.color_picker("Color",value="#0000ff")

    if choice == "Home":
        with st.expander("Data View"):
            st.dataframe(Rest_Mex)
        fig = px.scatter_mapbox(Rest_Mex,lat="Latitude",lon="Longitude",hover_name="Mexican restaurant",hover_data=["Address","City","state","Stars","Sentiment"],
                                    color_discrete_sequence=[color],zoom=2,height=700)
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig)

    elif choice == "States": 
        states_list =  Rest_Mex["state"].unique().tolist()
        selected_state = st.sidebar.selectbox("State",states_list)
        with st.expander("Data View"):
            df = Rest_Mex[Rest_Mex["state"] == selected_state]
            st.dataframe(df)
        fig = px.scatter_mapbox(df,lat="Latitude",lon="Longitude",hover_name="Mexican restaurant",hover_data=["Address","City","State","Stars","Sentiment"],
                                    color_discrete_sequence=[color],zoom=2,height=700)
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig)
    
    elif choice == "Cities":
        cities_list =  Rest_Mex["City"].unique().tolist()
        selected_city = st.sidebar.selectbox("City", cities_list)
        with st.expander("Data View"):
            df = Rest_Mex[Rest_Mex["City"] == selected_city]
            st.dataframe(df)
        fig = px.scatter_mapbox(df,lat="Latitude",lon="Longitude",hover_name="Mexican restaurant",hover_data=["Address","City","State","Stars","Sentiment"],
                                    color_discrete_sequence=[color],zoom=5,height=700)
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig)

    else:
        st.subheader("Mexican Restaurants")


if __name__ == "__main__":
    main()
