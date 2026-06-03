#Bus Station Payment System
print('1.Kalanki')
print('2.New Bus Park')
print('3.Chabhil')
print('4.Gausala ')
print('5.Koteshwork')
print('6.Gwarko')

pickup=int(input('Pick up Point :'))
dropPoint=int(input("Drop Point :"))
per_station_cost=15

if dropPoint-pickup <0:
    Travelled=dropPoint-pickup
    totalcost=Travelled*per_station_cost
    print("your cost is",-totalcost)

elif dropPoint-pickup==0:
    totalcost=5*15
    print("your cost is",totalcost)

else:
    Travelled=dropPoint-pickup
    totalcost=Travelled*per_station_cost
    print("yoyr cost is",totalcost)