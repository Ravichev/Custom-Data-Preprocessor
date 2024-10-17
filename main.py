import custom_data_preprocessor as cdp

dp1=cdp.DataPreprocessor()

converted_list = dp1.convert_list(dp1.list_input)
print(f"{converted_list} - Converted list.")
print(f"{dp1.type_counter(converted_list)} - The number of different types of objects in the list.")
print(f"{dp1.value_counter(converted_list)} - The number of different objects in the list.")
unrepeaded_list = dp1.del_repeat(converted_list)
print(f"{unrepeaded_list} - List without duplicates.")
list_index = input("Enter the index number of the object in the list without duplicates: ")
num_mult = input("Enter the number of repetitions of the object: ")

try:
    list_index = int(list_index)
except ValueError:
    print("not a number")
try:
    num_mult = int(num_mult)
except ValueError:
    print("not a number")

print(f"{dp1.mult_list(unrepeaded_list, list_index, num_mult)} - list with multiplication. {list_index} element {num_mult} times")

text_replace = input("Enter the value to replace empty cells: ")
print(f"{dp1.null_replacer(unrepeaded_list, text_replace)} - List without emptiness.")
print(f"{dp1.num_stat(unrepeaded_list)} - Statistics on the digits.")
obj_inp = input("Enter which element to remove from the list: ")
print(f"{dp1.del_obj(unrepeaded_list, obj_inp)}")