# range == -5 to 256
#agar -5 to 256 same memory
#agar -6 sy jitna chota 257 sy bara hoga to change memory
#variable ki location find krna
# a= 10
# b= 10
# print(id(a))   #output: 140725162972360
# print(id(b))   #output: 140725162972360
# a= 10
# b= 20
# print(id(a))      #output: 140725162972360
# print(id(b))      #output: 140725162972680
# a="hello"
# b="hello"
# print(id(a))       output: 2192774968064
# print(id(b))       output: 2192774968064
# a="hello_sana_assignment"
# b="hello_sana_assignment"
# print(id(a))       #output: 1614555697648
# print(id(b))       #output: 1614555697648
# a="hello sana"       output: 2666920460848       space dene sy location change ho jay gi
# b="hell0 sana"       output: 2666920460848
# print(id(a))
# print(id(b))
# tuple             
# change deta
# list
# set
# dict
# unchanged deta
# str
# int
# bool
# float
# tuple
# a=[10,20,30,40]
# b=[10,20,30,40]
# a.append(50)
# print(id(a))
# print(id(b))
# b=a
# print(id(a))
# print(id(b))
# b=a.copy
# print(id(a))
# print(id(b))
# a=("sana,hina,bisma")   str
# b=("sana,hina,bisma")
# print(id(a))
# print(id(b))
a=(10,20,30,40)           #int
b=(10,20,30,40)
# print(id(a))
# print(id(b))
# print(type(a))          #tuple
a= 1,2,3,4,5
b=1,2,3
print(tuple(a))
print(tuple(b))


