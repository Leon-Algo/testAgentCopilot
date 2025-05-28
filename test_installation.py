"""
Test script to verify the Test Engineer Intelligent Assistant installation
"""
import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import config
        print("✅ Config module imported successfully")
        
        from tools import FunctionalTestGenerator, DefectAnalyzer, APITestGenerator
        print("✅ Tools imported successfully")
        
        from test_engineer_agent import TestEngineerAgent
        print("✅ Agent imported successfully")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_configuration():
    """Test configuration settings"""
    print("\n🔧 Testing configuration...")
    
    try:
        import config
        
        # Check required config values
        if not config.OPENAI_API_KEY:
            print("❌ OPENAI_API_KEY not configured")
            return False
        
        if not config.OPENAI_API_BASE:
            print("❌ OPENAI_API_BASE not configured")
            return False
            
        if not config.OPENAI_MODEL:
            print("❌ OPENAI_MODEL not configured")
            return False
        
        print(f"✅ API Base: {config.OPENAI_API_BASE}")
        print(f"✅ Model: {config.OPENAI_MODEL}")
        print(f"✅ API Key: {'*' * 20}...{config.OPENAI_API_KEY[-4:]}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_tool_initialization():
    """Test that tools can be initialized"""
    print("\n🛠️ Testing tool initialization...")
    
    try:
        from tools import FunctionalTestGenerator, DefectAnalyzer, APITestGenerator
        
        # Test functional test generator
        func_gen = FunctionalTestGenerator()
        print(f"✅ Functional Test Generator: {func_gen.name}")
        
        # Test defect analyzer
        defect_analyzer = DefectAnalyzer()
        print(f"✅ Defect Analyzer: {defect_analyzer.name}")
        
        # Test API test generator
        api_gen = APITestGenerator()
        print(f"✅ API Test Generator: {api_gen.name}")
        
        return True
    except Exception as e:
        print(f"❌ Tool initialization error: {e}")
        return False

def test_agent_initialization():
    """Test that the main agent can be initialized"""
    print("\n🤖 Testing agent initialization...")
    
    try:
        from test_engineer_agent import TestEngineerAgent
        
        agent = TestEngineerAgent()
        print("✅ Test Engineer Agent initialized successfully")
        
        # Test tool info
        tool_info = agent.get_tool_info()
        print(f"✅ Available tools: {list(tool_info.keys())}")
        
        return True
    except Exception as e:
        print(f"❌ Agent initialization error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality with a simple request"""
    print("\n🧪 Testing basic functionality...")
    
    try:
        from test_engineer_agent import TestEngineerAgent
        
        agent = TestEngineerAgent()
        
        # Simple test request
        test_request = "What testing tools are available?"
        print(f"📝 Test request: {test_request}")
        
        response = agent.process_request(test_request)
        
        if response and len(response) > 10:
            print("✅ Agent responded successfully")
            print(f"📋 Response preview: {response[:100]}...")
            return True
        else:
            print("❌ Agent response was empty or too short")
            return False
            
    except Exception as e:
        print(f"❌ Basic functionality test error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Test Engineer Intelligent Assistant - Installation Test")
    print("=" * 60)
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_configuration),
        ("Tool Initialization Test", test_tool_initialization),
        ("Agent Initialization Test", test_agent_initialization),
        ("Basic Functionality Test", test_basic_functionality)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} FAILED with exception: {e}")
    
    print(f"\n{'='*60}")
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Installation is successful.")
        print("🚀 You can now run: python main.py --interactive")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
        print("💡 Make sure all dependencies are installed: pip install -r requirements.txt")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
