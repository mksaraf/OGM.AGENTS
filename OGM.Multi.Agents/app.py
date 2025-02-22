#### Import ####
import sys
module_path = '/Users/manishkumarsaraf/Library/Mobile Documents/com~apple~CloudDocs/OGM/OGM.Bots/OGM.Agents/OGM.Multi.Agents/'
# Add the module directory to sys.path
sys.path.append(module_path)
# Print sys.path to verify
print(f"sys.path: {sys.path}")
import os
import streamlit as st
from dotenv import load_dotenv
# from fastapi import FastAPI
# from fastapi.testclient import TestClient
# from fastapi_app import fast_app
from modules.key_ogm import get_openai_key_st, get_serper_api_key_st
from modules.crew import \
    SalesCrew, \
    ContentCrew, \
    FinancialTradingCrew, \
    CustomerSupportCrew, \
    EventManagementCrew, \
    JobApplicationCrew \

#### Key ####
#load_dotenv()
# openai_api_key = os.environ.get("OPENAI_API_KEY")
openai_api_key = get_openai_key_st()
#print(f"OpenAI API Key: {openai_api_key}")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4-turbo'
#serper_api_key=os.environ["SERPER_API_KEY"] 
serper_api_key = get_serper_api_key_st()


# #### FastAPI ####
# client = TestClient(fast_app)

#### Streamlit App ####
# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Home", "Blog Write", "Customer Outreach", "Financial Analysis", "Tailored Resume", "Customer Support", "Event Planning"])

# Tab 1: Home
with tab1:
    st.write("Welcome to the Content Generation App!")
    st.write("This app generates content based on a given topic.")
    st.write("Please navigate to the Generate Content tab to get started.")

# Tab 2: Blog Write
with tab2:
    topic = st.text_input("Enter topic", "")
    if st.button("Generate Content"):
        crew = ContentCrew()
        result = crew.kickoff(inputs={"topic": topic})
        st.write(result)

# Tab 3: Customer Outreach
with tab3:
    st.write("Sales Crew")
    lead_name = st.text_input("Enter lead name", "")
    industry = st.text_input("Enter industry", "")
    key_decision_maker = st.text_input("Enter key decision maker", "")
    position = st.text_input("Enter position", "")
    milestone = st.text_input("Enter milestone", "")
    if st.button("Generate Sales Outreach"):
        crew = SalesCrew()
        inputs = {
            "lead_name": lead_name,
            "industry": industry,
            "key_decision_maker": key_decision_maker,
            "position": position,
            "milestone": milestone
        }
        result = crew.kickoff(inputs=inputs)
        st.write(result)

# Tab 4: Financial Analysis
with tab4:
    st.write("Financial Trading Crew")
    stock_selection = st.text_input("Enter stock selection", "")
    initial_capital = st.text_input("Enter initial capital", "")
    risk_tolerance = st.text_input("Enter risk tolerance", "")
    trading_strategy_preference = st.text_input("Enter trading strategy preference", "")
    news_impact_consideration = st.checkbox("Consider news impact")
    if st.button("Generate Financial Trading Plan"):
        crew = FinancialTradingCrew()
        inputs = {
            'stock_selection': stock_selection,
            'initial_capital': initial_capital,
            'risk_tolerance': risk_tolerance,
            'trading_strategy_preference': trading_strategy_preference,
            'news_impact_consideration': news_impact_consideration
        }
        result = crew.kickoff(inputs=inputs)
        st.write(result)

# Tab 5: Job Application Crew
with tab5:
    st.write("Job Application Crew")
    job_posting_url = st.text_input("Enter job posting URL", "")
    github_url = st.text_input("Enter GitHub URL", "")
    personal_writeup = st.text_area("Enter personal writeup", "")
    if st.button("Generate Job Application"):
        crew = JobApplicationCrew()
        inputs = {
            'job_posting_url': job_posting_url,
            'github_url': github_url,
            'personal_writeup': personal_writeup
        }
        result = crew.kickoff(inputs=inputs)
        st.write(result)

# Tab 6: Customer Support Crew
with tab6:
    st.write("Customer Support Crew")
    customer = st.text_input("Enter customer name", "")
    person = st.text_input("Enter person name", "")
    inquiry = st.text_area("Enter inquiry", "")
    if st.button("Generate Support Response"):
        crew = CustomerSupportCrew()
        inputs = {
            "customer": customer,
            "person": person,
            "inquiry": inquiry
        }
        result = crew.kickoff(inputs=inputs)
        st.write(result)

# Tab 7: Event Management Crew
with tab7:
    st.write("Event Management Crew")
    event_topic = st.text_input("Enter event topic", "")
    event_description = st.text_area("Enter event description", "")
    event_city = st.text_input("Enter event city", "")
    tentative_date = st.text_input("Enter tentative date", "")
    expected_participants = st.text_input("Enter expected participants", "")
    budget = st.text_input("Enter budget", "")
    venue_type = st.text_input("Enter venue type", "")
    if st.button("Generate Event Plan"):
        crew = EventManagementCrew()
        inputs = {
            'event_topic': event_topic,
            'event_description': event_description,
            'event_city': event_city,
            'tentative_date': tentative_date,
            'expected_participants': expected_participants,
            'budget': budget,
            'venue_type': venue_type
        }
        result = crew.kickoff(inputs=inputs)
        st.write(result)

