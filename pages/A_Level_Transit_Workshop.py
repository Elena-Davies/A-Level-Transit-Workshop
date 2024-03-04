import streamlit as st

# Title the app
st.title('A-Level Transit Method: The Transit Trail!')

# adding pages
st.set_page_config(page_title="A-Level Transit Workshop")
st.write("# Welcome to The Transit Trail!")
st.sidebar.success("Select a level above.")
    
st.set_page_config(page_title='Level Two')
st.markdown('# Level Two: Transit Curve Adventure')
st.sidebar.header("Level Two")
st.write('Level Two: Cloudy (with no chance of meatballs), rocky terrain and with 50% chance of rain!')

# Define section titles
sectiontitles2 = ['Mission One', 'Mission Two', 'Mission Three','Mission Four','Level Two Questions']

# Define section titles
def sectiontitle(number):
    return "{0}: {1}".format(number, sectiontitles2[number-1])

# Define section
section2 = st.radio('Select mission:', [1,2,3,4,5], format_func=sectiontitle)

# Write section headers
st.markdown("## {}".format(sectiontitle(section2)))

if section2==1:
    # Add text
    st.write('When the planet moves in front of the star, the light of the star dims slightly for a short period of time. Think about when you put your hand in front of a torch and the light gets dimmer! Now, imagine this but the torch is the size of the Sun and your hand is the size of the Earth and both are thousands of kilometres away! This is very hard to see so astronomers have to use sensitive instruments that monitor the brightness of stars and analyse plots called transit light curves to see the dips in brightness. Have a look at the transit light curve of a real exoplanet called K2-18 b below!')

    #import PyTransit and some key modules.
    from pytransit import QuadraticModel
    # from pytransit import UniformModel
    from scipy.optimize import minimize
    import numpy as np
    import matplotlib.pyplot as plt
    from astropy import units as u
    from astropy import constants as const

    #enter the parameters needed by the model.
    rp18b = 14271000 #radius of K2-18 b in metres
    sma18b = 21380000000 #semi-major axis in metres
    rs18 = 0.41*696340000 #radius of K2-18 in metres
    t0_18b = 0.                        #time of inferior conjunction in days
    per18b = 32.9                     #orbital period in days
    rp_rs18b = rp18b/rs18              #planet radius (K2-18 b) / stellar radius ratio
    ars18b = sma18b/rs18                    #semi-major axis / stellar radius ratio
    inc18b =  (89.58*u.deg).to(u.rad).value      #orbital inclination (in radians) using astropy to convert to radians
    ecc18b = 0.09                       #eccentricity
    w18b = (-5.70*u.deg).to(u.rad).value      #longitude of periastron (in radians)
    gamma18b = [0.083, 0.191]                 #limb darkening coefficients [u1, u2]
    t = np.linspace(-0.1, 0.1, 1200)  #times at which to calculate light curve (days)

    rp391b = 1818041.56 #radius of planet (Kepler-391 b) in metres
    rp_rs391b = rp391b/rs18 # planet radius (Kepler-391 b) / stellar radius ratio

    rp132b = 7721136 #radius of planet (Kepler-132 b) in metres
    rp_rs132b = rp132b/rs18 # planet radius (Kepler-132 b) / stellar radius ratio

    rp116b = 21805060 #radius of planet (Kepler-116 b) in metres
    rp_rs116b = rp116b/rs18 # planet radius (Kepler-116 b) / stellar radius ratio

    tm = QuadraticModel() # a model that uses two limb-darkening coefficients
    tm.set_data(t)

    lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    plt.figure('lc18b')

    plt.plot(t,lc18b, '-o', label='K2-18 b')
    plt.grid(True)
    plt.ylabel('Relative signal')
    plt.xlabel('Time (days)')
    plt.legend();
    plt.title('Transit Light Curve');
    plt.show();