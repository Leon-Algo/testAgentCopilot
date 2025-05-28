"""
Functional Test Case Generation Tool
Generates comprehensive test cases based on functional requirements
"""
from typing import Dict, List, Any, Optional
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
import json
import config

class FunctionalTestInput(BaseModel):
    """Input schema for functional test case generation"""
    requirements: str = Field(description="Functional requirements description")
    test_format: str = Field(default="standard", description="Test case format (standard/gherkin)")
    coverage_level: str = Field(default="comprehensive", description="Coverage level (basic/comprehensive/exhaustive)")
    priority_focus: str = Field(default="high", description="Priority focus (high/medium/low/all)")

class FunctionalTestGenerator(BaseTool):
    """Tool for generating functional test cases from requirements"""

    name: str = "functional_test_generator"
    description: str = """
    Generates comprehensive functional test cases based on requirements.
    Supports multiple formats and coverage levels.
    Covers normal, abnormal, and edge cases.
    """
    args_schema: type = FunctionalTestInput

    def _get_llm(self):
        """Get LLM instance"""
        return ChatOpenAI(
            base_url=config.OPENAI_API_BASE,
            api_key=config.OPENAI_API_KEY,
            model=config.OPENAI_MODEL,
            temperature=0.3
        )

    def _run(self, requirements: str, test_format: str = "standard",
             coverage_level: str = "comprehensive", priority_focus: str = "high") -> str:
        """Generate functional test cases"""

        # Create prompt template based on format
        if test_format == "gherkin":
            prompt_template = self._get_gherkin_prompt()
        else:
            prompt_template = self._get_standard_prompt()

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["requirements", "coverage_level", "priority_focus"]
        )

        # Generate test cases
        formatted_prompt = prompt.format(
            requirements=requirements,
            coverage_level=coverage_level,
            priority_focus=priority_focus
        )

        llm = self._get_llm()
        response = llm.invoke(formatted_prompt)
        return response.content

    def _get_standard_prompt(self) -> str:
        """Get standard test case generation prompt"""
        return """
        You are an expert test engineer. Generate comprehensive functional test cases based on the following requirements.

        Requirements: {requirements}
        Coverage Level: {coverage_level}
        Priority Focus: {priority_focus}

        Generate test cases in the following JSON format:
        {{
            "test_cases": [
                {{
                    "test_id": "TC_001",
                    "test_name": "Test case name",
                    "description": "Detailed description",
                    "preconditions": "Prerequisites for test execution",
                    "steps": [
                        "Step 1: Action description",
                        "Step 2: Action description"
                    ],
                    "expected_result": "Expected outcome",
                    "priority": "High/Medium/Low",
                    "category": "Positive/Negative/Edge Case"
                }}
            ]
        }}

        Ensure coverage of:
        1. Positive scenarios (normal flow)
        2. Negative scenarios (error conditions)
        3. Edge cases (boundary conditions)
        4. Data validation scenarios
        5. User interface scenarios (if applicable)

        Generate at least 10 test cases for comprehensive coverage.
        """

    def _get_gherkin_prompt(self) -> str:
        """Get Gherkin/BDD test case generation prompt"""
        return """
        You are an expert test engineer. Generate BDD-style test cases in Gherkin format based on the following requirements.

        Requirements: {requirements}
        Coverage Level: {coverage_level}
        Priority Focus: {priority_focus}

        Generate test cases in Gherkin format:

        Feature: [Feature name]

        Scenario: [Scenario name]
            Given [precondition]
            When [action]
            Then [expected result]

        Include scenarios for:
        1. Happy path scenarios
        2. Error handling scenarios
        3. Edge cases and boundary conditions
        4. Data validation scenarios

        Generate at least 8 scenarios for comprehensive coverage.
        """

    async def _arun(self, *args, **kwargs):
        """Async version of _run"""
        return self._run(*args, **kwargs)
