1. install python
- https://www.python.org/
- when installing, must be enabled "Add python.exe to PATH"
2. install pytest
- run in the command line: "pip install -U pytest"
- check that `pytest` is installed correctly: "pytest --version"
- update "pip" if necessary: "python -m pip install --upgrade pip"
3. install selenium
- run in the command line "pip install selenium"
- check that `selenium` is installed correctly: "pip show selenium"
4. run tests
- "pytest <test_name.py>" - by default, the browser "Chrome" and the environment "production" are used
- "pytest <test_name.py> --browser=firefox --env=test" - setting the necessary parameters for the browser or environment