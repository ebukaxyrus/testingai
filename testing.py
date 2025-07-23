import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

# Google Analytics 4 Tag Injection
components.html(
    """
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-JRZNTB02YQ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-JRZNTB02YQ');
    </script>
    """,
    height=0,
    width=0
)

# Nektic-style Component Kit Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Root Variables - Nektic Dark Theme */
    :root {
        --bg-primary: #0a0a0a;
        --bg-secondary: #1a1a1a;
        --bg-card: #2a2a2a;
        --bg-input: #1e1e1e;
        --primary-purple: #8b5cf6;
        --primary-purple-hover: #7c3aed;
        --primary-purple-light: rgba(139, 92, 246, 0.1);
        --accent-orange: #f97316;
        --accent-red: #ef4444;
        --text-primary: #ffffff;
        --text-secondary: #a1a1aa;
        --text-muted: #71717a;
        --border-color: #404040;
        --border-input: #525252;
        --success: #22c55e;
        --warning: #eab308;
        --error: #ef4444;
        --radius: 8px;
        --radius-lg: 12px;
        --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        --shadow-purple: 0 4px 14px 0 rgba(139, 92, 246, 0.39);
    }
    
    /* Global Dark Theme */
    .stApp {
        background: var(--bg-primary);
        color: var(--text-primary);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        min-height: 100vh;
    }
    
    /* Main Container */
    .main .block-container {
        padding: 2rem 1rem;
        max-width: 1000px;
        background: var(--bg-primary);
    }
    
    /* Card Components */
    div[data-testid="stVerticalBlock"] {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: var(--shadow-lg);
        transition: all 0.3s ease;
    }
    
    div[data-testid="stVerticalBlock"]:hover {
        border-color: var(--primary-purple);
        box-shadow: var(--shadow-purple);
        transform: translateY(-2px);
    }
    
    /* Typography */
    h1 {
        color: var(--text-primary) !important;
        font-weight: 800 !important;
        font-size: 3rem !important;
        text-align: left;
        margin-bottom: 0.5rem !important;
        line-height: 1.1;
    }
    
    .app-subtitle {
        color: var(--text-secondary) !important;
        font-size: 1.25rem !important;
        font-weight: 400 !important;
        margin-bottom: 3rem !important;
        line-height: 1.5;
    }
    
    h2, h3 {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
    }
    
    h3 {
        font-size: 1.5rem !important;
    }
    
    p, div, label, span {
        color: var(--text-secondary) !important;
        font-weight: 400 !important;
        line-height: 1.6;
    }
    
    /* File Uploader - Nektic Style */
    .stFileUploader {
        margin: 2rem 0;
    }
    
    .stFileUploader > label {
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        font-size: 1.1rem !important;
        margin-bottom: 1rem !important;
        display: block;
    }
    
    .stFileUploader div[data-testid="stFileDropzone"] {
        background: var(--bg-input);
        border: 2px dashed var(--border-input);
        border-radius: var(--radius-lg);
        padding: 3rem 2rem;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
    }
    
    .stFileUploader div[data-testid="stFileDropzone"]:hover {
        border-color: var(--primary-purple);
        background: var(--primary-purple-light);
    }
    
    .stFileUploader div[data-testid="stFileDropzone"] * {
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
    }
    
    .stFileUploader button {
        background: var(--primary-purple) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius) !important;
        padding: 0.75rem 1.5rem !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stFileUploader button:hover {
        background: var(--primary-purple-hover) !important;
        transform: translateY(-1px) !important;
        box-shadow: var(--shadow-purple) !important;
    }
    
    /* Number Input - Nektic Style */
    .stNumberInput > label {
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        font-size: 0.875rem !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem !important;
    }
    
    .stNumberInput input {
        background: var(--bg-input) !important;
        border: 1px solid var(--border-input) !important;
        border-radius: var(--radius) !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        color: var(--text-primary) !important;
        transition: all 0.2s ease !important;
    }
    
    .stNumberInput input:focus {
        border-color: var(--primary-purple) !important;
        box-shadow: 0 0 0 3px var(--primary-purple-light) !important;
        outline: none !important;
    }
    
    /* Button Styling - Nektic CTA Style */
    .stButton > button {
        background: var(--primary-purple) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius) !important;
        padding: 0.875rem 2rem !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        transition: all 0.2s ease !important;
        box-shadow: var(--shadow-md) !important;
        width: 100% !important;
        height: 48px !important;
    }
    
    .stButton > button:hover {
        background: var(--primary-purple-hover) !important;
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-purple) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
    }
    
    /* Image Container */
    .image-container {
        background: var(--bg-secondary);
        border: 1px solid var(--border-color);
        border-radius: var(--radius-lg);
        padding: 1.5rem;
        margin: 2rem 0;
        text-align: center;
    }
    
    /* Color Result Card - Success Style */
    .color-result {
        background: linear-gradient(135deg, var(--success), #16a34a);
        color: white;
        padding: 2rem;
        border-radius: var(--radius-lg);
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 4px 14px 0 rgba(34, 197, 94, 0.39);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .color-result h3 {
        color: white !important;
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }
    
    .color-result p {
        color: rgba(255, 255, 255, 0.9) !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        margin: 0.5rem 0 !important;
    }
    
    /* Color Display - Circular with Nektic styling */
    .color-display {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        margin: 1.5rem auto;
        border: 4px solid var(--border-color);
        box-shadow: var(--shadow-lg);
        transition: all 0.3s ease;
        position: relative;
    }
    
    .color-display:hover {
        transform: scale(1.1);
        border-color: var(--primary-purple);
        box-shadow: var(--shadow-purple);
    }
    
    .color-display::after {
        content: '';
        position: absolute;
        inset: -2px;
        border-radius: 50%;
        padding: 2px;
        background: linear-gradient(45deg, var(--primary-purple), var(--accent-orange));
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .color-display:hover::after {
        opacity: 1;
    }
    
    /* Info Messages - Nektic Style */
    .stInfo {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--primary-purple) !important;
        border-radius: var(--radius) !important;
        padding: 1rem 1.5rem !important;
        color: var(--text-primary) !important;
    }
    
    .stInfo [data-testid="stMarkdownContainer"] p {
        color: var(--text-primary) !important;
        margin: 0 !important;
    }
    
    .stWarning {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--warning) !important;
        border-radius: var(--radius) !important;
        padding: 1rem 1.5rem !important;
        color: var(--text-primary) !important;
    }
    
    .stWarning [data-testid="stMarkdownContainer"] p {
        color: var(--text-primary) !important;
        margin: 0 !important;
    }
    
    /* Coordinate Grid */
    .coordinate-grid {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 2rem 0;
        border-top: 1px solid var(--border-color);
        color: var(--text-muted);
        font-size: 0.875rem;
    }
    
    /* Custom Speak Button */
    .nektic-speak-btn {
        background: linear-gradient(135deg, var(--accent-orange), #ea580c) !important;
        color: white !important;
        border: none !important;
        border-radius: var(--radius) !important;
        padding: 12px 24px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 14px 0 rgba(249, 115, 22, 0.39) !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 8px !important;
    }
    
    .nektic-speak-btn:hover {
        background: linear-gradient(135deg, #ea580c, #dc2626) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(249, 115, 22, 0.5) !important;
    }
    
    .nektic-speak-btn:active {
        transform: translateY(0) !important;
    }
    
    /* Version Badge */
    .version-badge {
        background: var(--primary-purple-light);
        color: var(--primary-purple);
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: inline-block;
        margin-bottom: 1rem;
    }
    
    /* Component Tags */
    .component-tags {
        display: flex;
        gap: 0.5rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    
    .component-tag {
        background: var(--bg-secondary);
        color: var(--text-secondary);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 500;
        border: 1px solid var(--border-color);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .component-tag.active {
        background: var(--primary-purple);
        color: white;
        border-color: var(--primary-purple);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem 0.5rem;
        }
        
        div[data-testid="stVerticalBlock"] {
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        h1 {
            font-size: 2.5rem !important;
        }
        
        .coordinate-grid {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page settings
st.set_page_config(
    page_title="AI Color Recognizer", 
    layout="centered",
    page_icon="🎨",
    initial_sidebar_state="collapsed"
)

# Header with Nektic styling
st.markdown("""
<div class="version-badge">v1.0</div>
<h1>AI Color Recognizer</h1>
<p class="app-subtitle">Advanced color recognition powered by AI technology. Upload images and discover precise color information with professional-grade accuracy.</p>

<div class="component-tags">
    <span class="component-tag active">Color Recognition</span>
    <span class="component-tag">Image Processing</span>
    <span class="component-tag">AI Analysis</span>
    <span class="component-tag">+ 3 more features</span>
</div>
""", unsafe_allow_html=True)

# Load color dataset
@st.cache_data
def load_colors():
    try:
        return pd.read_csv("cleaned_color.csv")
    except FileNotFoundError:
        # Create a comprehensive color dataset if file doesn't exist
        colors_data = {
            'color_name': [
                'Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown',
                'Black', 'White', 'Gray', 'Cyan', 'Magenta', 'Lime', 'Navy', 'Maroon',
                'Olive', 'Teal', 'Silver', 'Gold', 'Indigo', 'Violet', 'Turquoise',
                'Coral', 'Salmon', 'Khaki', 'Plum', 'Orchid', 'Tan', 'Beige',
                'Crimson', 'Forest Green', 'Royal Blue', 'Amber', 'Lavender'
            ],
            'r': [
                255, 0, 0, 255, 255, 128, 255, 165, 0, 255, 128, 0, 255, 0, 0, 128,
                128, 0, 192, 255, 75, 238, 64, 255, 250, 240, 221, 218, 210, 245,
                220, 34, 65, 255, 230
            ],
            'g': [
                0, 255, 0, 255, 165, 0, 192, 42, 0, 255, 128, 255, 0, 255, 0, 0,
                128, 128, 192, 215, 0, 130, 224, 127, 128, 230, 160, 112, 180, 245,
                20, 139, 105, 191, 230
            ],
            'b': [
                0, 0, 255, 0, 0, 128, 203, 42, 0, 255, 128, 255, 255, 0, 128, 0,
                0, 128, 192, 0, 130, 238, 208, 80, 114, 140, 221, 214, 140, 220,
                60, 34, 225, 0, 250
            ]
        }
        return pd.DataFrame(colors_data)

colors = load_colors()

# Color matching function
def get_color_name(R, G, B):
    min_diff = float('inf')
    cname = ""
    for i in range(len(colors)):
        r_c, g_c, b_c = colors.loc[i, ["r", "g", "b"]]
        d = ((R - r_c) ** 2 + (G - g_c) ** 2 + (B - b_c) ** 2) ** 0.5
        if d < min_diff:
            min_diff = d
            cname = colors.loc[i, "color_name"]
    return cname

# Main application
with st.container():
    # Upload section
    st.markdown("""
    ### 📤 Upload Image
    Select an image file to begin color analysis. Our AI will process your image and provide accurate color identification.
    """)
    
    uploaded_file = st.file_uploader(
        "Choose an image file", 
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, JPEG, PNG • Max size: 200MB"
    )

if uploaded_file:
    # Process image
    img = Image.open(uploaded_file)
    
    # Resize image if needed
    max_width = 600
    if img.width > max_width:
        scale = max_width / img.width
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size)

    img_array = np.array(img)
    
    # Display image
    st.markdown("""
    <div class="image-container">
        <h3>📷 Uploaded Image</h3>
        <p>Use the coordinate inputs below to analyze specific points in your image</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.image(img, use_column_width=True)
    
    # Coordinate input section with Nektic styling
    st.markdown("""
    ### 🎯 Coordinate Selection
    Enter precise X and Y coordinates to analyze the color at that specific pixel location.
    """)
    
    # Image dimensions info
    st.info(f"📏 Image Dimensions: **{img.width} × {img.height}** pixels")
    
    # Coordinate inputs in grid layout
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        x = st.number_input(
            "X Coordinate", 
            min_value=0, 
            max_value=img.width-1, 
            value=img.width//2,
            help="Horizontal position (0 to image width)"
        )
    
    with col2:
        y = st.number_input(
            "Y Coordinate", 
            min_value=0, 
            max_value=img.height-1, 
            value=img.height//2,
            help="Vertical position (0 to image height)"
        )
    
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)  # Spacing
        analyze_button = st.button("🔍 Analyze Color", use_container_width=True)

    if analyze_button or (x is not None and y is not None):
        if y < img_array.shape[0] and x < img_array.shape[1]:
            pixel = img_array[y, x]
            r, g, b = pixel[:3]
            cname = get_color_name(r, g, b)

            # Display results with Nektic styling
            st.markdown(f"""
            <div class="color-result">
                <h3>🎯 Color Identified: {cname}</h3>
                <p><strong>RGB Values:</strong> ({r}, {g}, {b})</p>
                <p><strong>HEX Code:</strong> #{r:02x}{g:02x}{b:02x}</p>
                <p><strong>Coordinates:</strong> ({x}, {y})</p>
            </div>
            """, unsafe_allow_html=True)

            # Color display with enhanced styling
            st.markdown(f"""
            <div style="text-align: center; margin: 2rem 0;">
                <div class="color-display" style="background-color: rgb({r},{g},{b});"></div>
                <p style="color: var(--text-secondary); font-size: 0.875rem; margin-top: 1rem;">
                    Color Preview • Click to interact
                </p>
            </div>
            """, unsafe_allow_html=True)

            # Enhanced speak button with Nektic styling
            components.html(f"""
            <div style="text-align: center; margin: 2rem 0;">
                <button class="nektic-speak-btn" onclick="speakColor()">
                    🔊 Speak Color
                </button>
            </div>
            <script>
            function speakColor() {{
                const msg = new SpeechSynthesisUtterance("{cname}");
                msg.lang = "en-US";
                msg.pitch = 1.1;
                msg.rate = 0.9;
                msg.volume = 0.8;
                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(msg);
                
                // Visual feedback
                const button = document.querySelector('.nektic-speak-btn');
                const originalText = button.innerHTML;
                button.innerHTML = '🔊 Speaking...';
                button.style.transform = 'scale(0.95)';
                
                setTimeout(() => {{
                    button.innerHTML = originalText;
                    button.style.transform = 'scale(1)';
                }}, 1500);
            }}
            </script>
            """, height=120)

            # Additional color information
            st.markdown(f"""
            ### 📊 Color Analysis
            
            **Color Properties:**
            - **Name:** {cname}
            - **RGB:** ({r}, {g}, {b})
            - **HEX:** #{r:02x}{g:02x}{b:02x}
            - **Brightness:** {int((r + g + b) / 3)}
            - **Coordinates:** ({x}, {y})
            
            **Technical Details:**
            - **Red Channel:** {r}/255 ({r/255:.2%})
            - **Green Channel:** {g}/255 ({g/255:.2%})
            - **Blue Channel:** {b}/255 ({b/255:.2%})
            """)

        else:
            st.warning("🎯 Coordinates are outside image boundaries. Please enter valid coordinates.")

# Footer with Nektic styling
st.markdown("""
<div class="footer">
    <p><strong>AI Color Recognizer</strong> • Built with Streamlit</p>
    <p>Advanced color recognition technology • Professional-grade accuracy</p>
</div>
""", unsafe_allow_html=True)
