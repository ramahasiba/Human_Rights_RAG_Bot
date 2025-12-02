# 🧠 Human Rights Information Assistant

A Retrieval-Augmented Generation (RAG) web application that allows users to explore, search, and understand international human-rights documents using AI-powered semantic search and GPT-4o-mini.

## 📄 Overview

This application makes complex human-rights treaties, conventions, and declarations easier to access and understand.
It uses web-scraped documents from the Human Rights Library, stores them in a **vector database**, and answers user questions by retrieving relevant text and generating clear English explanations.

The system supports **English only** (current version).

---

## 🎥 Demo

▶️ **Video Demo:** [https://youtu.be/QGbVrpP1vGo](https://youtu.be/QGbVrpP1vGo)

📑 **Presentation Deck:**
[https://docs.google.com/presentation/d/1NVAxctJnB2ULwqxYxFRcY2fCzEm-JOt523BWnorggCk/edit?usp=sharing](https://docs.google.com/presentation/d/1NVAxctJnB2ULwqxYxFRcY2fCzEm-JOt523BWnorggCk/edit?usp=sharing)

---

## 🚀 Features

* Natural-language Q&A about human-rights conventions
* RAG architecture (retrieves real document sources before answering)
* Transparent responses including citations + source text
* Fast semantic search using vector embeddings
* Clean Gradio web interface
* Works entirely in English
* Lightweight, runs in Colab or any local environment

---

## 🧠 Tech Stack

### **AI & NLP**

* **OpenAI GPT-4o-mini** — LLM for reasoning + answer generation
* **OpenAI/Embeddings** — vector representation of documents
* **RAG Pipeline** — retrieval + LLM response generation

### **Data & Retrieval**
 
* **ChromaDB** — vector store for document embeddings
* **Recursive text splitter** — chunks text for better retrieval

### **Frameworks & Tools**

* **LangChain** — retrieval + orchestration 
* **Gradio** — user interface

### **Deployment**

* Runs in **Google Colab / local machine**
* No backend server required for the MVP

--- 
---

## 🏁 How It Works

1. Scraper collects documents from the Human Rights Library
2. Text is cleaned, split, and embedded
3. Embeddings stored in ChromaDB
4. User submits a question in Gradio
5. System retrieves most similar chunks
6. GPT-4o-mini generates an answer grounded in retrieved content

---

## 📌 Limitations

* English only
* Dataset limited to the Human Rights Library (current version)
* Not intended to replace legal expertise
 
