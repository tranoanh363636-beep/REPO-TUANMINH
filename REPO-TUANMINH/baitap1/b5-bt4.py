sophut=int(input())
if sophut<=50:
    tiencuoc=sophut*600
elif sophut<=200:
    tiencuoc=50*600+(sophut-50)*400
else:
    tiencuoc=50*600+150*400+(sophut-200)*200
tongtien=25000+tiencuoc
print(tongtien)