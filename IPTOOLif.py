"""
IPToolIF.isValid(ip:IPAddress) -> bool
IPToolIF.areSameNet(ip1:IPAddress,ip2: IPAddress,mask:IPAddress) -> bool
IPToolIF.broadcast(ip: IPAddress, mask:IPAddress) -> IPAddress
IPToolIF.network(ip: IPAddress, mask:IPAddress ) -> IPAddress

Deve existir uma classe de nome IPAddress com os seguintes métodos:
IPAddress(str) // Construtor recebendo o IP (Deve receber bits ou formato AAA.BBB.CCC.DDD)
IPAddress.toBits() -> str //retorna os 32 bits do endereço
IPAddress.toIPv4() -> str //retorna endereço no formato AAA.BBB.CCC.DDD
IPAddress.isMask() -> bool //retorna se é uma máscara de rede
IPAddress.maskBits() -> int // retorna a quantidade de bits da máscara


"""

class IPAddress:
    def __init__(self, ip):
        self.__ip = ip
        
    def toBits(self):
        ip_formated = self.__ip.split(".")
        primeiro_octeto = f"{int(bin(int(ip_formated[0]))[2:]):08d}"
        segundo_octeto = f"{int(bin(int(ip_formated[1]))[2:]):08d}"
        terceiro_octeto = f"{int(bin(int(ip_formated[2]))[2:]):08d}"
        quarto_octeto = f"{int(bin(int(ip_formated[3]))[2:]):08d}"
        return f"{primeiro_octeto}.{segundo_octeto}.{terceiro_octeto}.{quarto_octeto}"
    
    def toIPv4(self):
        ip_formated = self.__ip.split(".")
        primeiro_octeto = f"{int(ip_formated[0]):03d}"
        segundo_octeto = f"{int(ip_formated[1]):03d}"
        terceiro_octeto = f"{int(ip_formated[2]):03d}"
        quarto_octeto = f"{int(ip_formated[3]):03d}"
        return f"{primeiro_octeto}.{segundo_octeto}.{terceiro_octeto}.{quarto_octeto}"
    
    def isMask(self):
        ip_formated = self.__ip.split(".")
        try:
            mask_bin = ''.join(f"{int(octeto):08b}" for octeto in ip_formated)
        except ValueError:
            return False
        if len(mask_bin) != 32:
            return False
        if '01' in mask_bin:
            return False
        return True
    
    def maskBits(self):
        if not self.isMask():
            raise ValueError("maskBits só pode ser chamada para máscaras válidas.")
        ip_formated = self.__ip.split(".")
        bits = 0
        for i in range(4):
            bits += bin(int(ip_formated[i])).count('1')
        return bits
    
class IPToolIF:
    @staticmethod
    def isValid(ip: IPAddress) -> bool:
        ip_formated = ip.toIPv4().split(".")
        for i in range(4):
            if int(ip_formated[i]) > 255:
                return False
        return True

    @staticmethod
    def areSameNet(ip1: IPAddress, ip2: IPAddress, mask: IPAddress) -> bool:
        if not (IPToolIF.isValid(ip1) and IPToolIF.isValid(ip2) and IPAddress.isMask(mask)):
            raise ValueError("Todos os IPs devem ser válidos.")
        ip1_bits = ip1.toBits().split(".")
        ip2_bits = ip2.toBits().split(".")
        mask_bits = mask.toBits().split(".")
        for i in range(4):
            if (int(ip1_bits[i]) & int(mask_bits[i])) != (int(ip2_bits[i]) & int(mask_bits[i])):
                return False
        return True

    @staticmethod
    def broadcast(ip: IPAddress, mask: IPAddress) -> IPAddress:
        if not (IPToolIF.isValid(ip) and IPAddress.isMask(mask)):
            raise ValueError("IP e máscara devem ser válidos.")
        ip_bits = ip.toBits().split(".")
        mask_bits = mask.toBits().split(".")
        broadcast_bits = []
        for i in range(4):
            ip_oct = int(ip_bits[i], 2)
            mask_oct = int(mask_bits[i], 2)
            broadcast_oct = ip_oct | (255 - mask_oct)
            broadcast_bits.append(str(broadcast_oct))
        broadcast_ip = ".".join(broadcast_bits)
        return IPAddress(broadcast_ip)

    @staticmethod
    def network(ip: IPAddress, mask: IPAddress) -> IPAddress:
        if not (IPToolIF.isValid(ip) and IPAddress.isMask(mask)):
            raise ValueError("IP e máscara devem ser válidos.")
        ip_bits = ip.toBits().split(".")
        mask_bits = mask.toBits().split(".")
        network_bits = []
        for i in range(4):
            network_bits.append(str(int(ip_bits[i], 2) & int(mask_bits[i], 2)))
        network_ip = ".".join(network_bits)
        return IPAddress(network_ip)
    
# Testando a classe IPAddress
if __name__ == "__main__":
    ip1 = IPAddress("192.168.20.2")
    ip2 = IPAddress("192.169.20.20")
    mask = IPAddress("255.240.0.0")
    print("IP1:", ip1.toIPv4())
    print("IP1 em bits:", ip1.toBits())
    print("IP2:", ip2.toIPv4())
    print("IP2 em bits:", ip2.toBits())
    print("Máscara:", mask.toIPv4())
    print("Máscara em bits:", mask.toBits())
    print("IP1 é uma máscara?", ip1.isMask())
    print("IP2 é uma máscara?", ip2.isMask())
    print("IP1 é válido?", IPToolIF.isValid(ip1))
    print("IP2 é válido?", IPToolIF.isValid(ip2))
    print("IP1 e IP2 estão na mesma rede?", IPToolIF.areSameNet(ip1, ip2, mask))
    print("Broadcast de IP1:", IPToolIF.broadcast(ip1, mask).toIPv4())
    print("Rede de IP1:", IPToolIF.network(ip1, mask).toIPv4())
    print("Broadcast de IP2:", IPToolIF.broadcast(ip2, mask).toIPv4())
    print("Rede de IP2:", IPToolIF.network(ip2, mask).toIPv4())
# Testando a classe IPToolIF
    ip3 = IPAddress("200.70.50.1")
    ip4 = IPAddress("200.70.20.4")
    mask2 = IPAddress("255.255.0.0")
    print("IP3:", ip3.toIPv4())
    print("IP3 em bits:", ip3.toBits())
    print("IP4:", ip4.toIPv4())
    print("IP4 em bits:", ip4.toBits())
    print("Máscara 2:", mask2.toIPv4())
    print("Máscara 2 em bits:", mask2.toBits())
    print("IP3 é uma máscara?", ip3.isMask())
    print("IP4 é uma máscara?", ip4.isMask())
    print("IP3 é válido?", IPToolIF.isValid(ip3))
    print("IP4 é válido?", IPToolIF.isValid(ip4))
    print("IP3 e IP4 estão na mesma rede?", IPToolIF.areSameNet(ip3, ip4, mask2))
    print("Broadcast de IP3:", IPToolIF.broadcast(ip3, mask2).toIPv4())
    print("Rede de IP3:", IPToolIF.network(ip3, mask2).toIPv4())
    print("Broadcast de IP4:", IPToolIF.broadcast(ip4, mask2).toIPv4())
    print("Rede de IP4:", IPToolIF.network(ip4, mask2).toIPv4())