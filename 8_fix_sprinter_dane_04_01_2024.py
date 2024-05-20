import arcpy
print('Skrypt z dnia 12_01_2023')
print('\n')
#arcpy.SetLogHistory(True)
# log file  C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.5\ArcToolbox\History

# Local variables:
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde"

#lsita_1  =  arcpy.ListTables("pgq_sde.ogolne.mv_f*", "ALL")
lsita_1  =  arcpy.ListTables("pgq_sde.ogolne.mv_fix_sprinter_dane", "ALL")

#print(lsita_1)
epsg_2180 = "_2180"
epsg_3857 = "_3857"
epsg_4326 = "_4326"

e2180 = r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\projections\\ETRS 1989 Poland CS92.prj"
e3857 = r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\projections\\WGS 1984 Web Mercator (auxiliary sphere).prj"
e4326 = r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\projections\\WGS 1984.prj"
# arcpy.env.outputCoordinateSystem = e3857

for x in lsita_1:
	print(x)
	#print("{} test".format(x))

	desc = arcpy.Describe(r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde\\{}".format(x))
	path = desc.path
	print('path')
	print(path)
	whole_path = path+'\\'+x
	print('whole_path')
	print(whole_path)
	#print(path)
	name = desc.name
	print('name')
	print(name)

	print('Start - arcpy.management.XYTableToPoint')
	#wynik_1 = arcpy.management.XYTableToPoint(whole_path, "wsp_geo_x", "wsp_geo_y", None, "C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde\\{}{}".format(name,epsg_4326), coordinate_system=e4326,)
	wynik_1 = arcpy.management.XYTableToPoint(whole_path,
											  "C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde\\{}{}".format(
												  name, epsg_4326), "wsp_geo_x", "wsp_geo_y", None,
											  coordinate_system=e4326)

	#wynik_1 = arcpy.XYTableToPoint_management(whole_path, "wsp_geo_x", "wsp_geo_y", None,"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde\\{}{}".format(name, epsg_4326), coordinate_system=e4326)

	print('Meta - arcpy.management.XYTableToPoint')
	#print(f'{path}\\{name}{epsg3}')
	#print('\n')
	#print(f'Etap1: Wrstwa zdarzen o nazwie: {name}{epsg_4326} - tymczasowo - zostala utworzona w opraciu o {epsg_4326}')

	print('Start - CopyFeatures_management 3857')
	print(r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde\\{}{}".format(name, epsg_3857))
	arcpy.env.outputCoordinateSystem = e3857
	arcpy.CopyFeatures_management(wynik_1, r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde\\{}{}".format(name,epsg_3857))

	#print(f'Etap 2: kopiowanie warstwy tymczasowej {name}{epsg_4326} i dodanie do bazy {name}{epsg_3857} z ukladem: {epsg_3857}')

	print('Meta- CopyFeatures_management 3857')
	print('\n')


	print('Start - CopyFeatures_management 2180')
	print(r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde\\{}{}".format(name,epsg_2180))
	arcpy.env.outputCoordinateSystem = e2180
	arcpy.CopyFeatures_management(wynik_1, r"C:\\Users\\zz_gis_esri\\AppData\\Roaming\\ESRI\\Desktop10.8\\ArcCatalog\\126.185.136.190_ogolne.sde\\{}{}".format(name,epsg_2180))

	#print(f'Etap 3: kopiowanie warstwy tymczasowej {name}{epsg_4326} i dodanie do bazy {name}{epsg_2180} z ukladem: {epsg_2180}')

	print('Meta- CopyFeatures_management 2180')
	print('\n')


print('Skrypt skoczyl prace')

