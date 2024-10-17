#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='data/raw/transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.read().split("\n")

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3
#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for line in lineList[1:-1]:
    #Split the data into values
    values = line.split(",")
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = values[mmsi_idx]
    #Extract the fleet value
    fleet = values[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet

len(vesselDict.keys())
# %% Task 4.4

#Assign string to variable
vesselID = "440196000"

#Use dictionary to lookup MMSI value
fleet_value = vesselDict[vesselID]

#Print statement
print("Vessel # %s flies the flag of %s" %(vesselID, fleet_value))

# %% Task 5.1

#Create a Python file object, i.e., a link to the file's contents
fileObj2 = open(file='data/raw/loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList2 = fileObj2.read().split("\n")

#Release the link to the file objects (now that we have all its contents)
fileObj2.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString2"
headerLineString2 = lineList2[0]

#Print the contents of the headerLine
print(headerLineString2)

# %% Task 5.2

#Split the headerLineString into a list of header items
headerItems2 = headerLineString2.split(",")

#Store headers to variables
mmsi2_idx = headerItems2.index("transshipment_mmsi")
start_lat_idx = headerItems2.index("starting_latitude")
start_long_idx = headerItems2.index("starting_longitude")
end_lat_idx = headerItems2.index("ending_latitude")
end_long_idx = headerItems2.index("ending_longitude")

#Assign variable
any_meet_criteria = False

#Iterate through all lines (except the header) in the data file:
for line in lineList2[1:-1]:
    #Split the data into values
    values = line.split(",")
    #Extract the values from the list using the index values
    mmsi2 = values[mmsi2_idx]
    start_lat = float(values[start_lat_idx])
    start_long = float(values[start_long_idx])
    end_lat = float(values[end_lat_idx])
    end_long = float(values[end_long_idx])
    #Examine if vessel crosses the equator and is between longitude of interest
    equator_cross = (start_lat < 0) and (end_lat > 0)
    long_placement = (145 < start_long < 155)
    #Check if both Booleans are true and query dictionary
    if equator_cross and long_placement:
        #Set variable to True
        any_meet_criteria = True
        #Print statement
        print("Vessel # %s flies the flag of %s" %(mmsi2, vesselDict[mmsi2]))

#If none True
if not any_meet_criteria:
    print("No vessels met criteria")

    