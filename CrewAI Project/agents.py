from crewai import Agent

profile_analyzer = Agent(
    role='Profile Analyzer',
    goal='Analyze freelancer profiles to find improvement areas',
    backstory='You are an expert at evaluating online freelance profiles.',
    verbose=True
)

niche_researcher = Agent(
    role='Niche Researcher',
    goal='Identify high-demand niches based on freelancer skills',
    backstory='You know how to find profitable freelance niches.',
    verbose=True
)

gig_writer = Agent(
    role='Gig Writer',
    goal='Write optimized freelance gig listings',
    backstory='You specialize in writing compelling Fiverr/Upwork gigs.',
    verbose=True
)