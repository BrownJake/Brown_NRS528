# Coding Challenge 8
# Creating a function

# For this coding assignment I created a buffer function that can be used with point, line, and polygon data.
# I demonstrate this function using data for these three feature class types using course data from NRS 522.
# This buffer function will set the workspace, print the files for the selected feature class type, and create a
# buffer for a specified distance.

# First, import arcpy to allow the list feature classes and buffer tools to run in the function.
import arcpy

# This function requires three inputs: a, b, and c
# a is the workspace or directory
# b is the feature class type (point, line, or polygon)
# c is the specified buffer distance with units

# The list feature classes tool will list all the files in the workspace that correspond to the feature class type of
# interest. In this case, only one file for each type will be listed.
# Define the input feature, output feature, and buffer distance for the buffer analysis tool. I spliced the name for
# the output feature by the first five letters to avoid the issue with multiple extensions in the file name, similar to
# the midterm assignment.
def Buffer(a, b, c):
    arcpy.env.workspace = a
    BufferFile = arcpy.ListFeatureClasses("*", b)
    print("The feature class type for " + b + " has files called " + str(BufferFile))
    for Buff in BufferFile:
        in_feature = Buff
        out_feature_class = Buff[0:5] + "_Buffer.shp"
        buffer_distance = c
        arcpy.Buffer_analysis(in_feature, out_feature_class, buffer_distance)

# No code in the buffer function above should have to be changed. The three inputs, however, will vary depending on the
# workspace, the feature class type for the files of interest, and the desired buffer distance. Enter "Point",
# "Polyline", or "Polygon" depending on which feature class type you want to work with. The units must be specified for
# the buffer distance, otherwise, the units for the input features' spatial reference will be used. I currently have
# this function set to my directory, for the point feature class data (RI town halls), with a desired buffer distance
# of 1000 feet. Two other example data include a line feature class (RI rivers) and a polygon feature class (RI lakes).
Directory = r"C:\Data\Coding_Challenge_8\Challenge_8_Data"
FileType = "Point"
Distance = "1000 feet"

# This buffer function can be used with different point, line, and polygon data. Use a print statement to confirm that
# the buffer analysis is finished.
Buffer(Directory, FileType, Distance)
print("Buffering Complete")