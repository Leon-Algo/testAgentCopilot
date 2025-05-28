"""
测试Web应用的基本功能
"""
import sys
import os

def test_web_app_imports():
    """测试Web应用的导入"""
    print("🧪 测试Web应用导入...")
    
    try:
        import streamlit as st
        print("✅ Streamlit导入成功")
        
        # 测试主要组件导入
        from test_engineer_agent import TestEngineerAgent
        print("✅ TestEngineerAgent导入成功")
        
        from tools import FunctionalTestGenerator, DefectAnalyzer, APITestGenerator
        print("✅ 工具模块导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 导入失败: {e}")
        return False

def test_agent_initialization():
    """测试智能体初始化"""
    print("\n🤖 测试智能体初始化...")
    
    try:
        from test_engineer_agent import TestEngineerAgent
        agent = TestEngineerAgent()
        print("✅ 智能体初始化成功")
        
        # 测试工具信息获取
        tool_info = agent.get_tool_info()
        print(f"✅ 可用工具: {list(tool_info.keys())}")
        
        return True
    except Exception as e:
        print(f"❌ 智能体初始化失败: {e}")
        return False

def test_web_app_structure():
    """测试Web应用文件结构"""
    print("\n📁 测试Web应用文件结构...")
    
    required_files = [
        "web_app.py",
        "run_web.py", 
        "test_engineer_agent.py",
        "config.py",
        "requirements.txt"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
        else:
            print(f"✅ {file} 存在")
    
    if missing_files:
        print(f"❌ 缺少文件: {missing_files}")
        return False
    
    print("✅ 所有必需文件都存在")
    return True

def main():
    """主测试函数"""
    print("🌐 测试工程师智能助手 - Web应用测试")
    print("=" * 50)
    
    tests = [
        ("文件结构测试", test_web_app_structure),
        ("导入测试", test_web_app_imports),
        ("智能体初始化测试", test_agent_initialization)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} 通过")
            else:
                print(f"❌ {test_name} 失败")
        except Exception as e:
            print(f"❌ {test_name} 异常: {e}")
    
    print(f"\n{'='*50}")
    print(f"📊 测试结果: {passed}/{total} 测试通过")
    
    if passed == total:
        print("🎉 Web应用准备就绪！")
        print("\n🚀 启动Web应用:")
        print("   python run_web.py")
        print("   或")
        print("   streamlit run web_app.py")
        print("\n🌐 然后访问: http://localhost:8501")
    else:
        print("⚠️ 部分测试失败，请检查错误信息")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
