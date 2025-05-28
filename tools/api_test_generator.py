"""
API Test Case Generation Tool
Generates comprehensive API test cases based on API specifications
"""
from typing import Dict, List, Any, Optional
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
import json
import config

class APITestInput(BaseModel):
    """Input schema for API test case generation"""
    api_specification: str = Field(description="API specification (OpenAPI/Swagger, or description)")
    test_framework: str = Field(default="requests", description="Test framework (requests/pytest/postman)")
    coverage_type: str = Field(default="comprehensive", description="Coverage type (basic/comprehensive/security)")
    output_format: str = Field(default="python", description="Output format (python/postman/curl)")

class APITestGenerator(BaseTool):
    """Tool for generating API test cases from specifications"""

    name: str = "api_test_generator"
    description: str = """
    Generates comprehensive API test cases based on API specifications.
    Supports multiple test frameworks and output formats.
    Covers positive, negative, security, and performance scenarios.
    """
    args_schema: type = APITestInput

    def _get_llm(self):
        """Get LLM instance"""
        return ChatOpenAI(
            base_url=config.OPENAI_API_BASE,
            api_key=config.OPENAI_API_KEY,
            model=config.OPENAI_MODEL,
            temperature=0.3
        )

    def _run(self, api_specification: str, test_framework: str = "requests",
             coverage_type: str = "comprehensive", output_format: str = "python") -> str:
        """Generate API test cases"""

        prompt_template = self._get_api_test_prompt(test_framework, output_format, coverage_type)

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["api_specification", "test_framework", "coverage_type", "output_format"]
        )

        formatted_prompt = prompt.format(
            api_specification=api_specification,
            test_framework=test_framework,
            coverage_type=coverage_type,
            output_format=output_format
        )

        llm = self._get_llm()
        response = llm.invoke(formatted_prompt)
        return response.content

    def _get_api_test_prompt(self, framework: str, output_format: str, coverage_type: str) -> str:
        """Get API test generation prompt"""

        base_prompt = """
        You are an expert API test engineer. Generate comprehensive API test cases based on the following specification.

        API Specification: {api_specification}
        Test Framework: {test_framework}
        Coverage Type: {coverage_type}
        Output Format: {output_format}
        """

        if output_format == "python":
            return base_prompt + """
            Generate Python test cases using the specified framework. Include:

            1. **Positive Test Cases:**
               - Valid requests with expected responses
               - Different valid input combinations
               - Successful authentication scenarios

            2. **Negative Test Cases:**
               - Invalid parameters
               - Missing required fields
               - Invalid data types
               - Boundary value testing

            3. **Security Test Cases:**
               - Authentication/authorization testing
               - Input validation testing
               - SQL injection attempts (if applicable)
               - XSS attempts (if applicable)

            4. **Error Handling:**
               - HTTP error codes (400, 401, 403, 404, 500)
               - Malformed requests
               - Timeout scenarios

            Generate complete, runnable Python code with:
            - Proper imports
            - Test class structure
            - Setup and teardown methods
            - Assertion statements
            - Clear test documentation

            Example structure:
            ```python
            import requests
            import pytest
            import json

            class TestAPIEndpoint:
                def setup_method(self):
                    self.base_url = "https://api.example.com"
                    self.headers = {{"Content-Type": "application/json"}}

                def test_positive_scenario(self):
                    # Test implementation
                    pass
            ```
            """

        elif output_format == "postman":
            return base_prompt + """
            Generate Postman collection JSON format with:
            - Collection metadata
            - Request definitions
            - Test scripts
            - Environment variables
            - Pre-request scripts

            Include comprehensive test scenarios covering:
            1. Positive scenarios
            2. Negative scenarios
            3. Boundary testing
            4. Authentication testing
            5. Error handling

            Format as valid Postman Collection v2.1 JSON.
            """

        else:  # curl
            return base_prompt + """
            Generate curl commands for API testing with:
            - Complete curl syntax
            - Headers and authentication
            - Request bodies (JSON/XML)
            - Response validation suggestions
            - Error scenario testing

            Organize by test categories:
            1. Positive scenarios
            2. Negative scenarios
            3. Security testing
            4. Performance testing

            Include comments explaining each test case purpose.
            """

    async def _arun(self, *args, **kwargs):
        """Async version of _run"""
        return self._run(*args, **kwargs)
