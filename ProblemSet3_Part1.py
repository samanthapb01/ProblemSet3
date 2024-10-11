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
data_folder = 'W:\\859_data\\triangle'

#Create a list using specified string objects
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

#Assign a variable to the string
user_item = "roads.shp"

#Add string object to list
data_list.append(user_item)

#Loop through list and print file paths
for item in data_list:
    full_path = data_folder + "\\" + item
    print(full_path)

# %% Task 3

#Create empty list variable
user_numbers = []

#Iterate 3x to get user input
for item in range(3):
    #Ask user for integer
    number = int(input("Enter an integer: "))
    #Add integer to list
    user_numbers.append(number)

#Sort list in ascending order
user_numbers.sort()

#Print highest value in sorted list
print("The highest value is: ", user_numbers[-1])
# %% Task 3 - Challenge

#Create empty list variable
user_numbers = []

#Iterate 3x to get user input
for item in range(3):
    #Ask user for integer
    number = int(input("Enter an integer: "))
    #Add integer to list
    user_numbers.append(number)

#Sort list in ascending order
user_numbers.sort(reverse=True)

#Print highest value in sorted list
print(user_numbers)
