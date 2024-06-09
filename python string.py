#strings are arry(remember first one is identify with 0)
x="mahirulalam"
print(x[0])
print(x[3])
#slicing string
Y="hellow \n world"
print(Y[3:6])
print(Y[3:]) #if we skip first word
print(Y[:5]) #if we skip last word
#upper and lower string
print(Y.upper())
print(Y.lower())
#replace string
print(Y.replace("h","m"))
# add two string
print(x + Y)
# if we want to add string and variable use f-string
age=9*2
info=f"{x} is {age} year old"
print(info)
#Escape character
intro="he belongs to \"Muslim\"family"
print(intro)
