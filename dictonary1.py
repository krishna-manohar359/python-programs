d={"name":"krishna","branch":"cse","id no":174}
d["name"]="harsh"
print(d)
del d["branch"]#delets the branch key
print(d)
d["height"]=17.5#height is added
print(d)
a=d.copy()#used to copy
d.clear()#clears d dictonary
print(a)
a.items()
print(a.values())#return value
print(a.keys())#prints key
a.update({"name":"manohar"})#updates the dictonary
print(a.pop("name"))#removes this key and returns key name
print(a)
print(a.get("height"))#return key value