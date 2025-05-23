class ipadress:
    def __init__(self, ip):
        self.__ip=ip
    def toBits(self):
        ip_formated=self.__ip.split(".")
        primeiro_octeto=f"{int(bin(int(ip_formated[0]))[2:]):08d}"
        segundo_octeto=f"{int(bin(int(ip_formated[1]))[2:]):08d}"
        terceiro_octeto=f"{int(bin(int(ip_formated[2]))[2:]):08d}"
        quarto_octeto=f"{int(bin(int(ip_formated[3]))[2:]):08d}"
        return f"{primeiro_octeto}.{segundo_octeto}.{terceiro_octeto}.{quarto_octeto}"
    def toIPv4(self):
        ip_formated=self.__ip.split(".")
        primeiro_octeto=f"{int(ip_formated[0]):03d}"
        segundo_octeto=f"{int(ip_formated[1]):03d}"
        terceiro_octeto=f"{int(ip_formated[2]):03d}"
        quarto_octeto=f"{int(ip_formated[3]):03d}"
        return f"{primeiro_octeto}.{segundo_octeto}.{terceiro_octeto}.{quarto_octeto}"
