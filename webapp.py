#display the console processing on streamlit UI
import streamlit as st 
import re
from crew import crewai_setup
import sys 
import os 
import json 
import html_content 

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

class StreamToExpander:
    def __init__(self, expander):
        self.expander = expander
        self.buffer = []

    def write(self, data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)

        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer))
            self.buffer = []

# # Redirect stdout to our custom stream
# sys.stdout = StreamToUI(st)
# sys.stdout = sys.__stdout__

def run_crewai_app():
    

    with st.sidebar:
        st.write('Crew AI Pharma company ')
        def refresh_page():
            refresh_code = """
                <script>
                if (window.location !== window.parent.location) {
                    window.parent.location.reload(true);
                } else {
                    window.location.reload(true);
                }
                </script>
            """
            st.markdown(refresh_code, unsafe_allow_html=True)

# Create a button to trigger page refresh
        if st.button("Refresh Page"):
            refresh_page()



    st.title("Cyber month 2024")
    st.empty()
    # st.image('architecture.png', use_column_width="auto")
    # st.divider()
    #business_overview = st.text_area('Tell me about your business', placeholder="I run a digital marketing agency... ")
    st.markdown("""

        ### Agent Overview     

    """, unsafe_allow_html=True)

    #st.markdown(html_content.agent_cards_html(), unsafe_allow_html=True)
    st.components.v1.html(html_content.agent_cards_html(),height=800,scrolling=True)
   
    st.sidebar.header('⚙️ Parameters')

    def on_click_btn(folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        else:
            st.error('Folder exists')
    
    def is_any_directory_not_empty(directories):
        """Check if any of the specified directories is not empty."""
        
        if os.listdir(directories):
            # Found a non-empty directory
            return True
        # All directories are empty
        return False


    # Allow users to select a folder
    def file_selector(folder_path='.'):
        folders = []
        files = os.listdir(folder_path)
        new_folder = '➕ new folder'
        for folder in files:
            flags =['.streamlit','__pycache__']
            if os.path.isdir(folder) and folder not in flags:
                folders.append(folder)
        
        folders.append(new_folder)
        selected_filename = st.sidebar.selectbox('📁 Select a folder for saving', folders)
        if selected_filename==folders[-1]: #if we select "add new folder"
            fn,fb=st.sidebar.columns(2)
            folder_name = fn.text_input('Folder name',placeholder="Folder name", label_visibility='collapsed')
            add_btn = fb.button('Add')
            if add_btn:
                try:
                    on_click_btn(folder_name=folder_name)
                    st.experimental_rerun()
                except:
                    st.sidebar.error("Error with folder name ")
                
        elif is_any_directory_not_empty(selected_filename):
            st.sidebar.warning("This folder is not empty! it's content will be erased ")
        
        return os.path.join(folder_path, selected_filename)
    


    filename = file_selector()
    #filename+="/"
    
    st.sidebar.write('You selected `%s`' % filename)

    c1,c2=st.columns(2)    
    run = c1.button("Run Analysis", type="primary")
    if run:
        stop=c2.button('stop', type="secondary")
        if not stop:
            with st.container(border=True):
                sys.stdout = StreamToExpander(st)
                
                with st.spinner("Generating Results"):
                    crew_result = crewai_setup()
                    
            
        st.header("Results:")
        st.markdown(crew_result)
        with st.expander("Output"):
            # Redirect stdout to our custom stream
            sys.stdout = StreamToExpander(st)
if __name__ == "__main__":
    run_crewai_app()