# 🌸 BlushAI — Your Intelligent Document Assistant

**Upload documents. Ask questions. Discover insights.**

BlushAI is a Streamlit app that lets you upload a document, index it, and ask questions about it using Retrieval-Augmented Generation (RAG). Answers come only from your document, with the retrieved sources shown for transparency.

## Features

- **Four document formats:** PDF, CSV, XML and DOCX. Everything else (TXT, JSON, XLSX, PPTX, images…) is rejected.
- **Real validation:** file extension, size (max 25 MB) and file signature are checked before processing. Empty, corrupted, malformed or unreadable files produce friendly messages.
- **API key screen:** the app starts on a welcome screen. The dashboard only appears after your OpenAI key is verified with a tiny real request. Disconnect any time to clear the key from the session.
- **Format-aware parsing:**
  - PDF: page numbers preserved.
  - CSV: column names and row numbers preserved.
  - XML: element paths, attributes and text extracted.
  - DOCX: headings, paragraphs and tables extracted.
- **Cited answers:** answers cite the page, row range or section they came from, and the retrieved chunks are listed under each answer.
- **Honest progress:** the processing steps shown (validate, extract, split, embed and index) match what the app actually does.
- **Session chat history** with a "Clear chat" button that keeps the processed document.
- **Baby-pink UI** with light animations, a responsive layout, and support for reduced-motion settings.

## Project structure

```
your-project/
├── rag.py               # Main app: screens, sidebar, RAG pipeline (run this)
├── loaders.py           # File validation and PDF/CSV/XML/DOCX parsing
├── styles.py            # Theme, CSS, animations and HTML helpers
├── requirements.txt     # Python dependencies
└── .streamlit/
    └── config.toml      # Theme colors and 25 MB upload limit
```

## Getting started

### 1. Requirements

- Python 3.10 or newer
- An [OpenAI API key](https://platform.openai.com/api-keys) with access to embeddings and a chat model

### 2. Install

```bash
pip install -r requirements.txt
```

### 3. Run

```bash
streamlit run rag.py
```

Open the address shown in the terminal (usually http://localhost:8501).

### 4. Use it

1. Paste your OpenAI API key and click **Connect & Continue**.
2. Upload a PDF, CSV, XML or DOCX file.
3. Click **Process Document** and wait for "Document ready".
4. Type a question under **Ask Your Document** and press Enter or click **Ask AI**.

> Optional: if the `OPENAI_API_KEY` environment variable is set, leave the key field empty on the welcome screen to use it.

## Settings (sidebar)

| Setting | Default | Notes |
|---|---|---|
| Chat model | `gpt-4o-mini` | Also: `gpt-4o`, `gpt-4.1-mini` |
| Chunk size | 1000 | Must be greater than 0 |
| Chunk overlap | 150 | Must be 0 or more and smaller than chunk size |
| Retrieved chunks (k) | 4 | Number of chunks sent to the model per question |

Chunk settings take effect the next time you click **Process Document**. Model and k apply immediately.

## How it works

```
Upload → Validate → Extract (loaders.py) → Split into chunks
       → Embed (text-embedding-3-small) → FAISS index
Question → Retrieve top-k chunks → Prompt + chat model → Cited answer
```

The index lives in the browser session's memory, so it is cleared when you disconnect or close the session. Re-processing is skipped when the same file and settings are processed again.

## Security notes

- The API key is kept only in Streamlit session state and is never written to disk.
- Logs redact anything that looks like a key, and error messages shown to users never include stack traces or secrets.
- XML is parsed with `defusedxml`, which blocks external entities and entity-expansion attacks.
- Uploaded file names are HTML-escaped before display.

## Limitations

- Scanned or image-only PDFs aren't supported because there is no OCR.
- Word files have no reliable page numbers, so DOCX and XML answers cite sections. CSV answers cite row ranges.
- CSV files are assumed to have their header in the first row.
- Legacy `.doc` files aren't supported, only `.docx`.
- A document that creates more than 5,000 chunks is rejected. Increase the chunk size or upload a smaller file.
- Each question is answered independently. Earlier chat turns are shown on screen but aren't sent to the model.
- Only OpenAI is supported as the provider.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: loaders` or `styles` | Keep `rag.py`, `loaders.py` and `styles.py` in the same folder and run from that folder |
| "Your API key was rejected" | Check the key, or create a new one |
| "Out of credit or quota" | Add billing credit to your OpenAI account |
| Pink theme not applied | Make sure the folder is named `.streamlit` (with the dot) and sits next to `rag.py` |
| Text hard to read | Hard-refresh the page (Ctrl+F5) after replacing `styles.py` |

## Tech stack

Streamlit · LangChain · OpenAI · FAISS · pypdf · python-docx · defusedxml
