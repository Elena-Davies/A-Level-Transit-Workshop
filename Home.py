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

# Title the app
st.title('A-Level Transit Method: The Transit Trail!')

st.write("# Welcome to The Transit Trail!")

# Parameters
star_radius = 1.0
planet_radius = 0.3
orbit_radius = 3.0
angular_velocity = 0.02
frames = 315

with _lock:
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Planet Orbit')

    star = plt.Circle((0, 0), star_radius, color='yellow')
    planet = plt.Circle((0, orbit_radius), planet_radius, color='blue')

    ax.add_patch(star)
    planet_patch = ax.add_patch(planet)

    def update(frame):
            angle = frame * angular_velocity
            # Update position of the planet
            x_planet = orbit_radius * np.cos(angle)
            y_planet = orbit_radius * np.sin(angle)
            planet_patch.set_center((x_planet, y_planet))
            x_above, y_above = orbit_radius * np.sin(angle), -orbit_radius * np.cos(angle)
            # Check if the planet is behind the star in both views
            if np.pi/2 < angle % (2 * np.pi) < 3 * np.pi / 2:
                planet_patch.set_alpha(0.2)
            else:
                planet_patch.set_alpha(1.0)
            return planet_patch
    
    # Create animation
        ani = FuncAnimation(fig, update, frames=frames, blit=True)
        # Convert animation to HTML
        #Convert the animation to HTML format using to_jshtml() method of the FuncAnimation object.
        #html = ani.to_html5_video()
        # Display the animation in Streamlit
        components.html(ani.to_jshtml(), height=100, width=300)
    

st.write('You have been tasked with finding habitable exoplanets to find potential signs of life on other planets!')
st.write('However, before you can find E.T., you have to learn what to look for and how!')
st.write('This is where this workshop comes in! You will complete missions and levels to become a planet hunter in no time!')
st.write('On your journey, you will encounter levels, missions, different terrains and chances of rain! These will announce which levels are more harder than others, so take care out in the rainy and rocky terrains!')
st.write('Are you ready to start your journey? If so, select a level from the sidebar to start!')
st.sidebar.success("Select a level above.")
    
