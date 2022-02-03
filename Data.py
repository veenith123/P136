import pandas as pd
df = pd.read_csv("filtered_stars.csv")

name_list = df["Star_name"]
mass_list = df["Mass"]
radius_list = df["Radius"]
distance_list = df["Distance"]
gravity_list = df["gravity"]

dict_data_list = []

for index,i in enumerate(mass_list):
    data_list = []
    data_list.append(i)
    data_list.append(radius_list[index])
    data_list.append(distance_list[index])
    data_list.append(gravity_list[index])
    dict_data_list.append(data_list)
    
final_dict = {}
for index,i in enumerate(name_list):
    final_dict[i] = dict_data_list[index]
print(final_dict)