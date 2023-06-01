import psutil
import socket

class Network:
    def __init__(self):
        self.host_name = socket.gethostname()
        self.host_address = socket.gethostbyname(self.host_name)

    def get_stats(self):
        stats = psutil.net_if_stats()
        return stats

    def get_addrs(self):
        addrs = psutil.net_if_addrs()
        return addrs

    def get_connections (self, kind='inet'):
        connections = psutil.net_connections(kind=kind)
        return connections
    
    def get_name(self):
        return self.host_name
    
    def get_addr(self):
        return self.host_address

    def monitor_packages(self, instance = None):
        pernic = False

        if instance:
            pernic = True
            counters = psutil.net_io_counters(pernic=pernic)[instance]
            return counters

        counters = psutil.net_io_counters(pernic=pernic)
        return counters

