from utils import extract_text
from comparator import compare_documents
from summarizer import summarize_diff
import os

def main():
    file1 = "sample_docs/version1.docx"
    file2 = "sample_docs/version2.docx"

    print("🔍 Checking file paths...")
    print("file1:", os.path.abspath(file1))
    print("Exists:", os.path.exists(file1))
    print("file2:", os.path.abspath(file2))
    print("Exists:", os.path.exists(file2))

    if not os.path.exists(file1) or not os.path.exists(file2):
        print("❌ One or both files are missing. Exiting.")
        return

    print("🔍 Comparing documents...")
    # Pass file paths directly to compare_documents
    diff = compare_documents(file1, file2)
    print("\n📝 DIFF OUTPUT:\n")
    print(diff)

    print("\n🤖 Summarizing with GPT...")
    summary = summarize_diff(diff)
    print("\n🧠 GPT SUMMARY OF CHANGES:\n")
    print(summary)

    with open("output_summary.txt", "w", encoding="utf-8") as f:
        f.write("📝 DIFF OUTPUT:\n")
        f.write(diff)
        f.write("\n\n🧠 GPT SUMMARY OF CHANGES:\n")
        f.write(summary)
    print("\n✅ Output written to output_summary.txt")

if __name__ == "__main__":
    main()