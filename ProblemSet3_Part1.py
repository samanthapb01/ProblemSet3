#%%Samantha Pasciullo Boychuck slp87@duke.edu 10/7/2024

#%% Task 1 - Edit code to print as requested
#/*-PS3: Code Block 1--*/

#Assign names to variables
mountain = "Denali"
nickname = "Mt. McKinley"
elevation = "20322"

#Print string
print(f'{mountain}, sometimes \ncalled "{nickname}", \nis {elevation}\' above sea level.')

#%% Task 2 - Lists and Iteration

#Assign variable to string object
data_folder = r"W:\859_data\triangle"

#Create a list using specified string objects
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

#Assign a variable to the string
user_item = "roads.shp"

#Add string object to list
data_list.append(user_item)

#Loop through list and print file paths
for item in data_list:
    full_path = f"{data_folder}\\{item}"
    print(full_path)

# %% Task 3
