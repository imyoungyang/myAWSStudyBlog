import os
import json
import time
import dateutil.parser
import boto3

client = boto3.client('logs')
EXPORT_PERIOD = 24 * 60 * 60 * 1000    ## export period from task start time
EXPORT_BUCKET = "CHANGE_TO_EXPORT_BUCKET"   ## bucket for store exported log
CLOUDWATCH_LOG_GROUP = "CHANGE_TO_LOG_GROUP_TO_EXPORT"  ## cloudwatch log group to export

def lambda_handler(event, context):
    print("Message from event :{}".format(event))
    print(event)
    ## should be schedule event, otherwise will use current time
    try:
        date_now = event['time']
        dt = dateutil.parser.parse(date_now)
        dt_to = int(time.mktime(dt.timetuple())) * 1000
        dt_from = dt_to - int(EXPORT_PERIOD)
    except Exception as ex :
        print( "Couldn't find 'time' field in event, use current time instead." )
        print(ex)
        dt_to = int(round(time.time() * 1000))
        dt_from = dt_to - int(EXPORT_PERIOD)
  
    response = client.create_export_task(
        #taskName='export-task',
        logGroupName=CLOUDWATCH_LOG_GROUP,
        #logStreamNamePrefix='string',
        fromTime=dt_from,
        to=dt_to,
        destination=EXPORT_BUCKET,
        #destinationPrefix='log'  # default is exportedlog
        )
    print(response)
    return response