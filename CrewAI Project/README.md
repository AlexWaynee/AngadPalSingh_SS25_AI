# 🧠 Freelancer Gig Optimizer (CrewAI Multi-Agent Project)

A multi-agent AI tool that analyzes a freelancer's profile, suggests high-demand niches, and generates optimized Fiverr/Upwork gig listings — all fully automated using [CrewAI](https://docs.crewai.com).

---

## 🚀 What It Does

This project uses AI agents to help freelancers stand out in the competitive gig economy by:

1. **Analyzing their profile and skills**
2. **Researching profitable freelance niches**
3. **Generating a professional gig listing** with:
   - Title
   - Short and long description
   - SEO tags
   - Pricing tiers (Basic, Standard, Premium)

---

## 🤖 Agents Involved

### 1. Profile Analyzer
- Reviews the freelancer’s background and writing style.
- Identifies strengths and areas of improvement.

### 2. Niche Researcher
- Suggests 3–5 in-demand niches based on profile analysis.
- Explains why each niche is a good fit.

### 3. Gig Writer
- Generates a full Fiverr-style gig optimized for conversions.
- Includes descriptions, tags, and tiered pricing.

---

## 📄 Sample Input

```text
Hi, I'm a graphic designer with 5 years of experience in logo design, branding, and creating social media content.
I've worked with over 200 clients and enjoy creating minimal and modern designs.

📝 Sample Output (Excerpt)
Gig Title: Elevate Your Brand with Stunning Minimalist Logo & Branding Designs
Short Description: Transform your brand’s identity with professionally crafted logo and branding solutions.
Pricing: Basic ($50), Standard ($100), Premium ($200)
Tags: #LogoDesign #Branding #MinimalDesign ...

(Full gig is available in output.txt)

💻 How to Run

1. Clone the repo or download the project folder

git clone https://github.com/your-username/freelancer-gig-optimizer.git
cd freelancer-gig-optimizer

2. Set up virtual environment

python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt

3. Set your OpenAI API key

$env:OPENAI_API_KEY = "sk-your-key-here"

4. Run the app

python main.py

5. To run Gradio UIs
   
   . python app.py

📁 Project Structure

freelancer_gig_optimizer/
├── agents.py            # Agent definitions
├── tasks.py             # Task definitions
├── main.py              # Entry point for execution
├── output.txt           # Final gig output
├── README.md            # This file
└── requirements.txt     # Dependencies

✅ Dependencies
crewai

langchain

openai

Install with:

pip install -r requirements.txt

📌 Credits

Created as part of a CrewAI multi-agent Project.
Developed by Angad Pal Singh
