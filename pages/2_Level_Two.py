#Imports
import streamlit as st
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# use the non-interactive Agg backend to be more thread safe
mpl.use("agg")

#import PyTransit and some key modules
from pytransit import QuadraticModel
# from pytransit import UniformModel
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u

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

if section2==1:
    # Add text
    st.write('When the planet moves in front of the star, the light of the star dims slightly for a short period of time. Think about when you put your hand in front of a torch and the light gets dimmer! Now, imagine this but the torch is the size of the Sun and your hand is the size of the Earth and both are thousands of kilometres away! This is very hard to see so astronomers have to use sensitive instruments that monitor the brightness of stars and analyse plots called transit light curves to see the dips in brightness. Have a look at the transit light curve of a real exoplanet called K2-18 b below!')

    lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    
    fig_lc18b = plt.figure('lc18b')
    lc18b = plt.plot(t,lc18b, '-o', label='K2-18 b')
    plt.grid(True)
    plt.ylabel('Relative signal')
    plt.xlabel('Time (days)')
    plt.legend();
    plt.title('Transit Light Curve');
    st.pyplot(fig_lc18b);

    st.write('Think you got it? Answer the questions below to test your knowledge!')

    question2_1_1 = "What do scientists look for to confirm the presence of an exoplanet using the transit method?"
    st.write(question2_1_1)
    options2_1_1=["Change in the star's colour", "Variations in the star's size", "Repeated dips in the star's brightness at regular intervals", "Fluctuations in the star's temperature"]
    st.write(options2_1_1)
     # Display Question 2.1.1 and options
    selected_option2_1_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_1_1')
    # Check the selected option
    if selected_option2_1_1 == "2":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_1_1 == "0":
            st.write("Try again!")
        elif selected_option2_1_1 == "1":
            st.write("Try again!")
        elif selected_option2_1_1 == "3":
            st.write("Try again!")

    question2_1_2 = "When does the planet pass in front of the star?"
    options2_1_2=["Between -0.100 and -0.075 days", "Between -0.075 and 0.075 days", "Between 0.075 and 0.100 days", "None of the above"]
    st.write(question2_1_2)
    st.write(options2_1_2)
     # Display Question 2.2.1 and options
    selected_option2_2_2 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_1_2')
    # Check the selected option
    if selected_option2_2_2 == "1":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_2_2 == "0":
            st.write("Try again!")
        elif selected_option2_2_2 == "2":
            st.write("Try again!")
        elif selected_option2_2_2 == "3":
            st.write("Try again!")

    question2_1_6 = "If the transit of an exoplanet in front of its star causes a change in the star's brightness by 0.05 magnitudes and the star's initial brightness is 13.5 magnitudes, what is its brightness during the transit?"
    options2_1_6 = ["10.05 magnitudes", "13.45 magnitudes", "9.95 magnitudes", "13.55 magntiudes"]
    st.write(question2_1_6)
    st.write(options2_1_6)
    # Display question and options
    selected_option2_1_6 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_1_6')
    # Check the selected option
    if selected_option2_1_6 == "1":
        st.write("Correct! :)")
    else:
        # Provide a hint if possible
        if selected_option2_1_6 == "0":
            st.write("Try again! Check your numbers!")
        elif selected_option2_1_6 == "2":
            st.write("Try again! Check your numbers!")
        elif selected_option2_1_6 == "3":
            st.write("Try again! Check your numbers!")

    question2_1_3 = "What happens to a star's light during a transit caused by an exoplanet?"
    options2_1_3=["It brightens", "It remains constant", "It dims slightly", "It disappears completely"]
    st.write(question2_1_3)
    st.write(options2_1_3)    
    selected_option2_1_3 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_1_3')
    # Check the selected option
    if selected_option2_1_3 == "1":
        st.write("Correct!  :)")
    else:
        # Provide a hint
        if selected_option2_1_3 == "0":
            st.write("Try again!")
        elif selected_option2_1_3 == "2":
            st.write("Try again!")
        elif selected_option2_1_3 == "3":
            st.write("Try again!")

    question2_1_4 ="Why does the brightness of a star decrease during a transit?"
    options2_1_4=["Due to the presence of sunspots on the star's surface", "Because the exoplanet blocks a portion of the star's light as it passes in front of it", "As a result of an error in the data", "Because of fluctuations in the star's internal temperature"]
    st.write(question2_1_4)
    st.write(options2_1_4)
    selected_option2_1_4 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_1')
    # Check the selected option
    if selected_option2_1_4 == "1":
        st.write("Correct!  :)")
    else:
        # Provide a hint
        if selected_option2_1_4 == "0":
            st.write("Try again!")
        elif selected_option2_1_4 == "2":
            st.write("Try again!")
        elif selected_option2_1_4 == "3":
            st.write("Try again!")

    question2_1_5 = "What is represented by the slopes in the transit light curve?"
    options2_1_5=["Velocity of the exoplanet", "Change in brightness over time", "Atmospheric density of the exoplanet", "None of the above"]
    st.write(question2_1_5)
    st.write(options2_1_5)
    selected_option2_1_5 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_5_1')
    # Check the selected option
    if selected_option2_1_5 == "1":
        st.write("Correct!  :)")
    else:
        # Provide a hint
        if selected_option2_1_5 == "0":
            st.write("Try again!")
        elif selected_option2_1_5 == "2":
            st.write("Try again!")
        elif selected_option2_1_5 == "3":
            st.write("Try again!")

