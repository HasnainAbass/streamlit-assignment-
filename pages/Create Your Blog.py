import streamlit as st
Upload_images = st.file_uploader("Choose your Image", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
Upload_texts = st.file_uploader("Choose your Text", accept_multiple_files=True, type=["text", "txt"])
Upload_video = st.file_uploader("Choose your Video", accept_multiple_files=True, type=["mp4", "avi", "mov"])

# ----------------------------------------------------------------
for Upload_image in Upload_images:
    st.write("Filename:", Upload_image.name)
    st.image(Upload_image)
# ---------------------------------------------------------------
for Upload_text in Upload_texts:
    st.write("Filename:", Upload_text.name)
    bytes_data = Upload_text.read()
    st.text(bytes_data.decode("utf-8")) 
# ----------------------------------------------------------------
for Upload_vide in Upload_video:
     st.write("Filename:", Upload_vide.name)
     st.video(Upload_vide) 
