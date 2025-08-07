import gradio as gr
from main import run_freelancer_optimizer

def optimize_gig(profile_text):
    """Process the profile text and return optimized gig."""
    if not profile_text.strip():
        return "Please enter a valid freelancer profile."
    
    try:
        result = run_freelancer_optimizer(profile_text)
        return result
    except Exception as e:
        return f"Error processing your profile: {str(e)}"

# Create Gradio interface
interface = gr.Interface(
    fn=optimize_gig,
    inputs=gr.Textbox(
        lines=8, 
        placeholder="Enter your freelancer profile here...\n\nExample:\nHi, I'm a graphic designer with 5 years of experience in logo design, branding, and creating social media content. I've worked with over 200 clients and enjoy creating minimal and modern designs.",
        label="Freelancer Profile",
        info="Describe your skills, experience, and what you do"
    ),
    outputs=gr.Textbox(
        label="Optimized Gig Output",
        lines=20,
        show_copy_button=True
    ),
    title="🚀 Freelancer Gig Optimizer",
    description="Analyze your freelancer profile and generate optimized gig listings for Fiverr/Upwork using AI agents",
    examples=[
        ["Hi, I'm a graphic designer with 5 years of experience in logo design, branding, and creating social media content. I've worked with over 200 clients and enjoy creating minimal and modern designs."],
        ["I'm a web developer specializing in WordPress and e-commerce sites. I have 3 years of experience and have built over 50 websites for small businesses."],
        ["I'm a content writer with expertise in blog posts, SEO content, and copywriting. I've been writing for 4 years and have helped many businesses improve their online presence."]
    ]
)

if __name__ == "__main__":
    interface.launch()