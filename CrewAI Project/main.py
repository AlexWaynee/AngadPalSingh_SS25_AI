from crewai import Crew
from agents import profile_analyzer, niche_researcher, gig_writer
from tasks import get_tasks

def run_freelancer_optimizer(profile_text):
    """Main function to run the freelancer optimization pipeline."""
    
    # Create tasks with the profile text
    tasks = get_tasks(profile_text)
    
    # Create Crew
    crew = Crew(
        agents=[profile_analyzer, niche_researcher, gig_writer],
        tasks=tasks,
        verbose=True
    )
    
    # Run Crew
    result = crew.kickoff()
    
    return str(result)

def main():
    # Sample input
    profile_text = """
    Hi, I'm a graphic designer with 5 years of experience in logo design, branding, and creating social media content.
    I've worked with over 200 clients and enjoy creating minimal and modern designs.
    """
    
    print("🚀 Starting Freelancer Gig Optimizer...")
    print(f"📝 Analyzing profile: {profile_text[:100]}...")
    
    # Run the optimization pipeline
    result = run_freelancer_optimizer(profile_text)
    
    print("\n=== Final Output ===\n")
    print(result)
    
    # Save output
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(str(result))
    print("\n✅ Output saved to output.txt")
    
    return result

if __name__ == "__main__":
    main()