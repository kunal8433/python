s={1,2,3,4,5,5,5,5}
#add() a single element
s.add(6)
print(s)  # {1, 2, 3, 4, 5, 6}
#update() multiple elements     
s.update([7,8,9,10])
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#remove() a single element
s.remove(10)
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
s.clear()  #removes all elements
print(s)  # set()

