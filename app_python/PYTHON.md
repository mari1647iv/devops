# Python Web Application Description

## Python Best Practices

- Code repository and version control
  - `README.md` placed in the root folder
  - `requirements.txt` with project dependencies placed in the root
  - `__init__.py` to mark the folder as a package
  - `setup.py` with set up script placed in the root
  - license for the repository placed in the root
  - `.gitignore` to list the files and directories to be ignored by git 
- Readable documentation
  - `README.md` in Markdown using readme template
- Style Guideline - PEP 8
- Immediate Correction of Broken Code
- The Zen of Python
- Separate Virtual Environment for Each Project
- Avoid Importing Everything from Package
- Use Linters:
  - `pylint` - for Python
  - `markdownlint` - for Markdown

## Application Unit Tests

I decided to test the `moscow_time()` help function, that returns current time in Moscow, Russia,  the final `index()` function, that returns html code in string format that will display the current Moscow time on the web page and the flask app start. To implement this task I used the `unittest` Python framework.

To test the start of Flask application I check whether the app has something on the home page `'/'`.

To test the `moscow_time()` function I need to check if the result equals to the current time. Because of the processing time difference the comparison does not include microseconds.

To test `index()` function I need to be sure that it will display the actually updated time in Moscow, therefore I introduced the `.assertIn` check to verify the resulting string contains current Moscow time in string format.

## Unit Testing Best Practices

- Tests should be fast
- Tests should be simple
- Test shouldn’t duplicate implementation logic
- Tests should be readable, cause they double as a form of documentation
  - One logical assertion per method
  - Arrange-Act-Assert pattern
  - BDD-style test cases - Given/When/Then pattern (alternative to AAA)
- Tests should be deterministic and completely isolated
- Make sure they’re part of the build process
- Unit tests should verify a single use case
- Use framework for unit testing:
  - `unittest` - for Python
- Use naming conventions
  - `name of the code/unit + test` separated by an underscore or `test + name of the code/unit` separated by an underscore
- Start with a smallest testable unit of your code, then move on to other units and see how they interact with each other