if section2==2:
    st.write('Play with the slider below to see how the radius can impact the transit curve in real time! What do you notice? Discuss with the person next to you!')
    tm = QuadraticModel() # a model that uses two limb-darkening coefficients
    t = np.linspace(-0.1, 0.1, 1200)
    tm.set_data(t)

    # slider
    k = st.slider("Value for radius of planet over radius of star", 0.006, 0.8, 0.1)
    lc5  = tm.evaluate(k=k, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    fig_lck=plt.figure('fig_lck')
    lc5 = plt.plot(t, lc5, '-o')
    plt.ylabel('Relative signal')
    plt.xlabel('Time (days)')
    plt.xlim(-0.1,0.1)
    plt.ylim(0.5,1.1)
    # Add minor ticks
    plt.minorticks_on()
    # Customise minor tick appearance
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
    st.pyplot(fig_lck)
    st.write('From your plot, think about how you can calculate the time range of when the planet passes in front of the star.')
    st.write("You should be able to notice that the bigger the ratio of planet radius and star radius makes a lower dip in the star's brightness! How would you go about calculating the transit depth of the exoplanet? (Remember that transit depth is the name for how big the dip is!)")

    st.write('Look at the above slider plot in a different way below!')
    lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    lc391b  = tm.evaluate(k=rp_rs391b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    lc132b  = tm.evaluate(k=rp_rs132b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    lc116b  = tm.evaluate(k=rp_rs116b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b)
    fig_lcs = plt.figure('fig_lcs')
    lc391b = plt.plot(t,lc391b,'-o', label='Kepler-391 b')
    lc132b = plt.plot(t,lc132b,'-o', label='Kepler-132 b')
    lc18b = plt.plot(t,lc18b, '-o', label='K2-18 b')
    lc116b = plt.plot(t,lc116b,'-o', label='Kepler-116 b')
    plt.ylabel('Relative signal')
    plt.xlabel('Time (days)')
    plt.legend();
    plt.minorticks_on();
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray');
    st.pyplot(fig_lcs)
    t = np.linspace(0, 5, 1200)  #times at which to calculate light curve (days)
    st.write("Answer the question below to complete the mission!")

    question2_2_1 = "In the plot above, which is the largest radius?"
    st.write(question2_2_1)
    options2_2_1=["Kepler-391 b", "Kepler-132 b", "K2-18 b", "Kepler-116 b"]
    st.write(options2_2_1)
     # Display Question 2.2.1 and options
    selected_option2_2_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_2_1')
    # Check the selected option
    if selected_option2_2_1 == "3":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_2_1 == "0":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_2_1 == "1":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_2_1 == "2":
            st.write("Try again! Have another look at the plot above.")

    question2_2_2 = "If an exoplanet has a radius of 2.6 times that of Earth and its transit depth is 0.29%, what is the radius of its parent star? The Sun's radius is about 109 times the radius of the Earth."
    st.write(question2_2_2)
    options2_2_2=["0.044 times the size of the Sun", "48 times the size of the Sun", "0.48 times the size of the Sun", "0.44 times the size of the Sun"]
    st.write(options2_2_1)
     # Display Question 2.2.1 and options
    selected_option2_2_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_2_1')
    # Check the selected option
    if selected_option2_2_1 == "3":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_2_1 == "0":
            st.write("Try again! Remember that the transit depth is a percentage!")
        elif selected_option2_2_1 == "1":
            st.write("Try again! Use all the information in the question!")
        elif selected_option2_2_1 == "2":
            st.write("Try again! Remember to check over your calculations!")
    hint2_2_2 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_2_2')
    if hint2_2_2:
        st.markdown('---')
        st.markdown("You've seen used the hint power-up! Your hint is: transit depth is calculated by the radius of the exoplanet divided by the radius of the star squared! Use your power-up wisely!")
        st.markdown('---')


if section2==3:
    st.write('Different transit events can tell you how far away the planet is from the star! This is all due to perspective. For example, if you cover a light source with a shield that is right in front of the light source it will block a lot of light but if you place the shield very far from the light source it will only block some of the light. See this in action with the interactive plot below!')
    per = st.slider("Value for period", 1.0, 50.0, 5.0)
    lc  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per, a=ars18b, i=inc18b)
    #with _lock:
    fig_lc_plt = plt.figure('lc_plt')
    lc_plt = plt.plot(t, lc, '-o')
    plt.ylabel('Relative signal')
    plt.xlabel('Time (days)')
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
    st.pyplot(fig_lc_plt)

    st.write('Now, look at a static plot of planets with different orbital periods. Remember that period is the time taken for the exoplanet to complete one orbit around its host star!')
    lc83c  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=10.00102551, a=ars18b, i=inc18b, e=ecc18b, w=w18b) #K2-83 c
    lc1h  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=20, a=ars18b, i=inc18b, e=ecc18b, w=w18b) #TRAPPIST-1 h
    lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per18b, a=ars18b, i=inc18b, e=ecc18b, w=w18b) #K2-18 b
    lc1260d  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=49.8251659648395, a=ars18b, i=inc18b, e=ecc18b, w=w18b) #TOI-1260 d

    #with _lock:
    fig_lcs_per = plt.figure('lcs_per')

    lc83c = plt.plot(t,lc83c, '-o', label='K2-83 c') #K2-83 c
    lc1h = plt.plot(t,lc1h,'-o', label='TRAPPIST-1 h') #TRAPPIST-1 h
    lc18b = plt.plot(t,lc18b, '-o', label='K2-18 b') #K2-18 b
    lc1260 = plt.plot(t,lc1260d,'-o', label='TOI-1260 d') #TOI-1260 d
    plt.ylabel('Relative signal')
    plt.xlabel('Time (days)')
    plt.legend();
    plt.minorticks_on();
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray');
    st.pyplot(fig_lcs_per)

    st.write("Complete the questions below to succeed in your mission!")

    question2_3_1 = "From the plot above, which planet has the longest period?"
    st.write(question2_3_1)
    options2_3_1=["TRAPPIST-1 h", "TOI-1260 d", "K2-18 b", "K2-83 c"]
    st.write(options2_3_1)
     # Display Question 2.3.1 and options
    selected_option2_3_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_3_1')
    # Check the selected option
    if selected_option2_3_1 == "1":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_3_1 == "0":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_3_1 == "3":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_3_1 == "2":
            st.write("Try again! Have another look at the plot above.")

    question2_3_2 = "From the plot above, which planet has the shortest transit duration?"
    st.write(question2_3_2)
    options2_3_2=["TRAPPIST-1 h", "K2-83 c", "K2-18 b", "TOI-1260 d"]
    st.write(options2_3_2)
     # Display Question 2.3.2 and options
    selected_option2_3_2 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_3_2')
    # Check the selected option
    if selected_option2_3_2 == "3":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_3_2 == "0":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_3_2 == "1":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_3_2 == "2":
            st.write("Try again! Have another look at the plot above.")
    hint2_3_2 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_3_2')
    if hint2_3_2:
        st.markdown('---')
        st.markdown("You've seen used the hint power-up! Your hint is: remember that shorter periods result in shorter transit durations. Use it wisely!")
        st.markdown('---')
 
    question2_3_3 = "From the plot above, which planet has the shortest transit duration?"
    st.write(question2_3_3)
    options2_3_3=["TRAPPIST-1 h", "K2-83 c", "K2-18 b", "TOI-1260 d"]
    st.write(options2_3_3)
     # Display Question 2.3.3 and options
    selected_option2_3_3 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_3_3')
    # Check the selected option
    if selected_option2_3_3 == "1":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_3_3 == "0":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_3_3 == "3":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_3_3 == "2":
            st.write("Try again! Have another look at the plot above.")
    hint2_3_3 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_3_3')
    if hint2_3_3:
        st.markdown('---')
        st.markdown("You've seen used the hint power-up! Your hint is: remember that frequency (f) in inversely proportional to period (T)! Use it wisely!")
        st.markdown('---')

    question2_3_4 = "If an exoplanet's transit lasts for 2 hours and it occurs every 32.9 days, what is the orbital period of the exoplanet?"
    st.write(question2_3_4)
    options2_3_4=["32.9 days", "35.9 days", "30.9 days", "37.9 days"]
    st.write(options2_3_4)
     # Display Question 2.3.4 and options
    selected_option2_3_4 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_3_4')
    # Check the selected option
    if selected_option2_3_4 == "0":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_3_4 == "1":
            st.write("Try again! Have another look at the question above.")
        elif selected_option2_3_4 == "2":
            st.write("Try again! Have another look at the question above.")
        elif selected_option2_3_4 == "3":
            st.write("Try again! Have another look at the question above.")
    hint2_3_4 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_3_4')
    if hint2_3_4:
        st.markdown('---')
        st.markdown("You've seen used the hint power-up! Your hint is: remember what orbital period means! Use it wisely!")
        st.markdown('---')

