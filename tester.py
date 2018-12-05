import arcpy
import os

arcpy.env.workspace = "U:\Shared\GIS\StuData\ARJOHN8714\Fall 2018\GISC 3200K Python Programming\GIT\FinalProject"
arcpy.MakeFeatureLayer_management("DissolvedCalifornia.shp", "DissolvedCalifornia1")


arcpy.env.workspace = "U:\Shared\GIS\Studata\ARJOHN8714\Fall 2018\GISC 4601K Spatial Analysis for Society\Final\crithab_all_layers"
arcpy.MakeFeatureLayer_management("CRITHAB_POLY.shp", "CritHabPoly")
arcpy.MakeFeatureLayer_management("CRITHAB_LINE.shp", "CritHabLine")
arcpy.Clip_analysis('CritHabLine', 'DissolvedCalifornia1', r'U:\Shared\GIS\StuData\ARJOHN8714\Fall 2018\GISC 3200K Python Programming\GIT\FinalProject\CaliCritline2.shp', '#')
arcpy.Clip_analysis('CritHabPoly', 'DissolvedCalifornia1', r'U:\Shared\GIS\StuData\ARJOHN8714\Fall 2018\GISC 3200K Python Programming\GIT\FinalProject\CaliCritPoly2.shp', '#')
arcpy.env.workspace = "U:\Shared\GIS\StuData\ARJOHN8714\Fall 2018\GISC 4601K Spatial Analysis for Society\Final\PADUS1_4CA_Shapefile"
arcpy.MakeFeatureLayer_management("PADUS1_4Fee_Easements_CA.shp", "ConservationAreas")

arcpy.env.workspace = "U:\Shared\GIS\StuData\ARJOHN8714\Fall 2018\GISC 3200K Python Programming\GIT\FinalProject"
arcpy.MakeFeatureLayer_management("unpro.shp", "UnprotectedAreas")
arcpy.Clip_analysis('CaliCritline2', 'UnprotectedAreas', r'U:\Shared\GIS\StuData\ARJOHN8714\Fall 2018\GISC 3200K Python Programming\GIT\FinalProject\UnprotectedStreams.shp', '#')
arcpy.Clip_analysis('CaliCritPoly2', 'UnprotectedAreas', r'U:\Shared\GIS\StuData\ARJOHN8714\Fall 2018\GISC 3200K Python Programming\GIT\FinalProject\UnprotectedLakes.shp', '#')







