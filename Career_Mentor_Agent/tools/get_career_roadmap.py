import os
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import function_tool, RunContextWrapper, AsyncOpenAI
from setup_config import model

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

client = AsyncOpenAI(
        api_key = gemini_api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class CareerOption(BaseModel):
    career_field: str

@function_tool  
async def get_career_roadmap(wrapper: RunContextWrapper, input: CareerOption) -> dict:
    """Generates a personalized career roadmap for the specified career field."""
    
    try:
        print("Running get_career_roadmap tool")
        
        prompt = (
            f"I'm interested in becoming {input.career_field}. "
            "Please provide a simple step-by-step roadmap from beginner to advanced level. "
            "Structure it professionally using bullet points and highlight key milestones."
        )
        
        response = await client.chat.completions.create(
            model="gemini-2.5-flash",  # Replace with actual Gemini model name
            messages=[{"role": "user", "content": prompt}]
        )
        
        return {"roadmap": response.choices[0].message.content.strip()}
    
    except Exception as e:
        print("Exception in get_career_roadmap tool:", str(e))
        return {
            "error": f"Exception in get_career_roadmap tool: {str(e)}"
        }
