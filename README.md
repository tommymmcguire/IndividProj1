
[![CI](https://github.com/tommymmcguire/IndividProj1/actions/workflows/python.yml/badge.svg)](https://github.com/tommymmcguire/IndividProj1/actions/workflows/python.yml)

[![Install](https://github.com/tommymmcguire/IndividProj1/actions/workflows/install.yml/badge.svg)](https://github.com/tommymmcguire/IndividProj1/actions/workflows/install.yml)
[![Lint](https://github.com/tommymmcguire/IndividProj1/actions/workflows/lint.yml/badge.svg)](https://github.com/tommymmcguire/IndividProj1/actions/workflows/lint.yml)
[![Format](https://github.com/tommymmcguire/IndividProj1/actions/workflows/format.yml/badge.svg)](https://github.com/tommymmcguire/IndividProj1/actions/workflows/format.yml)
[![Test](https://github.com/tommymmcguire/IndividProj1/actions/workflows/test.yml/badge.svg)](https://github.com/tommymmcguire/IndividProj1/actions/workflows/test.yml)

---
**Walk Through Youtube Video**
[Youtube](https://youtu.be/NBLgnxiIn5I)


---
**About**

This project serves as a practical example of how to implement Continuous Integration (CI) using GitHub Actions in Python-based Data Science projects. This will contribute to the upkeep of code quality and uniformity during the development cycle through automation. The workflows, which encompass tasks like lint, format, install, and test, ensure that these essential processes are triggered each time code changes are pushed or pull requests are made to the repository. This ultimately leads to faster and more reliable software delivery.

---

**Details**

This project uses the Python libraries ruff, black, and polars to ensure code quality, consistency, and efficient data manipulation.

--- 

**Files**

  - descriptivestats.py
      - Performs descriptive statistics using Polars
   
  - descriptivestats.ipynb
      - Jupyter notebook that performs the same descriptive statistics

  - lib.py
      - Shares the common code between the script and the notebook

  - Makefile
      - Install: install dependencies
      - Test: runs tests
      - Format: formats the code using black
      - Lint: lints the code using ruff
      - All: performs all
   
  - Workflows (.github/workflows): used to automate various aspects of the software development lifecycle, including building, testing, and 
    deploying code.
      - format.yml
      - install.yml
      - lint.yml
      - python.yml
      - test.yml

  - requirements.txt
      - All of the dependencies to be installed

`make install` to install, `make lint` to lint, `make format` to format, `make test` to perform tests
   
--- 

### Visualization of the distribution of wine ratings
Also found in (output/wine_rating.png)
  
![wine_rating](https://github.com/tommymmcguire/pandasdescript/assets/141086024/4703fd7b-7e56-4b55-8adb-4fea7237eea1)

### Descriptive Statistics
Also found in (output/summary_stats.md)

<img width="998" alt="Screen Shot 2023-09-14 at 10 10 26 AM" src="https://github.com/tommymmcguire/polarsdescript/assets/141086024/6db5f72d-5ff2-48c2-9263-60e3cf5ffc59">

