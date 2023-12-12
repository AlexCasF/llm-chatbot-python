import streamlit as st
import pandas as pd
import os
from datetime import datetime


#Check-In app
def create_gpt_checkin_form():
    #create raw data storage
    file_folder = 'uploaded_files'
    os.makedirs(file_folder, exist_ok=True)
    csv_file = 'gpt_data.csv'

    #GUI - (auto-coded by ChatGPT from OpenAI's GPT backend Screenshot, what a time to be alive)
    st.title("GPT Check-in")
    gpt_link = st.text_input("Link to GPT")
    name = st.text_input("Name your GPT")
    description = st.text_area("Description", "Add a short description about what this GPT does")
    instructions = st.text_area("Instructions", "What does this GPT do? How does it behave? What should it avoid doing?")
    uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)
    web_browsing = st.checkbox("Web Browsing", value=False)
    dalle_image_generation = st.checkbox("DALL-E Image Generation", value=False)
    code_interpreter = st.checkbox("Code Interpreter", value=False)

    if st.button("Submit"):
        file_paths = []
        for uploaded_file in uploaded_files:
            if uploaded_file is not None:
                file_path = os.path.join(file_folder, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                file_paths.append(file_path)

        # Prepare data for CSV
        data = {
            "Link to GPT": gpt_link,
            "Name": name,
            "Description": description,
            "Instructions": instructions,
            "Web Browsing": web_browsing,
            "DALL-E Image Generation": dalle_image_generation,
            "Code Interpreter": code_interpreter,
            "File Paths": ", ".join(file_paths),
            "Timestamp": datetime.now()
        }

        # Append data to CSV file
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            df = df.append(data, ignore_index=True)
        else:
            df = pd.DataFrame([data])
        df.to_csv(csv_file, index=False)

        st.success("GPT model data submitted successfully!")

# Run the Streamlit form function
if __name__ == "__main__":
    create_gpt_checkin_form()