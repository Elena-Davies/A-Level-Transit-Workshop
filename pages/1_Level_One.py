#Imports
import streamlit as st
import matplotlib as mpl
# use the non-interactive Agg backend to be more thread safe
mpl.use("agg")
#_lock = RendererAgg.lock

st.markdown("# Level One: Uncovering The Transit Method")
st.sidebar.header("Level One")
st.write("Level One: clear, smooth terrain with 10% chance of rain!")

# Define section titles
sectiontitles1 = ['Mission One', 'Mission Two']

# Define section titles
def sectiontitle(number):
    return "{0}: {1}".format(number, sectiontitles1[number-1])

# Define section
section1 = st.radio('Select mission:', [1,2], format_func=sectiontitle)

# Write section headers
st.markdown("## {}".format(sectiontitle(section1)))

if section1==1:
    # Add an image from local file
    caption = 'An illustration of an exoplanet Kb-18 b! The red sphere is the cool dwarf star that it orbits around called K2-18. Illustration: NASA, CSA, ESA, J. Olmsted (STScI), Science: N. Madhusudhan (Cambridge University)'
    st.image('Images/k218b.jpg', caption='An illustration of an exoplanet Kb-18 b! The red sphere is the cool dwarf star that it orbits around called K2-18. Illustration: NASA, CSA, ESA, J. Olmsted (STScI), Science: N. Madhusudhan (Cambridge University)', output_format="jpeg")
    # Add text
    st.write('# Mission One objective: Find out what the transit method is.')
    st.write('Welcome to your first mission! To start off, we need to remember what an exoplanet is, which is simple! An exoplanet, short for "extrasolar planet", is a planet that orbits a star outside of our solar system! This means that these planets are exclusively orbiting other stars in the Milky Way (our galaxy) and beyond. Exoplanets have been able to deepen our understanding of planetary systems and the potential for life beyond our solar system!')
    st.write('As a result, astronomers have developed numerious ways to find these exoplanets, such as the radial velocity method (which detects the gravitational wobble of a star caused by its orbiting planet), direct imaging (which is capturing an image of the exoplanet) and the transit method, which is our focus of today!')
    st.write("So then, what is the transit method? Well, the transit method is a way astronomers detect exoplanets.")
    st.write('The picture above shows an illustration of an exoplanet called K2-18 b. It was found using the transit method and could potentially have life on it! We will be looking at this exoplanet a lot in our studies!')
    st.write('Answer the question below by putting the number of the option you think is the answer!')

    question1_1_1 = "What is the transit method used for?"
    st.write(question1_1_1)
    options1_1_1 = ["Detecting exoplanets", "Detecting comets", "Studying asteroids", "Observing galaxies"]
    st.write(options1_1_1)
    # Display Question 1.1.1 and options
    selected_option1_1_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q1_1_1')
    # Check the selected option
    if selected_option1_1_1 == "0":
        st.write("Correct! The transit method is used for detecting exoplanets. Mission One complete! Proceed to your next Mission :)")
    else:
        # Provide a hint
        if selected_option1_1_1 == "1":
            st.write("Try again! Re-read the Mission One details.")
        elif selected_option1_1_1 == "2":
            st.write("Try again! Re-read the Mission One details.")
        elif selected_option1_1_1 == "3":
            st.write("Try again! Re-read the Mission One details.")

    

