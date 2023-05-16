# Make up 4 names and 3 sizes for them
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]

#Add a size for Depak
preferred_size.append("Medium")
print(preferred_size)

#Make up a customer data set with names, sizesm and a boolean statment
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

#Change Chani's order from True to False
customer_data[-2][-1] = False
print(customer_data)

#Remove False from Ben's order
customer_data[1].remove(False)
print(customer_data)

#Add two new customers to the list and name the new list customer_data_final
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
