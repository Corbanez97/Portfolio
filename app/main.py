import streamlit as st
import uuid

from utils import generate_image

def on_page_load():
    with open('assets/style/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    if "session_id" not in st.session_state:
        st.session_state.session_id = uuid.uuid4()
        
    if "dream" not in st.session_state:
        st.session_state.dream = False

    if "img" not in st.session_state:
        st.session_state.img = ''

def main():

    on_page_load()

    st.title("Hi:wave: :I I'm Lucas Corbanez.")
    st.subheader("Physicist, Data Engineer, and Data Scientist.")
    st.markdown("---")
    st.markdown("<h4 style='text-align: center;'>Ask me anything!</h4>", unsafe_allow_html=True)
    # image = "assets\images\\tcc.jpg" 
    # st.image(image, width=500)

    # image = "assets\images\datalake_arch.png" 
    # st.image(image, use_column_width=True)

    
    st.text_area("", height=100, key='input', help='')

    if st.button("Dream"):
        if st.session_state.input != "" and "prompt" not in st.session_state:
            st.session_state.prompt = st.session_state['input']
            st.session_state.generated = generate_image(st.session_state.prompt)
            st.session_state.dream = True
        elif st.session_state.input != "" and st.session_state['input'] != st.session_state.prompt:
            st.session_state.prompt = st.session_state['input']
            st.session_state.generated = generate_image(st.session_state.prompt)
        else:
            st.error("Provide Input to Dream")

    if "generated" in st.session_state and st.session_state.dream == True:
        try:
            st.image(st.session_state.generated, use_column_width=True, output_format="JPEG")
        except Exception as e:
            st.error(e)

    st.markdown('---')


if __name__ == '__main__':
    main()