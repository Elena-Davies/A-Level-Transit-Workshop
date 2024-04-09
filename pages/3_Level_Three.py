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
#_lock = RendererAgg.lock
from matplotlib.animation import FuncAnimation

st.markdown('# Level Three: Atmospheres and Spectra')
st.sidebar.header("Level Three")
st.write('Level Three: Stomry, rocky terrain and with 90% chance of rain!')

# Define section titles
sectiontitles3 = ['Mission One', 'Mission Two']

# Define section titles
def sectiontitle(number):
    return "{0}: {1}".format(number, sectiontitles3[number-1])

# Define section
section3 = st.radio('Select mission:', [1,2], format_func=sectiontitle)

# Write section headers
st.markdown("## {}".format(sectiontitle(section3)))

if section3==1:

    st.markdown("So far, we've only considered planets that have atmopsheres, however, not all planets do!")
    st.markdown("Astronomers are very interested in planets with atmospheres because you're more likely to find life on those planets. ")
    st.markdown("*But how do they know the planet has an atmosphere?*")
    st.markdown(" Look at the two plots of transit light curves below, which one do you think has an atmosphere and which one doesn't?")

    st.image('Images/atmosphere.png')

    question3_1_1 = "Which plot has the atmosphere?"
    options3_1_1=["Plot 1", "Plot 2", "Both plots", "Neither plots", "None of the above"]
    st.write(question3_1_1)
    st.write(options3_1_1)
    selected_option3_1_1 = st.text_input("Type the number (0-4) corresponding to your solution:", key='q3_1_1')
    # Check the selected option
    if selected_option3_1_1 == "4":
        st.write("Correct!  Proceed to the next mission:)")
    else:
        # Provide a hint
        if selected_option3_1_1 == "0":
            st.write("Try again!")
        elif selected_option3_1_1 == "1":
            st.write("Try again!")
        elif selected_option3_1_1 == "2":
            st.write("Try again!")
        elif selected_option3_1_1 == "3":
            st.write("Try again!")

if section3==2:

    st.markdown("That's right! In reality, astronomers don't use transits to determine if a planet has an atmosphere. Instead, they use the spectra of the star's light! They observe spectral emission and aborption lines to see what molecules the planet is absorbing!")

    st.markdown("Take a look at an example of a transmission spectrum of an exoplanet called K2-18 b!")
    st.image('Images/trans_spec_K218b.jpg')

    st.markdown("So how do astronomers use this to determine whether it was has atmosphere or not? The answer lies in your knowledge of emission and absorption spectra!")
    st.markdown("Remember that stars, like our Sun, are blackbodies. This means that they emit and absorb all wavelengths. Therefore, if you were to look at a star's light through a prism, you would see all the colours in the rainbow!")
    st.markdown("However, when a planet creeps in front of the star, the star's light shines only through the planet's atmosphere - if it has one! This means that the molecules and compounds in the planet's atmosphere will absorb the light at its usual wavelength. Therefore, when astronomers observe the absorption spectrum at this point, they will see lines missing in it, according to the molecules that have absorped the light. As a result, the spectrum won't look like a full rainbow anymore!")
    st.markdown("Scientists already know what wavelengths molecules and compounds emit and absorp so all that's left to do is compare the spectrum observed from the star with the spectra of molecules and compounds we've measured in labs on Earth!")

    st.markdown("Now, it's your turn to look at the absorption spectra of compounds and molecules. Play around with it!")

    # Load initial data
    molecule_data = {
        'CH4': 'CSV Data/CH4 Dataset 2.csv',
        'H2O': 'CSV Data/H20 Dataset 2.csv',
        'CO2': 'CSV Data/CO2 Dataset 2.csv',
        'NH3': 'CSV Data/NH3 Dataset 2.csv',
        'HCN': 'CSV Data/HCN Dataset 2.csv',
        'CO': 'CSV Data/CO Dataset 2.csv',
        'DMS': 'CSV Data/DMS Dataset 2.csv',
        'CH3Cl': 'CSV Data/CH3Cl Dataset 2.csv'
    }

    # Create sliders for molecule selection
    selected_molecule = st.selectbox('Select a molecule:', list(molecule_data.keys()))

    # Load data based on selected molecule
    data_file = molecule_data[selected_molecule]
    x, y = np.loadtxt(data_file, delimiter=',', unpack=True)

    # Plot the data
    #with _lock:
    fig_transspec = plt.figure('transspec')
    transspec = plt.plot(x, y, label=selected_molecule)
    plt.xlabel('Wavelength (micrometers)')
    plt.ylabel('Transit Depth (%)')
    plt.legend()
    # Show plot
    st.pyplot(fig_transspec)

    st.markdown("Here are the molecules and compounds in subplots, which ones do you recognise?")
    st.image('Images/subplot_transspec.png')

    st.markdown("Some of the elements above are evidence for potential human life. In astronomy, they are called biomarkers. A biomarker in exoplanets is a clue or sign that 'marks' potential biological life forms on exoplanets! We determine what counts as biomarkers by comparing the elements, chemicals and gases in the exoplanet's atmosphere with the Earth's atmosphere, as we know life is there!")
    st.markdown("From the picture above, we can see that scientists have potentially detected methane, carbon dioxide and dimethyl sulfide. These are all things that are produced by living things here on Earth!")
    st.markdown("Methane can be produced by agriculture, fossil fuels and decomposition of landfill waste.")
    st.markdown("Carbon dioxide can be produced by volcanoes, the breath of animals and plant decay. (In astronomy, we consider plants to be life as well as animals and humans!)")
    st.markdown("DMS is probably something you haven't heard of before, but it's just as important! DMS can be produced by bacteria in the sea and phytoplankton - more life!")
    st.markdown("This is also why K2-18 b is believed to be what astronomers call a Hycean world. These are planets that are believed to have large oceans and hydrogen-rich atmospheres, like our Earth, which is promising if we want to find life!")

    st.markdown("And that's that! You've found an exciting exoplanet that has evidence for an atmosphere and even potentially life, too!")
    st.markdown("# Thank you for playing! :)")