"""
Test Engineer Intelligent Assistant - Main Application
Entry point for the Test Engineer AI Assistant MVP
"""
import json
import sys
from typing import Dict, Any
from test_engineer_agent import TestEngineerAgent

class TestEngineerAssistant:
    """Main application class for the Test Engineer Assistant"""
    
    def __init__(self):
        """Initialize the assistant"""
        print("🤖 Initializing Test Engineer Intelligent Assistant...")
        try:
            self.agent = TestEngineerAgent()
            print("✅ Assistant initialized successfully!")
        except Exception as e:
            print(f"❌ Failed to initialize assistant: {e}")
            sys.exit(1)
    
    def run_interactive_mode(self):
        """Run the assistant in interactive mode"""
        print("\n" + "="*60)
        print("🧪 TEST ENGINEER INTELLIGENT ASSISTANT")
        print("="*60)
        print("Available commands:")
        print("  1. Generate functional test cases")
        print("  2. Analyze defects")
        print("  3. Generate API test cases")
        print("  4. Create testing strategy")
        print("  5. Generate comprehensive test suite")
        print("  6. Free-form testing assistance")
        print("  'quit' or 'exit' to stop")
        print("="*60)
        
        while True:
            try:
                user_input = input("\n💬 How can I help you with testing today? ")
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye! Happy testing!")
                    break
                
                if user_input.strip() == "":
                    continue
                
                print("\n🔄 Processing your request...")
                response = self.agent.process_request(user_input)
                print(f"\n📋 Response:\n{response}")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye! Happy testing!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
    
    def run_demo_scenarios(self):
        """Run demonstration scenarios"""
        print("\n🎯 Running Demo Scenarios...")
        
        scenarios = [
            {
                "name": "Functional Test Generation",
                "description": "Generate test cases for a user login feature",
                "input": """Generate comprehensive functional test cases for a user login feature with the following requirements:
                - Users can login with email and password
                - System should validate email format
                - Password must be at least 8 characters
                - Account gets locked after 3 failed attempts
                - Users can reset password via email
                - Remember me functionality available"""
            },
            {
                "name": "API Test Generation", 
                "description": "Generate API tests for a REST endpoint",
                "input": """Generate API test cases for a user management REST API with these endpoints:
                - POST /api/users (create user)
                - GET /api/users/{id} (get user by ID)
                - PUT /api/users/{id} (update user)
                - DELETE /api/users/{id} (delete user)
                
                Authentication: Bearer token required
                User fields: id, email, name, role, created_at"""
            },
            {
                "name": "Defect Analysis",
                "description": "Analyze a performance defect",
                "input": """Analyze this defect:
                Issue: Application response time is extremely slow (>10 seconds) when loading user dashboard
                Environment: Production web application
                Symptoms: 
                - Dashboard takes 10-15 seconds to load
                - Database queries are timing out
                - High CPU usage on application server
                - Memory usage gradually increasing
                Error logs show: "Connection pool exhausted" and "Query timeout after 30 seconds"
                Recent changes: Added new reporting feature last week"""
            }
        ]
        
        for i, scenario in enumerate(scenarios, 1):
            print(f"\n{'='*60}")
            print(f"📝 Demo {i}: {scenario['name']}")
            print(f"📄 {scenario['description']}")
            print(f"{'='*60}")
            
            try:
                response = self.agent.process_request(scenario['input'])
                print(f"\n📋 Result:\n{response}")
            except Exception as e:
                print(f"❌ Error in demo {i}: {e}")
            
            input("\nPress Enter to continue to next demo...")

def main():
    """Main entry point"""
    print("🚀 Starting Test Engineer Intelligent Assistant MVP")
    
    # Initialize assistant
    assistant = TestEngineerAssistant()
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            assistant.run_demo_scenarios()
        elif sys.argv[1] == "--interactive":
            assistant.run_interactive_mode()
        else:
            print("Usage: python main.py [--demo|--interactive]")
    else:
        # Default to interactive mode
        assistant.run_interactive_mode()

if __name__ == "__main__":
    main()
