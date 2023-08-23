import speedtest
from ping3 import ping, verbose_ping

target_host = "google.com"

def get_speeds():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # in Mbps
    upload_speed = st.upload() / 10**6  # in Mbps
    return download_speed, upload_speed

def get_ping():
    response_time = ping(target_host)
    return response_time

def get_packet_loss():
    packet_loss = ping(target_host, count=10)  # Send 10 ping requests
    return packet_loss

print(get_speeds())
print(get_ping())
print(get_packet_loss())