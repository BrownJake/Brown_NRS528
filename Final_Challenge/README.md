For this final toolbox assignment, I created an all python toolbox that allows the toolbox and parameters to be created within the python software. The user does not need to interact with ArcCatalog to create anything. This toolbox contains three tools, including a List Feature Classes tool, a 1000-ft Buffer tool, and an NDVI Creation tool. These three tools are adapted from previous coding assignments in NRS 528. The List Feature Classes and 1000-ft Buffer tools are adapted from Coding Assignment 8 and use the same point (town halls), line (rivers), and polygon (lakes) data. The NDVI Creation tool is adapted from Coding Assignment 6 and uses the same raster data from spectral bands four and five. 

Tool Descriptions:

1. List Feature Classes: This tool requires two inputs: (1) a folder location and (2) a feature class type. The tool will search the chosen folder for the desired feature class type, then prints the associated files.

2. 1000-ft Buffer: This tool requires at least two inputs: (1) a feature class (point, line, polygon) and (2) an output location. The other inputs are optional for the Buffer tool. This tool will create a 1000-ft buffer, for up to three input feature classes. 

3. NDVI Creation: This tool requires two inputs: (1) a folder location containing the raster inputs and (2) an output NDVI file calculated from the raster input files, in this case images from bands four (red) and five (near-infrared). PLEASE NOTE: I cannot upload the example data for this tool because the file size is too large, so please obtain the data from the Class 6 (Cheating) folder. It is the Step 3 data that was the same data used for Coding Assignment 6. 
