# Test Automation Final Project

A comprehensive multi-platform test automation framework covering Web (E-commerce), API, Database, Mobile, Electron, and Windows Desktop applications — built with Selenium WebDriver, Appium, Pytest, and Allure reporting.

## About

This project is a Page Object Model (POM) test automation framework spanning six testing surfaces:

| Suite | Target |
|---|---|
| Web | ATID Store e-commerce site |
| API | Grafana teams API |
| Database | PostgreSQL (Supabase) |
| Mobile | UK Mortgage Calculator (Android) |
| Electron | Todolist desktop app |
| Desktop | Windows Calculator |

**Testing Scope:**
- Web: product search, filtering/sorting, cart add/view/remove, cart validation
- API: create/read/update/delete a Grafana team, status code and field verification
- Database: pull product data from PostgreSQL and verify it against the web UI
- Mobile: mortgage repayment calculation, saved transaction verification, swipe/delete
- Electron: add tasks and verify task list count
- Desktop: calculator arithmetic and result verification

## Project Overview

The framework is built around:

- **Page Object Model** — locators and element access separated per application
- **Workflows layer** — reusable multi-step user flows built on top of page objects
- **Data-Driven Configuration** — URLs, credentials, timeouts, and test data are externalized so tests can change without touching code
- **Cross-Browser Support** — Chrome, Firefox, or Edge, selected via config
- **Allure Reporting** — step-by-step HTML reports with screenshots attached on failure
- **Soft Assertions** — a test can report multiple failed checks instead of stopping at the first
- **Event Listener** — every driver logs navigation, find, and click events during execution
- **Screenshot on Failure** — a failure hook automatically attaches a screenshot to the Allure report
- **Teardown Handling** — each suite resets app state after every test (clear cart, empty task list, clear calculator)
- **WebDriver Manager** — automatic driver binary management for web browsers

## Project Structure

```
test_automation_final_project/
├── configuration/
│   └── data.xml              # All environment/test config (URLs, creds, timeouts, per-suite settings)
├── page_objects/
│   ├── web_objects/          # Home, search results, product, cart
│   ├── mobile_objects/       # Mortgage calculator, saved transactions
│   ├── electron_objects/     # Todolist tasks
│   └── desktop_objects/      # Windows Calculator
├── workflows/                 # Reusable flows built on page objects (web, api, db, mobile, electron, desktop)
├── extensions/                 # Low-level actions: UI, mobile gestures, API calls, DB queries, verifications
├── utilities/                  # Config reader, page manager, event listener, wait/price helpers
├── test_cases/
│   ├── conftest.py            # Driver fixtures for all six suites + screenshot-on-fail hook
│   ├── test_web.py
│   ├── test_web_db.py
│   ├── test_api.py
│   ├── test_mobile.py
│   ├── test_electron.py
│   └── test_desktop.py
├── .env.example                # Placeholder for DB_USER / DB_PASS (copy to .env locally)
├── requirements.txt            # Web / API / DB dependencies (Selenium 4)
└── mobile-requirements.txt     # Mobile / Electron / Desktop overlay (Selenium 3 + Appium 1.x)
```

## Tools and Frameworks Used

### Core Testing
- **Python** — programming language
- **Pytest 8.4.2** — test framework
- **Selenium WebDriver** — `4.36.0` for web; `3.141.0` for mobile/electron/desktop (see [Two Requirements Files](#two-requirements-files) below)
- **Appium-Python-Client 1.3.0** — mobile (Android) and Windows Desktop (WinAppDriver) automation

### Reporting & Assertions
- **Allure (`allure-pytest` 2.15.3)** — HTML reports with steps, titles, descriptions, and failure screenshots
- **smart-assertions 1.0.2** — soft assertions (continue after a failed check) and hard assertion helpers

### Data & Integrations
- **psycopg2-binary 2.9.12** — PostgreSQL connection for the DB-driven web test
- **python-dotenv 1.2.1** — loads local `.env` values for database credentials
- **requests 2.32.5** — HTTP client for the Grafana API tests

### Browser/Driver Management
- **webdriver-manager 4.0.2** — automatic Chrome/Firefox/Edge driver downloads
- **Supported browsers:** Chrome, Firefox, Edge

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git (optional, for version control)
- One of the supported browsers: Chrome, Firefox, or Edge (for web tests)
- For mobile: Appium server + Android device/emulator with the mortgage calculator app installed
- For Electron: the Todolist app + matching Electron chromedriver
- For Desktop: WinAppDriver running + Windows Calculator
- For DB tests: network access to the configured PostgreSQL instance
- For API tests: a reachable Grafana instance

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env        # then fill in DB_USER and DB_PASS
```

### Database credentials

`DB_User` and `DB_Pass` are not stored in `data.xml`. Copy `.env.example` to `.env` in the project root and set:

```
DB_USER=
DB_PASS=
```

`.env` is gitignored and stays on your machine. The DB tests read these values through `get_data`.

### Two requirements files

Web/API/DB uses **Selenium 4**; Mobile/Electron/Desktop uses **Appium 1.x**, which requires **Selenium 3.141**. These cannot be installed at the same time, so switch as needed:

```bash
# Web, API, DB tests
pip install -r requirements.txt

# Mobile, Electron, Desktop tests
pip install -r mobile-requirements.txt
```

## Configuration

Non-secret runtime settings are in [`configuration/data.xml`](configuration/data.xml): wait times, screenshot path, browser choice, store URL/test data, Grafana API credentials, mobile device/app IDs, Electron app paths, WinAppDriver settings, and DB host/port/name.

`get_data` loads that XML using a path relative to the project, so it works from any working directory. Database username and password come from `.env` (see Setup). Electron app paths in `data.xml` are still machine-specific and need updating on another PC.

## Running Tests

```bash
# Run everything currently installable (web/API/DB suites)
pytest test_cases/test_web.py test_cases/test_web_db.py test_cases/test_api.py

# Run a single suite
pytest test_cases/test_web.py -v

# Generate an Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

Mobile, Electron, and Desktop tests require `mobile-requirements.txt` installed and their respective drivers/apps running (see Prerequisites).
