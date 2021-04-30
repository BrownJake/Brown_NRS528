# Final Challenge
# Refer to README.md file for background information on toolbox and descriptions of tools. Use the point (town halls),
# line (rivers), and polygon (lakes) data for tools 1 (List Feature Classes) and 2 (1000-ft Buffer), and use the NDVI
# raster inputs data for tool 3 (NDVI Creation). Note, these are the same data used in Coding Assignments 8 and 6,
# respectively.

# First, import arcpy
import arcpy

# Define the toolbox itself, consisting of a label that matches the name in ArcGIS, an alias (if necessary), and a list
# of the tools contained within the toolbox, which in this case there are three.
class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Brown_Final_Toolbox"
        self.alias = ""
        self.tools = [FeatureList, Buffer1000ft, MakeNDVI]

# Define the first tool, consisting of a label that matches the name in ArcGIS, a brief description, and whether it can
# run in the background (i.e., enable background processing).
class FeatureList(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "List Feature Classes"
        self.description = "This tool will search through a folder and list all shapefiles of a certain feature class."
        self.canRunInBackground = False

    # Define the parameter definitions for the first tool, in this case the folder location of the shapefiles and type
    # of feature class of the shapefiles.
    def getParameterInfo(self):
        """Define parameter definitions"""
        parameters = []
        shp_folder = arcpy.Parameter(name="shp_folder",
                                     displayName="Enter desired folder:",
                                     datatype="DEFolder",
                                     parameterType="Required",
                                     direction="Input")
        parameters.append(shp_folder)
        feature_type = arcpy.Parameter(name="feature_type",
                                       displayName="Enter desired type of feature class:",
                                       datatype="GPString",
                                       parameterType="Required",
                                       direction="Input")
        parameters.append(feature_type)
        return parameters

    # Set the first tool's license and allow for the values, properties, and messages of the parameters to be modified
    # before use.
    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    # Set the code that actually executes the first tool by defining a workspace, using the List Feature Classes tool
    # and adding a message to demonstrate that the tool was successful.
    def execute(self, parameters, messages):
        """The source of code of the tool."""
        shp_folder = parameters[0].valueAsText
        feature_type = parameters[1].valueAsText

        arcpy.env.workspace = shp_folder
        ListFeatures = arcpy.ListFeatureClasses("*", feature_type)
        arcpy.AddMessage("The feature class type for " + feature_type + " has files called " + str(ListFeatures))
        return


# Define the second tool, consisting of a label that matches the name in ArcGIS, a brief description, and whether it can
# run in the background (i.e., enable background processing).
class Buffer1000ft(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buffer 1000 feet"
        self.description = "This tool will apply a 1000-ft buffer around three feature classes."
        self.canRunInBackground = False

    # Define the parameter definitions for the second tool, in this case the input original files and the output buffer
    # files for each of the three feature classes used.
    def getParameterInfo(self):
        """Define parameter definitions"""
        parameters = []
        feature1 = arcpy.Parameter(name="feature1",
                                   displayName="Enter first shapefile:",
                                   datatype="DEFeatureClass",
                                   parameterType="Required",
                                   direction="Input")
        parameters.append(feature1)
        feature1_output = arcpy.Parameter(name="feature1_output",
                                          displayName="Enter output for first shapefile",
                                          datatype="DEFeatureClass",
                                          parameterType="Required",
                                          direction="Output")
        parameters.append(feature1_output)
        feature2 = arcpy.Parameter(name="feature2",
                                   displayName="Enter second shapefile:",
                                   datatype="DEFeatureClass",
                                   parameterType="Required",
                                   direction="Input")
        parameters.append(feature2)
        feature2_output = arcpy.Parameter(name="feature2_output",
                                          displayName="Enter output for second shapefile",
                                          datatype="DEFeatureClass",
                                          parameterType="Required",
                                          direction="Output")
        parameters.append(feature2_output)
        feature3 = arcpy.Parameter(name="feature3",
                                   displayName="Enter third shapefile:",
                                   datatype="DEFeatureClass",
                                   parameterType="Required",
                                   direction="Input")
        parameters.append(feature3)
        feature3_output = arcpy.Parameter(name="feature3_output",
                                          displayName="Enter output for third shapefile",
                                          datatype="DEFeatureClass",
                                          parameterType="Required",
                                          direction="Output")
        parameters.append(feature3_output)
        return parameters

    # Set the second tool's license and allow for the values, properties, and messages of the parameters to be modified
    # before use.
    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    # Set the code that actually executes the second tool by defining the mandatory and optional parameters for the
    # Buffer tool to run it for each of the three feature classes. Also add a message to demonstrate that the tool was
    # successful.
    def execute(self, parameters, messages):
        """The source code of the tool."""
        feature1 = parameters[0].valueAsText
        feature1_output = parameters[1].valueAsText
        feature2 = parameters[2].valueAsText
        feature2_output = parameters[3].valueAsText
        feature3 = parameters[4].valueAsText
        feature3_output = parameters[5].valueAsText

        in_features = feature1
        out_feature_class = feature1_output
        buffer_distance = "1000 feet"
        line_side = "FULL"
        line_end_type = "ROUND"
        dissolve_option = "NONE"
        dissolve_field = "#"
        method = "PLANAR"
        arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance, line_side,
                              line_end_type, dissolve_option, dissolve_field, method)

        if len(parameters) > 2:
            in_features = feature2
            out_feature_class = feature2_output
            buffer_distance = "1000 feet"
            line_side = "FULL"
            line_end_type = "ROUND"
            dissolve_option = "NONE"
            dissolve_field = "#"
            method = "PLANAR"
            arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance, line_side,
                                  line_end_type, dissolve_option, dissolve_field, method)

        if len(parameters) > 4:
            in_features = feature3
            out_feature_class = feature3_output
            buffer_distance = "1000 feet"
            line_side = "FULL"
            line_end_type = "ROUND"
            dissolve_option = "NONE"
            dissolve_field = "#"
            method = "PLANAR"
            arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance, line_side,
                                  line_end_type, dissolve_option, dissolve_field, method)

            arcpy.AddMessage("Buffering complete")
            return


