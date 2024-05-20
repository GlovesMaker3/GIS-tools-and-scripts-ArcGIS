# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True

paths = {
    "sde": r'C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\ArcCatalog\126.185.136.190_stacje.sde',
    "_PUWG_92_": r'C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\projections\ETRS 1989 Poland CS92.prj',
    "_WGS_84_": r'C:\Users\zz_gis_esri\AppData\Roaming\ESRI\Desktop10.8\projections\WGS 1984 Web Mercator (auxiliary sphere).prj',
    "geobaza": r'D:\arcgisserver\mxd\2024_05_13_Stacje_act\2024_05_13_Stacje_act.gdb',
}

# Lista nazw warstw
warstwy = [
    "mv_stacje_act",
    "mv_stacje_act_gsm",
    "mv_stacje_act_indoor",
    "mv_stacje_act_l800",
    "mv_stacje_act_l1800",
    "mv_stacje_act_l2100",
    "mv_stacje_act_l2600",
    "mv_stacje_act_macro",
    "mv_stacje_act_micro",
    "mv_stacje_act_small",
    "mv_stacje_act_w900",
    "mv_stacje_act_w2100",
    "mv_stacje_act_5g1800",
    "mv_stacje_act_5g2100",
    "mv_stacje_act_5g3600"
]

tabele = [
    "stacje_act",
    "stacje_act_gsm",
    "stacje_act_indoor",
    "stacje_act_l800",
    "stacje_act_l1800",
    "stacje_act_l2100",
    "stacje_act_l2600",
    "stacje_act_macro",
    "stacje_act_micro",
    "stacje_act_small",
    "stacje_act_w900",
    "stacje_act_w2100",
    "stacje_act_5g1800",
    "stacje_act_5g2100",
    "stacje_act_5g3600"
]


for warstwa, tabela in zip(warstwy, tabele):


    arcpy.management.XYTableToPoint(fr'{paths["sde"]}\pgq_sde.stacje.{warstwa}', fr'{paths["geobaza"]}\\{warstwa}_geom_2180_XY', 'x', 'y', None, paths["_PUWG_92_"])
    print(f'wykonanie warstwy {paths["geobaza"]}\\{warstwa}_geom_2180_XY')
    print('-------------------------------------------')
    print('-------------------------------------------')
    arcpy.management.Project(fr'{paths["geobaza"]}\\{warstwa}_geom_2180_XY', fr'{paths["geobaza"]}\\{tabela}_geom_3857_t', paths["_WGS_84_"])
    print(f'wykonanie warstwy {paths["geobaza"]}\\{tabela}_geom_3857_t')
    print('-------------------------------------------')
    print('-------------------------------------------')

    arcpy.management.TruncateTable(fr"{paths['sde']}\\pgq_sde.stacje.{tabela}_geom_3857_t")
    print(f'wykonanie TruncateTable {tabela}_geom_3857_t')
    print('-------------------------------------------')
    print('-------------------------------------------')
    arcpy.management.Append(fr'{paths["geobaza"]}\\{tabela}_geom_3857_t', fr"{paths['sde']}\\pgq_sde.stacje.{tabela}_geom_3857_t", "NO_TEST",
                            r'loc_obj "loc_obj" true true false 8 Double 0 12,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,loc_obj,-1,-1;loc_name "loc_name" true true false 200 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,loc_name,0,200;loc_code "loc_code" true true false 4 Long 0 10,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,loc_code,-1,-1;x "x" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,x,-1,-1;y "y" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,y,-1,-1;height "height" true true false 4 Float 1 4,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,height,-1,-1;networks_name "networks_name" true true false 200 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,networks_name,0,200;networks_code "networks_code" true true false 4 Long 0 10,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,networks_code,-1,-1;mno_name "mno_name" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,mno_name,0,1073741822;rainbow_type "rainbow_type" true true false 50 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,rainbow_type,0,50;lon84 "lon84" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lon84,-1,-1;lat84 "lat84" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lat84,-1,-1;gloc "gloc" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,gloc,-1,-1;wloc2100 "wloc2100" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,wloc2100,-1,-1;wloc900 "wloc900" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,wloc900,-1,-1;wloc "wloc" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,wloc,-1,-1;lloc "lloc" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc,-1,-1;lloc800 "lloc800" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc800,-1,-1;lloc1800 "lloc1800" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc1800,-1,-1;lloc2100 "lloc2100" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc2100,-1,-1;lloc2600 "lloc2600" true true false 8 Double 3 16,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc2600,-1,-1;indoor "indoor" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,indoor,0,1073741822;macro "macro" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,macro,0,1073741822;micro "micro" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,micro,0,1073741822;small "small" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,small,0,1073741822;gloc_1 "gloc_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,gloc_1,0,1073741822;wloc_1 "wloc_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,wloc_1,0,1073741822;lloc_1 "lloc_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc_1,0,1073741822;wloc2100_1 "wloc2100_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,wloc2100_1,0,1073741822;wloc900_1 "wloc900_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,wloc900_1,0,1073741822;lloc1800_1 "lloc1800_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc1800_1,0,1073741822;lloc800_1 "lloc800_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc800_1,0,1073741822;lloc2100_1 "lloc2100_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc2100_1,0,1073741822;lloc2600_1 "lloc2600_1" true true false 1073741822 Text 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lloc2600_1,0,1073741822;lte_ca "lte_ca" true true false 4 Long 0 10,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,lte_ca,-1,-1;data_aktualizacji "data_aktualizacji" true true false 8 Date 0 0,First,#,' +
                            f'{paths["geobaza"]}\\{tabela}_geom_3857_XY_t,data_aktualizacji,-1,-1', '', '')
    print(f'wykonanie Append do pgq_sde.stacje.{tabela}_geom_3857_t')
