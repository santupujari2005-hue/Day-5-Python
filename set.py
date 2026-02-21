#SET IN PYTHON 
collection={1,2,3,4,"Santosh","hello","hello",2,2,"Santosh","world",5} 
print(collection) #repeated elements stored only once,so it resolved to{1,2}
print(type(collection))
print(len(collection))
#collection1={} thise is empty dictionary not a set
collection1=set() #Thise is an empty set
print(collection1)
print(type(collection))

#SET METHODS
#1.set.add(el) ,adds an element
collection2=set()
collection2.add(1)
collection2.add(2)
collection2.add(3)
collection2.add("python")
collection2.add(6)
print(collection2)

#2.set.remove(el) ,remove the element
collection3={1,2,3,4,5}
collection3.remove(1)
print(collection3)
collection3.remove(4)
print(collection3)

#3.set.clear() ,empties the set
collection4={6,7,8,9,5}
collection4.clear()
print(collection4)
print(type(collection4))

#4.set.pop() ,removes a random value
collection5={"santosh","python","java","virat"}
collection5.pop()
print(collection5)
collection5.pop()
print(collection5)
collection5.pop()
print(collection5)

#5.set.union(set2) , combines both set values and returns new
collection6={11,12,13,14,15}
collection7={34,35,37,56,78,11,15}
print(collection6.union(collection7))
print(collection6)
print(collection7)
#6.set.intersection(set2) ,combine common values & return new
collection8={1,2,3,4,8,9}
collection9={1,3,5,6,9}
print(collection8.intersection(collection9))