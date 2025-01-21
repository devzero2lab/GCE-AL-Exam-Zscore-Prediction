import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model.pickle', 'rb'))

# Page configuration
st.set_page_config(page_title="Zscore Prediction", page_icon="🎓", layout="centered")

st.title("🎓 GCE AL Exam Zscore Prediction")
st.markdown(
    """
    **Welcome!**  
    Predict Z-scores based on student performance in the GCE AL Exam 2020 (Sri Lanka).
    <hr>
    """,unsafe_allow_html=True,
)


# Input form with enhanced layout
st.markdown("<div class='form-title'>🔢 Input Details</div>", unsafe_allow_html=True)

# Mapping dictionaries
stream_map = {"ARTS": 0, "COMMERCE": 1, "SCIENCE": 2}
grade_map = {"A": 4, "B": 3, "C": 2, "S": 1, "F": 0}
syllabus_map = {"New": 1, "Old": 0}
gender_map = {"Male": 0, "Female": 1}
sub_map = {
    'ACCOUNTING': 0, 'AGRICULTURAL SCIENCE': 1, 'AGRO TECHNOLOGY': 2, 'ART': 3,
    'BIO SYSTEMS TECHNOLOGY': 4, 'BIO-RESOURCE TECHNOLOGY': 5, 'BIOLOGY': 6,
    'BUDDHISM': 7, 'BUDDHIST CIVILIZATION': 8, 'BUSINESS STATISTICS': 9,
    'BUSINESS STUDIES': 10, 'CARNATIC MUSIC': 11, 'CHEMISTRY': 12,
    'CHRISTIAN CIVILIZATION': 13, 'CHRISTIANITY': 14, 'CIVIL TECHNOLOGY': 15,
    'COMBINED MATHEMATICS': 16, 'COMMUNICATION & MEDIA STUDIES': 17,
    'DANCING(BHARATHA)': 18, 'DANCING(INDIGENOUS)': 19, 'DRAMA AND THEATRE (SINHALA)': 20,
    'ECONOMICS': 21, 'ELECTRICAL,ELECTRONIC AND IT': 22, 'ENGINEERING TECHNOLOGY': 23,
    'ENGLISH': 24, 'FOOD TECHNOLOGY': 25, 'GEOGRAPHY': 26,
    'GREEK & ROMAN CIVILIZATION': 27, 'HIGHER MATHEMATICS': 28, 'HINDU CIVILIZATION': 29,
    'HINDUISM': 30, 'HISTORY OF EUROPE': 31, 'HISTORY OF INDIA': 32,
    'HISTORY OF MODERN WORLD': 33, 'HISTORY OF SRI LANKA & EUROPE': 34,
    'HISTORY OF SRI LANKA & INDIA': 35, 'HISTORY OF SRI LANKA & MODERN WORLD': 36,
    'HOME ECONOMICS': 37, 'INFORMATION & COMMUNICATION TECHNOLOGY': 38, 'ISLAM': 39,
    'ISLAMIC CIVILIZATION': 40, 'LOGIC & SCIENTIFIC METHOD': 41, 'MATHEMATICS': 42,
    'MECHANICAL TECHNOLOGY': 43, 'ORIENTAL MUSIC': 44, 'PALI': 45, 'PHYSICS': 46,
    'POLITICAL SCIENCE': 47, 'SINHALA': 48, 'TAMIL': 49, 'WESTERN MUSIC': 50
}

# Form layout
with st.form("prediction_form"):
    stream = st.selectbox("Stream:", stream_map.keys())
    col1, col2 = st.columns(2)
    
    with col1:
        sub1 = st.selectbox("Subject 1:", sub_map.keys())
        sub2 = st.selectbox("Subject 2:", sub_map.keys())
        sub3 = st.selectbox("Subject 3:", sub_map.keys())
    
    with col2:
        sub1_r = st.selectbox("Subject 1 Grade:", grade_map.keys())
        sub2_r = st.selectbox("Subject 2 Grade:", grade_map.keys())
        sub3_r = st.selectbox("Subject 3 Grade:", grade_map.keys())
    
    syllabus = st.selectbox("Syllabus:", syllabus_map.keys())
    gender = st.selectbox("Gender:", gender_map.keys())

    # Submit button
    submitted = st.form_submit_button("Predict 💡")

# Prediction logic
if submitted:
    inp = np.array([[
        stream_map[stream],
        sub_map[sub1],
        grade_map[sub1_r],
        sub_map[sub2],
        grade_map[sub2_r],
        sub_map[sub3],
        grade_map[sub3_r],
        syllabus_map[syllabus],
        gender_map[gender]
    ]])

    try:
        # Make prediction
        prediction = model.predict(inp)
        st.success(f"🎯 Estimated Zscore: **{prediction[0]:,.2f}**")
    except Exception as e:
        st.error(f"❌ An error occurred during prediction: {e}")

# Footer with credits
st.markdown(
    """
    <hr>
    <footer style="text-align: center; color: #95a5a6;">
    Developed with ❤️ by [zero2learn].
    </footer>
    """,
    unsafe_allow_html=True,
)
