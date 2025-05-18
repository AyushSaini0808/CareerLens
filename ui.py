css_setup='''<style>
        .main {
            background-color: #f5f7fa;
        }
        div[data-testid="InputInstructions"] > span:nth-child(1) {
            visibility: hidden;
        }
        [data-testid="stBaseButton-secondary"]:hover{
            background-color:#554FDD;
            color:#FFFFFF;
            border:2px blue;
        }
        .stAppViewContainer{
            background-image: radial-gradient(circle, #ffffff, #eaecf5, #cfdbeb, #b0cce0, #8dbed0);
        }
        [data-testid="stHeader"]{
            background-color:rgba(0,0,0,0);
        }
        .stButton>button {
            background-color: #4F8BF9;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1.5em;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 2px solid #4F8BF9;
        }
        .stHeading>div>div>h1{
            font-size:3em;
            font-weight: bold;
            color: #294D5A
            
        }
</style>'''