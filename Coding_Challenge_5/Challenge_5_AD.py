# Coding Challenge 5
# Generating Heatmaps for Two Species

# For this coding challenge I used harbor seal (Phoca vitulina) and gray seal (Halichoerus grypus) data
# obtained from the Ocean Biodiversity Information System (OBIS)
# We have been talking about these two seals this week in NRS 406: Wetland Wildlife Management, and had a trip
# to Rome Point to observe the harbor seals there

# Thus, I thought it would be interesting to use data for these species for this challenge

# First, import arcpy and csv, then set the workspace which can be changed depending on the folder location
# Override any outputs file that are duplicates from running the code multiple times times
# This is how it is set up for mine
import arcpy
import csv
import os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Data\Students_2021\Brown\Coding_Challenge_5\Seal_Data"
file_name = "Harbor_Gray_Seal_Data.csv"
file_path = arcpy.env.workspace

#WORKSPACE IS NOT USED BY CSV.READER
# IMPORTANT NOTE: for lines 26 and 48 I had to put the entire folder path name, not just the name of csv file,
# otherwise it would not read in the csv file

# Create an empty list to populate with the imported csv file
seal_list = []

# Use for/if loop to create csv for the two seal species data
with open(os.path.join(file_path, file_name)) as seal_csv:
    csv_reader = csv.reader(seal_csv, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            if row[0] not in seal_list:
                seal_list.append(row[0])
        if line_count == 0:
            print("Column Names: " + str(row))
            line_count += 1
        line_count += 1

# Print the two seal species to check
print(seal_list)
print("Processed " + str(line_count) + " lines.")

# Start the loop that will go through the csv twice for each seal species
# First, open the csv, create a file based on the first and second letters of the scientific names
# Write in the column names, use if loop for extracting data lines and create extracted line of data
# Use string to start the next line of data, and then print the line of data
# file.close is used to avoids errors for unreadable column names
for seal in seal_list:
    with open(os.path.join(file_path, file_name)) as seal_csv:
        csv_reader = csv.reader(seal_csv, delimiter=',')
        file = open(seal + ".csv", "w") #I would not slice this down this much, as it may not be unique
        file.write("scientificName, decimalLongitude, decimalLatitude\n")
        for row in csv_reader:
            if row[0] == seal:
                string = ",".join(row)
                string = string + "\n"
                file.write(string)
        file.close()

# Convert the split csv into a shapefile, and name them both
# Set the x/y coordinates and the output layer
    in_Table = seal + ".csv"
    x_coords = "decimalLongitude"
    y_coords = "decimalLatitude"
    out_Layer = "CombinedSeal"
    saved_Layer = seal + ".shp"

# Set the spatial reference to 4326 which is WGS 1984, define the layer and save it
    spRef = arcpy.SpatialReference(4326)
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")
    arcpy.CopyFeatures_management(lyr, saved_Layer)

# Use print statement to check if the shapefile was created
    if arcpy.Exists(saved_Layer):
        print("Created the shapefile successfully")
    else:
        print("Error")

# Describe the extent of the new shapefile
    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

# Create the fishnet from the shapefile and name it
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
    outFeatureClass = seal + "_fishnet.shp"

# Set the origin of the fishnet
# First, set the coordinates and then define the width/height of the cells
# The number of rows/columns can be left blank due to cell size
# The opposite corner is the max x/y coordinates
# We do not need labels or template extent, and create a polygon
    originCoordinate = str(XMin) + " " + str(YMin) # Your mistake is with the formatting of this, need a space
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)
    cellSizeWidth = "0.25"
    cellSizeHeight = "0.25"
    numRows = ""
    numColumns = ""
    oppositeCorner = str(XMax) + " " + str(YMax)
    labels = "NO_LABELS"
    templateExtent = "#"
    geometryType = "POLYGON"

    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                                   cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                   oppositeCorner, labels, templateExtent, geometryType)

# Use print statement to check if fishnet file was created
    if arcpy.Exists(outFeatureClass):
        print("Created the fishnet file successfully")

# Create the heatmap by joining the shapefile and the fishnet, some parameters can be left blank
    target_features = seal + "_fishnet.shp"
    join_features = seal + ".shp"
    out_feature_class = seal + "heatmap.shp"
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

# Use print statement to check if heatmap was created
    if arcpy.Exists(out_feature_class):
        print("Created the heatmap file successfully")

    # Delete the intermediate files
    #This needs to be inside the seal loop to delete the stuff we don't want any more
    print("Deleting the intermediate files")
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)
