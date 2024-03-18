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

st.image('atmosphere.png')

question3_1_1 = "Which plot has the atmosphere?"
options3_1_1=["Plot 1", "Plot 2", "Both plots", "Neither plots"]
st.write(question3_1_1)
st.write(options3_1_1)
selected_option3_1_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q3_1_1')
# Check the selected option
if selected_option3_1_1 == "3":
    st.write("Correct!  :)")
else:
    # Provide a hint
    if selected_option3_1_1 == "0":
        st.write("Try again!")
    elif selected_option3_1_1 == "2":
        st.write("Try again!")
    elif selected_option3_1_1 == "1":
        st.write("Try again!")

st.markdown("In reality, astronomers don't use transits like above to determine if a planet has an atmosphere. Instead, they use the spectra of the star's light! They observe spectral emission and aborption lines to see what molecules the planet is absorbing!")

st.markdown("Take a look at an example of a transmission spectrum of an exoplanet called K2-18 b!")
st.image('trans_spec_K218b.jpg')

st.markdown("Now let's look at a more detailed plot. Play around with it!")

# Load initial data
molecule_data = {
    'CH4': 'CH4 Dataset 2.csv',
    'H2O': 'H20 Dataset 2.csv',
    'CO2': 'CO2 Dataset 2.csv',
    'NH3': 'NH3 Dataset 2.csv',
    'HCN': 'HCN Dataset 2.csv',
    'CO': 'CO Dataset 2.csv',
    'DMS': 'DMS Dataset 2.csv',
    'CH3Cl': 'CH3Cl Dataset 2.csv'
}

# Create sliders for molecule selection
selected_molecule = st.selectbox('Select a molecule:', list(molecule_data.keys()))

# Load data based on selected molecule
data_file = molecule_data[selected_molecule]
x, y = np.loadtxt(data_file, delimiter=',', unpack=True)

# Plot the data
with _lock:
    fig_transspec = plt.figure('transspec')
    transspec = plt.plot(x, y, label=selected_molecule)
    plt.xlabel('Wavelength (micrometers)')
    plt.ylabel('Transit Depth (%)')
    plt.legend()
    # Show plot
    st.pyplot(transspec)
