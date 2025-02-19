# L1: Automated Project: Planning, Estimation, and Allocation


# Warning control
import warnings
warnings.filterwarnings('ignore')


from crewai import Agent, Task, Crew

# Set up Environment

import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4-turbo'
print(openai_api_key)
serper_api_key=os.environ["SERPER_API_KEY"] 
print(serper_api_key)