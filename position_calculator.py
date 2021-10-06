import random as rd
x = 372
y = 152

radius = radius = rd.random() * 0.15 + 0.0602

newx = (((x - 103) - 187) * 0.00403) * (radius/0.0602)
newy = (((374 - (y - 160) - 187) * 0.00403) * (radius/0.0602)) + 1.6
newz = -5 * (radius/0.0602)

radius += rd.random() * 0.02
#print(round(radius, 4))
print("<a-sphere position='" + str(round(newx, 4)) + " " + str(round(newy, 2)) + " " +  str(round(newz, 2))
+ "' radius= '" + str(round(radius, 4)) + "' color=''></a-sphere>")

    


