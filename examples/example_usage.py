"""
Example usage of the Test Engineer Intelligent Assistant
Demonstrates various capabilities and use cases
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_engineer_agent import TestEngineerAgent
import json

def example_functional_test_generation():
    """Example: Generate functional test cases"""
    print("🧪 Example: Functional Test Case Generation")
    print("-" * 50)
    
    agent = TestEngineerAgent()
    
    requirements = """
    E-commerce Shopping Cart Feature:
    - Users can add products to cart
    - Users can update quantities
    - Users can remove items from cart
    - Cart calculates total price including tax
    - Cart persists across browser sessions
    - Maximum 10 items per product
    - Discount codes can be applied
    """
    
    result = agent.process_request(f"""
    Generate comprehensive functional test cases for this e-commerce shopping cart feature:
    {requirements}
    
    Please use standard format and include positive, negative, and edge cases.
    """)
    
    print("📋 Generated Test Cases:")
    print(result)
    return result

def example_api_test_generation():
    """Example: Generate API test cases"""
    print("\n🔌 Example: API Test Case Generation")
    print("-" * 50)
    
    agent = TestEngineerAgent()
    
    api_spec = """
    Product API Specification:
    
    POST /api/products
    - Creates a new product
    - Body: {"name": "string", "price": "number", "category": "string", "description": "string"}
    - Returns: 201 with product object, 400 for validation errors
    
    GET /api/products/{id}
    - Retrieves product by ID
    - Returns: 200 with product object, 404 if not found
    
    PUT /api/products/{id}
    - Updates existing product
    - Body: Same as POST
    - Returns: 200 with updated product, 404 if not found, 400 for validation errors
    
    DELETE /api/products/{id}
    - Deletes product by ID
    - Returns: 204 on success, 404 if not found
    
    Authentication: Bearer token required for all operations
    """
    
    result = agent.process_request(f"""
    Generate comprehensive API test cases in Python using requests library for:
    {api_spec}
    
    Include positive scenarios, negative scenarios, authentication testing, and error handling.
    """)
    
    print("📋 Generated API Tests:")
    print(result)
    return result

def example_defect_analysis():
    """Example: Analyze a defect"""
    print("\n🐛 Example: Defect Analysis")
    print("-" * 50)
    
    agent = TestEngineerAgent()
    
    defect_info = """
    Defect Report:
    Title: User registration fails with database connection error
    
    Description:
    When users try to register new accounts, the system shows "Database connection failed" error.
    This started happening after the recent deployment on Friday.
    
    Environment: Production
    Browser: Chrome, Firefox (both affected)
    
    Error Details:
    - Error message: "Unable to connect to database server"
    - HTTP Status: 500 Internal Server Error
    - Frequency: 100% of registration attempts
    - Time: Started Friday 3 PM after deployment
    
    Logs:
    [ERROR] DatabaseConnectionPool: Connection timeout after 30 seconds
    [ERROR] UserService: Failed to create user - database unavailable
    [WARN] ConnectionManager: Pool size exceeded maximum limit (50)
    
    Recent Changes:
    - Updated user service to include new profile fields
    - Migrated to new database server
    - Added email verification feature
    """
    
    result = agent.process_request(f"""
    Perform comprehensive defect analysis for this issue:
    {defect_info}
    
    Provide root cause analysis, impact assessment, resolution strategy, and prevention recommendations.
    """)
    
    print("📋 Defect Analysis:")
    print(result)
    return result

def example_testing_strategy():
    """Example: Create testing strategy"""
    print("\n📋 Example: Testing Strategy Planning")
    print("-" * 50)
    
    agent = TestEngineerAgent()
    
    project_requirements = """
    Project: Mobile Banking Application
    
    Features to test:
    1. User authentication (biometric, PIN, password)
    2. Account balance viewing
    3. Money transfers between accounts
    4. Bill payments
    5. Transaction history
    6. Push notifications
    7. Offline mode capabilities
    
    Constraints:
    - High security requirements
    - Must work on iOS and Android
    - Performance critical (< 2 second response times)
    - Regulatory compliance required
    - 24/7 availability needed
    """
    
    result = agent.plan_testing_strategy(project_requirements, "Mobile banking with strict security and performance requirements")
    
    print("📋 Testing Strategy:")
    print(result['strategy'])
    return result

def example_comprehensive_test_suite():
    """Example: Generate comprehensive test suite"""
    print("\n📦 Example: Comprehensive Test Suite Generation")
    print("-" * 50)
    
    agent = TestEngineerAgent()
    
    requirements = """
    Online Food Ordering System:
    - Browse restaurants and menus
    - Add items to cart with customizations
    - Apply promo codes and discounts
    - Choose delivery or pickup
    - Process payments (credit card, digital wallet)
    - Track order status in real-time
    - Rate and review orders
    """
    
    api_spec = """
    Key APIs:
    - GET /api/restaurants (list restaurants)
    - GET /api/restaurants/{id}/menu (get menu)
    - POST /api/orders (create order)
    - GET /api/orders/{id}/status (track order)
    - POST /api/payments (process payment)
    """
    
    result = agent.generate_comprehensive_test_suite(
        requirements=requirements,
        include_api=True,
        api_spec=api_spec
    )
    
    print("📋 Comprehensive Test Suite:")
    print(result['test_suite'])
    return result

def main():
    """Run all examples"""
    print("🚀 Test Engineer Intelligent Assistant - Examples")
    print("=" * 60)
    
    examples = [
        ("Functional Test Generation", example_functional_test_generation),
        ("API Test Generation", example_api_test_generation),
        ("Defect Analysis", example_defect_analysis),
        ("Testing Strategy", example_testing_strategy),
        ("Comprehensive Test Suite", example_comprehensive_test_suite)
    ]
    
    for name, example_func in examples:
        try:
            print(f"\n🎯 Running: {name}")
            example_func()
            input("\nPress Enter to continue to next example...")
        except Exception as e:
            print(f"❌ Error in {name}: {e}")
            input("\nPress Enter to continue...")
    
    print("\n✅ All examples completed!")

if __name__ == "__main__":
    main()
