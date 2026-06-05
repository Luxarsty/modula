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
icon_base64 = get_image_base64("logo.jpg")

# Custom CSS for Galaxy Theme, Input Elements, and Fixed Header Elements
st.markdown("""
    <style>
    /* Galaxy Background & Text Coloring */
    .stApp {
        background-image: radial-gradient(circle at center, #111222 0%, #080810 70%, #020205 100%);
        color: #ffffff;
    }
    
    /* Make all default text, headers, and labels bright white for visibility */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #ffffff !important;
    }

    /* Completely neutralize the default Streamlit glass block header */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        z-index: 1 !important;
        pointer-events: none;
    }

    /* --- GLOBAL TOP FLOATING HEADER --- */
    .custom-top-header {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 70px;
        padding: 5px max(6vw, 30px);
        background: rgba(8, 8, 16, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-bottom: 1px solid rgba(147, 51, 234, 0.2);
        z-index: 999999 !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
        pointer-events: auto !important;
    }

    /* Brand Logo Graphic Sizing */
    .brand-logo-container img {
        height: 55px;
        width: auto;
        object-fit: contain;
        display: block;
    }

    /* Menu container */
    .custom-top-nav {
        display: flex;
        gap: 12px;
        pointer-events: auto !important;
    }

    /* Base interactive button styling */
    .nav-btn {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(147, 51, 234, 0.25) !important;
        color: rgba(255, 255, 255, 0.65) !important;
        border-radius: 20px !important;
        padding: 6px 16px !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        text-decoration: none !important;
        cursor: pointer !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        pointer-events: auto !important;
        display: inline-block;
    }

    .nav-btn:hover {
        color: #ffffff !important;
        background-color: rgba(147, 51, 234, 0.12) !important;
        border-color: rgba(168, 85, 247, 0.7) !important;
        transform: translateY(-3px); 
        box-shadow: 0 6px 16px rgba(147, 51, 234, 0.4) !important;
    }

    .nav-btn.active {
        color: #ffffff !important;
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.35), rgba(236, 72, 153, 0.35)) !important;
        border-color: #a855f7 !important;
        box-shadow: 0 0 12px rgba(168, 85, 247, 0.6) !important;
        transform: translateY(0px) scale(0.97);
    }

    .header-space-offset {
        margin-top: 60px;
    }
    
    div.stButton > button {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #a855f7 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Generate logo layout
logo_html = f'<img src="data:image/png;base64,{logo_base64}" alt="modula. logo">' if logo_base64 else '<div style="font-size:1.8rem; font-weight:800; background:linear-gradient(45deg, #a855f7, #ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">modula.</div>'

# --- INTEGRATED HEADER: ICON & LOGO (LEFT) & NAV (CENTER/RIGHT) ---
st.markdown(f"""
    <div class="custom-top-header">
        <div class="brand-logo-container" style="display: flex; align-items: center; gap: 10px;">
            <img src="data:image/jpeg;base64,{icon_base64}" alt="modula icon" style="height: 45px; width: auto; border-radius: 50%;">
            {logo_html}
        </div>
        <div class="custom-top-nav">
            <a href="?page=Stock+Catalog" target="_self" class="nav-btn {'active' if current_page == 'Stock Catalog' else ''}">Stock Catalog</a>
            <a href="?page=Our+Responsibility" target="_self" class="nav-btn {'active' if current_page == 'Our Responsibility' else ''}">Our Responsibility</a>
            <a href="?page=Community+Survey" target="_self" class="nav-btn {'active' if current_page == 'Community Survey' else ''}">Community Survey</a>
        </div>
    </div>
    <div class="header-space-offset"></div>
""", unsafe_allow_html=True)


# ==========================================
# PAGE ROUTING SECTIONS
# ==========================================

if current_page == "Stock Catalog":
    st.markdown("## 🚀 Stock Catalog")
    st.markdown("#### Hand-built for performance. Zero compromises, fair pricing.")
    st.divider()

    st.markdown("### cosmic. Series")
    st.markdown("**Full PC Component Set Bundle:** `$1400` *(Includes 64GB RAM + items below)*")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="cosmic. 8GB RAM (DDR5 : 6200MHz)", value="$50")
        st.metric(label="cosmic. CPU", value="$400")
    with col2:
        st.metric(label="cosmic. 4TB SSD (14,500 Speeds)", value="$350")
        st.metric(label="cosmic. GPU", value="$300")

    st.divider()

    st.markdown("### 🖱️ util. Series (ODelay set)")
    col3, col4, col5 = st.columns(3)
    with col3:
        st.info("**ODelay Keyboard**\n\n(100% Layout)\n\n**$80**")
    with col4:
        st.info("**ODelay Mouse**\n\n(No side buttons: m3 & m4)\n\n**$40**")
    with col5:
        st.info("**ODelay Headset**\n\n(With integrated mic)\n\n**$60**")


elif current_page == "Our Responsibility":
    st.markdown("## 🌱 Responsibility Studio Poster")
    st.divider()

    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown("### ♻️ E-Waste Recycling Program")
        st.write("We host a dedicated in-store drop-off station for customers.")
    with right_col:
        st.markdown("### 🔌 Ethical Material Sourcing")
        st.write("We prioritize suppliers guaranteeing ethical labor practices.")

    st.divider()

    left_col2, right_col2 = st.columns(2)
    with left_col2:
        st.markdown("### 📦 Sustainable Packaging")
        st.write("100% recyclable, plastic-free shipping.")
    with right_col2:
        st.markdown("### 🎨 Local Artisan Support")
        st.write("Shelf space for independent local artists at zero consignment cost.")

    st.divider()
    st.markdown("### 🧠 Community STEM Funding")
    st.write("Donating 5% of monthly profits to local youth coding workshops.")


elif current_page == "Community Survey":
    st.markdown("## 📋 Customer Satisfaction Survey")
    st.divider()

    st.markdown("### ⭐ Rating Section")
    q1 = st.slider("1. Store layout rating", 1, 5, 3)
    q2 = st.slider("2. ODelay mouse/keyboard latency rating", 1, 5, 3)
    q3 = st.slider("3. Website navigation ease", 1, 5, 3)

    st.divider()

    st.markdown("### ❓ Verification")
    q4 = st.radio("4. Perfect condition arrival?", ["Yes", "No"])
    q5 = st.radio("5. Recommend modula. to others?", ["Yes", "No"])
    q6 = st.radio("6. Pricing accessibility?", ["Yes", "No"])

    st.divider()

    st.markdown("### ✍️ Short Answer Feedback")
    q7 = st.text_input("7. How did you discover us?")
    q8 = st.text_input("8. Main centerpiece of your setup?")
    q9 = st.text_input("9. Upgrade frequency?")
    q10 = st.text_area("10. Bundle ideas?")

    st.divider()
    
    if st.button("Submit Survey Response"):
        st.success("Thank you for your feedback! Use code INFINITY15 for $15 off!")