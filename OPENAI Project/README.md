# 🧠 DocDiff AI – Document Comparator with GPT Summary

**DocDiff AI** is a smart tool to compare two `.docx` or `.txt` files and automatically generate:
- A unified line-by-line **diff**
- A natural language **AI summary** of the changes (via GPT-4)

Ideal for writers, editors, developers, and researchers who need to track document revisions clearly and concisely.

---

## 📂 Folder Structure

document_comparator/
├── main.py # Main entry point
├── utils.py # Utility functions
├── comparator.py # Diff generator logic
├── summarizer.py # GPT-powered summarization
├── generate_sample_docx.py # Optional script to generate sample .docx files
├── sample_docs/
│ ├── version1.docx
│ └── version2.docx
---

## ▶️ How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

2. Set your OpenAI API key (temporary session)
    $env:OPENAI_API_KEY="sk-..."    # Windows PowerShell
    export OPENAI_API_KEY="sk-..."  # macOS/Linux

3. (Optional) Generate sample documents
Instead of manually writing .docx files, you can auto-generate two versions for testing:
    python generate_sample_docx.py

4. Run the comparator    
    python main.py

5. Check the results
    . output_summary.txt – AI summary of changes
    . diff_output.txt – Line-by-line raw diff

To run Gradio UIs
    . python app.py

💡 Example Use Case
Two document versions:

. Version 1 describes "basic text comparison"

. Version 2 introduces "support for DOCX and richer formatting"

DocDiff AI will:

. Highlight modified lines

. Summarize: “Added support for DOCX file types and improved formatting.”

🛠 Powered By
. python-docx – Word document parsing

. difflib – Unified diff generation

. OpenAI GPT-4 – AI summarization

. Standard Python libraries

📌 Notes
. Requires OpenAI GPT API access.

. Works with both .docx and .txt files.

. Designed for simplicity and extensibility.
