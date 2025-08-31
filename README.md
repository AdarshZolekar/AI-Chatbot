## AI Chatbot with Hugging Face and Streamlit

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Yes-green.svg)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-API-orange.svg)](https://huggingface.co/)

A simple chatbot built using **Streamlit** and the **Hugging Face Inference API**.  
The chatbot uses the **Mistral-7B-Instruct-v0.2** model for conversational AI.

---

## Features

- Conversational AI powered by Hugging Face LLM  
- Clean and intuitive **Streamlit** interface  
- Direct API requests to Hugging Face's free server  

---

## Getting Started

### 1. Prerequisites

- Python 3.9+  
- pip  
- Hugging Face API token ([get it here](https://huggingface.co/settings/tokens))  

---

### 2. Installation

Clone the repository:

```bash
git clone https://github.com/AdarshZolekar/AI-Chatbot.git
cd AI-Chatbot
```

Install dependencies:

```
pip install Requirements.txt
```

### 3. Environment Setup

Create a .env file in the project root:

```
HUGGINGFACE_API_TOKEN=your_token_here
```

### 4. Run the App

```
streamlit run AI-Chatbot.py
```

---

## Deployment

Deploy on Streamlit Cloud:

1. Push your code to GitHub.

2. Connect the repo to Streamlit Cloud.

3. Add HUGGINGFACE_API_TOKEN in App Secrets.

---

## Limitations

- Responses depend on Hugging Face’s free API quota.

- Latency may be high.

---

## Contributing

Contributions are welcome! Fork the repo, make changes and submit a PR.

---

<p align="center">
  <a href="#top">
    <img src="https://img.shields.io/badge/%E2%AC%86-Back%20to%20Top-blue?style=for-the-badge" alt="Back to Top"/>
  </a>
</p>
