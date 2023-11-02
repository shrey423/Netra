import streamlit as st
import pandas as pd
import cloudDyn 
import folium
from streamlit_folium import st_folium



@st.cache_data()
def initialize_session_data():
        data =  cloudDyn.get_from_cloud()
        return pd.DataFrame(data)

def mapdataF(session_data):
    li = []
    for session in session_data.itertuples(index=False):
        li.append({'latitude': session.latitude, 'longitude': session.longitude})
    return li
# Initialize session data
session_data = initialize_session_data()
data = mapdataF(session_data)
orderedColumn = ['sid', 'number_of_pothole', 'latitude', 'longitude', 'date&time']
session_data = session_data[orderedColumn].sort_values(by='sid', ascending=True)

c = (20.59, 78.96)
map=folium.Map(location=c,zoom_start=5)
for i in data:
    location = float(i['latitude']), float(i['longitude'])
    folium.Marker(location, popup=f"Latitude: {i['latitude']}, Longitude: {i['longitude']}").add_to(map)

st_folium(map,width=700)


# Streamlit app layout
st.title('Current Sessions Data')

# Display current session data in a table
st.table(session_data)

# Button to simulate sending data to the cloud (dummy function)
if st.button('Send Data to Cloud'):
    # Call the function to send data to the cloud (placeholder for actual function)
    # Placeholder for the cloud function (replace with your actual cloud function)
    def send_data_to_cloud(data):
        st.success('Data has been sent to the cloud.')
    
    # Call the cloud function with session_data as argument
    send_data_to_cloud(session_data)