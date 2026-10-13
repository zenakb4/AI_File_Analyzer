import streamlit as st
import pymupdf

st.set_page_config(
    page_title="AI File Analyzer",
    page_icon="📄",
    layout="centered",
)

st.title("📄 AI File Analyzer")
st.write(
    "Upload a PDF file to extract its text and view basic document statistics."
)

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"],
)

if uploaded_file is not None:
    try:
        pdf_bytes = uploaded_file.getvalue()

        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as document:
            page_count = len(document)
            extracted_text = "\n".join(page.get_text() for page in document)

        word_count = len(extracted_text.split())
        character_count = len(extracted_text)
        average_words_per_page = (
            word_count / page_count if page_count > 0 else 0
        )

        st.subheader("Analysis Results")
        col1, col2 = st.columns(2)
        col1.metric("Pages", page_count)
        col2.metric("Words", word_count)
        col1.metric("Characters", character_count)
        col2.metric("Average Words per Page", round(average_words_per_page, 2))

        st.subheader("Extracted Text")
        if extracted_text.strip():
            st.text_area(
                "File Content",
                value=extracted_text,
                height=300,
            )
        else:
            st.info(
                "No selectable text was found in this PDF. "
                "It may contain scanned images rather than text."
            )

        st.download_button(
            label="Download Extracted Text",
            data=extracted_text,
            file_name="extracted_text.txt",
            mime="text/plain",
        )

    except Exception:
        st.error(
            "The PDF could not be read. Please try a valid, unencrypted PDF file."
        )
