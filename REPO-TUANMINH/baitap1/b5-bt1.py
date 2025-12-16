a=int(input("nhap luong cua nhan vien vao:"))
if a == 15:
    thue=0.3 *a
elif 7<=a<=15:
    thue=0.2*a
elif 7<a:
    thue=0.1*a
else:
    thue=0.3*a
luongrong=a-thue    
print("thue thu nhap la:",thue)
print("luong rong la:",luongrong)