if section2==4:
    st.write('Astronomers love to find patterns and if you see that a dip in brightness happens regularly then you can start to predict when the next dip will occur because then you are most likely looking at the orbit of a planet!')
    tlong=np.linspace(0,5,10000)
    tm.set_data(tlong)

    per = st.slider('Values for the period', 1.0, 2.0, 0.01)

    lc  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=per, a=ars18b*0.05, i=inc18b)
    fig_tlong_plt = plt.figure('tlong_plt')
    tlong_plt = plt.plot(tlong,lc, '-o')
    plt.xlim(0, 5)
    plt.ylim(0.997,1.001)
    plt.ylabel('Relative signal')
    plt.xlabel('Time (days)')
    # Add minor ticks
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
    st.pyplot(fig_tlong_plt)
    
    lc18b  = tm.evaluate(k=rp_rs18b, ldc=gamma18b, t0=t0_18b, p=2.00, a=ars18b*0.05, i=inc18b)
    #with _lock:
    fig_tlong_lc18b = plt.figure('tlong_lc18b')
    tlong_lc18b = plt.plot(tlong,lc18b, '-o')
    plt.xlim(0, 5)
    plt.ylim(0.9972,1.0001)
    plt.ylabel('Relative Flux')
    plt.xlabel('Time (days)')
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')
    st.pyplot(fig_tlong_lc18b)

    st.write("Ready to test your skills? Complete the questions below!")

    question2_4_1 = "Estimate the period of the exoplanet's orbit based on the transit light curve above."
    st.write(question2_4_1)
    options2_4_1=["1 day", "72 hours", "172800 seconds", "4 days"]
    st.write(options2_4_1)
     # Display Question 2.4.1 and options
    selected_option2_4_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_1')
    # Check the selected option
    if selected_option2_4_1 == "2":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_4_1 == "0":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_1 == "1":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_1 == "3":
            st.write("Try again! Have another look at the plot above.")
    hint2_4_1 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_4_1')
    if hint2_4_1:
        st.markdown('---')
        st.markdown("You've used the hint power-up! Your hint is: remember that the period can be determined by measuring the time between consecutive transit events! Use it wisely!")
        st.markdown('---')

    question2_4_2 = "What is the depth of the transit?"
    st.write(question2_4_2)
    options2_4_2=["0.9973", "0.0025", "1.000", "0.9975"]
    st.write(options2_4_2)
     # Display Question 2.4.2 and options
    selected_option2_4_2 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_2')
    # Check the selected option
    if selected_option2_4_2 == "1":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_4_2 == "0":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_2 == "2":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_2 == "3":
            st.write("Try again! Have another look at the plot above.")
    hint2_4_2 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_4_2')
    if hint2_4_2:
        st.markdown('---')
        st.markdown("You've used the hint power-up! Your hint is: the depth represents the decrease in brightness of the host star during a transit event and the y-axis is already measured in the 'Relative Flux'. Use it wisely!")
        st.markdown('---')

    question2_4_3 = "How many transit events are observed within the given timeframe?"
    st.write(question2_4_3)
    options2_4_3=["1/2", "1", "2", "5/2"]
    st.write(options2_4_3)
     # Display Question 2.4.3 and options
    selected_option2_4_3 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_3')
    # Check the selected option
    if selected_option2_4_3 == "3":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_4_3 == "0":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_3 == "1":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_3 == "2":
            st.write("Try again! Have another look at the plot above.")
    hint2_4_3 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_4_3')
    if hint2_4_3:
        st.markdown('---')
        st.markdown("You've used the hint power-up! Your hint is: Count the number of distinct dips in brightness in the transit light curve. Use it wisely!")
        st.markdown('---')

    question2_4_4 = "What is the average transit duration of the exoplanet based on the observed transit event(s)?"
    st.write(question2_4_4)
    options2_4_4=["Approximately 1.0 day", "Approximately 0.8 days", "Approximately 0.4 days", "Approximately 0.2 days"]
    st.write(options2_4_4)
     # Display Question 2.4.4 and options
    selected_option2_4_4 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_4')
    # Check the selected option
    if selected_option2_4_4 == "1":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_4_4 == "0":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_4 == "2":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_4 == "3":
            st.write("Try again! Have another look at the plot above.")
    hint2_4_4 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_4_4')
    if hint2_4_3:
        st.markdown('---')
        st.markdown("You've used the hint power-up! Your hint is: alculate the average duration by summing the durations of all transit events and dividing by the total number of events. Use it wisely!")
        st.markdown('---')

    question2_4_5 = "What is the transit depth ratio between two consecutive transit events?"
    st.write(question2_4_5)
    options2_4_5=["2.5x10^-3", "0.9975", "1", "0"]
    st.write(options2_4_5)
     # Display Question 2.4.5 and options
    selected_option2_4_5 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_5')
    # Check the selected option
    if selected_option2_4_5 == "0":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_4_5 == "1":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_5 == "2":
            st.write("Try again! Have another look at the plot above.")
        elif selected_option2_4_5 == "3":
            st.write("Try again! Have another look at the plot above.")
    hint2_4_5 = st.checkbox("Need to use a hint power-up?", value=False, key='hint2_4_5')
    if hint2_4_5:
        st.markdown('---')
        st.markdown("You've used the hint power-up! Your hint is: alculate the average duration by summing the durations of all transit events and dividing by the total number of events. Use it wisely!")
        st.markdown('---')

    question2_4_6 = "What can scientists learn about an exoplanet from its transit?"
    st.write(question2_4_6)
    options2_4_6=["Its surface temperature", "Its atmospheric composition", "Its size and orbit", "All of the above"]
    st.write(options2_4_6)
     # Display Question 2.4.6 and options
    selected_option2_4_6 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_6')
    # Check the selected option
    if selected_option2_4_6 == "3":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_4_6 == "0":
            st.write("Try again! Have another look at the mission details above.")
        elif selected_option2_4_6 == "1":
            st.write("Try again! Have another look at the mission detials above.")
        elif selected_option2_4_6 == "2":
            st.write("Try again! Have another look at the mission details above.")

    question2_4_7 = "How do astronomers determine the characteristics of an exoplanet using the transit method?"
    st.write(question2_4_7)
    options2_4_7=["By measuring the exoplanet's surface temperature", "By analysing changes in the star's magnetic field", "By observing variations in the star's size", "By studying the duration and depth of the transit event"]
    st.write(options2_4_7)
     # Display Question 2.4.7 and options
    selected_option2_4_7 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_7')
    # Check the selected option
    if selected_option2_4_7 == "3":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_4_7 == "0":
            st.write("Try again! Have another look at the mission details above.")
        elif selected_option2_4_7 == "1":
            st.write("Try again! Have another look at the mission detials above.")
        elif selected_option2_4_7 == "2":
            st.write("Try again! Have another look at the mission details above.")

    question2_4_8 = "What can the time between each dip tell you?"
    st.write(question2_4_8)
    options2_4_8=["The exoplanet's distance from its star and orbital period", "The colour of the exoplanet's atmosphere and its composition", "The size of the exoplanet and the number of moons it has", "The temperature of the exoplanet's surface and the intensity of its magnetic field"]
    st.write(options2_4_8)
     # Display Question 2.4.8 and options
    selected_option2_4_8 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q2_4_8')
    # Check the selected option
    if selected_option2_4_8 == "0":
        st.write("Correct! :)")
    else:
        # Provide a hint
        if selected_option2_4_8 == "1":
            st.write("Try again! Have another look at the mission details above.")
        elif selected_option2_4_8 == "2":
            st.write("Try again! Have another look at the mission detials above.")
        elif selected_option2_4_8 == "3":
            st.write("Try again! Have another look at the mission details above.")
    