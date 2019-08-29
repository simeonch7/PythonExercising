import copy

print("-------LIST--------")

my_list = [1 ,2]
my_list1 = my_list
print("{} -> {}".format(id(my_list), my_list))
print("{} -> {}".format(id(my_list1), my_list1))
my_list[0] = "Test"
print("{} -> {}".format(id(my_list), my_list))
print("{} -> {}".format(id(my_list1), my_list1))
for el in my_list:
	print("{}: Hello".format(el))

print("-------SET--------")

my_set = {1 ,2, 2, 3}
my_set1 = my_set
print("{} -> {}".format(id(my_set), my_set))
print("{} -> {}".format(id(my_set1), my_set1))
my_set.add("Test2")
my_set1.add("Test2")


print("{} -> {}".format(id(my_set), my_set))
print("{} -> {}".format(id(my_set1), my_set1))

last = my_set.pop()
last1 = my_set.pop()
print(my_set)
print(last)
print(last1)
print("{} -> {}".format(id(my_set), my_set))
for el in my_set:
	print(el)

print("-------TUP--------")
my_tup = (1, 2, len("asd"))*3
my_tup1 = my_tup
print("{} -> {}".format(id(my_tup), my_tup))
print("{} -> {}".format(id(my_tup1), my_tup1))
print(my_tup)

print("-------DICTIONARY--------")

my_dict = {
	"Name": "Simeon",
	"Age": 18,
	"OS": 'iOS'
}

my_dict1 = my_dict
print("{} -> {}".format(id(my_dict), my_dict))
print("{} -> {}".format(id(my_dict1), my_dict1))
print(my_dict1["Age"])
my_dict1["Name"] = "Simeon Chakarov"
my_dict1["Age"] = 19
print("{} -> {}".format(id(my_dict), my_dict))


my_dict_copy = copy.copy(my_dict)
my_dict_deep_copy = copy.deepcopy(my_dict)
print("{} -> {}".format(id(my_dict), my_dict))
print("{} -> {}".format(id(my_dict_copy), my_dict_copy))
print("{} -> {}".format(id(my_dict_deep_copy), my_dict_deep_copy))


print("*")
print("{} -> {}".format(id(my_dict["Name"]), my_dict["Name"]))
print("{} -> {}".format(id(my_dict_copy["Name"]), my_dict_copy["Name"]))
print("{} -> {}".format(id(my_dict_deep_copy["Name"]), my_dict_deep_copy["Name"]))


print("*")
# my_dict_copy["Name"] = "Preslav"
my_dict_deep_copy["Name"] = "Samuil"
print("{} -> {}".format(id(my_dict["Name"]), my_dict["Name"]))
print("{} -> {}".format(id(my_dict_copy["Name"]), my_dict_copy["Name"]))
print("{} -> {}".format(id(my_dict_deep_copy["Name"]), my_dict_deep_copy["Name"]))

for key, val in list(my_dict.items()):
	print("{}: {}".format(key, val))