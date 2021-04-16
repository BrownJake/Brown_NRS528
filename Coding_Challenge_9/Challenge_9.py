# Coding Challenge 9
# Using the arcpy.da module

# First, import arcpy.
import arcpy

# Set the workspace, which will need to be changed depending on the folder.
# Allow us to overwrite files when rerunning the code.
arcpy.env.workspace = r'C:\Data\Challenge_9'
arcpy.env.overwriteOutput = True

# Define the shapefile that will be used as the input.
input_shp = 'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'

# 1. Count how many sites have photos, and how many do not (2 numbers), print the results.
# Create a list for the two fields we need from the attribute table: "Site" and "photo".
fields = ['Site', 'photo']

# Create an expression that will select rows within "photo" that have photos.
# Use cursor to manipulate the data to count how many sites have photos.
expressionPhoto = arcpy.AddFieldDelimiters(input_shp, "photo") + " = 'y'"
countPhoto = 0
with arcpy.da.SearchCursor(input_shp, fields, expressionPhoto) as cursor:
    for row in cursor:
        print(u'{0}, {1}'.format(row[0], row[1]))
        countPhoto = countPhoto + 1

# Create an expression that will select rows within "photos" that do not have photos.
# Use cursor to manipulate the data to count of how many sites do not have photos.
expressionNoPhoto = arcpy.AddFieldDelimiters(input_shp, "photo") + " <> 'y'"
countNoPhoto = 0
with arcpy.da.SearchCursor(input_shp, fields, expressionNoPhoto) as cursor:
    for row in cursor:
        print(u'{0}, {1}'.format(row[0], row[1]))
        countNoPhoto = countNoPhoto + 1

# Use print statements to show the number of sites that have and do not have photos, as well as to check that the
# process worked.
print(countPhoto, "sites have photos")
print(countNoPhoto, "sites do not have photos")

# 2. Count how many unique species there are in the dataset, print the result.
# Define the input shapefile and the field we want ("Species") to obtain unique values which are the different species
# names within this field.
# Use cursor to manipulate the data to sort the individual species names, and assign them to their own object.
input = input_shp
field2 = "Species"
def unique_values(input, field2):
    with arcpy.da.SearchCursor(input, field2) as cursor:
        return sorted({row[0] for row in cursor})
uniqueSpecies = unique_values(input_shp, field2)

# Use print statement to show the number of unique species, as well as to check that the process worked.
print("There are "+str(len(uniqueSpecies))+" unique species")

# 3. Generate two shapefiles, one with photos and the other without.
# Name the output shapefile for photos, create an expression to select rows within "photos" that have photos, and use
# the Select tool to extract the points with photos into their own shapefile.
outputPhoto = "Invasive_Photo.shp"
ExpressionPhoto = "photo = 'y'"
arcpy.Select_analysis(input_shp, outputPhoto, ExpressionPhoto)

# Use the Exists tool to check that the photo shapefile was created.
if arcpy.Exists(outputPhoto):
    print("Photo shapefile created")

# Name the output shapefile for no photos, create an expression to select rows within "photos" that do not have photos,
# and use the Select tool to extract the points with no photos into their own shapefile.
outputNoPhoto = "Invasive_No_Photo.shp"
ExpressionNoPhoto = "photo <> 'y'"
arcpy.Select_analysis(input_shp, outputNoPhoto, ExpressionNoPhoto)

# Use the Exists tool to check that the no photos shapefile was created.
if arcpy.Exists(outputNoPhoto):
    print("No photo shapefile created")