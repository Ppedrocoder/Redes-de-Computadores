class ipadress:
    def __init__(self, ip):
        self.__ip=ip
    def toBits(self):
        ip_formated=self.ip.split(".")
        primeiro_octeto=f"{int(bin(int(ip_formated[0])).replace("0b","")):03d}"
        segundo_octeto=f"{int(bin(int(ip_formated[1])).replace("0b","")):03d}"
        terceiro_octeto=f"{int(bin(int(ip_formated[2])).replace("0b","")):03d}"
        quarto_octeto=f"{int(bin(int(ip_formated[3])).replace("0b","")):03d}"
        return f"{primeiro_octeto}+{segundo_octeto}+{terceiro_octeto}+{quarto_octeto}"

ip=ipadress("13.12.1.10")
print(ip.toBits)