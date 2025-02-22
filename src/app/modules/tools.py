from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool
from crewai.tools import BaseTool

class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis Tool"
    description: str = ("Analyzes the sentiment of text "
                        "to ensure positive and engaging communication.")

    def _run(self, text: str) -> str:
        # Your custom code tool goes here
        return "positive"

directory_read_tool = DirectoryReadTool(directory='src/app/OGM.MultiAgent.CustomeOurReach/instructionsforOutReach')
file_read_tool = FileReadTool()
search_tool = SerperDevTool()
sentiment_analysis_tool = SentimentAnalysisTool()
docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)
