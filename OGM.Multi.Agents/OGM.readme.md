# Project Path
- OGM.AGENTS: 
- OGM.Multi.Agents: 

# Virtual Env: .venv-stage
python3.10 -m venv .venv-stage
source .venv-stage/bin/activate

# Install python libraries
<!-- pip3 install pydantic fastapi crew langchain-openai openai streamlit python-dotenv crewai-tools crewai -->
pip3 install -r ./OGM.Multi.Agents/requirements.txt -v > install_log.txt 2>&1
pip cache purge   
# Requirements Check
python3 OGM.Multi.Agents/modules/check_requirements.py ./OGM.Multi.Agents/requirements.txt

# Run streamlit
- cd OGM.Multi.Agents

# Git
- git pull
- git checkout stage
- git add .
- git commit -m "message..."
- git push origin stage 
- git push origin -d stage
- git branch -D stage
- 
