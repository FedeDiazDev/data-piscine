ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# List
ft_list[1] = "World!"
# Tuple
tuple_aux = list(ft_tuple)
tuple_aux[1] = "France!"
ft_tuple = tuple(tuple_aux)
# Set
ft_set.remove("tutu!")
ft_set.add("Paris!")
# Dict
ft_dict["Hello"] = "42Paris!"

# Print
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
