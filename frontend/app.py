import streamlit as st
import requests
from config import BACKEND_URL

st.set_page_config(page_title="Document Text to Excel", layout="centered")

st.title("📄 Document Text Extraction → Excel")
st.write("Upload **Invoices or Resumes** and convert them into Excel.")

uploaded_file = st.file_uploader(
    "Upload PDF / Image / DOCX",
    type=["pdf","png","jpg","jpeg","docx"]
)

if uploaded_file:
    if st.button("Extract & Convert"):
        with st.spinner("Processing... hang tight 🚀"):
            files = {
                    "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }
            resp = requests.post(f"{BACKEND_URL}/extract", files=files)

        if resp.status_code == 200:
            data = resp.json()
            st.success("Done! Click below to download Excel")

            download_url = f"{BACKEND_URL}/download?path={data['excel_path']}"

            st.download_button(
                label="⬇️ Download Excel",
                data=requests.get(download_url).content,
                file_name=data["excel_path"].split("/")[-1]
            )
        else:
            st.error("Something went wrong 😬")
