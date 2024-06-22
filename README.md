# stockAnalyzer

Specify custom rules to automatically analyze stocks.

Project is composed of three parts:

### Downloader

Here is were we download historical data and store it locally. We refer to this data as ground truth.

### Updater

Here we ensure our ground truth is properly updated in a daily basis.

### Analyzer

Here is where the magic happens; data is analyzed through custom rules and results are sent via email.

## Helpful Links

API Guide for Yahoo Finance  
https://algotrading101.com/learn/yahoo-finance-api-guide/

Selenium with Python Docs  
https://selenium-python.readthedocs.io/

Explanation on how to use chromedriver along with Chrome for Testing
https://www.youtube.com/watch?v=zWxDWrl701o

Explanation on how to do web scraping using Python, Lambda, S3 and Eventbridge
https://medium.com/@vinodvidhole/automate-web-scraping-using-python-aws-lambda-amazon-s3-amazon-eventbridge-cloudwatch-c4c982c35fa7
