from crewai import Task
from agents import profile_analyzer, niche_researcher, gig_writer

def get_tasks(profile_text):
    # Task 1: Analyze the profile
    task1 = Task(
        agent=profile_analyzer,
        description=f"Analyze this freelancer profile: '''{profile_text}'''. "
                    "Identify strengths, weaknesses, skills, experience level, and writing tone. "
                    "Return a detailed analysis in bullet points covering: "
                    "- Key skills and expertise areas "
                    "- Experience level and credentials "
                    "- Strengths that can be leveraged "
                    "- Areas for improvement "
                    "- Overall profile tone and presentation",
        expected_output="Comprehensive profile analysis in bullet points with actionable insights"
    )

    # Task 2: Research niches based on profile analysis
    task2 = Task(
        agent=niche_researcher,
        description="Based on the profile analysis from the previous task, "
                    "research and suggest 3-5 profitable freelance niches that match the freelancer's skills. "
                    "For each niche, provide: "
                    "- Niche name and description "
                    "- Why it's a good fit for this freelancer "
                    "- Market demand and earning potential "
                    "- Competition level "
                    "Then select the BEST niche and explain why it's the top choice.",
        expected_output="List of 3-5 niche suggestions with analysis, plus the best niche selection with rationale",
        context=[task1]  # This task depends on task1 output
    )

    # Task 3: Create gig based on selected niche
    task3 = Task(
        agent=gig_writer,
        description="Using the profile analysis and the selected best niche from previous tasks, "
                    "create a complete, professional Fiverr/Upwork gig listing that includes: "
                    "- Compelling gig title (under 80 characters) "
                    "- Short description (under 120 characters) "
                    "- Detailed long description (engaging and conversion-focused) "
                    "- Relevant SEO tags (8-10 tags) "
                    "- Three pricing tiers (Basic, Standard, Premium) with clear deliverables "
                    "Make it professional, engaging, and optimized for the selected niche.",
        expected_output="Complete gig listing with title, descriptions, tags, and pricing tiers",
        context=[task1, task2]  # This task depends on both previous tasks
    )

    return [task1, task2, task3]