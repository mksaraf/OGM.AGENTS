from crewai import Task
from modules.models import VenueDetails
from crewai_tools import ScrapeWebsiteTool

docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)


class PlanTask(Task):
    def __init__(self, planner):
        super().__init__(
            description=(
                "1. Prioritize the latest trends, key players, "
                "and noteworthy news on {topic}.\n"
                "2. Identify the target audience, considering "
                "their interests and pain points.\n"
                "3. Develop a detailed content outline including "
                "an introduction, key points, and a call to action.\n"
                "4. Include SEO keywords and relevant data or sources."
            ),
            expected_output="A comprehensive content plan document "
                            "with an outline, audience analysis, "
                            "SEO keywords, and resources.",
            agent=planner
        )

class WriteTask(Task):
    def __init__(self, writer):
        super().__init__(
            description=(
                "1. Use the content plan to craft a compelling "
                "blog post on {topic}.\n"
                "2. Incorporate SEO keywords naturally.\n"
                "3. Sections/Subtitles are properly named "
                "in an engaging manner.\n"
                "4. Ensure the post is structured with an "
                "engaging introduction, insightful body, "
                "and a summarizing conclusion.\n"
                "5. Proofread for grammatical errors and "
                "alignment with the brand's voice.\n"
            ),
            expected_output="A well-written blog post "
                            "in markdown format, ready for publication, "
                            "each section should have 2 or 3 paragraphs.",
            agent=writer
        )

class EditTask(Task):
    def __init__(self, editor):
        super().__init__(
            description=("Proofread the given blog post for "
                         "grammatical errors and "
                         "alignment with the brand's voice."),
            expected_output="A well-written blog post in markdown format, "
                            "ready for publication, "
                            "each section should have 2 or 3 paragraphs.",
            agent=editor
        )

class LeadProfilingTask(Task):
    def __init__(self, agent, tools):
        super().__init__(
            description=(
                "Conduct an in-depth analysis of {lead_name}, "
                "a company in the {industry} sector "
                "that recently showed interest in our solutions. "
                "Utilize all available data sources "
                "to compile a detailed profile, "
                "focusing on key decision-makers, recent business "
                "developments, and potential needs "
                "that align with our offerings. "
                "This task is crucial for tailoring "
                "our engagement strategy effectively.\n"
                "Don't make assumptions and "
                "only use information you absolutely sure about."
            ),
            expected_output=(
                "A comprehensive report on {lead_name}, "
                "including company background, "
                "key personnel, recent milestones, and identified needs. "
                "Highlight potential areas where "
                "our solutions can provide value, "
                "and suggest personalized engagement strategies."
            ),
            tools=tools,
            agent=agent,
        )

class PersonalizedOutreachTask(Task):
    def __init__(self, agent, tools):
        super().__init__(
            description=(
                "Using the insights gathered from "
                "the lead profiling report on {lead_name}, "
                "craft a personalized outreach campaign "
                "aimed at {key_decision_maker}, "
                "the {position} of {lead_name}. "
                "The campaign should address their recent {milestone} "
                "and how our solutions can support their goals. "
                "Your communication must resonate "
                "with {lead_name}'s company culture and values, "
                "demonstrating a deep understanding of "
                "their business and needs.\n"
                "Don't make assumptions and only "
                "use information you absolutely sure about."
            ),
            expected_output=(
                "A series of personalized email drafts "
                "tailored to {lead_name}, "
                "specifically targeting {key_decision_maker}."
                "Each draft should include "
                "a compelling narrative that connects our solutions "
                "with their recent achievements and future goals. "
                "Ensure the tone is engaging, professional, "
                "and aligned with {lead_name}'s corporate identity."
            ),
            tools=tools,
            agent=agent,
        )

class DataAnalysisTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Continuously monitor and analyze market data for "
                "the selected stock ({stock_selection}). "
                "Use statistical modeling and machine learning to "
                "identify trends and predict market movements."
            ),
            expected_output=(
                "Insights and alerts about significant market "
                "opportunities or threats for {stock_selection}."
            ),
            agent=agent,
        )

class StrategyDevelopmentTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Develop and refine trading strategies based on "
                "the insights from the Data Analyst and "
                "user-defined risk tolerance ({risk_tolerance}). "
                "Consider trading preferences ({trading_strategy_preference})."
            ),
            expected_output=(
                "A set of potential trading strategies for {stock_selection} "
                "that align with the user's risk tolerance."
            ),
            agent=agent,
        )

class ExecutionPlanningTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Analyze approved trading strategies to determine the "
                "best execution methods for {stock_selection}, "
                "considering current market conditions and optimal pricing."
            ),
            expected_output=(
                "Detailed execution plans suggesting how and when to "
                "execute trades for {stock_selection}."
            ),
            agent=agent,
        )

class RiskAssessmentTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Evaluate the risks associated with the proposed trading "
                "strategies and execution plans for {stock_selection}. "
                "Provide a detailed analysis of potential risks "
                "and suggest mitigation strategies."
            ),
            expected_output=(
                "A comprehensive risk analysis report detailing potential "
                "risks and mitigation recommendations for {stock_selection}."
            ),
            agent=agent,
        )

class ResearchTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Analyze the job posting URL provided ({job_posting_url}) "
                "to extract key skills, experiences, and qualifications "
                "required. Use the tools to gather content and identify "
                "and categorize the requirements."
            ),
            expected_output=(
                "A structured list of job requirements, including necessary "
                "skills, qualifications, and experiences."
            ),
            agent=agent,
            async_execution=True
        )

class ProfileTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Compile a detailed personal and professional profile "
                "using the GitHub ({github_url}) URLs, and personal write-up "
                "({personal_writeup}). Utilize tools to extract and "
                "synthesize information from these sources."
            ),
            expected_output=(
                "A comprehensive profile document that includes skills, "
                "project experiences, contributions, interests, and "
                "communication style."
            ),
            agent=agent,
            async_execution=True
        )

class ResumeStrategyTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Using the profile and job requirements obtained from "
                "previous tasks, tailor the resume to highlight the most "
                "relevant areas. Employ tools to adjust and enhance the "
                "resume content. Make sure this is the best resume even but "
                "don't make up any information. Update every section, "
                "inlcuding the initial summary, work experience, skills, "
                "and education. All to better reflrect the candidates "
                "abilities and how it matches the job posting."
            ),
            expected_output=(
                "An updated resume that effectively highlights the candidate's "
                "qualifications and experiences relevant to the job."
            ),
            output_file="tailored_resume.doc",
            context=None,
            agent=agent
        )

class InterviewPreparationTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Create a set of potential interview questions and talking "
                "points based on the tailored resume and job requirements. "
                "Utilize tools to generate relevant questions and discussion "
                "points. Make sure to use these question and talking points to "
                "help the candiadte highlight the main points of the resume "
                "and how it matches the job posting."
            ),
            expected_output=(
                "A document containing key questions and talking points "
                "that the candidate should prepare for the initial interview."
            ),
            output_file="interview_materials.doc",
            context=None,
            agent=agent
        )

class InquiryResolutionTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "{customer} just reached out with a super important ask:\n"
                "{inquiry}\n\n"
                "{person} from {customer} is the one that reached out. "
                "Make sure to use everything you know "
                "to provide the best support possible."
                "You must strive to provide a complete "
                "and accurate response to the customer's inquiry."
            ),
            expected_output=(
                "A detailed, informative response to the "
                "customer's inquiry that addresses "
                "all aspects of their question.\n"
                "The response should include references "
                "to everything you used to find the answer, "
                "including external data or solutions. "
                "Ensure the answer is complete, "
                "leaving no questions unanswered, and maintain a helpful and friendly "
                "tone throughout."
            ),
            tools=[docs_scrape_tool],
            agent=agent,
        )

class QualityAssuranceReviewTask(Task):
    def __init__(self, agent):
        super().__init__(
            description=(
                "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
                "Ensure that the answer is comprehensive, accurate, and adheres to the "
                "high-quality standards expected for customer support.\n"
                "Verify that all parts of the customer's inquiry "
                "have been addressed "
                "thoroughly, with a helpful and friendly tone.\n"
                "Check for references and sources used to "
                "find the information, "
                "ensuring the response is well-supported and "
                "leaves no questions unanswered."
            ),
            expected_output=(
                "A final, detailed, and informative response "
                "ready to be sent to the customer.\n"
                "This response should fully address the "
                "customer's inquiry, incorporating all "
                "relevant feedback and improvements.\n"
                "Don't be too formal, we are a chill and cool company "
                "but maintain a professional and friendly tone throughout."
            ),
            agent=agent,
        )

class VenueTask(Task):
    def __init__(self, agent):
        super().__init__(
            description="Find a venue in {event_city} "
                        "that meets criteria for {event_topic}.",
            expected_output="All the details of a specifically chosen"
                            "venue you found to accommodate the event.",
            human_input=True,
            output_json=VenueDetails,
            output_file="venue_details.json",  
            agent=agent
        )

class LogisticsTask(Task):
    def __init__(self, agent):
        super().__init__(
            description="Coordinate catering and "
                         "equipment for an event "
                         "with {expected_participants} participants "
                         "on {tentative_date}.",
            expected_output="Confirmation of all logistics arrangements "
                            "including catering and equipment setup.",
            human_input=False,
            async_execution=True,
            agent=agent
        )

class MarketingTask(Task):
    def __init__(self, agent):
        super().__init__(
            description="Promote the {event_topic} "
                        "aiming to engage at least"
                        "{expected_participants} potential attendees.",
            expected_output="Report on marketing activities "
                            "and attendee engagement formatted as markdown.",
            async_execution=False,
            output_file="marketing_report.doc",  
            agent=agent
        )

