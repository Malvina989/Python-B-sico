#  El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list =[]

for i in range(len(my_list)):
    if my_list[i] not in new_list:
        new_list.append(my_list[i])
    
my_list = new_list

print("La lista con elementos únicos:")
print(my_list)


