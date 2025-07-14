import psutil
import socket
class cliente:
    def __init__(self):
        pass
    def get_processadores():
        return psutil.cpu_count
    def get_freeram():
        return psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
    def get_freediskspace():
        return psutil.disk_usage().free
    def get_interfaces_ips():
        interfaces_ips = {}
        interfaces = psutil.net_if_addrs()
        stats = psutil.net_if_stats()

        for interface_name, snics in interfaces.items():
            if interface_name in stats and stats[interface_name].isup:
                for snic in snics:
                    if snic.family == socket.AF_INET:
                        interfaces_ips[interface_name] = snic.address
                        break #Pega o primeiro endereço IPv4 encontrado

        return interfaces_ips

    #parte do servidor abaixo para pegae
    #interface_ips = get_interfaces_ips()

    #for interface, ip in interface_ips.items():
    #print(f"Interface: {interface}, IP: {ip}")

    def get_interfacesdesativadas():
        interfaces = psutil.net_io_counters()
        interfaces_on = psutil.net_connections()

