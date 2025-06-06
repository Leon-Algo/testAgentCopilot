# 测试工程师智能助手 MVP

一个基于LangChain和OpenAI的综合性AI测试助手，提供自主测试规划、生成和分析能力。支持命令行和Web界面两种使用方式。

## 🎯 功能特性

### 核心功能
1. **功能测试用例生成** - 根据需求生成全面的测试用例
2. **测试缺陷分析** - 分析缺陷、识别根本原因并提供修复建议
3. **接口测试用例生成** - 根据API规范生成接口测试
4. **测试策略规划** - 制定全面的测试策略和计划

### 智能体能力
- **自主规划** - 智能体可以规划和协调多个测试任务
- **多格式支持** - 支持各种输入格式（文本、文档、规范）
- **全面覆盖** - 生成正向、负向和边界测试场景
- **专业输出** - 标准化、行业级测试产物
- **Web界面** - 用户友好的Web操作界面

### 界面支持
- **🌐 Web界面** - 基于Streamlit的现代化Web界面
- **💻 命令行界面** - 支持交互模式和演示模式
- **🔧 编程接口** - 支持直接API调用

## 🏗️ 系统架构

```
测试工程师智能体
├── 功能测试生成工具
├── 缺陷分析工具
├── API测试生成工具
├── 自主规划与协调
└── Web界面 (Streamlit)
```

## 🚀 快速开始

### 环境要求
- Python 3.8+
- OpenAI API 访问权限

### 安装步骤

1. **克隆并设置项目：**
```bash
cd testAgentCopilot
pip install -r requirements.txt
```

2. **配置环境：**
`.env` 文件已配置好API凭据：
```
OPENAI_API_BASE=https://api.chatanywhere.tech/v1
OPENAI_API_KEY=xxx
OPENAI_MODEL=gpt-4o
```

### 使用方法

#### 🌐 Web界面（推荐）
```bash
# 方式1：使用启动脚本
python run_web.py

# 方式2：直接运行Streamlit
streamlit run web_app.py
```
然后在浏览器中访问：http://localhost:8501

#### 💻 命令行界面

**交互模式：**
```bash
python main.py --interactive
```

**演示模式：**
```bash
python main.py --demo
```

#### 🔧 编程接口
```python
from test_engineer_agent import TestEngineerAgent

# 初始化智能体
agent = TestEngineerAgent()

# 生成功能测试用例
result = agent.process_request("""
为用户登录功能生成测试用例，包括邮箱验证、
密码要求和3次失败后账户锁定功能。
""")

print(result)
```

## 📚 使用示例

### 1. 功能测试生成
```python
requirements = """
电商购物车功能：
- 添加/删除商品
- 更新数量
- 计算含税总价
- 应用优惠券
"""

response = agent.process_request(f"为以下需求生成全面的测试用例：{requirements}")
```

### 2. API测试生成
```python
api_spec = """
POST /api/users - 创建用户
GET /api/users/{id} - 获取用户信息
PUT /api/users/{id} - 更新用户信息
DELETE /api/users/{id} - 删除用户
"""

response = agent.process_request(f"为以下API生成Python测试代码：{api_spec}")
```

### 3. 缺陷分析
```python
defect_info = """
问题：登录页面在移动设备上崩溃
错误：认证模块中的JavaScript类型错误
频率：80%的移动用户受影响
"""

response = agent.process_request(f"分析此缺陷：{defect_info}")
```

## 🌐 Web界面功能

### 主要页面
1. **智能对话模式** - 自由对话，系统自动选择合适工具
2. **功能测试生成** - 专门的功能测试用例生成界面
3. **缺陷分析** - 缺陷分析和解决方案推荐界面
4. **API测试生成** - API测试代码生成界面
5. **测试策略规划** - 全面的测试策略制定界面

### Web界面特性
- **响应式设计** - 适配不同屏幕尺寸
- **实时交互** - 即时响应用户输入
- **文件下载** - 支持下载生成的测试用例和报告
- **历史记录** - 保存对话历史
- **多格式输出** - 支持Markdown、Python代码等多种格式

## 🛠️ 工具详情

