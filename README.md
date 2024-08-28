# stockAnalyzer

Specify custom rules to automatically analyze stocks.

### Ground Truth Gathering

The plan is to create a file that runs every day (initially as a batch file in personal computer; later as a lambda function in AWS) were we download historical data for a given list of stocks and store it locally. If data has already been downloaded for the first time, update it by removing the oldest entry and appending the most recent one (this so that data remains in an x-number-of-years range).

### Ground Truth Processsing

TODO
https://medium.com/@kroeze.wb/running-selenium-in-aws-lambda-806c7e88ec64
### Ground Truth Analysis

Here is where the magic will happen; data will be analyzed with machine learning algorithm(s), deep learning algorithm(s) and/or common technical indicators such as moving average, bollinger bands, etc.

As a nice to have, email updates might be implemented.

## Helpful Links

API Guide for Yahoo Finance  
https://algotrading101.com/learn/yahoo-finance-api-guide/

Documentation of Yahoo Query
https://yahooquery.dpguthrie.com/

Selenium with Python Docs  
https://selenium-python.readthedocs.io/

Explanation on how to use chromedriver along with Chrome for Testing
https://www.youtube.com/watch?v=zWxDWrl701o

Easily Use Selenium with AWS Lambda (Jul 7 2024)
https://towardsdev.com/easily-use-selenium-with-aws-lambda-2cc49ca43b93

Automate Web Scraping Using Python, AWS Lambda, Amazon S3 and Amazon EventBridge CloudWatch  
[Medium Article](https://medium.com/@vinodvidhole/automate-web-scraping-using-python-aws-lambda-amazon-s3-amazon-eventbridge-cloudwatch-c4c982c35fa7)  
_Note: Includes some embeded python scripts_

How I built a Scalable Web-Scraper with AWS  
[Medium Article](https://towardsdatascience.com/get-your-own-data-building-a-scalable-web-scraper-with-aws-654feb9fdad7)&emsp;[GitHub Repo](https://github.com/aaronglang/cl_scraper)  
_Note: Uses BeautifulSoup instead of Selenium_

Other links:
https://googlechromelabs.github.io/chrome-for-testing/
https://www.youtube.com/watch?v=zWxDWrl701o


### Machine Learning Specific / Literature Review

Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review, Performance Analysis and Discussion of Implications  
[MDPI Journal](https://www.mdpi.com/2227-7072/11/3/94)

Machine learning techniques and data for stock market forecasting: A literature review  
[Elsevier Article](https://www.sciencedirect.com/science/article/pii/S0957417422001452)

How I’m using Machine Learning to Trade in the Stock Market  
[Medium Blog](https://medium.com/analytics-vidhya/how-im-using-machine-learning-to-trade-in-the-stock-market-3ba981a2ffc2)&emsp;[GitHub Repo](https://github.com/kaneelgit/Trading-strategy-/tree/main)

Stock Market Prediction using Machine Learning in 2024    
[SimpliLearn Article](https://www.simplilearn.com/tutorials/machine-learning-tutorial/stock-price-prediction-using-machine-learning)   
_Note: Code included in article; uses LSTM; trains only on 'open' price; 1258 entries, from 01/03/2012 to 12/30/2016; predicts Google Stock Price_

Machine Learning for Stock Price Prediction   
[neptune.ai Blog](https://neptune.ai/blog/predicting-stock-prices-using-machine-learning)   
_Note: Code included in blog; uses Moving Averages, LSTM and comparison between them; trains only on 'close' price; Apple stock data from 11/01/1999 to 07/09/2021_

Transformers vs. LSTM for Stock Price Time Series Prediction   
[Medium Blog](https://medium.com/@mskmay66/transformers-vs-lstm-for-stock-price-time-series-prediction-3a26fcc1a782)&emsp;[GitHub Repo](https://github.com/maym5/lstm_vs_transformer/blob/main/lstm_vs__transformer.ipynb)   
_Note: It seems it trains on all of AAPL's historical data; it seems it uses close prices only; LSTM is more predictable and seems to be better for online (incremental learning); transformers seem like a better option for batch learning; LSTM uses ~10x more params._


Calculate Stochastic Oscillator in Python and Pandas and Chart with Matplotlib   
[Medium Blog](https://rbdundas.medium.com/calculate-stochastic-oscillator-in-python-and-pandas-and-chart-with-matplotlib-aafde26b4a1f)&emsp;[GitHub Repo](https://github.com/rbdundas/stockapi)   
_NOTE: Good explanation on how to programatically calculat stochastic oscillator._