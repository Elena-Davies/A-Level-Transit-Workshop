#Imports
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
# use the non-interactive Agg backend to be more thread safe
mpl.use("agg")
from matplotlib.backends.backend_agg import RendererAgg
#_lock = RendererAgg.lock
from matplotlib.animation import FuncAnimation

import pytransit

# Title the app
st.title('A-Level Transit Method: The Transit Trail!')

st.write("# Welcome to The Transit Trail!")

st.video('planet_orbit_animation.mp4')

st.write('You have been tasked with finding habitable exoplanets to find potential signs of life on other planets!')
st.write('However, before you can find E.T., you have to learn what to look for and how!')
st.write('This is where this workshop comes in! You will complete missions and levels to become a planet hunter in no time!')
st.write('On your journey, you will encounter levels, missions, different terrains and chances of rain! These will announce which levels are more harder than others, so take care out in the rainy and rocky terrains!')
st.write('Are you ready to start your journey? If so, select a level from the sidebar to start!')
st.sidebar.success("Select a level above.")
    
