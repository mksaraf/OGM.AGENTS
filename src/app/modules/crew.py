from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from modules.agents import Planner, Writer, Editor, SalesRepresentativeAgent, LeadSalesRepresentativeAgent, DataAnalystAgent, TradingStrategyAgent, ExecutionAgent, RiskManagementAgent, ResearcherAgent, ProfilerAgent, ResumeStrategistAgent, InterviewPreparerAgent, SupportAgent, SupportQualityAssuranceAgent, VenueCoordinatorAgent, LogisticsManagerAgent, MarketingCommunicationsAgent
from modules.tasks import PlanTask, WriteTask, EditTask, LeadProfilingTask, PersonalizedOutreachTask, DataAnalysisTask, StrategyDevelopmentTask, ExecutionPlanningTask, RiskAssessmentTask, InquiryResolutionTask, QualityAssuranceReviewTask, VenueTask, LogisticsTask, MarketingTask, ResearchTask, ProfileTask, ResumeStrategyTask, InterviewPreparationTask
from modules.tools import directory_read_tool, file_read_tool, search_tool, sentiment_analysis_tool, docs_scrape_tool

class ContentCrew(Crew):
    def __init__(self):
        planner = Planner()
        writer = Writer()
        editor = Editor()
        plan_task = PlanTask(planner)
        write_task = WriteTask(writer)
        edit_task = EditTask(editor)
        super().__init__(
            agents=[planner, writer, editor],
            tasks=[plan_task, write_task, edit_task],
            verbose=True
        )

class SalesCrew(Crew):
    def __init__(self):
        sales_rep_agent = SalesRepresentativeAgent()
        lead_sales_rep_agent = LeadSalesRepresentativeAgent()
        lead_profiling_task = LeadProfilingTask(sales_rep_agent, [directory_read_tool, file_read_tool, search_tool])
        personalized_outreach_task = PersonalizedOutreachTask(lead_sales_rep_agent, [sentiment_analysis_tool, search_tool])
        super().__init__(
            agents=[sales_rep_agent, lead_sales_rep_agent],
            tasks=[lead_profiling_task, personalized_outreach_task],
            verbose=True,
            memory=True
        )

class FinancialTradingCrew(Crew):
    def __init__(self):
        data_analyst_agent = DataAnalystAgent()
        trading_strategy_agent = TradingStrategyAgent()
        execution_agent = ExecutionAgent()
        risk_management_agent = RiskManagementAgent()
        data_analysis_task = DataAnalysisTask(data_analyst_agent)
        strategy_development_task = StrategyDevelopmentTask(trading_strategy_agent)
        execution_planning_task = ExecutionPlanningTask(execution_agent)
        risk_assessment_task = RiskAssessmentTask(risk_management_agent)
        super().__init__(
            agents=[data_analyst_agent, 
                    trading_strategy_agent, 
                    execution_agent, 
                    risk_management_agent],
            
            tasks=[data_analysis_task, 
                   strategy_development_task, 
                   execution_planning_task, 
                   risk_assessment_task],
            
            manager_llm=ChatOpenAI(model="gpt-3.5-turbo", 
                                   temperature=0.7),
            process=Process.hierarchical,
            verbose=True
        )

class JobApplicationCrew(Crew):
    def __init__(self):
        researcher = ResearcherAgent()
        profiler = ProfilerAgent()
        resume_strategist = ResumeStrategistAgent()
        interview_preparer = InterviewPreparerAgent()
        research_task = ResearchTask(researcher)
        profile_task = ProfileTask(profiler)
        resume_strategy_task = ResumeStrategyTask(resume_strategist)
        interview_preparation_task = InterviewPreparationTask(interview_preparer)
        super().__init__(
            agents=[researcher, profiler, resume_strategist, interview_preparer],
            tasks=[research_task, profile_task, resume_strategy_task, interview_preparation_task],
            manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
            process=Process.hierarchical,
            verbose=True
        )

class CustomerSupportCrew(Crew):
    def __init__(self):
        support_agent = SupportAgent()
        support_quality_assurance_agent = SupportQualityAssuranceAgent()
        inquiry_resolution_task = InquiryResolutionTask(support_agent)
        quality_assurance_review_task = QualityAssuranceReviewTask(support_quality_assurance_agent)
        super().__init__(
            agents=[support_agent, support_quality_assurance_agent],
            tasks=[inquiry_resolution_task, quality_assurance_review_task],
            verbose=2,
            memory=True
        )

class EventManagementCrew(Crew):
    def __init__(self):
        venue_coordinator = VenueCoordinatorAgent()
        logistics_manager = LogisticsManagerAgent()
        marketing_communications = MarketingCommunicationsAgent()
        venue_task = VenueTask(venue_coordinator)
        logistics_task = LogisticsTask(logistics_manager)
        marketing_task = MarketingTask(marketing_communications)
        super().__init__(
            agents=[venue_coordinator, 
                    logistics_manager, 
                    marketing_communications],
            
            tasks=[venue_task, 
                   logistics_task, 
                   marketing_task],
            
            verbose=True
        )