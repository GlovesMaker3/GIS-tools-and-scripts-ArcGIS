# -*- coding: utf-8 -*-
import arcpy

print("Start")
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\arcgisserver\mxd\Rollout\Rollout.sde"
lista  =  arcpy.ListTables("pgq_sde.rollout.mv_*", "ALL")


e2180 = r"C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\projections\ETRS 1989 Poland CS92.prj"
e3857 = r"C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\projections\WGS 1984 Web Mercator (auxiliary sphere).prj"

for x in lista:

    print(f'Wykotanie dla: {x}')
    wynik1 = arcpy.management.XYTableToPoint(fr"{x}", fr"{x}_2180_t", "xpos", "ypos", None, e2180)
    arcpy.management.Project(wynik1, fr"{x}_3857_t", e3857)

print('Koniec')