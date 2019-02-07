#!/usr/bin/env python

import grass.script as gscript
from grass.pygrass.modules import Module

def ExportTiff(inRas, outPath = "L:\\_04_LiDAR_Workspace\\Trinity_Geomorph\\"):
    modN = "r.out.gdal"
    outName = inRas.split("@")[0]
    print(outName)
    Module(modN,
        input="rasTrinityDetrend_fomrms@DetrendSurface", 
        output=outPath+outName+".tif", 
        format='GTiff',
        overwrite = True)
