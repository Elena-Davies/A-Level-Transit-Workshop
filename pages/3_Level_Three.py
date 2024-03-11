#Imports
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
# use the non-interactive Agg backend to be more thread safe
#mpl.use("agg")
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock
from matplotlib.animation import FuncAnimation

st.markdown('# Level Three: Atmospheres and Spectra')
st.sidebar.header("Level Three")
st.write('Level Three: Stomry, rocky terrain and with 90% chance of rain!')
st.markdown("So far, we've only considered planets that have atmopsheres, however, not all planets do!")
st.markdown("Astronomers are very interested in planets with atmospheres because you're more likely to find life on those planets. ")
st.markdown("*But how do they know the planet has an atmosphere?*")
st.markdown(" Look at the two plots of transit light curves below, which one do you think has an atmosphere and which one doesn't?")

st.image('atmosphere')
