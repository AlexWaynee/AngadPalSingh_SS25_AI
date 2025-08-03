# 🧠 Freelancer Gig Optimizer (CrewAI Multi-Agent Project)

**Freelancer Gig Optimizer** is a multi-agent AI tool built using [CrewAI](https://github.com/joaomdmoura/crewAI) that helps freelancers thrive in the gig economy. The system analyzes a freelancer's profile, identifies high-demand niches, and automatically generates optimized Fiverr/Upwork gig listings — including SEO tags and tiered pricing.

---

## 🚀 What It Does

This project uses autonomous AI agents to assist freelancers in creating compelling and marketable gig listings by:

- Analyzing the freelancer’s profile and skills  
- Researching profitable freelance niches  
- Generating a complete, professional gig listing with:
  - 🎯 Title  
  - ✍️ Short and long descriptions  
  - 🔍 SEO tags  
  - 💰 Tiered pricing (Basic, Standard, Premium)  

---

## 🤖 Agents Involved

1. **Profile Analyzer**  
   - Reviews the freelancer’s background and writing style  
   - Identifies strengths and areas of improvement  

2. **Niche Researcher**  
   - Suggests 3–5 in-demand niches based on profile analysis  
   - Explains why each niche is a good fit  

3. **Gig Writer**  
   - Generates a Fiverr-style gig optimized for conversions  
   - Includes titles, descriptions, tags, and pricing tiers  

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

See full output in output.txt
```
💻 How to Run

1. Clone the repository
   git clone [https://github.com/your-username/freelancer-gig-optimizer.git](https://github.com/AlexWaynee/AngadPalSingh_SS25_AI.git)
   cd freelancer-gig-optimizer
   
2. Set up virtual environment
    python -m venv venv
    # Windows
      .\venv\Scripts\Activate
    # macOS/Linux
      source venv/bin/activate

3. Install dependencies
    pip install -r requirements.txt

4. Set your OpenAI API key
   # Windows (PowerShell)
    $env:OPENAI_API_KEY = "your-key-here"
   # macOS/Linux
    export OPENAI_API_KEY="your-key-here"

5. Run the app
    python main.py

📁 Project Structure
freelancer_gig_optimizer/
├── agents.py          # Agent definitions
├── tasks.py           # Task definitions
├── main.py            # Entry point
├── output.txt         # Generated gig output
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies

✅ Dependencies
  . crewai
  . langchain
  . openai

Install all with:
  pip install -r requirements.txt

📌 Credits
Created as part of a CrewAI Multi-Agent Project
Developed by Angad Pal Singh
