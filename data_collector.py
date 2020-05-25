import boto3
import os
import subprocess
import sys
import json
import yfinance as yf
# import random


#CHOICES = ["TECHNOLOGY", "ENERGY", "FINANCIAL"]

def lambda_handler(event, context):
    # just generate some random data
    # data = {"ticker_symbol":"HJK","sector":random.choice(CHOICES),"change":0.04,"price":4.79}
    data = yf.download(tickers = "FB SHOP BYND NFLX PINS SQ TTD OKTA SNAP DDOG", start = "2020-05-14", end="2020-05-15", interval="1m")
    data['datetime'] = data.index.astype(str)
    data[['Date','Time']] = data.datetime.str.split(expand=True)
    data[['Time','Useless']] = data.Time.str.split("-",expand=True)
    data[['Hour','Minute', 'Second']] = data.Time.str.split(":",expand=True)
    data = data.drop(['Useless', 'datetime'], axis=1).reset_index(drop=True)
    data.columns = [' '.join(col).strip() for col in data.columns.values]
    data.columns = data.columns.str.replace(' ', '_')

    # convert it to JSON -- IMPORTANT!!
    as_jsonstr = data.to_json(orient='records')
    str_serialized = ''
    for t in json.loads(as_jsonstr):
        str_serialized += json.dumps(t) + "\n" 
    # RecordKinesis = []
    # for t in json.loads(as_jsonstr):
    #     recordkinesis = {'Data': json.dumps(t)}
    #     RecordKinesis.append(recordkinesis)

    # initialize boto3 client
    fh = boto3.client("firehose", "us-east-1")
    
    # this actually pushed to our firehose datastream
    # we must "encode" in order to convert it into the
    # bytes datatype as all of AWS libs operate over
    # bytes not strings
    fh.put_record(
        DeliveryStreamName="yahoo-stock-data", 
        Record={"Data": str_serialized})
    # fh.put_records(DeliveryStreamName="yahoo-stock-data", Records=RecordKinesis)

    # return
    return {
        'statusCode': 200,
        'body': json.dumps('Done! Recorded')
    }
