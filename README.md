# Streaming and Analyzing Yahoo Finance Stock data in AWS

- Language: Python, Jupyter notebook, SQL, Docker
  - Libraries: pandas, yfinance, boto3, os, subprocess, sys, json, yfinance
- Service: AWS S3, Kinesis, Athena, Glue, and Lambda function
- [Code for collecting and transforming](data_collector.py)
  - this code is implemented in Lambda function with [Deployment Package](lambda.zip) using Docker.
- [Code for querying](query.sql)

In this project, several AWS services(S3, Kinesis, Lambda function) are implemented to stream Yahoo Finance stock price data in json format. In addition, Glue and Athena is used to query the datset using SQL language.

The purpose is to stream yahoo finance stock data of 10 companies to AWS S3 and query in AWS Athena. Lambda function in AWS has a major role in collecting data from Yahoo Finance and storing it to S3.

After I encountered several errors when coding in lambda fucntion, I decided to apply Deployment Package using docker. I can achieve intalling Python dependencies in lambda function by uploading the deployment package, which is a zip file. Deployment Package is [here](lambda.zip).

Data collector lambda fuction url is [https://sdx5x1k8od.execute-api.us-east-1.amazonaws.com/default/collector3]( https://sdx5x1k8od.execute-api.us-east-1.amazonaws.com/default/collector3) and datacollector source code is also in the deployment pacakge. The source code transforms the dataframe from yfiance module to json format. In order to connect to AWS Kinesis Firehose, boto3.client is used.

For the analysis, hourly high stock price is extracted for the companies as below.
![results](3.png)
Analysis using this hourly high stock price dataset is [here](Analysis.ipynb).