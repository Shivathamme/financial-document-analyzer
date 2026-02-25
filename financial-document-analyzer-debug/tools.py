## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

# from crewai_tools.tools.serper_dev_tool import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader

## Creating search tool
# search_tool = SerperDevTool()
from crewai.tools import tool
## Creating custom pdf reader tool
@tool("Read Financial PDF")
def read_data_tool(path: str ='data/sample.pdf')-> str:
    """
    Read financial PDF document and return full text content.
    """
    if not os.path.exists(path):
        return "File not found."
    
    loader = PyPDFLoader(path)
    docs = loader.load()

    full_report = ""
    for data in docs:
        # Clean and format the financial document data
        content = data.page_content
            
        # Remove extra whitespaces and format properly
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")
                
        full_report += content + "\n"
            
    return full_report

