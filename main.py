from IPadress import ipadress

ip = input()
obj= ipadress(ip)
print(obj.toIPv4())