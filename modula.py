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

# Convert modula.png to an active inline base64 string
logo_base64 = get_image_base64("modula.png")

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

    /* Completely neutralize the default Streamlit glass block header so mouse clicks pass through */
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
        /* Raised z-index ensures elements are entirely physical and clickable */
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

    /* Menu container shifted smoothly left of the Deploy cluster */
    .custom-top-nav {
        display: flex;
        gap: 12px;
        margin-right: 140px;
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

    /* 🚀 HOVER EFFECT: Physically pops out toward user with an intense cosmic neon shadow */
    .nav-btn:hover {
        color: #ffffff !important;
        background-color: rgba(147, 51, 234, 0.12) !important;
        border-color: rgba(168, 85, 247, 0.7) !important;
        transform: translateY(-3px); 
        box-shadow: 0 6px 16px rgba(147, 51, 234, 0.4) !important;
    }

    /* ✨ ACTIVE STATE: Mimics a mechanical switch being pressed down and staying lit */
    .nav-btn.active {
        color: #ffffff !important;
        background: linear-gradient(135deg, rgba(168, 85, 247, 0.35), rgba(236, 72, 153, 0.35)) !important;
        border-color: #a855f7 !important;
        box-shadow: 0 0 12px rgba(168, 85, 247, 0.6) !important;
        transform: translateY(0px) scale(0.97);
    }

    /* Padding offset helper to prevent main layout from hiding behind fixed header bar */
    .header-space-offset {
        margin-top: 60px;
    }

    /* Standard Streamlit Action Buttons Pop Custom Settings */
    div.stButton > button {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #a855f7 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(147, 51, 234, 0.4) !important;
    }
    
    /* Smooth fading transition whenever pages change */
    .element-container, .stMarkdown, div[data-testid="stVerticalBlock"] {
        animation: fadeIn 0.4s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(4px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Subtle glow effect around metrics */
    div[data-testid="stMetricValue"], .stAlert {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(147, 51, 234, 0.3);
        border-radius: 8px;
        padding: 10px !important;
        box-shadow: 0 0 10px rgba(147, 51, 234, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Generate fallback text layout if modula.png is missing locally
logo_html = f'<img src="data:image/png;base64,{logo_base64}" alt="modula. logo">' if logo_base64 else '<div style="font-size:1.8rem; font-weight:800; background:linear-gradient(45deg, #a855f7, #ec4899); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">modula.</div>'

# --- INTEGRATED HEADER INJECTION: GALAXY IMAGE (LEFT) & NAV BUTTONS (RIGHT) ---
st.markdown(f"""
    <div class="custom-top-header">
        <div class="brand-logo-container">
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
    st.caption("*Plan: Prices curated for organic growth, subject to adjustments as our community expands.*")
    st.divider()

    # Cosmic PC Series
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

    # Util Peripherals Series
    st.markdown("### 🖱️ util. Series (ODelay set)")
    st.caption("* Bundles strictly priced as written below *")

    col3, col4, col5 = st.columns(3)
    with col3:
        st.info("**ODelay Keyboard**\n\n(100% Layout)\n\n**$80**")
    with col4:
        st.info("**ODelay Mouse**\n\n(No side buttons: m3 & m4)\n\n**$40**")
    with col5:
        st.info("**ODelay Headset**\n\n(With integrated mic)\n\n**$60**")


elif current_page == "Our Responsibility":
    st.markdown("## 🌱 Responsibility Studio Poster")
    st.markdown("#### How modula. impacts our community and planet responsibly.")
    st.divider()

    # Row 1: E-Waste & Sourced Materials
    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown("### ♻️ E-Waste Recycling Program")
        st.write("We host a dedicated in-store drop-off station where customers can safely recycle broken or outdated tech, keyboards, and mice.")
    with right_col:
        st.markdown("### 🔌 Ethical Material Sourcing")
        st.write("We prioritize purchasing our raw materials—such as high-quality resin and copper wiring—from suppliers who explicitly guarantee ethical labor practices and fair wages.")

    st.divider()

    # Row 2: Packaging & Artisans
    left_col2, right_col2 = st.columns(2)
    with left_col2:
        st.markdown("### 📦 Sustainable Packaging")
        st.write("All products are shipped and sold in 100% recyclable, plastic-free cardboard boxes to minimize our environmental impact.")
    with right_col2:
        st.markdown("### 🎨 Local Artisan Support")
        st.write("We dedicate shelf space to showcase and sell custom artisan keycaps created by independent local artists without charging them any consignment fees.")

    st.divider()

    # Row 3: STEM Focus
    st.markdown("### 🧠 Community STEM Funding")
    st.write("We donate 5% of our monthly profits to a local youth program to help fund after-school coding and hardware assembly workshops.")


elif current_page == "Community Survey":
    st.markdown("## 📋 Customer Satisfaction Survey")
    st.markdown("#### Help us improve our operations. Your thoughts build our reputation.")
    st.divider()

    st.markdown("### ⭐ Rating Section (1-5)")
    q1 = st.slider("1. How do you like the store layout?", 1, 5, 3)
    q2 = st.slider("2. How would you rate the latency and responsiveness of your ODelay gaming mouse/keyboard?", 1, 5, 3)
    q3 = st.slider("3. How easy and straightforward was it to navigate our boutique online shop menu?", 1, 5, 3)

    st.divider()

    st.markdown("### ❓ Verification (Yes / No)")
    q4 = st.radio("4. Did your components arrive perfectly intact with zero damage to the custom braided cabling or casing?", ["Yes", "No"])
    q5 = st.radio("5. Would you recommend 'modula.' to other gamers, creators, or streamers?", ["Yes", "No"])
    q6 = st.radio("6. Did our pricing make high-end custom hardware accessible for your current budget?", ["Yes", "No"])

    st.divider()

    st.markdown("### ✍️ Short Answer Feedback")
    q7 = st.text_input("7. How did you first discover the modula. studio?")
    q8 = st.text_input("8. Which custom-built item is currently the main centerpiece of your desk setup?")
    q9 = st.text_input("9. How frequently do you typically look to upgrade or customize elements of your hardware?")
    q10 = st.text_area("10. What should we add next as a bundle? (ideas)")

    st.divider()
    
    if st.button("Submit Survey Response"):
        st.success("Thank you for your feedback! Use your coupon code INFINITY15 on checkout for $15 off!")