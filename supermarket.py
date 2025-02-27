from datetime import datetime

name=input('enter customer name:')
#list of items 
lists='''
rice RS 70 for kg
tamato rs 20 per kg
oil rs 100 per kg
banana rs60 for dozen
maggi rs 15 for each one
boost rs 50 for pack
ORS rs 35 for one piece
sugar rs 35 for kg 
chana dal 120 for kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rate for item
items={'rice':70,'tamato':20,'oil':100,'banana':60,'maggi':15,
'boost':50,'ORS':30
,'chana dal':120,'sugar':35}
option=int(input('for grocery list click-> 1'))
if(option==1):
    print(lists)
for i in range(len(items)):
    inp1=int(input('if you want to buy click1 and 2 for exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input('enter your items:')
        quantity=int(input('enter quantitya:'))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print('enterd item is not available')
            
    else:('you enterd wrong input')
inp=input('do you want to generate bill')
if inp=='yes':
    pass
    if finalprice!=0:
        print(25*"=","sai supermarket",25*"=")
        print(25*"dilshuknar,508114")
        print("name:",name,30*" ",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ",'quantity',3*" ",'price')
        for i in range(len(pricelist)):
            print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
        print(75*"-")
        print(50*" ",'totalprice:','rs',totalprice)
        print("gst amount",50*" ",'rs',gst)
        print(75*"-")
        print(50*" ",'finalprice:','rs',finalprice)
        print(75*"-")
        print(50*" ",'thanks for visiting')
        print(75*"-")
                
    
            