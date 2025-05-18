# CareerLens - An AI-powered Resume Analyzer and Interview Coach

## Overview 
CareerLens is a Streamlit-based web application that acts as an interview coach providing guidance in 
various aspects pertaining to interview preparation. The application is powered by models provided by Groq.

## Key Features
- **Resume Analysis**: Gain in-depth insights about your resume, highlighting overall impact and areas of improvement.
- **Chat with the Coach**: AI coach that can help you prepare for your interviews (technical, behavioral or general) and suggest ways you can improve upon your skills for the job role that you provide.

## How It Works 
1. Obtain your Groq API key from [Groq's website](https://groq.com/)
2. Enter your API key credentials in the app
3. Upon validation, the application opens up the main page. This contains a sidebar for resume analysis and the hero section is a chat interface where you can interact with the AI coach.
4. Upload your resume (PDF format) and specify the job role you're applying for
5. Get instant analysis and personalized interview preparation assistance

## Technologies Used 
- **Streamlit**: For the web interface
- **PyPDF2**: For parsing PDF resumes
- **Groq API**: For AI-powered analysis and chat capabilities
- **LangChain**: For handling conversation context

## Installation

### Prerequisites
Ensure you have Python 3.10+ installed on your machine. You can download it from the [official Python website](https://www.python.org/).

The application was built using [uv](https://docs.astral.sh/uv/) for dependency management.

### Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/CareerLens.git
cd CareerLens
```

### Install Dependencies

Using uv:
```bash
uv init .
uv add langchain-groq streamlit groq pypdf2
```

### Set Up Environment Variables

Create a `.env` file in the project root directory:
```
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL provided in the terminal (typically http://localhost:8501)

3. Enter your Groq API key if not set in the environment variables

4. Upload your resume PDF and enter the job role you're targeting

5. Click "Analyze Resume" to get insights

6. Use the chat interface to ask questions and prepare for your interview

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to Groq for providing the AI backend
- Streamlit for the wonderful web app framework
