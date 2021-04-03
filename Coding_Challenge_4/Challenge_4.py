# Coding Challenge 4
# Running a Tool From Arcpy

# For this coding challenge, I used arcpy to run the Select Analysis tool to extract
# Kent County from within a dataset for the towns of RI

# The towns data were part of the class data for NRS 522: Advanced GIS
# I thought it would be interesting to use these data for this challenge, as I live in Kent County
# These data are included, along with this python file, in my submission for this assignment

# First, import arcpy
import arcpy

# Next, set the workspace which can be changed depending on the base folder location
# This is how it is set up for mine
arcpy.env.workspace = r"C:\Data\Coding_Challenge_4\Coding_Challenge_4_Data"

# Setting up the Select Analysis tool
# First, select towns as the input feature class from which features will be selected
# Second, name the output feature class to be created
# Third, set an SQL expression used to select a subset of features
in_feature = "towns.shp"
out_feature = "Kent_County.shp"
where_clause = '"COUNTY" = \'KENT\''

# Use the Select Analysis tool to extract features from towns that are in Kent County
arcpy.Select_analysis(in_feature, out_feature, where_clause)

# Display the Kent County feature on ArcGIS Pro and compare it with the original towns data to make sure it worked



### Feedback - Great work once more Jake, only suggestion is to improve your use of
# print statements to provide user updates. Without it, it is not intuitive what is happening.