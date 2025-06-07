import streamlit as st #type:ignore
from PIL import Image #type:ignore

# Set page config
st.set_page_config(
    page_title="GSV Freshers' Guide",
    page_icon="🎓",
    layout="wide"
)

# Sidebar navigation
menu = [
    "Home",
    "Admissions & Enrollment",
    "Academics",
    "Campus Life",
    "Hostel & Accommodation",
    "Student Support",
    "Vadodara City Guide",
    "FAQs",
    "Contact Us / Connect"
]

st.sidebar.title("GSV Freshers' Guide")
choice = st.sidebar.radio("Navigate", menu)

# Search bar
search_query = st.sidebar.text_input("🔍 Search the Guide")

# Hero image (replace with your own campus image if available)
hero_img_url = "https://www.gsv.ac.in/images/gsv-campus.jpg"  # Official GSV campus image

# Add GSV logo as a fixed, semi-transparent background only for the Home page
if choice == "Home":
    st.markdown(
        f"""
        <style>
        /* Use a background image on the main content area for Home page */
        .stApp {{
            background: none !important;
        }}
        .block-container::before {{
            content: "";
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: url('GSV%20logo_BG%20white%20FG%20blue.png') center center no-repeat;
            background-size: 45vw;
            opacity: 0.13;
            z-index: 0;
            pointer-events: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Home Page
if choice == "Home":
    st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>Welcome to Gati Shakti Vishwavidyalaya! Your Journey Begins Here.</h1>
    """, unsafe_allow_html=True)
    st.image(hero_img_url, use_container_width=True, caption="GSV Campus")
    st.markdown("""
    <div style='text-align: center;'>
        <h3>GSV Freshers' Guide: Your Smooth Start at Gati Shakti Vishwavidyalaya</h3>
        <p>Welcome! This guide is created by students, for students, to help you settle in and thrive at GSV. Explore the sections to find answers to all your fresher questions!</p>
        <a href='#' style='background: #2E86C1; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;'>Explore the Fresher's Guide</a>
    </div>
    <br>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .stButton > button {
        background: #181818;
        color: #fff;
        border: 3px solid #2E86C1;
        border-radius: 14px;
        padding: 0.7em 1.5em;
        font-size: 1.15em;
        font-weight: 600;
        box-shadow: 0 2px 8px rgba(44,62,80,0.10);
        position: relative;
        z-index: 1;
        transition: color 0.3s, background 0.3s, box-shadow 0.3s, border-image 0.3s;
        overflow: hidden;
    }
    .stButton > button:before {
        content: '';
        position: absolute;
        top: -3px; left: -3px; right: -3px; bottom: -3px;
        z-index: -1;
        background: transparent;
        border-radius: 16px;
        filter: blur(2px);
        opacity: 0;
        transition: opacity 0.3s;
    }
    .stButton > button:hover {
        color: #fff;
        background: linear-gradient(90deg, #3333ff 0%, #ff00cc 100%);
        box-shadow: 0 6px 24px rgba(44,62,80,0.18);
        border-image: linear-gradient(90deg, #ff00cc, #3333ff, #00ffcc, #ffcc00, #ff00cc) 1;
    }
    .stButton > button:hover:before {
        background: linear-gradient(270deg, #ff00cc, #3333ff, #00ffcc, #ffcc00, #ff00cc);
        background-size: 600% 600%;
        opacity: 0.7;
        filter: blur(0.5px);
        animation: rgbmove 3s linear infinite;
    }
    @keyframes rgbmove {
        0% {background-position:0% 50%}
        50% {background-position:100% 50%}
        100% {background-position:0% 50%}
    }
    </style>
    """, unsafe_allow_html=True)
    st.subheader("Quick Links")
    cols = st.columns(4)
    quick_links = [
        ("Hostel Info", "Hostel & Accommodation"),
        ("Admission Checklist", "Admissions & Enrollment"),
        ("Academic Programs", "Academics"),
        ("Vadodara City Guide", "Vadodara City Guide")
    ]
    for i, (label, section) in enumerate(quick_links):
        with cols[i]:
            st.button(label, key=section)

# Admissions & Enrollment
elif choice == "Admissions & Enrollment":
    st.header("Admissions & Enrollment")
    st.markdown("""
    - **Admission Checklist**: Documents, photos, medical certificate, anti-ragging affidavit, fee payment, reporting day info.
    - **Important Dates**: Fee deadlines, orientation, class start.
    - **Scholarships**: [GSV Scholarships Page](https://www.gsv.ac.in)
    """)
    st.info("Add more details as needed.")

# Academics
elif choice == "Academics":
    st.header("Academics")
    st.markdown("""
    - **Programs Offered**: B.Tech, MBA, M.Tech, etc.
    - **Course Structure**: Syllabus, credits, electives.
    - **Academic Calendar**: Exams, breaks, holidays.
    - **Mentorship, Departments, Library, Labs.**
    """)
    st.info("Add more details as needed.")

# Campus Life
elif choice == "Campus Life":
    st.header("Campus Life")
    st.markdown("""
    - **Student Clubs & Societies**: Technical, cultural, sports, etc.
    - **Sports Facilities**: Gym, grounds, teams.
    - **Cultural Events**: Fests, annual events.
    - **Student Council, Campus Map, FAQs.**
    """)
    st.info("Add more details as needed.")

# Hostel & Accommodation
elif choice == "Hostel & Accommodation":
    st.header("Hostel & Accommodation")
    st.markdown("""
    - **Hostel Facilities**: Room types, amenities, security.
    - **Mess & Food**: Timings, menu, dietary options.
    - **Hostel Rules**: Guidelines, what to pack.
    - **Off-Campus Options** (if any).
    """)
    st.info("Add more details as needed.")

# Student Support
elif choice == "Student Support":
    st.header("Student Support")
    st.markdown("""
    - **Counseling, Medical, Anti-Ragging, Grievance, Disability Support.**
    - **Emergency Contacts**
    """)
    st.info("Add more details as needed.")

# Vadodara City Guide
elif choice == "Vadodara City Guide":
    st.header("Vadodara City Guide")
    st.markdown("""
    - **Getting to GSV**: Directions, transport.
    - **Nearby Amenities**: Banks, stores, restaurants, hospitals.
    - **Places to Visit**: Attractions, safety tips.
    """)
    st.info("Add more details as needed.")

# FAQs
elif choice == "FAQs":
    st.header("Frequently Asked Questions")
    st.markdown("""
    **Admission & Enrollment**
    - What documents do I need to bring for reporting?
    - How do I pay my fees?
    **Hostel Life**
    - Is Wi-Fi available in hostels?
    - What are the mess timings?
    **Academics**
    - Whom do I contact for academic doubts?
    **General GSV**
    - Is ragging tolerated at GSV? (No, strict anti-ragging policy)
    """)
    st.info("Add more FAQs as needed.")

# Contact Us / Connect
elif choice == "Contact Us / Connect":
    st.header("Contact Us / Connect")
    st.markdown("""
    - **WhatsApp Group**: [Join Here](https://chat.whatsapp.com/https://chat.whatsapp.com/JcnEQWtD2zg41iQdEL8NU0)
    - **Social Media**: [Facebook](#), [Instagram](#), [LinkedIn](#)
    - **Department Contacts**: Admissions, Hostel Warden, Dean, etc.
    """)
    st.subheader("Feedback Form")
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Question or Feedback")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for your feedback! We will get back to you soon.")

# Search functionality (basic)
if search_query:
    st.write(f"Search results for: {search_query}")
    st.info("(Search functionality can be enhanced with more content and filtering.)")
