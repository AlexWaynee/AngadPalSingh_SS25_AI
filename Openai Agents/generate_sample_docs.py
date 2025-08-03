from docx import Document
import os

os.makedirs("sample_docs", exist_ok=True)

def create_doc(filename, content):
    print(f"📝 Writing to {filename}...")
    doc = Document()
    for line in content.strip().split("\n"):
        doc.add_paragraph(line.strip())
    doc.save(filename)
    print(f"✅ Saved: {filename}")

content_v1 = """
Project Report – AI Document Comparator

This project is aimed at comparing two text-based documents and identifying changes.

The tool helps editors and reviewers keep track of revisions between versions.

The current version supports only plain text and basic formatting.
"""

content_v2 = """
Project Report – DocDiff AI

This project is designed to compare DOCX and TXT documents and highlight all textual changes.

It assists writers, editors, and reviewers in efficiently identifying differences.

The tool now supports both plain text and DOCX files, including basic formatting.
"""

create_doc("sample_docs/version1.docx", content_v1)
create_doc("sample_docs/version2.docx", content_v2)
