import difflib
from docx import Document

def read_file(file_path):
    if file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

def compare_documents(file1_path, file2_path):
    text1 = read_file(file1_path)
    text2 = read_file(file2_path)

    diff = difflib.unified_diff(
        text1.splitlines(),
        text2.splitlines(),
        fromfile="Version 1",
        tofile="Version 2",
        lineterm=''
    )
    return "\n".join(diff)
