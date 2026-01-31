import warnings
import asyncio
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
from google.adk.auth.credential_service.in_memory_credential_service import InMemoryCredentialService
from google.adk.apps.app import App
from agent import root_agent
from dotenv import load_dotenv
warnings.filterwarnings("ignore", category=UserWarning)
load_dotenv()  # loads .env into os.environ

# Suppress ADK experimental warnings
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module=r"google\.adk\..*"
)

# Optional: suppress only function_call concatenation warnings
warnings.filterwarnings(
    "ignore",
    message=r".*non-text parts in the response.*"
)

# Task 1: Import Libraries



# Task 9: Connect CLI with Root Agent
async def run_cli():
    return


if __name__ == "__main__":
    asyncio.run(run_cli())