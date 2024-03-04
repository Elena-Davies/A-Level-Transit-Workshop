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
#Import the HTML class from the IPython.display module. HTML is used to display HTML content in Jupyter notebooks.
#from IPython.display import HTML

# Title the app
st.title('A-Level Transit Method: The Transit Trail!')

# adding pages
st.markdown("# Level One: Uncovering The Transit Method")
st.sidebar.markdown("# Level One")
st.write("Level One: clear, smooth terrain with 10% chance of rain!")

# Define section titles
sectiontitles = ['Mission One', 'Mission Two']

# Define section titles
def sectiontitle(number):
    return "{0}: {1}".format(number, sectiontitles[number-1])

# Define section
section = st.radio('Select mission:', [1,2], format_func=sectiontitle)

# Write section headers
st.markdown("## {}".format(sectiontitle(section)))

if section==1:
    # Add text
    st.write("The transit method is a way astronomers detect exoplanets, which are planets outside of our solar system.")
    import streamlit as st
    # Add an image title
    #st.title('K2-18 b')
    # Add an image from local file
    #st.image('C:\Users\elena\Pictures\Desktop background\Exoplanet_K2-18_b_(Illustration).jpg', caption='The above image is an illustration of an exoplanet Kb-18 b! The red sphere is the cool dwarf star that it orbits around called K2-18. Illustration: NASA, CSA, ESA, J. Olmsted (STScI), Science: N. Madhusudhan (Cambridge University)')
    # Define the question and options
    question1_1_1 = "What is the transit method used for?"
    st.write(question1_1_1)
    options1_1_1 = ["Detecting exoplanets", "Detecting comets", "Studying asteroids", "Observing galaxies"]
    st.write(options1_1_1)
    # Display the question and options
    selected_option = st.text_input("Type the number (0-3) corresponding to your solution:")
    # Check the selected option
    if selected_option == "0":
        st.write("Correct! The transit method is used for detecting exoplanets. Mission One complete! Provide to your next Mission :)")
    else:
        # Provide a hint
        if selected_option == "1":
            st.write("Try again! Re-read the Mission One details.")
        elif selected_option == "2":
            st.write("Try again! Re-read the Mission One details.")
        elif selected_option == "3":
            st.write("Try again! Re-read the Mission One details.")

if section==2:
    # Add progress bar in sidebar
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empt
    # Parameters
    star_radius = 1.0
    planet_radius = 0.3
    orbit_radius = 3.0
    angular_velocity = 0.02
    frames = 400
    with _lock:
        # Create figure and subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        # Set up first subplot (edge-on view)
        ax1.set_aspect('equal')
        ax1.set_xlim(-5, 5)
        ax1.set_ylim(-5, 5)
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_title('Edge-On View')
        # Set up second subplot (birds-eye view)
        ax2.set_aspect('equal')
        ax2.set_xlim(-5, 5)
        ax2.set_ylim(-5, 5)
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.set_title('Above View')
        # Draw line segment representing the orbital plane (edge-on view)
        orbital_plane_edgeon, = ax1.plot([-orbit_radius, orbit_radius], [0, 0], linestyle='--', color='gray')
        ax1.annotate('Orbital Plane', xy=(2, 0), xytext=(2, -2), arrowprops=dict(facecolor='black', arrowstyle='->'))
        # Draw circle segment representing the orbital plane (above view)
        theta = np.linspace(0, 2*np.pi, 100)
        orbital_plane_above, = ax2.plot(orbit_radius * np.cos(theta), orbit_radius * np.sin(theta), linestyle='--', color='gray')
        ax2.annotate('Orbital Plane', xy=(0, 3), xytext=(2, 4), arrowprops=dict(facecolor='black', arrowstyle='->'))
        # Draw the star and planet in both subplots
        star = ax1.add_patch(plt.Circle((0, 0), star_radius, color='yellow'))
        planet_edgeon = ax1.add_patch(plt.Circle((0, orbit_radius), planet_radius, color='blue'))
        star = ax2.add_patch(plt.Circle((0, 0), star_radius, color='yellow'))
        planet_above = ax2.add_patch(plt.Circle((0, orbit_radius), planet_radius, color='blue'))
        ax1.annotate('Star', xy=(-1, 0), xytext=(-1, -1.5))
        ax2.annotate('Star', xy=(0, 0), xytext=(0.5, -1.5))
        # Animation function
        def update(frame):
            angle = frame * angular_velocity
            # Update position of the planet in edge-on view
            x_edgeon, y_edgeon = orbit_radius * np.cos(angle), 0
            planet_edgeon.set_center((x_edgeon, y_edgeon))
            # Update position of the planet in above view
            x_above, y_above = orbit_radius * np.sin(angle), -orbit_radius * np.cos(angle)
            planet_above.set_center((x_above, y_above))
            # Check if the planet is behind the star in both views
            if np.pi/2 < angle % (2 * np.pi) < 3 * np.pi / 2:
                planet_edgeon.set_alpha(0.2)
                planet_above.set_alpha(0.2)
            else:
                planet_edgeon.set_alpha(1.0)
                planet_above.set_alpha(1.0)
            return planet_edgeon, planet_above,
        # Create animation
        ani = FuncAnimation(fig, update, frames=frames, blit=True)
        # Convert animation to HTML
        #Convert the animation to HTML format using to_jshtml() method of the FuncAnimation object.
        #html = ani.to_html5_video()
        # Display the animation in Streamlit
        components.html(ani.to_jshtml(), height=1000)
    st.markdown("Imagine you're standing far away and watching a distant star. Now, if a planet passes in front of that star from your perspective, you will see a tiny shadow. This is the planet blocking some of the star's light! Have a look at the plot below of a planet going around a star.")
    st.markdown("Astronomers can detect this because they see a small dip in the star's brightness. By carefully observing these dips in brightness over time, astronomers can figure out if there might be a planet orbiting that star. They can also learn about the size of the planet, how long it takes to orbit its star, and sometimes even its atmosphere!")
    st.markdown("Ready to proceed to the next level? Answer the questions below!")
