# AI Financial Document Assistant

An AI-powered application that allows users to ask questions about financial PDF documents using **Retrieval-Augmented Generation (RAG)**.

## 🚀 Features

- Upload and process PDF documents.
- Extract text from financial documents.
- Generate embeddings using Sentence Transformers.
- Store and retrieve document information using FAISS vector search.
- Ask questions in natural language.
- Generate context-aware answers using Google Gemini.
- Interactive user interface built with Gradio.

## 🛠️ Technology Stack

- **Python**
- **RAG (Retrieval-Augmented Generation)**
- **Google Gemini API**
- **Sentence Transformers**
- **FAISS**
- **LangChain**
- **PyPDF**
- **Gradio**

## 🧠 How It Works

1. The PDF document is loaded and its text is extracted.
2. The extracted text is split into smaller chunks.
3. Each chunk is converted into numerical vectors called **embeddings**.
4. FAISS stores the embeddings and performs similarity search.
5. When a user asks a question, the most relevant document chunks are retrieved.
6. The retrieved context and user question are sent to Google Gemini.
7. Gemini generates a context-aware answer based on the document.

## 📂 Project Structure

```text
AI-Financial-Document-Assistant/
│
├── data/              # PDF documents
├── app.py             # Gradio application
├── chatbot.py         # RAG and Gemini question answering
├── ingest.py          # PDF processing and vector creation
├── models.py          # Model configuration
├── requirements.txt   # Project dependencies
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Naresh150805/AI-Financial-Document-Assistant.git
cd AI-Financial-Document-Assistant
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup

Create a `.env` file in the project folder:

```text
GOOGLE_API_KEY=your_api_key_here
```

**Never upload your `.env` file or API key to GitHub.**

## ▶️ Run the Project

First, process the PDF documents:

```bash
python ingest.py
```

Then run the application:

```bash
python app.py
```

## 🎯 Future Improvements

- Support multiple PDF uploads.
- Add chat history.
- Display source document references.
- Deploy the application online.
- Support additional document formats such as DOCX and TXT.