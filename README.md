Data Visualization and Summarization App
Project Description
This project is a Streamlit-based application designed for summarizing CSV data and generating visualizations based on user queries. The application allows users to upload a CSV file, receive a summary of the data, and visualize it through various charts. The app utilizes different APIs for text generation and visualization to provide an interactive and user-friendly experience.

Libraries and Tools Used
Streamlit: For building the web application interface.
Pandas: For data manipulation and processing.
Pillow (PIL): For handling image processing.
Base64: For converting images to and from base64 encoding.
Lida: For integrating with various text generation models.
API Integration Issues
During the development of this project, several API integration issues were encountered:

OpenAI: Initially, the project aimed to use OpenAI for text generation. However, OpenAI does not provide free API keys, which limited access to their services.

Google Gemini: The project then attempted to use the Gemini API for text generation and visualization. While text generation worked, visualization through Gemini was problematic and did not meet the project's needs.

Google PALM: An attempt was made to use Google's PALM API for visualization. However, it was found that the PALM API has been discontinued by Google, making it an unsuitable option.

Cohere: Finally, Cohere's API was used, which successfully met the project's requirements. Cohere provided the necessary text generation capabilities and worked well with the application's visualization needs.

Lida Integration
Lida was used for integrating text generation models into the application. While Lida's integration with models like OpenAI, Hugging Face, and Cohere was successful, it did not support the Gemini model. Therefore, for this project, the following models were used:

OpenAI: Initially considered but ultimately not used due to API access issues.
Hugging Face: Supported but not used in the final implementation.
Cohere: Successfully used for text generation and visualization.
Running the Application
To run the Streamlit application, follow these steps:

Ensure you have Python installed.
Install the required libraries:
bash
Copy code
pip install streamlit pandas pillow cohere
Set the COHERE_API_KEY environment variable with your Cohere API key:
bash
Copy code
set COHERE_API_KEY=your_cohere_api_key
Run the Streamlit application:
bash
Copy code
streamlit run app4.py
Access the application in your browser at http://localhost:8501.

Acknowledgements
Special thanks to the developers and maintainers of the libraries and APIs used in this project. Their tools and services made it possible to build a functional and interactive data visualization application.
