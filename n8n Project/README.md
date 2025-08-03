# 📝 Feedback Analyzer (Multi-Agent System in n8n)

An intelligent multi-agent feedback analysis pipeline built using **n8n**, **OpenAI**, and **Google Sheets**. This system automatically processes customer/student feedback, detects sentiment, highlights problems, and alerts support if needed.

## 📌 Description

The **Feedback Analyzer** is designed to:
- Collect user feedback via Google Forms
- Perform **sentiment analysis** using OpenAI (GPT-4)
- Extract and summarize **key issues** from negative feedback
- Detect **critical problems**
- Automatically log results and send alerts when needed

---

## 🛠 Tools Used

- [n8n](https://n8n.io) – Automation and workflow orchestration
- [Google Forms](https://www.google.com/forms/about/) – For collecting feedback
- [Google Sheets](https://www.google.com/sheets/about/) – For logging results
- [OpenAI GPT-4](https://openai.com/) – For sentiment & issue analysis
- Gmail – For critical feedback alerts

---

## ⚙️ System Workflows

### `01 - Feedback Trigger Dispatcher`
Receives webhook input when a new Google Form response is submitted. Passes the feedback to the next agent in the pipeline.

### `02 - Sentiment Analysis Agent`
- Classifies feedback as `Positive`, `Neutral`, or `Negative` using GPT-4
- Updates Google Sheets with sentiment
- If **Negative**, triggers the next workflow

### `03 - Problem Extraction`
- Uses GPT-4 to extract clear, bullet-pointed **problems** from the feedback
- Sends them to the reporting workflow

### `04 - Criticality Reporting`
- Determines if any extracted problem is **critical**
- Sends email alerts for critical issues
- Logs everything to Google Sheets

---

## 🔁 Flow Summary

```plaintext
Google Form ➜ Webhook (n8n) ➜ Sentiment Agent ➜ Problem Analyzer ➜ Criticality Detector ➜ Sheets + Email Alert
