"""
Test Engineer Intelligent Assistant Agent
Main agent that coordinates and plans testing tasks using available tools
"""
from typing import List, Dict, Any, Optional
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import BaseMessage
import config
from tools import FunctionalTestGenerator, DefectAnalyzer, APITestGenerator

class TestEngineerAgent:
    """
    Intelligent agent for test engineering tasks
    Coordinates multiple testing tools and provides autonomous planning
    """

    def __init__(self):
        """Initialize the Test Engineer Agent"""
        self.llm = ChatOpenAI(
            base_url=config.OPENAI_API_BASE,
            api_key=config.OPENAI_API_KEY,
            model=config.OPENAI_MODEL,
            temperature=0.1
        )

        # Initialize tools
        self.tools = [
            FunctionalTestGenerator(),
            DefectAnalyzer(),
            APITestGenerator()
        ]

        # Create agent prompt
        self.prompt = self._create_agent_prompt()

        # Initialize memory
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # Create agent
        self.agent = create_openai_tools_agent(
            llm=self.llm,
            tools=self.tools,
            prompt=self.prompt
        )

        # Create agent executor
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=5
        )

    def _create_agent_prompt(self) -> ChatPromptTemplate:
        """Create the agent prompt template"""
        return ChatPromptTemplate.from_messages([
            ("system", """You are an expert Test Engineer Intelligent Assistant with autonomous planning capabilities.

Your role is to help with comprehensive software testing tasks by:
1. Analyzing user requirements and determining the best testing approach
2. Planning and coordinating multiple testing activities
3. Generating appropriate test artifacts using available tools
4. Providing expert testing guidance and recommendations

Available Tools:
- functional_test_generator: Generate functional test cases from requirements
- defect_analyzer: Analyze defects and provide insights
- api_test_generator: Generate API test cases from specifications

Key Capabilities:
- Autonomous task planning and decomposition
- Multi-format support (text, documents, specifications)
- Comprehensive test coverage (positive, negative, edge cases)
- Integration with existing testing platforms
- Standardized output formats

When given a task:
1. Analyze the requirements thoroughly
2. Determine which tools are needed
3. Plan the execution sequence
4. Execute tools in logical order
5. Synthesize results into actionable deliverables
6. Provide recommendations for next steps

Always aim for comprehensive coverage and professional quality outputs.
Be proactive in suggesting additional testing scenarios that might be valuable.
"""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])

    def process_request(self, user_input: str) -> str:
        """
        Process user request and coordinate appropriate tools

        Args:
            user_input: User's testing request or requirements

        Returns:
            Comprehensive response with testing artifacts and recommendations
        """
        try:
            result = self.agent_executor.invoke({"input": user_input})
            return result["output"]
        except Exception as e:
            return f"Error processing request: {str(e)}"

    def plan_testing_strategy(self, requirements: str, project_context: str = "") -> Dict[str, Any]:
        """
        Create a comprehensive testing strategy plan

        Args:
            requirements: Project or feature requirements
            project_context: Additional project context

        Returns:
            Dictionary containing testing strategy and recommendations
        """
        planning_prompt = f"""
        Create a comprehensive testing strategy for the following requirements:

        Requirements: {requirements}
        Project Context: {project_context}

        Provide a detailed testing plan including:
        1. Testing scope and objectives
        2. Required test types (functional, API, performance, etc.)
        3. Test case generation recommendations
        4. Defect analysis approach
        5. Tools and frameworks to use
        6. Timeline and resource estimates
        7. Risk assessment and mitigation
        """

        result = self.process_request(planning_prompt)
        return {"strategy": result, "status": "completed"}

    def generate_comprehensive_test_suite(self, requirements: str,
                                        include_api: bool = False,
                                        api_spec: str = "") -> Dict[str, Any]:
        """
        Generate a complete test suite including functional and API tests

        Args:
            requirements: Functional requirements
            include_api: Whether to include API tests
            api_spec: API specification if API tests are needed

        Returns:
            Dictionary containing all generated test artifacts
        """
        suite_prompt = f"""
        Generate a comprehensive test suite for:

        Requirements: {requirements}
        Include API Tests: {include_api}
        API Specification: {api_spec}

        Please:
        1. Generate functional test cases covering all scenarios
        2. {"Generate API test cases based on the specification" if include_api else "Skip API test generation"}
        3. Provide test execution recommendations
        4. Suggest automation strategies
        5. Include test data requirements
        """

        result = self.process_request(suite_prompt)
        return {"test_suite": result, "status": "completed"}

    def analyze_and_recommend(self, defect_info: str, context: str = "") -> Dict[str, Any]:
        """
        Analyze defects and provide comprehensive recommendations

        Args:
            defect_info: Defect information and details
            context: Additional context about the system/environment

        Returns:
            Dictionary containing analysis results and recommendations
        """
        analysis_prompt = f"""
        Perform comprehensive defect analysis and provide recommendations:

        Defect Information: {defect_info}
        Context: {context}

        Please:
        1. Analyze the defect thoroughly
        2. Identify root causes and patterns
        3. Provide resolution recommendations
        4. Suggest prevention strategies
        5. Recommend additional test cases to prevent similar issues
        """

        result = self.process_request(analysis_prompt)
        return {"analysis": result, "status": "completed"}

    def get_tool_info(self) -> Dict[str, str]:
        """Get information about available tools"""
        return {
            tool.name: tool.description for tool in self.tools
        }
