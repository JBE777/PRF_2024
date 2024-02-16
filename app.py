import streamlit as st
import pandas as pd
import plotly.express as px

def load_data(data):
    return pd.read_csv(data)

def main():
    st.title("Suggestions")
    Rest_Mex = load_data("dataset_rm.csv")
    menu = ["Home","States","Restaurants","Mexican Restaurants"]

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
    
    elif choice == "Restaurants":
        restaurants_list =  Rest_Mex["Mexican restaurant"].unique().tolist()
        selected_restaurant = st.multiselect("Restaurant", restaurants_list,default=["Taco Bell"])
        with st.expander("Data View"):
            df = Rest_Mex[Rest_Mex["Mexican restaurant"].isin(selected_restaurant)]
            st.dataframe(df)
        fig = px.scatter_mapbox(df,lat="Latitude",lon="Longitude",hover_name="Mexican restaurant",hover_data=["Address","City","State","Stars","Sentiment"],
                                    color_discrete_sequence=[color],zoom=5,height=700)
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig)

    else:
        st.subheader("🥪_Mexican Restaurants")


if __name__ == "__main__":
    main()
ipts