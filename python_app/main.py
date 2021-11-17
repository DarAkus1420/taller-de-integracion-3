from config import config
from modules.ImageRecognition.ImageRecognition import ImageRecognition
import stapi as st

enviroment = config['development']


img = st.value('image')

results = ImageRecognition.found_all_particles(img)

if(len(results['red_particles']) > 0):
    # st.msg(str(red_array))
    st.data("red", results['red_particles'])
if(len(results['blue_particles']) > 0):
    # st.msg(str(blue_array))
    st.data("blue", results['blue_particles'])
if(len(results['air_particles']) > 0):
    # st.msg(str(red_array))
    st.data("gray", results['air_particles'])
