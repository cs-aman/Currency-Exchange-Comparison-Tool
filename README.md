# Currency Exchange Comparison Tool
<br>
Currency Exchange Rate Comparison Tool Compares exchange rates between two currencies using different APIs like Fixer and Currency Beacon, helping users to find the best exchange rate along with rates they can get!"
 
# Table Of Contents
<br>
1.<a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/tree/main?tab=readme-ov-file#features">Features</a> <br>
2.<a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/tree/main?tab=readme-ov-file#pre-requisites">Pre-Requisites</a> <br>
3.<a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/tree/main?tab=readme-ov-file#code-file">Code File</a><br>
4.<a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/tree/main?tab=readme-ov-file#git">Git</a> <br>
5.<a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/tree/main?tab=readme-ov-file#uml">UML</a> <br> 
6.<a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/tree/main?tab=readme-ov-file#metrices">Metrices</a> <br> 
7.<a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/tree/main?tab=readme-ov-file#clean-code-development">Clean Code Development</a> <br> 

# Features
<br>
1. Allows users to compare exchange rates between two currencies.<br style="line-height: 0.5;"> 
2. Aims to help users find the best exchange rate available.<br  style="line-height: 0.5;"> 
3. Utilizes different APIs such as Fixer and Currency Beacon to retrieve exchange rates.<br style="line-height: 0.5;"> 

# Pre-Requisites
1. Ensure Python is installed on your system. You can download and install Python from <a href="https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe">here</a>.<br style="line-height: 0.5;">

2. Install the Requests library using pip (pip install requests). This library allows you to make HTTP requests, which is necessary to communicate with APIs like Fixer and Currency Beacon.<br style="line-height: 0.5;">

3. Obtain an API key from Fixer (or any other currency exchange API service you intend to use) to authenticate and access their services. If using Currency Beacon, acquire an API key for their services as well.<br style="line-height: 0.5;">

4. Install Visual Studio Code for editing and running your Python code from <a href="https://code.visualstudio.com/download">here</a>.<br style="line-height: 0.5;">

5. A stable internet connection is required to fetch data from the APIs.<br style="line-height: 0.5;">

# Code File 
 You can find the link <a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/blob/d5f2bb9caace9c4e5df23c522f043b95a929f96f/Python/code-file.py">here</a> to access the code and see how I built this project. 

# Git 
Usage of GitHub for the whole project time.<br style="line-height:1.5;">
→<a href='https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/commits/main/'>commit history here</a>.

# UML 
UML Diagramm created with Planttext (Activity, Class, Component Diagrams for the project with Edlich's Fund)<br style="line-height: 1.5;"> 
→<a href='https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/tree/main/uml-diagram'>UML PNG here</a>.

# Requirement Engineering 
In any undertaking, whether it's developing a Python application or assembling a piece of furniture, there are specific criteria to consider. For instance, in my current project, the key requirements are outlined below.

<b>1. API Interaction: <b>
The code relies on the requests library to communicate with external APIs, retrieving exchange rate data.

<b>2. Functions: <b>
get_exchange_rate Function: This function is designed to fetch exchange rate data from an API. It handles potential errors that might occur during the request and returns the data in JSON format.

<b>3. Compare_exchange_rates Function: <b>

API URLs Construction: It constructs URLs for both Fixer and Currency Beacon services using the specified currency pair.
Data Retrieval: It fetches exchange rate data from these APIs, then compares the rates retrieved.
Output Handling: The function prints the exchange rates and indicates which API offers a more favorable rate, or if both rates are identical.

<b>4. External Services:<b>
Fixer API: It's used to obtain exchange rate data.
Currency Beacon API: Another service used to retrieve exchange rates for comparison purposes.

<b>5. Additional Aspects:<b>
API Keys: Ensure valid keys are integrated into the code for both Fixer and Currency Beacon services.
Currency Pair: The functionality expects two specific currencies for comparison.
Output Presentation: Currently, the output is displayed in the console; other means of presentation or logging might be considered

# Metrices 
[![SonarCloud Mentainability](https://sonarcloud.io/api/project_badges/measure?project=cs-aman_Currency-Exchange-Comparison-Tool&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=cs-aman_Currency-Exchange-Comparison-Tool)
[![SonarCloud Bugs](https://sonarcloud.io/api/project_badges/measure?project=cs-aman_Currency-Exchange-Comparison-Tool&metric=bugs)](https://sonarcloud.io/summary/new_code?id=cs-aman_Currency-Exchange-Comparison-Tool)
[![SonarCloud Reliability](https://sonarcloud.io/api/project_badges/measure?project=cs-aman_Currency-Exchange-Comparison-Tool&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=cs-aman_Currency-Exchange-Comparison-Tool)
[![SonarCloud Duplicated Lines Density](https://sonarcloud.io/api/project_badges/measure?project=cs-aman_Currency-Exchange-Comparison-Tool&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=cs-aman_Currency-Exchange-Comparison-Tool)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=cs-aman_Currency-Exchange-Comparison-Tool&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=cs-aman_Currency-Exchange-Comparison-Tool)
[![SonarCloud Security](https://sonarcloud.io/api/project_badges/measure?project=cs-aman_Currency-Exchange-Comparison-Tool&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=cs-aman_Currency-Exchange-Comparison-Tool)
[![SonarCloud Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=cs-aman_Currency-Exchange-Comparison-Tool&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cs-aman_Currency-Exchange-Comparison-Tool)

# Clean Code Development
Adding clean code development for enhancing code usability, readability, and maintenance, promoting improved usage.<br>
→<a href="https://github.com/cs-aman/Currency-Exchange-Comparison-Tool/blob/main/ccd_cheat-sheet.md" target="_blank"> Cheat Sheet</a>
