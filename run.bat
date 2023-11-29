@echo off

echo Activating the virtual environment...
call venv\Scripts\activate

echo Running Pytest...
pytest --alluredir=test_results/report_allure

echo Generating Allure reports...
allure serve test_results/report_allure

echo Deactivating the virtual environment...
deactivate