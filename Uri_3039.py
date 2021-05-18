gifts=[]
n=int(input())
p= n*2
for x in range(0,p):
    a=str(input())
    gifts.append(a)
gift_count=gifts.count("f")
gift_counts=gifts.count("m")
print(f"{gift_count} carrinhos")
print(f" {gift_counts} bonecas")       
  
