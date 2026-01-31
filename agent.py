import random
import os
import json
# Task 1: Import Libraries
from google.genai import Client
from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.tools.example_tool import ExampleTool
from google.genai import types

# Task 2: Create the first agent
attractions_agent = Agent(
    model="gemini-2.5-flash",
    name="attractions_agent",
    description="Provides tourist attractions info for a given city.",
    instruction="""
      You are responsible for suggesting popular tourist attractions,
      sightseeing spots, and local activities for the given city.
      Provide concise and relevant recommendations to help the user plan their trip.
    """,
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)