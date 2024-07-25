# stockAnalyzer

Specify custom rules to automatically analyze stocks.

### Ground Truth Gathering

The plan is to create a file that runs every day (initially as a batch file in personal computer; later as a lambda function in AWS) were we download historical data for a given list of stocks and store it locally. If data has already been downloaded for the first time, update it by removing the oldest entry and appending the most recent one (this so that data remains in an x-number-of-years range).

### Ground Truth Processsing

TODO

### Ground Truth Analysis

Here is where the magic will happen; data will be analyzed with machine learning algorithm(s), deep learning algorithm(s) and/or common technical indicators such as moving average, bollinger bands, etc.

As a nice to have, email updates might be implemented.

## Helpful Links

API Guide for Yahoo Finance  
https://algotrading101.com/learn/yahoo-finance-api-guide/

Selenium with Python Docs  
https://selenium-python.readthedocs.io/

Explanation on how to use chromedriver along with Chrome for Testing
https://www.youtube.com/watch?v=zWxDWrl701o

Automate Web Scraping Using Python, AWS Lambda, Amazon S3 and Amazon EventBridge CloudWatch  
[Medium Article](https://medium.com/@vinodvidhole/automate-web-scraping-using-python-aws-lambda-amazon-s3-amazon-eventbridge-cloudwatch-c4c982c35fa7)  
_Note: Includes some embeded python scripts_

How I built a Scalable Web-Scraper with AWS  
[Medium Article](https://towardsdatascience.com/get-your-own-data-building-a-scalable-web-scraper-with-aws-654feb9fdad7)&emsp;[GitHub Repo](https://github.com/aaronglang/cl_scraper)  
_Note: Uses BeautifulSoup instead of Selenium_

### Machine Learning Specific

Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications  
[MDPI Journal](https://www.mdpi.com/2227-7072/11/3/94)

Machine learning techniques and data for stock market forecasting: A literature review  
[Elsevier Article](https://www.sciencedirect.com/science/article/pii/S0957417422001452)

How I’m using Machine Learning to Trade in the Stock Market  
[Medium Article](https://medium.com/analytics-vidhya/how-im-using-machine-learning-to-trade-in-the-stock-market-3ba981a2ffc2)&emsp;[GitHub Repo](https://github.com/kaneelgit/Trading-strategy-/tree/main)

Test