import ntplib
from time import ctime
import datetime
try:
    import httplib
except:
    import http.client as httplib

import time
import sys

INTERNET_AVAILABLE = False



def have_internet():
    return INTERNET_AVAILABLE

def request_goog_head():
    conn = httplib.HTTPConnection("www.google.com", timeout=2)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

c = ntplib.NTPClient()

def fetch_time_sys_ntp():
    if(have_internet()):
        response = c.request('europe.pool.ntp.org', version=3)
        NTPtime = datetime.datetime.utcfromtimestamp(response.tx_time)
        systemTime = datetime.datetime.now()
        return "NTP: "+str(NTPtime), "SYS: "+str(systemTime)
    else:
        return "No Internet Found"
    response = c.request('europe.pool.ntp.org', version=3)
    NTPtime = datetime.datetime.utcfromtimestamp(response.tx_time)
    systemTime = datetime.datetime.now()
    return "NTP: "+str(NTPtime), "SYS: "+str(systemTime)

def fetch_NTP():
    if(have_internet()):
        response = c.request('europe.pool.ntp.org', version=3)
        NTPtime = datetime.datetime.utcfromtimestamp(response.tx_time)
        return str(NTPtime)
    else:
        return False

def fetch_system_time():
    return str(datetime.datetime.now())

# try:
#     while True:
#         status = request_goog_head()
#         if status:
#             INTERNET_AVAILABLE = True
#             print "INTERNET_AVAILABLE = True"
#         else:
#             INTERNET_AVAILABLE = False
#             print "INTERNET_AVAILABLE = False"
#         time.sleep(5)
# except KeyboardInterrupt:
#     print("Quitting the program.")
# except:
#     print("Unexpected error: ")
#     raise