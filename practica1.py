import time 
print(time.localtime())
#devuelve el tiempo actual como año, dias, meses,horas, mintos
t=time.localtime()
year=t[0]
month=t[1]
day=t[2]
hora=t[3]
print(year)
print(month)
print(day)
print(hora)
