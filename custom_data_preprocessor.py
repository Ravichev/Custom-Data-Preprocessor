class DataPreprocessor:
 def __init__(self):
        str_input = input("Enter the data you want to present as a list. For example:|  Bogdan, 10, 0, True,,0.5  ,0.5,0.5,10,  |: ")
        list_input = str_input.split(",")
        self.list_input = [x.strip() for x in list_input]
        print(f"{list_input} - Cleansed of spaces, converted from a string into a list.")

 def convert_list(self, list_input):
     conv_list_input = []
     for item in list_input:
         try:
             conv_item = int(item)
         except ValueError:
             try:
                 conv_item = float(item)
             except ValueError:
                 if item.lower() == "true":
                     conv_item = True
                 elif item.lower() == "false":
                     conv_item = False
                 else:
                     conv_item = item

         conv_list_input.append(conv_item)
     return conv_list_input

 def type_counter(self, con_list):
     dict = {}
     for item in con_list:
         if type(item) in dict:
             dict[type(item)] += 1
         else:
             dict[type(item)] = 1
     return dict

 def value_counter(self, con_list):
     dict = {}
     for item in con_list:
         if item in dict:
             dict[item] += 1
         else:
             dict[item] = 1
     return dict

 def del_repeat(self, con_list):
     new_list = []
     for item in con_list:
         if item in new_list:
             con_list.remove(item)
         else:
             new_list.append(item)
     return new_list

 def mult_list(self, unR_list, l_index, n_mult):
     multiplied_list = unR_list[:]

     print(f"{unR_list} {l_index}, {n_mult}")

     for i in range(1, n_mult):
         multiplied_list.insert(l_index + i, unR_list[l_index])
     return multiplied_list

 def null_replacer(self, unR_list, txt_replace):
     null_repl_list = []
     for item in unR_list:
         if item == "":
             repl_item = txt_replace
         else:
             repl_item = item
         null_repl_list.append(repl_item)
     return null_repl_list

 def num_stat(self, unR_list):
     mean = 0
     dict_stats = {"min_stat": 0, "max_stat": 0, "mean_stat": 0}
     New_list = []

     for item in unR_list:
         if isinstance(item, (int, float)):
             New_list.append(item)

     if New_list:
         New_list.sort()
         dict_stats["min_stat"] = New_list[0]
         dict_stats["max_stat"] = New_list[-1]
         mean = sum(New_list) / len(New_list)
         dict_stats["mean_stat"] = mean
     return dict_stats

 def del_obj(self, unR_list, obj_txt):
     del_list = []
     for item in unR_list:
         new_item = str(item)
         del_list.append(new_item)

     print(del_list)
     try:
         del_list.remove(obj_txt)
     except ValueError:
         print("There is no such element in the list.")
     return del_list