## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools import read_data_tool

### Loading LLM
llm = LLM(
    model="gpt-4o-mini",
    temperature=0.3
)

# Creating an Experienced Financial Analyst agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal=(
        "Carefully analyze the uploaded financial document and provide "
        "evidence-based insights related to the user's query: {query}. "
        "Focus on financial metrics, trends, risks, and investment outlook."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced financial analyst with expertise in "
        "interpreting financial statements, earnings reports, and corporate disclosures. "
        "You rely strictly on document data and avoid speculation. "
        "Your analysis must be logical, structured, and professional."
    ),
    tools=[read_data_tool],
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal=(
        "Verify whether the uploaded file contains valid financial content. "
        "Identify document type (e.g., earnings report, balance sheet, investor update) "
        "and confirm its relevance before analysis."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are responsible for validating document authenticity and ensuring "
        "that only relevant financial documents are processed for analysis. "
        "You carefully review content before approval."
    ),
    llm=llm,
    max_iter=1,
    max_rpm=5,
    allow_delegation=False
)

# Creating investment advisor agent
investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal=(
        "Based on the financial analysis, provide balanced investment insights. "
        "Highlight strengths, weaknesses, potential opportunities, and risks. "
        "Avoid making unrealistic or speculative claims."
    ),
    verbose=True,
    backstory=(
        "You specialize in portfolio evaluation and investment strategy. "
        "You provide responsible, data-backed recommendations and clearly state assumptions."
    ),
    llm=llm,   # ← COMMA FIXED HERE
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)

# Creating risk assessor agent
risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal=(
        "Identify financial, operational, and market risks mentioned in the document. "
        "Provide a structured risk summary and categorize risks by severity."
    ),
    verbose=True,
    backstory=(
        "You are a financial risk expert trained in analyzing market volatility, "
        "liquidity risks, leverage exposure, and macroeconomic impact. "
        "Your analysis must remain realistic and evidence-based."
    ),
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)