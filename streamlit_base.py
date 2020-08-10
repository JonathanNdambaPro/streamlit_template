import pandas as pd
import streamlit as st
from PIL import Image
import os
import plotly.express as px


#Text/Title
st.title("Streamlit Tutorials")


#Header

st.header("This is a header")
st.subheader("This is a sub header")


#Text
st.text("Hello word")

st.markdown("This is a Mardown")

st.success("Succesful")

st.info("Info")

st.warning("Warning")

st.error("Error")

st.exception("Exception")

#Get help info about Python
st.help(range)

#writing test
st.write(range(10))

#images
sep = os.sep
img = Image.open(f"/home/jojo/Downloads/"
                 f"91919388_218246939444041_8943361635402121216_n.jpg")

st.image(img, width=300, caption="Jonathan")


# videos
vid_file = open(f"/home/jojo/Downloads/"
                f"video-1576869577.mp4", "rb").read()

st.video(vid_file)

#widget
#Checkbox
if st.checkbox("Show/Hide"): st.text("Showing or hiding Widget")

# Radio
status = st.radio("What is your status", ("Activate", "Inactivate"))
if status == "Activate": st.success("you're activate")
else : st.warning("Inactivate")


# selectbox
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Scientist", "Data Engineer"])
st.write("You selected this option", occupation)


# Multiselect
Location = st.multiselect("Where do you work", ("London", "New York", "Paris"))
st.write(f"You have select {len(Location)} location")

#Slider
level = st.slider("What is your level", 1, 5)



#Button
st.button("Simple Button")

if st.button("About"):
    st.text("Stremlit is cool")


# Text input

name = st.text_input("Enter your name ", "Type here")
if st.button("Submit"):
    result = name.title()
    st.success(result)



message = st.text_area("Enter your message ", "Type here")
if st.button("Submit_1"):
    result = message.title()
    st.success(result)


#Displaying JSON
st.text("Display JSON")
st.json({"name": "Jesse", "gender": "male"})

#Display Raw code
st.text("Display Raw Code")
st.code("import numpy as np")


#Or
with st.echo():
    # the comment
    import pandas as pd
    df = pd.DataFrame()

# Progress bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spinner
with st.spinner("Waiting...."):
    time.sleep(5)
st.success("Finished!")


# Ballons
# st.balloons()

# SideBar
st.sidebar.header("About")
st.sidebar.text("This is Streamlit Tut")

#  Plotting dataframe
# st.datafram(df)

# Plotting plotly
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
st.plotly_chart(fig)


### plotting Seaborn
import seaborn as sns

df = pd.DataFrame({'x': [1, 2, 3], 'y': [10, 30, 70]})
sns.lineplot(x='x', y='y', data=df)
st.pyplot()