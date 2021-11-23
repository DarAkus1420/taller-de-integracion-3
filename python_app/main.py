from dotenv import dotenv_values
from modules.ImageRecognition.ImageRecognition import ImageRecognition
import stapi as st


config = dotenv_values(".env")

url = config['API_URL']
img = st.value('image')

results = ImageRecognition.found_all_particles(img,  url)

if(len(results['red_particles']['particles']) > 0):
    st.data("red", results['red_particles']['particles'])
if(len(results['blue_particles']['particles']) > 0):
    st.data("blue", results['blue_particles']['particles'])
if(len(results['air_particles']['particles']) > 0):
    st.data("gray", results['air_particles']['particles'])
