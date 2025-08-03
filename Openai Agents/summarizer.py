import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_diff(diff_text):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if needed
        messages=[
            {"role": "system", "content": "You are a helpful assistant who summarizes edits between two document versions."},
            {"role": "user", "content": f"Summarize the key differences in this unified diff:\n\n{diff_text}"}
        ],
        max_tokens=300,
        temperature=0.5
    )
    return response.choices[0].message.content.strip()