if section1==2:
    
    st.video('Images/planet_orbit_animation1.mp4')

    st.markdown("The animation above shows a planet orbiting a star!")
    st.markdown("Imagine you're standing far away and watching a distant star. Now, if a planet passes in front of that star from your perspective, you will see a tiny shadow. This is the planet blocking some of the star's light! Have a look at the plot below of a planet going around a star.")
    st.markdown("Astronomers can detect this because they see a small dip in the star's brightness. By carefully observing these dips in brightness over time, astronomers can figure out if there might be a planet orbiting that star. They can also learn about the size of the planet, how long it takes to orbit its star, and sometimes even its atmosphere!")
    st.markdown("Astronomers call this a transit! It occurs when an exoplanet passes directly in front of its host star as viewed from Earth.")
    st.markdown("The transit method is a powerful technique used by astronomers to detect exoplanets!")
    st.markdown("However, the transit method can produce something called False Positives. This is where astronomers think they have detected an exoplanet but it is actually something else that they've detected. For example, astronomers shoul observe multiple transits as it means it's more likely that the dip in brightness is due to an exoplanet and not the star's activity or instrumental noise.")
    st.markdown("Side mission: What is noise? Noise is a technical term for unwanted variations in data that arise from the instruments used to collect data! The instruments are not always perfect and remember they are trying to measure things thousands of light-years away!")
    st.markdown("By measuring multiple transits, astronomers can also find the orbital period of the planet, which leads to the exoplanet's distance from its host star (think Kepler's laws)!")
    st.markdown("There are other limitations to the transit method, too. One being the bias towards exoplanets that orbit close to their host stars. This is because if the star was too far away then it would block out so little light that it would be very difficult to detect! This means that the transit method is more suited to rocky planets (like Earth!), however, that also means that you're more likely to find planets within the Goldilocks Zone with this method, good news for alien hunters!")
    st.markdown("Side mission: The Goldilocks Zone is the range of distances that a planet could potentially have the right conditions suitable for supporting liquid water on its surface.")
    
    st.markdown("Ready to proceed to the next level? Answer the questions below!")

    # Define Question 1.2.1 and options
    question1_2_1 = "What is a transit?"
    st.write(question1_2_1)
    options1_2_1 = ["The movement of stars across the sky during the night", "The passage of an exoplanet in front of its parent star", "The alignment of multiple planets in a solar system", "The change in brightness of a star caused by its rotation"]
    st.write(options1_2_1)
    # Display Question 1.2.1 and options
    selected_option1_2_1 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q1_2_1')
    # Check the selected option
    if selected_option1_2_1 == "1":
        st.write("Correct! A transit is the passage of an exoplanet in front of its parent star. :)")
    else:
        # Provide a hint
        if selected_option1_2_1 == "0":
            st.write("Try again! Re-read the Mission Two details.")
        elif selected_option1_2_1 == "2":
            st.write("Try again! Re-read the Mission Two details.")
        elif selected_option1_2_1 == "3":
            st.write("Try again! Re-read the Mission Two details.")

    # Define Question 1.2.2 and options
    question1_2_2 = "How does the transit method detect exoplanets?"
    st.write(question1_2_2)
    options1_2_2 = ["By measuring changes in the star's colour", "By observing fluctuations in the exoplanet's size", "By detecting dips in the star's brightness when an exoplanet passes in front of it", "By analysing the chnage in the star's temperature"]
    st.write(options1_2_2)
    # Display Question 1.2.2 and options
    selected_option1_2_2 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q1_2_2')
    # Check the selected option
    if selected_option1_2_2 == "2":
        st.write("Correct! The transit method detects exoplanets by detecting dips in the star's brightness when an exoplanet passes in front of it. :)")
    else:
        # Provide a hint
        if selected_option1_2_2 == "0":
            st.write("Try again! Re-read the Mission Two details.")
        elif selected_option1_2_2 == "1":
            st.write("Try again! Re-read the Mission Two details.")
        elif selected_option1_2_2 == "3":
            st.write("Try again! Re-read the Mission Two details.")

    # Define Question 1.2.3 and options
    question1_2_3 = "Why is it important for astronomers to observe multiple transits of an exoplanet?"
    st.write(question1_2_3)
    options1_2_3 = ["To determine the colour of the exoplanet", "To calculate the distance between the exoplanet and the star", "To confirm the presence of the exoplanet", "To estimate the exoplanet's composition"]
    st.write(options1_2_3)
    # Display Question 1.2.3 and options
    selected_option1_2_3 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q1_2_3')
    # Check the selected option
    if selected_option1_2_3 == "2":
        st.write("Correct! It is important for astronomers to observe multiple transits of an exoplanet so they can confirm the presence of the exoplanet. :)")
    else:
        # Provide a hint
        if selected_option1_2_3 == "0":
            st.write("Try again! Re-read the Mission Two details.")
        elif selected_option1_2_3 == "1":
            st.write("Try again! Re-read the Mission Two details.")
        elif selected_option1_2_3 == "3":
            st.write("Try again! Re-read the Mission Two details.")
    
    # Define Question 1.2.4 and options
    question1_2_4 = "Which of the following is a limitation of the transit method in detecting exoplanets?"
    st.write(question1_2_4)
    options1_2_4 = ["It can only detect large exoplanets", "It cannot detect exoplanets that are too far from their star", "It cannot detect exoplanets with irregular orbits", "It cannot detect exoplanets that are too close to their stars"]
    st.write(options1_2_4)
    # Display Question 1.2.4 and options
    selected_option1_2_4 = st.text_input("Type the number (0-3) corresponding to your solution:", key='q1_2_4')
    # Check the selected option
    if selected_option1_2_4 == "3":
        st.write("Correct! A limitation of the transit method in detecting exoplanets is that it cannot detect exoplanets that are too close to their stars. :)")
    else:
        # Provide a hint
        if selected_option1_2_4 == "0":
            st.write("Try again! Re-read the Mission Two details.")
        elif selected_option1_2_4 == "1":
            st.write("Try again! Re-read the Mission Two details.")
        elif selected_option1_2_4 == "2":
            st.write("Try again! Re-read the Mission Two details.")