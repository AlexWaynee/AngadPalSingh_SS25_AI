import gradio as gr
from comparator import compare_documents
from summarizer import summarize_diff

def docdiff_ui(file1, file2):
    diff = compare_documents(file1.name, file2.name)
    summary = summarize_diff(diff)
    return diff, summary

gr.Interface(
    fn=docdiff_ui,
    inputs=[
        gr.File(label="Version 1 (.docx or .txt)"),
        gr.File(label="Version 2 (.docx or .txt)")
    ],
    outputs=[
        gr.Textbox(label="Line-by-line Diff"),
        gr.Textbox(label="AI Summary")
    ],
    title="DocDiff AI – Compare Docs with GPT",
    description="Upload two document versions to see the diff and AI summary."
).launch()
