# Coding Challenge 4
# Running Tools From Arcpy

# For this coding challenge, I used arcpy to run two tools to:
# 1. Select Kent County within a dataset for the towns of RI, and
# 2. Clip the wetlands from a RI wetlands dataset that are within Kent County

# The towns and wetlands data were part of the class data for NRS 522: Advanced GIS
# I though it would be interesting to use these data for this challenge, as I live in Kent County
# These data are included, along with this python file, in my submission for this assignment

# First, import arcpy
import arcpy

# Next, set the workspace which can be changed depending on the base folder location
# This is how it is set up for mine
arcpy.env.workspace = r"C:\Data\Coding_Challenge_4\Coding_Challenge_4_Data"

# Step 1: Select Kent County from RI towns
# First, select towns as the input feature class from which features will be selected
# Second, name the output feature class to be created
# Third, set an SQL expression used to select a subset of features
in_feature_1 = "towns.shp"
out_feature_1 = "Kent_County.shp"
where_clause = '"COUNTY" = \'KENT\''

# Use the Select Analysis tool to extract features from towns that are in Kent County
arcpy.Select_analysis(in_feature_1, out_feature_1, where_clause)

# Step 2: Clip wetlands that are within Kent County
# First, name the feature to be clipped
# Second, name the feature used to clip the input feature
# Third, name the output clipped feature to be created
in_feature_2 = "wetlands.shp"
clip_feature = "Kent_County.shp"
out_feature_2 = "Wetlands_Clipped.shp"

# Use the CLip Analysis tool to select features from wetlands that are in Kent County
arcpy.Clip_analysis(in_feature_2, clip_feature, out_feature_2)

# Display features on ArcGIS Pro and compare with the original towns and wetlands data to make sure it worked
