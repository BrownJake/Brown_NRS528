# Midterm Challenge
# For this midterm assignment, I performed a suitability analysis to identify areas suitable for development or other
# activities that are at least outside a 200 ft buffer from lakes and rivers in Kent County, RI. This is adapted from
# a similar assignment in NRS 522: Advance GIS with Professor Jason Parent. Suitability analyses were a big part of this
# class, and so I thought it would be interesting to try it out in python. Additionally, this topic of having
# buffers around water bodies was discussed in NRS 423: Wetland Ecology with Professor Nancy Karraker. Thus, I'm
# combining ideas and concepts from previous classes into this assignment. This also acts as a continuation of Coding
# Challenge 4 where I selected Kent County from the towns of RI. This time after selecting Kent County, I then set it as
# an extent, create buffers around the lakes and rivers, overlay them onto Kent County and create a suitability raster.
# The towns, lakes, and rivers data were part of the class data for NRS 522, so I already had easy access to them.

# First, import os and arcpy. Arcpy.sa will be needed to use the Raster Calculator tool to create the final suitability
# raster towards the end. 
import os
import arcpy
from arcpy.sa import *

# Set the work environment, and allow us to overwrite files when rerunning the code.
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

# Set the working directory and the workspace, these will need to be changed depending on the folder location.
# Create a temporary directory to store the intermediate files and keep them separate from the main products.
# Use os.path.join to join the temporary directory within the main directory, but still keep the intermediate and final
# products separate.
midterm_directory = r"C:\Data\Midterm_Challenge\Midterm_Data"
arcpy.env.workspace = midterm_directory
temporary_directory = os.path.join(midterm_directory, "temporary_files")
if not os.path.exists(temporary_directory):
    os.mkdir(temporary_directory)

# As with Coding Challenge 4, use the Select tool to extract Kent County from the towns data.
in_features = "towns.shp"
out_feature_class = os.path.join(temporary_directory, "KentCounty.shp")
where_clause = '"COUNTY" = \'KENT\''

arcpy.Select_analysis(in_features, out_feature_class, where_clause)

# Use a print statement to confirm that Kent County was extracted.
if arcpy.Exists(out_feature_class):
    print("Kent County selected")

# Use the Describe tool to set Kent County as the extent for the suitability analysis by defining the minimum and
# maximum X and Y coordinates.
desc = arcpy.Describe(out_feature_class)
YMin = desc.extent.YMin
YMax = desc.extent.YMax
XMin = desc.extent.XMin
XMax = desc.extent.XMax

# Use a print statement to confirm that the extent for Kent County has been set.
arcpy.env.extent = arcpy.Extent(XMin, YMin, XMax, YMax)
print("Extent for Kent County:\n YMin: {0},\n YMax: {1},\n XMin: {2},\n XMax: {3}".format(desc.extent.YMin,
                                                                                          desc.extent.YMax,
                                                                                          desc.extent.XMin,
                                                                                          desc.extent.XMax))

# Create a list for the two water features (lakes and rivers) and make sure the towns data are not part of it, which
# can be confirmed by printing the list.
Lakes_Rivers = arcpy.ListFeatureClasses("*", "ALL")
Lakes_Rivers = [x for x in Lakes_Rivers if "towns" not in x]
print(Lakes_Rivers)

# Use a for loop and run the Euclidean Distance tool to create 200 ft buffers around both lakes and rivers.
# The .img extension will make them into raster files.
# The names need to be split (in this case by the first five letters), otherwise it causes issues with the file names
# in subsequent steps. If the names are not split, the file name would be, for example, Lakes.shp_buffer.img and this
# causes problems in subsequent steps, probably due to having more than one extension in the file name.
for water in Lakes_Rivers:
    in_source_data = water + ".shp"
    max_distance = 200
    cell_size = 4
    out_direction_raster = os.path.join(temporary_directory, water[0:5] + "_buffer.img")

    outEucDistance = EucDistance(in_source_data, max_distance, cell_size, out_direction_raster)

# Use a print statement to confirm that buffers were created for lakes and rivers.
    print("Euclidean Distance for " + water + " was created successfully")

# Use a for loop and the Is Null tool to classify areas within each buffer raster as either 0 for being a buffered area
# or 1 for being a non-buffered area.
# As before, the names are split by the first five letters to avoid issues wih the file names in subsequent steps.
arcpy.env.workspace = temporary_directory
buffer = arcpy.ListRasters("*", "ALL")
print(buffer)

for buff in buffer:
    in_raster = buff
    out_raster = arcpy.sa.IsNull(in_raster)
    out_raster.save(os.path.join(temporary_directory, buff[0:5] + "_Null.img"))

# Use a print statement to confirm that the buffers were separated into the two categories.
    print("Buffer areas set for " + buff)

# Use the Raster Calculator tool to multiply and join the lakes and river raster files to provide the suitability raster
# for both. This will represent the land in Kent County that is outside a 200 ft buffer from lakes and rivers.
# I believe the distance can vary between 100-200 ft depending on the width of the overflow, but this scenario assumes
# we want to be conservative with our lakes and rivers, as either for wildlife/plant habitat or for human use.
# Use a print statement to confirm that the suitability raster was created.
arcpy.env.workspace = temporary_directory
inputs = '"Lakes_Null.img" * "River_Null.img"'
arcpy.gp.RasterCalculator_sa(inputs, os.path.join(midterm_directory, "200ft_buffer.img"))
print("Suitability analysis completed")

# Display the 200 ft buffer raster file on ArcGIS Pro. There should be two colors, one for buffered areas (0) and
# another for non-buffered areas (1).
