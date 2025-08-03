from crewai import Crew
from agents import profile_analyzer, niche_researcher, gig_writer
from tasks import get_tasks

# Sample input
profile_text = """
Hi, I'm a graphic designer with 5 years of experience in logo design, branding, and creating social media content.
I've worked with over 200 clients and enjoy creating minimal and modern designs.
"""

# Create tasks
tasks = get_tasks(profile_text)

# Create Crew
crew = Crew(
    agents=[profile_analyzer, niche_researcher, gig_writer],
    tasks=tasks,
    verbose=True
)

# Run Crew
result = crew.kickoff()
print("\n=== Final Output ===\n")
print(result)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(str(result))
print("✅ Output saved to output.txt")
