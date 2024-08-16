import streamlit as st
from lida import Manager, TextGenerationConfig, llm
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import base64

# Load environment variables from .env file
load_dotenv()

# Get the Cohere API key from the environment variable
cohere_api_key = os.getenv('COHERE_API_KEY')

# Initialize the LIDA Manager with Cohere
lida = Manager(text_gen=llm("cohere"))

# Define a function to convert base64 image to PIL Image
def base64_to_image(base64_string):
    byte_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(byte_data))

# Define text generation configuration
textgen_config = TextGenerationConfig(n=1, temperature=0.5, model="command-r-plus", use_cache=True)

menu = st.sidebar.selectbox("Choose an Option", ["Summarize", "Question based Graph"])

if menu == "Summarize":
    st.subheader("Summarization of your Data")
    file_uploader = st.file_uploader("Upload your CSV", type="csv")
    if file_uploader is not None:
        path_to_save = "filename.csv"
        with open(path_to_save, "wb") as f:
            f.write(file_uploader.getvalue())
        
        # Summarize the CSV data
        summary = lida.summarize(path_to_save, summary_method="default", textgen_config=textgen_config)
        st.write(summary)
        
        # Generate goals based on the summary
        goals = lida.goals(summary, n=2, textgen_config=textgen_config)
        for goal in goals:
            st.write(goal)
        
        # Generate and display visualization
        i = 0
        library = "seaborn"
        textgen_config = TextGenerationConfig(n=1, temperature=0.2, use_cache=True)
        charts = lida.visualize(summary=summary, goal=goals[i], textgen_config=textgen_config, library=library)  
        img_base64_string = charts[0].raster
        img = base64_to_image(img_base64_string)
        st.image(img)

elif menu == "Question based Graph":
    st.subheader("Query your Data to Generate Graph")
    file_uploader = st.file_uploader("Upload your CSV", type="csv")
    if file_uploader is not None:
        path_to_save = "filename1.csv"
        with open(path_to_save, "wb") as f:
            f.write(file_uploader.getvalue())
        
        text_area = st.text_area("Query your Data to Generate Graph", height=200)
        if st.button("Generate Graph"):
            if len(text_area) > 0:
                st.info("Your Query: " + text_area)
                
                # Summarize the CSV data
                summary = lida.summarize(path_to_save, summary_method="default", textgen_config=textgen_config)
                
                # Generate and display visualization based on user query
                user_query = text_area
                charts = lida.visualize(summary=summary, goal=user_query, textgen_config=textgen_config)  
                img_base64_string = charts[0].raster
                img = base64_to_image(img_base64_string)
                st.image(img)
