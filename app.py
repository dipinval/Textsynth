# app.py

import streamlit as st


# Translations dictionary
translations = {
    "en": {
        "title": "TextSynth",
        "modes": "Modes:",
        "modes_options": ["Paragraph", "Bullet Points"],
        "task": "Task:",
        "task_options": ["Paraphrase", "Summarize"],
        "summary_length": "Summary Length:",
        "text_area": "Enter or paste your text (up to 1000 words) and press 'Execute.'",
        "execute_button": "Execute",
        "upload_doc": "Upload Doc",
        "word_limit_error": "The input text exceeds the 1000 words limit. Please reduce the text length.",
        "footer": "TextSynth Privacy Policy and Terms of Service apply."
    },
    "ne": {
        "title": "TextSynth",
        "modes": "मोडहरू:",
        "modes_options": ["अनुच्छेद", "बुलेट पोइन्टहरू"],
        "task": "कार्य:",
        "task_options": ["पैराफ्रेश", "सारांश"],
        "summary_length": "सारांश लम्बाइ:",
        "text_area": "तपाईंको पाठ (१००० शब्दसम्म) प्रविष्ट गर्नुहोस् वा टाँस्नुहोस् र 'कार्यान्वयन' थिच्नुहोस्।",
        "execute_button": "कार्यान्वयन",
        "upload_doc": "डक अपलोड गर्नुहोस्",
        "word_limit_error": "इनपुट पाठले १००० शब्दको सीमा नाघ्यो। कृपया पाठको लम्बाइ घटाउनुहोस्।",
        "footer": "TextSynth गोपनीयता नीति र सेवा सर्तहरू लागू हुन्छ।"
    }
}

# Streamlit app setup
st.set_page_config(page_title="TextSynth", layout="centered")

# Language selection
language = st.selectbox("Select Language:", ["English", "Nepali"])
lang_code = "en_XX" if language == "English" else "ne_NP"

# Translations
t = translations["en" if lang_code == "en_XX" else "ne"]

# Title
st.title(t["title"])

# Mode selection
mode = st.selectbox(t["modes"], t["modes_options"])

# Task selection
task = st.selectbox(t["task"], t["task_options"])

# Conditional display of summary length slider
if task == "Summarize":
    summary_length = st.slider(t["summary_length"], min_value=1, max_value=100, value=50)
else:
    summary_length = None

# Text input area
text_input = st.text_area(t["text_area"])

# Word count check
def word_count(text):
    return len(text.split())

# Execute button
if st.button(t["execute_button"]):
    if text_input:
        if word_count(text_input) > 1000:
            st.error(t["word_limit_error"])
        else:
            if task == "Paraphrase":
                paraphrased_texts = paraphrase_text(text_input, lang_code=lang_code)
                st.write("Paraphrased Texts:" if lang_code == "en_XX" else "पैराफ्रेश गरिएको पाठ:")
                for i, para in enumerate(paraphrased_texts, 1):
                    st.write(f"{t['task_options'][0]} {i}: {para}")
            elif task == "Summarize":
                summarized_texts = summarize_text(text_input, max_length=summary_length)
                st.write("Summarized Texts:" if lang_code == "en_XX" else "सारांश:")
                for i, summary in enumerate(summarized_texts, 1):
                    st.write(f"{t['task_options'][1]} {i}: {summary}")
    else:
        st.write("Please enter text to process." if lang_code == "en_XX" else "कृपया प्रक्रिया गर्न पाठ प्रविष्ट गर्नुहोस्।")

# File uploader (not used in this example)
uploaded_file = st.file_uploader(t["upload_doc"])

# Footer
st.markdown(f"""
    <div style="text-align: center; font-size: 12px; color: #999;">
        {t['footer']}
    </div>
""", unsafe_allow_html=True)
