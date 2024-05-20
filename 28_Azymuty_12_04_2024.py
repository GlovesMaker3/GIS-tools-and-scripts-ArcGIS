# -*- coding: utf-8 -*-
import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_azymut.sde"
u2180 = r'C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\projections\\ETRS 1989 Poland CS92.prj'
u3857 = r'C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\projections\\WGS 1984 Web Mercator (auxiliary sphere).prj'

lista = arcpy.ListTables("pgq_sde.azymuty.mv_*")
print(f'Wczytanie tabel: {lista}')

print('\n')
print('Start')
for x in lista:
    print(x)

    if 'fdd2100' in x or 'fdd3600' in x:
        print('Etap 1 - tworzenie wektora na podstawie tabeli w układzie 2180 - Poland CS92')
        print(f'Parametry: {x}')
        print(f'Parametry: {x}_2180')
        arcpy.management.BearingDistanceToLine(x, f'{x}_2180', 'xpos', 'ypos', 'radius', 'METERS', 'azimuth', 'DEGREES', 'GEODESIC', 'gcell_obj', u2180)

        print('Etap 2 - zamiana ukladu na 3857 - WGS 1984 Web Mercator')
        print(f'Parametry: {x}_2180')
        print(f'Parametry: {x}_3857')
        arcpy.Project_management(f'{x}_2180', f'{x}_3857', u3857)

        print('Etap - 5G DSS lub 5G C-BAND')
        print(f'Parametry: {x}_3857')
        print(f'Parametry: {x}')
        arcpy.management.JoinField(f'{x}_3857', "gcell_obj", f'{x}', "gcell_obj", "loc_name;loc_obj;loc_code;gsite_name;gsite_obj;gsite_id;gcell_name;gcell_obj;gcell_id;band;data_aktualizacji")

    else:
        print('Etap 1 - tworzenie wektora na podstawie tabeli w układzie 2180 - Poland CS92')
        print(f'Parametry: {x}')
        print(f'Parametry: {x}_2180')
        arcpy.management.BearingDistanceToLine(x, f'{x}_2180', 'xpos', 'ypos', 'radius', 'METERS', 'azimuth', 'DEGREES', 'GEODESIC', 'c_obj', u2180)

        print('Etap 2 - zamiana ukladu na 3857 - WGS 1984 Web Mercator')
        print(f'Parametry: {x}_2180')
        print(f'Parametry: {x}_3857')
        arcpy.Project_management(f'{x}_2180', f'{x}_3857', u3857)
        print('Etap - pozostale technologie')
        print(f'Parametry: {x}_3857')
        print(f'Parametry: {x}')
        arcpy.management.JoinField(f'{x}_3857', "c_obj", f'{x}', "c_obj", "loc_name;loc_obj;loc_code;site_name;site_obj;site_id;cell_name;cell_obj;cell_id;band;data_aktualizacji")

print('koniec')



import arcpy
import os

# Set output file names
outdir = r"D:\arcgisserver\mxd\2024_03_01_Cellnex"

#USLUGA ---------------------------
service_name = "cellnex"
#USLUGA ---------------------------

sddraft_filename = service_name + ".sddraft"
sddraft_output_filename = os.path.join(outdir, sddraft_filename)
sd_filename = service_name + ".sd"
sd_output_filename = os.path.join(outdir, sd_filename)

# Reference map to publish
aprx = arcpy.mp.ArcGISProject(r"D:\arcgisserver\mxd\2024_03_01_Cellnex\2024_03_01_Cellnex.aprx")

#Mapa ---------------------------
m = aprx.listMaps('Cellnex_map')[0]
#Mapa ---------------------------


# Create MapServiceDraft and set metadata and server folder properties
target_server_connection = r"C:\Users\buchadan\AppData\Roaming\ESRI\ArcGISPro\Favorites\admin on psgis01.tp.gk.corp.tepenet_6443 (1).ags"
sddraft = arcpy.sharing.CreateSharingDraft("STANDALONE_SERVER", "MAP_SERVICE", service_name, m)
sddraft.targetServer = target_server_connection
sddraft.credits = "Cellnex"
sddraft.description = "Cellnex"
sddraft.summary = "Cellnex"
sddraft.tags = "Cellnex"
sddraft.useLimitations = "Owned by Orange Polska"

#FOLDER ---------------------------
sddraft.serverFolder = "gisserver"
#FOLDER ---------------------------
sddraft.overwriteExistingService = True

# Create Service Definition Draft file
sddraft.exportToSDDraft(sddraft_output_filename)

# Stage Service
print("Start Staging")
arcpy.server.StageService(sddraft_output_filename, sd_output_filename)

# Publish to server
print("Start Uploading")
arcpy.server.UploadServiceDefinition(sd_output_filename, target_server_connection)

print("Finish Publishing_25_04_2024")