import difflib

def compare_texts(text1, text2):
    diff = difflib.unified_diff(
        text1.splitlines(),
        text2.splitlines(),
        lineterm='',
        fromfile="Version 1",
        tofile="Version 2"
    )
    return "\n".join(diff)