### 功能测试生成器
- **输入**: 需求描述、格式偏好、覆盖级别
- **输出**: 结构化测试用例（JSON/Gherkin）
- **特性**: 正向/负向/边界用例覆盖，多种格式支持

### 缺陷分析器
- **输入**: 缺陷信息、日志、上下文
- **输出**: 根因分析、解决方案建议
- **特性**: 模式识别、影响评估、预防策略

### API测试生成器
- **输入**: API规范、框架偏好
- **输出**: 可执行测试代码（Python/Postman/curl）
- **特性**: 安全测试、错误处理、多框架支持

## 🎯 应用场景

1. **测试规划** - 创建全面的测试策略
2. **测试自动化** - 生成自动化测试套件
3. **缺陷调查** - 快速分析和解决问题
4. **API测试** - 全面的API验证
5. **质量保证** - 确保全面的测试覆盖
6. **团队协作** - 标准化测试流程

## 📁 项目结构

```
testAgentCopilot/
├── main.py                     # 主应用程序入口
├── web_app.py                  # Web界面应用
├── run_web.py                  # Web应用启动脚本
├── test_engineer_agent.py      # 核心智能体实现
├── config.py                   # 配置设置
├── requirements.txt            # Python依赖
├── .env                        # 环境变量
├── tools/                      # 测试工具包
│   ├── __init__.py
│   ├── functional_test_generator.py
│   ├── defect_analyzer.py
│   └── api_test_generator.py
├── examples/                   # 使用示例
│   └── example_usage.py
├── test_installation.py       # 安装验证
├── README.md                   # 用户文档
└── IMPLEMENTATION_SUMMARY.md   # 实现总结
```

## 🔧 配置说明

系统使用以下配置：
- **API地址**: https://api.chatanywhere.tech/v1
- **模型**: gpt-4o
- **温度参数**: 0.1-0.3（根据任务调整）

## 🚀 高级功能

### 自主规划
智能体可以：
- 分析复杂需求
- 将任务分解为子任务
- 协调多个工具
- 提供全面的交付物

### 多模态支持
- 文本需求
- 文档解析
- API规范
- 错误日志和跟踪

### 集成就绪
- 标准输出格式
- 数据库导入兼容性
- CI/CD流水线集成
- 现有工具兼容性

## 🎯 验证测试

运行安装验证：
```bash
python test_installation.py
```

所有测试应该通过：
- ✅ 导入测试
- ✅ 配置测试
- ✅ 工具初始化测试
- ✅ 智能体初始化测试
- ✅ 基本功能测试

## 🎬 演示视频

### Web界面演示
1. 启动Web应用：`python run_web.py`
2. 访问 http://localhost:8501
3. 选择功能模式
4. 输入需求或问题
5. 获取AI生成的测试用例或分析报告

### 命令行演示
```bash
# 运行演示
python main.py --demo

# 交互模式
python main.py --interactive
```

## 🤝 贡献指南

这是一个MVP实现。未来增强功能可能包括：
- 更多测试框架支持
- 更多输出格式
- 与测试平台集成
- 性能测试能力
- 可视化测试用例管理
- 团队协作功能
- 测试数据管理

## 📞 技术支持

如果遇到问题，请检查：
1. Python版本是否为3.8+
2. 所有依赖是否正确安装
3. API密钥是否有效
4. 网络连接是否正常
5. 端口8501是否被占用（Web界面）

### 常见问题

**Q: Web界面无法启动？**
A: 确保已安装Streamlit：`pip install streamlit`

**Q: API调用失败？**
A: 检查网络连接和API密钥配置

**Q: 生成的测试用例质量不高？**
A: 提供更详细的需求描述，使用合适的覆盖级别

## 📄 许可证

本项目是AI学习计划的一部分，专注于测试自动化和智能测试辅助。

---

**准备好用AI革命化您的测试工作流程！🧪🤖**

### 快速体验
1. 安装依赖：`pip install -r requirements.txt`
2. 启动Web界面：`python run_web.py`
3. 在浏览器中访问：http://localhost:8501
4. 开始您的AI测试之旅！
