import ntplib
from time import ctime
import datetime
try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

c = ntplib.NTPClient()

def fetch_time_():
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