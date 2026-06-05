import streamlit as st
import base64
import os

# --- GLOBAL CONFIGURATION & GALAXY THEME CSS ---
st.set_page_config(
    page_title="modula. | Custom Hardware Studio",
    page_icon="🌌",
    layout="centered"
)

# Initialize navigation page routing via query parameters
if "page" not in st.query_params:
    st.query_params["page"] = "Stock Catalog"

current_page = st.query_params["page"]

# Function to convert your uploaded image banner safely into HTML format
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    return ""

# Convert images to active inline base64 strings
logo_base64 = get_image_base64("modula.png")
icon_base64 = get_image_base64("modulalogo.png")

# CSS with fixed dark background and star overlay
st.markdown("""
    <style>
    /* Set a flat dark background to prevent "white flash" */
    .stApp, body {
        background-color: #020617 !important;
    }
    
    /* Keep the stars on top of the background */
    body::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        background-image: radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
                          radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px);
        background-size: 550px 550px, 350px 350px;
        animation: twinkle 15s linear infinite;
        opacity: 0.3;
        pointer-events: none;
    }
    
    @keyframes twinkle {
        from { background-position: 0 0, 0 0; }
        to { background-position: 550px 550px, 350px 350px; }
    }
    
    /* Ensure all text remains visible */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, .stMetric, .stRadio, .stSlider {
        color: #ffffff !important;
    }

    /* Neutralize default Streamlit header */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        z-index: 1 !important;
    }

    /* --- GLOBAL TOP FLOATING HEADER --- */
    .custom-top-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 70px;
        padding: 5px max(6vw, 30px);
        background: rgba(8, 8, 16, 0.95);
        backdrop-filter: blur(16px);
        border-bottom: 1px solid rgba(147, 51, 234, 0.2);
        z-index: 999999 !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
        pointer-events: auto !important;
    }

    /* Interactive button styling */
    .nav-btn {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(147, 51, 234, 0.3) !important;
        color: #ffffff !important;
        border-radius: 20px !important;
        padding: 6px 16px !important;
        text-decoration: none !important;
        margin-left: 10px;
    }
    
    .header-space-offset { margin-top: 80px; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER LAYOUT ---
st.markdown(f"""
    <div class="custom-top-header">
        <div style="font-weight:bold; color:white;">modula.</div>
        <div>
            <a href="?page=Stock+Catalog" class="nav-btn">Stock Catalog</a>
            <a href="?page=Our+Responsibility" class="nav-btn">Our Responsibility</a>
            <a href="?page=Community+Survey" class="nav-btn">Community Survey</a>
        </div>
    </div>
    <div class="header-space-offset"></div>
""", unsafe_allow_html=True)

# --- PAGE CONTENT ---
if current_page == "Stock Catalog":
    st.markdown("## 🚀 Stock Catalog")
    st.markdown("#### Hand-built for performance. Zero compromises, fair pricing.")
    st.divider()
    
    st.markdown("### cosmic. Series")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("cosmic. 8GB RAM", "$50")
        st.metric("cosmic. CPU", "$400")
    with col2:
        st.metric("cosmic. 4TB SSD", "$350")
        st.metric("cosmic. GPU", "$300")
        
    st.divider()
    st.markdown("### 🖱️ util. Series (ODelay set)")
    col3, col4, col5 = st.columns(3)
    with col3: st.info("**ODelay Keyboard**\n\n(100% Layout)\n\n**$80**")
    with col4: st.info("**ODelay Mouse**\n\n(No side buttons)\n\n**$40**")
    with col5: st.info("**ODelay Headset**\n\n(Integrated mic)\n\n**$60**")

elif current_page == "Our Responsibility":
    st.markdown("## 🌱 Our Responsibility")
    st.write("Commitment to ethical hardware and sustainability.")

elif current_page == "Community Survey":
    st.markdown("## 📋 Community Survey")
    st.slider("Store layout rating", 1, 5, 3)
    st.button("Submit Survey Response")