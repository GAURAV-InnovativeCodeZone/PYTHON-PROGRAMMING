
   #  dictionary data type	
   
mydict = {
"gaurav" : "hacker",
"roman" : "wrestler", 
"ravi" : "coder", 
"ayush" : "coder",
"roman" : "cricketer",
"marks" : [1, 2, 3] , 
"anotherdict" : {'sam' : 'player'}
}
print(mydict)
print(len(mydict))
print("********************")

print(mydict.keys())
print(mydict.values())
print(mydict.items())

print(mydict["gaurav"])   #key as a index
print(mydict.get("roman")) #roman is key
print(mydict.get("coder")) #coder is not a key so output is none
print(mydict.get("sam"))  #sam is not a key so output is none

print(mydict["anotherdict"])
print(mydict["anotherdict"]["sam"])
(mydict.update({"ayush":"developer"}))
print(mydict)
