import speedtest
from ping3 import ping, verbose_ping
from datetime import datetime
import pandas as pd

target_host = "google.com"
spectrum_dl = 500 #(Mbps), quoted avlue by Spectrum
acceptable_ping = 69 #(ms), acceptable number we need for gaming, ask Michael & Cass
acceptable_packet_loss = 69 #(%), acceptable number we need for gaming, ask Michael & Cass

def get_speeds():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # in Mbps
    upload_speed = st.upload() / 10**6  # in Mbps
    return download_speed, upload_speed

def get_ping():
    response_time = ping(target_host)
    return response_time

def get_packet_loss():
    packet_loss = ping(target_host, count=10)
    return packet_loss

def alarms(speeds, ping_speed, packet_loss):
    if speeds[0] < 500:
        #Do something
    if ping_speed > acceptable_ping:
        print('Unacceptable ping!  T')
    if packet_loss > acceptable_packet_loss:
        #Do a third thing

def save_stats(speeds, ping, packet_loss):
    #Save stats to a daily CSV
    return 'TODO Implement'

speeds = get_speeds()
ping_speed = get_ping()
packet_loss = get_packet_loss()

save_stats(speeds, ping_speed, packet_loss)