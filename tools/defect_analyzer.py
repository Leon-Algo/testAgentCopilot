"""
Test Defect Analysis Tool
Analyzes defects, identifies patterns, and provides recommendations
"""
from typing import Dict, List, Any, Optional
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
import json
import config

class DefectAnalysisInput(BaseModel):
    """Input schema for defect analysis"""
    defect_data: str = Field(description="Defect information (description, logs, code snippets)")
    analysis_type: str = Field(default="comprehensive", description="Analysis type (quick/comprehensive/root_cause)")
    context: str = Field(default="", description="Additional context (system info, environment)")

class DefectAnalyzer(BaseTool):
    """Tool for analyzing test defects and providing insights"""

    name: str = "defect_analyzer"
    description: str = """
    Analyzes software defects to identify root causes, patterns, and provide recommendations.
    Supports multiple analysis types and can process various data formats.
    Provides actionable insights for defect resolution.
    """
    args_schema: type = DefectAnalysisInput

    def _get_llm(self):
        """Get LLM instance"""
        return ChatOpenAI(
            base_url=config.OPENAI_API_BASE,
            api_key=config.OPENAI_API_KEY,
            model=config.OPENAI_MODEL,
            temperature=0.2
        )

    def _run(self, defect_data: str, analysis_type: str = "comprehensive",
             context: str = "") -> str:
        """Analyze defect data and provide insights"""

        prompt_template = self._get_analysis_prompt(analysis_type)

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["defect_data", "context", "analysis_type"]
        )

        formatted_prompt = prompt.format(
            defect_data=defect_data,
            context=context,
            analysis_type=analysis_type
        )

        llm = self._get_llm()
        response = llm.invoke(formatted_prompt)
        return response.content

    def _get_analysis_prompt(self, analysis_type: str) -> str:
        """Get defect analysis prompt based on type"""

        base_prompt = """
        You are an expert software defect analyst. Analyze the following defect information and provide detailed insights.

        Defect Data: {defect_data}
        Additional Context: {context}
        Analysis Type: {analysis_type}
        """

        if analysis_type == "quick":
            return base_prompt + """
            Provide a quick analysis in JSON format:
            {{
                "defect_category": "functional/performance/security/usability/compatibility",
                "severity": "critical/high/medium/low",
                "likely_cause": "Brief description of likely cause",
                "immediate_action": "Immediate steps to take",
                "estimated_effort": "Low/Medium/High"
            }}
            """

        elif analysis_type == "root_cause":
            return base_prompt + """
            Perform detailed root cause analysis in JSON format:
            {{
                "root_cause_analysis": {{
                    "primary_cause": "Main root cause",
                    "contributing_factors": ["Factor 1", "Factor 2"],
                    "failure_chain": ["Event 1", "Event 2", "Event 3"],
                    "prevention_measures": ["Measure 1", "Measure 2"]
                }},
                "technical_details": {{
                    "affected_components": ["Component 1", "Component 2"],
                    "code_areas": ["Area 1", "Area 2"],
                    "data_flow_impact": "Description"
                }},
                "recommendations": {{
                    "immediate_fix": "Immediate solution",
                    "long_term_solution": "Sustainable solution",
                    "testing_strategy": "How to test the fix",
                    "monitoring": "What to monitor post-fix"
                }}
            }}
            """

        else:  # comprehensive
            return base_prompt + """
            Provide comprehensive defect analysis in JSON format:
            {{
                "defect_classification": {{
                    "category": "functional/performance/security/usability/compatibility",
                    "type": "bug/enhancement/design_issue",
                    "severity": "critical/high/medium/low",
                    "priority": "P1/P2/P3/P4",
                    "complexity": "simple/moderate/complex"
                }},
                "impact_analysis": {{
                    "user_impact": "How users are affected",
                    "business_impact": "Business consequences",
                    "system_impact": "Technical system impact",
                    "affected_features": ["Feature 1", "Feature 2"]
                }},
                "technical_analysis": {{
                    "likely_causes": ["Cause 1", "Cause 2"],
                    "affected_components": ["Component 1", "Component 2"],
                    "dependencies": ["Dependency 1", "Dependency 2"],
                    "code_quality_issues": ["Issue 1", "Issue 2"]
                }},
                "resolution_strategy": {{
                    "recommended_approach": "Detailed approach",
                    "alternative_solutions": ["Solution 1", "Solution 2"],
                    "testing_requirements": ["Test 1", "Test 2"],
                    "rollback_plan": "Rollback strategy"
                }},
                "prevention": {{
                    "process_improvements": ["Improvement 1", "Improvement 2"],
                    "code_review_focus": ["Focus area 1", "Focus area 2"],
                    "automated_checks": ["Check 1", "Check 2"]
                }}
            }}
            """

    async def _arun(self, *args, **kwargs):
        """Async version of _run"""
        return self._run(*args, **kwargs)
