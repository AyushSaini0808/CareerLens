css_setup = '''
<style>
    /* Main container styling */
    .main {
        background-color: #f5f7fa;
    }
    
    /* App container with gradient background */
    .stAppViewContainer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    /* Content area with glass morphism effect */
    .block-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Header styling */
    [data-testid="stHeader"] {
        background-color: rgba(0, 0, 0, 0);
    }
    
    /* Hide file uploader instructions */
    div[data-testid="InputInstructions"] > span:nth-child(1) {
        visibility: hidden;
    }
    
    /* Main heading styling */
    .stHeading h1 {
        font-size: 3.5em !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    /* Subheadings */
    .stHeading h2 {
        color: #2d3748;
        font-weight: 700;
        margin-top: 1.5rem;
    }
    
    .stHeading h3 {
        color: #4a5568;
        font-weight: 600;
    }
    
    /* Primary button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 12px;
        padding: 0.75em 2em;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.9em;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Secondary button styling */
    [data-testid="stBaseButton-secondary"] {
        background-color: #f7fafc;
        color: #667eea;
        border: 2px solid #667eea;
        border-radius: 12px;
        padding: 0.6em 1.5em;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    [data-testid="stBaseButton-secondary"]:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: transparent;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 0.75em 1em;
        font-size: 1em;
        transition: all 0.3s ease;
        background-color: #ffffff;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        outline: none;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* File uploader styling */
    [data-testid="stFileUploader"] {
        background-color: #f7fafc;
        border: 2px dashed #cbd5e0;
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #667eea;
        background-color: #edf2f7;
    }
    
    /* Chat message styling */
    [data-testid="stChatMessage"] {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    [data-testid="stChatMessage"]:hover {
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    
    /* AI message specific styling */
    [data-testid="stChatMessage"][data-testid*="assistant"] {
        background: linear-gradient(135deg, #f0f4ff 0%, #e9f0ff 100%);
        border-left: 4px solid #667eea;
    }
    
    /* User message specific styling */
    [data-testid="stChatMessage"][data-testid*="user"] {
        background: linear-gradient(135deg, #fef5ff 0%, #f3e8ff 100%);
        border-left: 4px solid #764ba2;
    }
    
    /* Chat input styling */
    [data-testid="stChatInput"] {
        border-radius: 15px;
        border: 2px solid #e2e8f0;
        background-color: #ffffff;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    
    [data-testid="stChatInput"]:focus-within {
        border-color: #667eea;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.2);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #ffffff;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
    }
    
    /* Sidebar widgets */
    [data-testid="stSidebar"] .stTextInput > div > div > input,
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        border: none;
    }
    
    /* Expander styling */
    [data-testid="stExpander"] {
        background-color: #ffffff;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    /* Info, success, warning, error boxes */
    .stAlert {
        border-radius: 12px;
        border: none;
        padding: 1rem 1.5rem;
        margin: 1rem 0;
    }
    
    /* Success message */
    [data-testid="stAlert"][data-baseweb="notification"] {
        background-color: #f0fdf4;
        border-left: 4px solid #22c55e;
    }
    
    /* Info message */
    .stInfo {
        background-color: #eff6ff;
        border-left: 4px solid #3b82f6;
        border-radius: 12px;
        padding: 1rem 1.5rem;
    }
    
    /* Error message */
    .stError {
        background-color: #fef2f2;
        border-left: 4px solid #ef4444;
        border-radius: 12px;
        padding: 1rem 1.5rem;
    }
    
    /* Spinner styling */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Divider styling */
    hr {
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
    }
    
    /* Markdown content styling */
    .stMarkdown {
        font-size: 1.05em;
        line-height: 1.7;
        color: #2d3748;
    }
    
    /* Code blocks */
    code {
        background-color: #f7fafc;
        padding: 0.2em 0.4em;
        border-radius: 6px;
        font-size: 0.9em;
        color: #d63384;
    }
    
    pre {
        background-color: #2d3748;
        border-radius: 12px;
        padding: 1.5rem;
        overflow-x: auto;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Animation for elements */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .element-container {
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .stHeading h1 {
            font-size: 2.5em !important;
        }
        
        .block-container {
            padding: 1rem;
        }
    }
</style>
'''
