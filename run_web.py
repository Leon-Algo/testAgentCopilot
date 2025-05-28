"""
测试工程师智能助手 - Web应用启动脚本
"""
import subprocess
import sys
import os

def check_dependencies():
    """检查依赖是否安装"""
    try:
        import streamlit
        print("✅ Streamlit 已安装")
        return True
    except ImportError:
        print("❌ Streamlit 未安装")
        return False

def install_dependencies():
    """安装依赖"""
    print("正在安装依赖...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ 依赖安装完成")
        return True
    except subprocess.CalledProcessError:
        print("❌ 依赖安装失败")
        return False

def run_streamlit():
    """运行Streamlit应用"""
    print("🚀 启动Web应用...")
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "web_app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 应用已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")

def main():
    """主函数"""
    print("🧪 测试工程师智能助手 - Web版本")
    print("=" * 50)
    
    # 检查当前目录
    if not os.path.exists("web_app.py"):
        print("❌ 请在项目根目录下运行此脚本")
        return
    
    # 检查依赖
    if not check_dependencies():
        print("正在安装缺失的依赖...")
        if not install_dependencies():
            print("请手动运行: pip install -r requirements.txt")
            return
    
    # 运行应用
    print("\n📱 Web应用将在浏览器中打开")
    print("🌐 访问地址: http://localhost:8501")
    print("⏹️  按 Ctrl+C 停止应用")
    print("-" * 50)
    
    run_streamlit()

if __name__ == "__main__":
    main()
