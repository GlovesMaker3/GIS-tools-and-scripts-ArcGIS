# -*- coding: utf-8 -*-
import arcpy
import logging

# Ustawienie konfiguracji logowania
logging.basicConfig(filename='D:\\replikacja\\model_builder\\Python_3\\log_Przeciazone.txt', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# Przykładowe logowanie
logging.debug('Rozpoczęcie skryptu.')
arcpy.env.workspace = r'C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\ArcCatalog\126.185.136.190_przeciazone.sde'
arcpy.env.overwriteOutput = True




lista = arcpy.ListTables("*", "ALL")

# Filtracja tabel rozpoczynających się od 'mv_przeciazone_' i niekończących się na 'a'
mv_przeciazone_tables = [table for table in lista if table.startswith('pgq_sde.przeciazone.mv_przeciazone_') and not table.endswith('a')]


# for table in mv_przeciazone_tables:
#     print("Kolumny dla tabeli:", table)
#     fields = arcpy.ListFields(table)
#     for field in fields:
#         print("\t", field.name)
print('-------------------------------------------')
print('-------------------------------------------')
print(mv_przeciazone_tables)
print('-------------------------------------------')
print('-------------------------------------------')
paths = {
    "sde": r'C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\ArcCatalog\126.185.136.190_przeciazone.sde',
    "_PUWG_92_": r'C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\projections\ETRS 1989 Poland CS92.prj',
	'_WGS_84_4326': r'C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\projections\WGS 1984.prj',
	"_WGS_84_3857": r'C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\projections\WGS 1984 Web Mercator (auxiliary sphere).prj',
    "geobaza": r'D:\arcgisserver\mxd\2024_05_15_Przeciazone\2024_05_15_Przeciazone.gdb',
}


warstwy = [
	"mv_przeciazone_gsm",
	"mv_przeciazone_lte700",
	"mv_przeciazone_lte800",
	"mv_przeciazone_lte1800",
	"mv_przeciazone_lte2100",
	"mv_przeciazone_lte2600",
	"mv_przeciazone_u900",
	"mv_przeciazone_u2100",
]

for x, t in zip(mv_przeciazone_tables, warstwy):

	try:
		arcpy.management.XYTableToPoint(fr'{paths["sde"]}\\{x}', fr'{paths["geobaza"]}\\{t}_t_4326', "e_lon84", "e_lat84", None, paths["_WGS_84_4326"])
		print(f'wykonanie warstwy {paths["geobaza"]}\\{t}_t')
		print('-------------------------------------------')
		print('-------------------------------------------')
		arcpy.management.Project(fr'{paths["geobaza"]}\\{t}_t_4326', fr'{paths["geobaza"]}\\{t}_3857_t', paths["_WGS_84_3857"])
		print(f'wykonanie warstwy {paths["geobaza"]}\\{t}_t')
		print('-------------------------------------------')
		print('-------------------------------------------')
		arcpy.management.TruncateTable(fr'{paths["sde"]}\\{t}_3857_t')
		print(f'wykonanie TruncateTable {paths["sde"]}\\{t}_3857_t')
		print('-------------------------------------------')
		print('-------------------------------------------')

		field_mapping = 'id "id" true true false 4 Long 0 10,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,id,-1,-1;cell_obj "cell_obj" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,cell_obj,-1,-1;cell_name "cell_name" true true false 150 Text 0 0,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,cell_name,0,150;e_lon84 "e_lon84" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,e_lon84,-1,-1;e_lat84 "e_lat84" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,e_lat84,-1,-1;radius "radius" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,radius,-1,-1;loc_name "loc_name" true true false 200 Text 0 0,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,loc_name,0,200;loc_obj "loc_obj" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,loc_obj,-1,-1;xpos "xpos" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,xpos,-1,-1;ypos "ypos" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,ypos,-1,-1;loc_n_name "loc_n_name" true true false 200 Text 0 0,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,loc_n_name,0,200;loc_n_code "loc_n_code" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,loc_n_code,-1,-1;day_wh_id "day_wh_id" true true false 8 Double 8 38,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,day_wh_id,-1,-1;mno "mno" true true false 20 Text 0 0,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,band1,-1,-1;vendor "vendor" true true false 40 Text 0 0,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,type1,0,10;cap_mark "cap_mark" true true false 1073741822 Text 0 0,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,cap_mark,0,20;nazwa_warstwy "nazwa_warstwy" true true false 25 Text 0 0,First,#;' + \
						f'data_aktualizacji "data_aktualizacji" true true false 8 Date 0 0,First,#,' + \
						f'{paths["geobaza"]}\\{t}_3857_t,data_aktualizacji,-1,-1'

		arcpy.management.Append(fr'{paths["geobaza"]}\\{t}_3857_t', fr'{paths["sde"]}\\{t}_3857_t',"NO_TEST", field_mapping)
		print(f'wykonanie Append do pgq_sde.pgq_sde.przeciazone.{t}_3857_t')

	except Exception as e:
		logging.error(f'Błąd {str(e)}')

logging.debug('Zakończenie skryptu.')