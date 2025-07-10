from agents import Runner, Agent, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
import os
from dotenv import load_dotenv
from tools import get_career_roadmap , suggest_jobs

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client= external_client
)

config = RunConfig(
    model = model,
    model_provider=external_client,
    tracing_disabled= True
)

career_agent = Agent(
    name="Career Agent",
    instructions=(
        "You ask about the user's interests and return a one- or two-word career field "
        "like 'web development', 'data science', etc. DO NOT explain. JUST return the field name."
    ),
    model=model,
)

skill_agent = Agent(
    name = "Skill Agent",
    instructions=(
        "Use the `get_career_roadmap` tool to get the list of skills required for the given field. "
        "Then, for first item in the roadmap, start the line with the word 'Learn'.\n"
        "Example Output: Learn HTML, CSS, JavaScript"
        "Only return the formatted roadmap list. Do not explain."
    ),
    model= model,
    tools= [get_career_roadmap]
)
job_agent = Agent(
    name = "Job Agent",
    instructions="You suggest the job title in the chosen career",
    model= model,
    tools=[suggest_jobs]
)



def main():
    print("\U0001F393 Career Mentor Agent\n")
    interest = input("What is your interest? ").strip().lower()


    result1 = Runner.run_sync(
    career_agent,
    interest,
    run_config = config
)
    field = result1.final_output.strip()
    print("\n Suggested Career", field)
    
    result2 = Runner.run_sync(
    skill_agent,
    field,
    run_config = config
)
    print("\n Required Skill", result2.final_output)

    result3 = Runner.run_sync(
    job_agent,
    field,
    run_config = config
)
    print("\n Suggested Job", result3.final_output)


if __name__ == "__main__":
    main()
