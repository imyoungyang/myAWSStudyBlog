# Usage
# `python test-beacon.py <BEACONURL> 10000 0.5`

import requests
import random
import sys
import argparse
import time
import json

def getEvent():
  events = {
    0 : 'click',
    1 : 'pageview',
    2 : 'conversion',
    3 : 'exception',
    4 : 'playvideo',
    5 : 'login',
    6 : 'logoff'
  }
  return events[random.randint(0,6)]

def getPage():
  return 'page_' + str(random.randint(1,100)) + '.html'

def getUser():
  return 'user' + str(random.randint(1,1000)) 

def getReferer():
  return 'referer_' + str(random.randint(1,20))

def getUserAgent():
  return 'python_manual_agent_' + str(random.randint(1,20))

def getIntMetricName():
  custom_metrics = {
    0 : 'page_load_time',
    1 : 'cart_item_quantity',
    2 : 'impression_count',
    3 : 'idle_time_ms',
    4 : 'mouse_distance_pixles'
  }
  return custom_metrics[random.randint(0,4)]

def getStringMetricName():
  custom_metrics = {
    0 : 'poll_response',
    1 : 'display_x_y',
    2 : 'blocker_type',
    3 : 'browser_version'
  }
  return custom_metrics[random.randint(0,3)]

def getFloatMetricName():
  custom_metrics = {
    0 : 'purchase_amount',
    1 : 'gpu_driver_version',
    2 : 'page_percent_displayed',
    3 : 'video_stopped_location',
    4 : 'compute_render_time'
  }
  return custom_metrics[random.randint(0,4)]

def getIntMetricValue():
  return str(random.randint(0,100))

def getFloatMetricValue():
  return str(random.random() * random.randint(0,100))

def getStringMetricValue():
  return  "dummy_string_value_" + str(random.random() * random.randint(0,10)) 

parser = argparse.ArgumentParser()
parser.add_argument("target", help="<http...> the http(s) location to send the GET request")
parser.add_argument("calls", help="the number of HTTP calls to make")
parser.add_argument("delay", help="the time in seconds to delay between calls (ie 0.5 is half a second)")

args = parser.parse_args()
i = 0
s = requests.Session()

while (i < int(args.calls)):
  time.sleep(float(args.delay))
  random_metric = random.randint(0,3)
  if (random_metric == 0):
    metrics = {'event' : getEvent(), 'clientid' : getUser(), 'page' : getPage(), 'Referer' : getReferer() }
  if (random_metric == 1):
    metrics = {'event' : getEvent(), 'clientid' : getUser(), 'page' : getPage(), 'Referer' : getReferer(), 'custom_metric_name' : getIntMetricName(), 'custom_metric_int_value' : getIntMetricValue() }
  if (random_metric == 2):
    metrics = {'event' : getEvent(), 'clientid' : getUser(), 'page' : getPage(), 'Referer' : getReferer(), 'custom_metric_name' : getFloatMetricName(), 'custom_metric_float_value' : getFloatMetricValue() }
  if (random_metric == 3):
    metrics = {'event' : getEvent(), 'clientid' : getUser(), 'page' : getPage(), 'Referer' : getReferer(), 'custom_metric_name' : getStringMetricName(), 'custom_metric_string_value' : getStringMetricValue() }
  body = json.dumps(metrics)
  #print(body)
  r = s.post(url=args.target + '?call=' + str(i), data=body)
  #r = requests.get(args.target)
  #print(r.text)
  if(r.status_code==200):
    sys.stdout.write( str(i) + "-")
  else:
    sys.stdout.write( str(i) + "---->" + str(r.status_code) + "\n")
  sys.stdout.flush()
  i+=1
