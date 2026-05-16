# Test Automation Final Project
A comprehensive E-commerce test automation framework for testing the ATID Store web application using Selenium WebDriver, Pytest, and Allure reporting.

## About
This project is a Selenium-based test automation framework for the ATID Store e-commerce application.
The framework follows the Page Object Model (POM) design pattern and focuses on maintainability, scalability, and reusable test architecture.

**Target Application**: [ATID Store](https://atid.store/store/)

**Testing Scope**:
- Product search functionality
- Product selection and navigation
- Shopping cart operations
- Price filtering and sorting
- Cart validation and verification

## Project Overview
This framework is built on a solid architectural foundation that emphasizes:
- Page Object Model: Clean separation of page structure and test logic, improving maintainability
- Data-Driven Testing: XML-based configuration for easy test data management without code changes
- Cross-Browser Support: Seamlessly run tests on Chrome, Firefox, or Edge browsers
- Allure Reporting: Rich, interactive HTML test reports with step-by-step execution details
- Soft Assertions: Continue test execution after assertion failures to gather all issues
- Screenshot on Failure: Automatic screenshot capture and attachment for failed tests
- Event Listener: Custom logging and monitoring of all Selenium WebDriver events
- Smart Waits: Implicit waits and explicit wait mechanisms for stable element interactions
- Modular Architecture: Clear separation of concerns across different layers (Page Objects, Workflows, Utilities, Tests)
- WebDriver Manager: Automatic browser driver download and management
- Teardown Handling: Automatic cart cleanup after each test execution

## Tools and Frameworks Used
### Core Testing
- **Python 3.9+** - Programming language
- **Pytest 8.4.2** - Testing framework for writing and executing tests
- **Selenium WebDriver 4.1.0** - Browser automation and interaction

### Reporting & Assertions
- **Allure Reports (allure-pytest 2.15.3)** - Rich HTML test reporting with screenshots
- **pytest-check 2.6.2** - Soft assertions for continuing tests after failures
- **smart-assertions 1.0.2** - Enhanced assertion capabilities

### Browser Management
- **WebDriver Manager 4.0.2** - Automatic browser driver management
- **Supported Browsers**: Chrome, Firefox, Edge

### Additional Libraries
- **python-dotenv 1.2.1** - Environment variable management
- **requests 2.32.5** - HTTP library for API interactions
- **selenium support libraries** - Waits, expected conditions, event handling

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git (optional, for version control)
- One of the supported browsers: Chrome, Firefox, or Edge

