class ipadress:
    def __init__(self, ip):
        self.__ip=ip
    def toBits(self):
        ip_formated=self.__ip.split(".")
        primeiro_octeto=f"{int(bin(int(ip_formated[0]))[2:]):04d}"
        segundo_octeto=f"{int(bin(int(ip_formated[1]))[2:]):04d}"
        terceiro_octeto=f"{int(bin(int(ip_formated[2]))[2:]):04d}"
        quarto_octeto=f"{int(bin(int(ip_formated[3]))[2:]):04d}"
        return f"{primeiro_octeto}.{segundo_octeto}.{terceiro_octeto}.{quarto_octeto}"