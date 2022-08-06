import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.io as pio
import plotly.graph_objects as go
import numpy as np




### Config
st.set_page_config(
    page_title="GetAround analysis",
    page_icon="🚘",
    layout="centered"
)

### Data upload
url = ("get_around_delay_analysis.xlsx")
@st.cache(suppress_st_warning=True)
def load_data():
    data = pd.read_excel(url)
    return data

data = load_data()
# Selecting data with delay info
data_complete = data.loc[data["time_delta_with_previous_rental_in_minutes"].notna(),:]

### Setting personalised palette
purples = ['#F6E5F5', '#CA6EC3', '#C04FB8', '#B01AA7', '#8D1586', '#5F1159']
pio.templates["purples"] = go.layout.Template(
    layout = {
        'title':
            {'font': {'color': '#0F0429'}
            },
        'font': {'color': '#0F0429'},
        'colorway': purples,
    }
)
pio.templates.default = "purples"

###Graph 1####################################################################################################
st.subheader("Rentals by checkintype")

fig = px.sunburst(data, path=['checkin_type'],
                  color_discrete_sequence = ['#0068c9'],
                  names='checkin_type',

)
fig.update_traces(textinfo="label+percent parent")
st.plotly_chart(fig, use_container_width=True)


###Graph 2####################################################################################################
st.subheader("Rentals by state")

fig = px.sunburst(data, path=['state'],
                  color_discrete_sequence = ['#09ab3b'],
                  names='state',

)
fig.update_traces(textinfo="label+percent parent")
st.plotly_chart(fig, use_container_width=True)


###Graph 1####################################################################################################
st.subheader("Rentals shares overview")

fig = px.sunburst(data, path=['checkin_type', 'state'],
                  color_discrete_sequence = ['#0068c9','#09ab3b']
)
fig.update_traces(textinfo="label+percent parent")
st.plotly_chart(fig, use_container_width=True)
#############################
data['Status_checkout'] = ["In_time" if s < 0 else "Late" for s in data['delay_at_checkout_in_minutes']]
st.subheader('STATUS CHECKOUT')
fig = px.pie(data, names='Status_checkout', title='STATUS CHECKOUT',color_discrete_sequence = ['#0068c9','#09ab3b'])
st.plotly_chart(fig)



fig = px.histogram(data["Status_checkout"],title='STATUS CHECKOUT', color_discrete_sequence = ['#0068c9','#09ab3b'])
st.plotly_chart(fig)

