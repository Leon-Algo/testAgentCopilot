"""
测试工程师智能助手 - Web界面
基于Streamlit的Web应用程序
"""
import streamlit as st
import json
import time
from test_engineer_agent import TestEngineerAgent
from tools import FunctionalTestGenerator, DefectAnalyzer, APITestGenerator

# 页面配置
st.set_page_config(
    page_title="测试工程师智能助手",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .tool-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 初始化会话状态
if 'agent' not in st.session_state:
    try:
        st.session_state.agent = TestEngineerAgent()
        st.session_state.agent_ready = True
    except Exception as e:
        st.session_state.agent_ready = False
        st.session_state.error_message = str(e)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# 主标题
st.markdown('<h1 class="main-header">🧪 测试工程师智能助手</h1>', unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    st.header("🛠️ 功能选择")
    
    mode = st.selectbox(
        "选择工作模式",
        ["智能对话模式", "功能测试生成", "缺陷分析", "API测试生成", "测试策略规划"]
    )
    
    st.markdown("---")
    
    # 系统状态
    if st.session_state.agent_ready:
        st.success("✅ 系统已就绪")
    else:
        st.error("❌ 系统初始化失败")
        if 'error_message' in st.session_state:
            st.error(f"错误信息: {st.session_state.error_message}")
    
    st.markdown("---")
    
    # 帮助信息
    with st.expander("📖 使用说明"):
        st.markdown("""
        **智能对话模式**: 自由对话，系统自动选择合适的工具
        
        **功能测试生成**: 根据需求生成功能测试用例
        
        **缺陷分析**: 分析缺陷并提供解决方案
        
        **API测试生成**: 生成API测试代码
        
        **测试策略规划**: 制定全面的测试策略
        """)
    
    # 清除历史按钮
    if st.button("🗑️ 清除对话历史"):
        st.session_state.chat_history = []
        st.rerun()

# 主内容区域
if not st.session_state.agent_ready:
    st.error("系统初始化失败，请检查配置后重新启动应用。")
    st.stop()

# 根据选择的模式显示不同界面
if mode == "智能对话模式":
    st.header("💬 智能对话模式")
    st.markdown("与AI助手自由对话，系统会自动选择合适的工具来处理您的请求。")
    
    # 显示对话历史
    for i, (user_msg, ai_msg) in enumerate(st.session_state.chat_history):
        with st.container():
            st.markdown(f"**👤 用户**: {user_msg}")
            st.markdown(f"**🤖 AI助手**: {ai_msg}")
            st.markdown("---")
    
    # 用户输入
    user_input = st.text_area(
        "请输入您的测试需求或问题：",
        height=100,
        placeholder="例如：为用户登录功能生成测试用例，包括邮箱验证和密码要求..."
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🚀 发送", type="primary"):
            if user_input.strip():
                with st.spinner("AI正在思考中..."):
                    try:
                        response = st.session_state.agent.process_request(user_input)
                        st.session_state.chat_history.append((user_input, response))
                        st.rerun()
                    except Exception as e:
                        st.error(f"处理请求时出错: {str(e)}")

elif mode == "功能测试生成":
    st.header("🧪 功能测试用例生成")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        requirements = st.text_area(
            "功能需求描述",
            height=200,
            placeholder="""请详细描述功能需求，例如：
            
用户登录功能：
- 用户可以使用邮箱和密码登录
- 系统应验证邮箱格式
- 密码必须至少8个字符
- 3次失败后账户被锁定
- 用户可以通过邮箱重置密码
- 提供"记住我"功能"""
        )
    
    with col2:
        test_format = st.selectbox(
            "测试用例格式",
            ["standard", "gherkin"],
            help="选择测试用例的输出格式"
        )
        
        coverage_level = st.selectbox(
            "覆盖级别",
            ["basic", "comprehensive", "exhaustive"],
            index=1,
            help="选择测试覆盖的详细程度"
        )
        
        priority_focus = st.selectbox(
            "优先级重点",
            ["high", "medium", "low", "all"],
            help="选择重点关注的优先级"
        )
    
    if st.button("🎯 生成测试用例", type="primary"):
        if requirements.strip():
            with st.spinner("正在生成测试用例..."):
                try:
                    generator = FunctionalTestGenerator()
                    result = generator._run(
                        requirements=requirements,
                        test_format=test_format,
                        coverage_level=coverage_level,
                        priority_focus=priority_focus
                    )
                    
                    st.success("✅ 测试用例生成完成！")
                    st.markdown("### 生成的测试用例")
                    st.markdown(result)
                    
                    # 提供下载功能
                    st.download_button(
                        label="📥 下载测试用例",
                        data=result,
                        file_name=f"test_cases_{int(time.time())}.md",
                        mime="text/markdown"
                    )
                    
                except Exception as e:
                    st.error(f"生成测试用例时出错: {str(e)}")
        else:
            st.warning("请输入功能需求描述")

elif mode == "缺陷分析":
    st.header("🐛 缺陷分析")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        defect_data = st.text_area(
            "缺陷信息",
            height=200,
            placeholder="""请详细描述缺陷信息，例如：

问题：应用程序响应时间极慢（>10秒）加载用户仪表板
环境：生产环境Web应用程序
症状：
- 仪表板加载需要10-15秒
- 数据库查询超时
- 应用服务器CPU使用率高
- 内存使用量逐渐增加
错误日志显示："连接池耗尽"和"查询30秒后超时"
最近更改：上周添加了新的报告功能"""
        )
        
        context = st.text_area(
            "附加上下文信息",
            height=100,
            placeholder="系统环境、版本信息、相关配置等..."
        )
    
    with col2:
        analysis_type = st.selectbox(
            "分析类型",
            ["comprehensive", "quick", "root_cause"],
            help="选择分析的详细程度"
        )
    
    if st.button("🔍 开始分析", type="primary"):
        if defect_data.strip():
            with st.spinner("正在分析缺陷..."):
                try:
                    analyzer = DefectAnalyzer()
                    result = analyzer._run(
                        defect_data=defect_data,
                        analysis_type=analysis_type,
                        context=context
                    )
                    
                    st.success("✅ 缺陷分析完成！")
                    st.markdown("### 分析结果")
                    st.markdown(result)
                    
                    # 提供下载功能
                    st.download_button(
                        label="📥 下载分析报告",
                        data=result,
                        file_name=f"defect_analysis_{int(time.time())}.md",
                        mime="text/markdown"
                    )
                    
                except Exception as e:
                    st.error(f"分析缺陷时出错: {str(e)}")
        else:
            st.warning("请输入缺陷信息")

elif mode == "API测试生成":
    st.header("🔌 API测试用例生成")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        api_specification = st.text_area(
            "API规范描述",
            height=200,
            placeholder="""请描述API规范，例如：

POST /api/users (创建用户)
GET /api/users/{id} (根据ID获取用户)
PUT /api/users/{id} (更新用户)
DELETE /api/users/{id} (删除用户)

认证：需要Bearer token
用户字段：id, email, name, role, created_at"""
        )
    
    with col2:
        test_framework = st.selectbox(
            "测试框架",
            ["requests", "pytest", "postman"],
            help="选择生成测试代码的框架"
        )
        
        output_format = st.selectbox(
            "输出格式",
            ["python", "postman", "curl"],
            help="选择测试代码的输出格式"
        )
        
        coverage_type = st.selectbox(
            "覆盖类型",
            ["basic", "comprehensive", "security"],
            index=1,
            help="选择测试覆盖的类型"
        )
    
    if st.button("⚡ 生成API测试", type="primary"):
        if api_specification.strip():
            with st.spinner("正在生成API测试..."):
                try:
                    generator = APITestGenerator()
                    result = generator._run(
                        api_specification=api_specification,
                        test_framework=test_framework,
                        coverage_type=coverage_type,
                        output_format=output_format
                    )
                    
                    st.success("✅ API测试生成完成！")
                    st.markdown("### 生成的API测试")
                    
                    if output_format == "python":
                        st.code(result, language="python")
                    else:
                        st.markdown(result)
                    
                    # 提供下载功能
                    file_extension = "py" if output_format == "python" else "md"
                    st.download_button(
                        label="📥 下载测试代码",
                        data=result,
                        file_name=f"api_tests_{int(time.time())}.{file_extension}",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"生成API测试时出错: {str(e)}")
        else:
            st.warning("请输入API规范描述")

elif mode == "测试策略规划":
    st.header("📋 测试策略规划")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        project_requirements = st.text_area(
            "项目需求",
            height=200,
            placeholder="""请描述项目需求，例如：

项目：移动银行应用程序

需要测试的功能：
1. 用户认证（生物识别、PIN、密码）
2. 账户余额查看
3. 账户间转账
4. 账单支付
5. 交易历史
6. 推送通知
7. 离线模式功能

约束条件：
- 高安全性要求
- 必须在iOS和Android上运行
- 性能关键（<2秒响应时间）
- 需要监管合规
- 需要24/7可用性"""
        )
        
        project_context = st.text_area(
            "项目上下文",
            height=100,
            placeholder="项目背景、技术栈、团队情况、时间限制等..."
        )
    
    with col2:
        st.markdown("### 策略选项")
        include_api = st.checkbox("包含API测试", value=True)
        include_performance = st.checkbox("包含性能测试", value=True)
        include_security = st.checkbox("包含安全测试", value=True)
        include_automation = st.checkbox("包含自动化建议", value=True)
    
    if st.button("📊 生成测试策略", type="primary"):
        if project_requirements.strip():
            with st.spinner("正在制定测试策略..."):
                try:
                    strategy_prompt = f"""
                    为以下项目制定全面的测试策略：
                    
                    项目需求：{project_requirements}
                    项目上下文：{project_context}
                    
                    请包括：
                    1. 测试范围和目标
                    2. 测试类型和方法
                    3. 测试用例生成建议
                    4. 缺陷分析方法
                    5. 工具和框架推荐
                    6. 时间线和资源估算
                    7. 风险评估和缓解措施
                    {"8. API测试策略" if include_api else ""}
                    {"9. 性能测试策略" if include_performance else ""}
                    {"10. 安全测试策略" if include_security else ""}
                    {"11. 自动化测试建议" if include_automation else ""}
                    """
                    
                    result = st.session_state.agent.process_request(strategy_prompt)
                    
                    st.success("✅ 测试策略生成完成！")
                    st.markdown("### 测试策略")
                    st.markdown(result)
                    
                    # 提供下载功能
                    st.download_button(
                        label="📥 下载测试策略",
                        data=result,
                        file_name=f"test_strategy_{int(time.time())}.md",
                        mime="text/markdown"
                    )
                    
                except Exception as e:
                    st.error(f"生成测试策略时出错: {str(e)}")
        else:
            st.warning("请输入项目需求")

# 页脚
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        🧪 测试工程师智能助手 | 基于LangChain和OpenAI | 
        <a href='https://github.com' target='_blank'>GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