# Define the third tool, consisting of a label that matches the name in ArcGIS, a brief description, and whether it can
# run in the background (i.e., enable background processing).
class MakeNDVI(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Create NDVI"
        self.description = "This tool will create an NDVI by providing a folder containing bands 4 and 5 rasters."
        self.canRunInBackground = False

    # Define the parameter definitions for the third tool, in this case the initial raster files and the output NDVI
    # that is calculated using bands four and five.
    def getParameterInfo(self):
        """Define parameter definitions"""
        parameters = []
        raster_input = arcpy.Parameter(name="raster_input",
                                       displayName="Folder containing rasters",
                                       datatype="DEFolder",
                                       parameterType="Required",
                                       direction="Input")
        parameters.append(raster_input)
        NDVI_output = arcpy.Parameter(name="NDVI_output",
                                      displayName="New NDVI raster",
                                      datatype="GPRasterLayer",
                                      parameterType="Required",
                                      diection="Output")
        parameters.append(NDVI_output)
        return parameters

    # Set the third tool's license and allow for the values, properties, and messages of the parameters to be modified
    # before use.
    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    # Set the code that actually executes the third tool by defining the workspace, bands four and five, the formula
    # used to calculate the NDVI, and using the Raster Calculator tool. Also add a message to demonstrate that the tool
    # was successful.
    def execute(self, parameters, messages):
        """The source code of the tool."""
        raster_input = parameters[0].valueAsText
        NDVI_output = parameters[1].valueAsText

        arcpy.env.workspace = raster_input
        bandFour = arcpy.ListRasters("*", "TIF")
        bandFour = [x for x in bandFour if "B4" in x]
        bandFive = arcpy.ListRasters("*", "TIF")
        bandFive = [x for x in bandFive if "B5" in x]

        formula = 'Float("' + bandFive[0] + '"-"' + bandFour[0] + '") / Float("' + bandFive[0] + '"+"' + bandFour[
            0] + '")'

        arcpy.gp.RasterCalculator_sa(formula, NDVI_output)
        arcpy.AddMessage("NDVI created")
        return