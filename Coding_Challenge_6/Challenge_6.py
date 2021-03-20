# Coding Challenge 6
# Calculating NDVI

# First, import os and arcpy
# Set up the spatial extension and allow us to overwrite files when rerunning the code
# Create a list for the months that we have data for in 2015
import os
import arcpy
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
listMonths = ["02", "04", "05", "07", "10", "11"]

# Set the directory that the NDVI files will be stored in
# This will need to be changed depending on the folder location
outputDirectory = r"C:\Data\6_Cheating\DataFolder_Step_3_data_lfs\Step_3_data"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

# Use a for loop and the List Rasters tool to extract bands 4 and 5 from each month and put them into a list
# Use print statements to confirm that the process is working
for month in listMonths:
    arcpy.env.workspace = r"C:\Data\6_Cheating\DataFolder_Step_3_data_lfs\Step_3_data\2015" + month
    print("Extracting Bands 4 and 5 from 2015" + month + "to create NDVI")
    bandFour = arcpy.ListRasters("*", "TIF")
    bandFour = [x for x in bandFour if "B4" in x]
    print("Band 4 is " + str(bandFour) + ".")
    bandFive = arcpy.ListRasters("*", "TIF")
    bandFive = [x for x in bandFive if "B5" in x]
    print("Band 5 is " + str(bandFive) + ".")

# Use the Raster Calculator tool to calculate the NDVI
# The formula for calculating NDVI is (NIR - Red) / (NIR + Red)
# Band four is the red band and band five in the NIR band
    arcpy.gp.RasterCalculator_sa(
        'Float("' + bandFive[0] + '"-"' + bandFour[0] + '") / Float("' + bandFive[0] + '"+"' + bandFour[0] + '")',
        os.path.join(outputDirectory, "NDVI_2015" + month + ".tif"))

# Use a print statement to confirm the NDVI was calculated
    print("NDVI is complete")
