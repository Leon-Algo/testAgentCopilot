"""
Configuration settings for the Test Engineer Intelligent Assistant
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.chatanywhere.tech/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

# Validate required environment variables
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required")

# Test case generation settings
TEST_CASE_FORMATS = {
    "standard": {
        "fields": ["test_id", "test_name", "description", "preconditions", "steps", "expected_result", "priority"],
        "template": "Standard test case format"
    },
    "gherkin": {
        "fields": ["feature", "scenario", "given", "when", "then"],
        "template": "Behavior-driven development format"
    }
}

# Defect analysis settings
DEFECT_ANALYSIS_CATEGORIES = [
    "functional_defects",
    "performance_issues", 
    "security_vulnerabilities",
    "usability_problems",
    "compatibility_issues"
]

# API testing settings
API_TEST_METHODS = ["GET", "POST", "PUT", "DELETE", "PATCH"]
API_TEST_SCENARIOS = [
    "positive_scenarios",
    "negative_scenarios", 
    "boundary_testing",
    "error_handling",
    "authentication_testing"
]
