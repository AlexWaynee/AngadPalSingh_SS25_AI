from crewai import Task
from agents import profile_analyzer, niche_researcher, gig_writer

def get_tasks(profile_text, profile_analysis=None, selected_niche=None):
    task1 = Task(
        agent=profile_analyzer,
        description=f"Analyze this freelancer profile: '''{profile_text}'''. "
                    "Identify strengths, weaknesses, and tone issues. Return bullet points.",
        expected_output="Profile analysis in bullet points"
    )

    task2 = Task(
        agent=niche_researcher,
        description=f"Based on this analysis: '''{profile_analysis}''', "
                    "suggest 3-5 profitable niches with short rationales.",
        expected_output="List of niche suggestions"
    )

    task3 = Task(
        agent=gig_writer,
        description=f"Create a Fiverr gig for this niche: '''{selected_niche}'''. "
                    "Include: title, short description, long description, tags, pricing tiers.",
        expected_output="Full gig listing"
    )

    return [task1, task2, task3]