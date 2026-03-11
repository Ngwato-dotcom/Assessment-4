Phase 3 Python Playwright Assessment
This project contains automated end-to-end tests for the Demo Web Shop website using Python, Pytest, and the Playwright framework. The project follows the Page Object Model (POM) design pattern to ensure tests are maintainable and easy to read.

Project Structure
tests/: Contains the test files (test_login.py, test_registration_page.py, test_checkout.py).

pages/: Contains Page Object classes for page interactions.

conftest.py: Contains global fixtures, including user registration and credential handling.

requirements.txt: Lists the necessary dependencies.

Setup Steps
Follow these steps to set up the project on your local machine:

Extract the ZIP file and open the Phase3Assessment folder in your terminal or IDE.

Create a Virtual Environment:
python -m venv .venv

Activate the Virtual Environment:

Windows: .venv\Scripts\activate

macOS/Linux: source .venv/bin/activate

To Install Dependencies:
pip install -r requirements.txt

To Install Playwright Browsers:
playwright install

To Run Command(s)
To run the full test suite, use the following commands in the terminal:

To Run all tests (Headed mode):
pytest --headed

To Run all tests (Headless mode):
pytest

To Run a specific test file:
pytest tests/test_login.py --headed