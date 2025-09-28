"""Este programa toma un archivo jerárquico en formato htext
 Y lo transforma en una tabla"""

#Archivos de entrada y salida

HTEXT = 'Viruses.htext'
OUTPUT = 'Viruses.tsv'


#Abrir un archivo de salida
with open(OUTPUT, "w") as out_file:
    tab = '\t'
    out_file.write(tab.join(['name', 'RS', 'TAX', '\n']))           #Crear los títulos de las columnas

    with open(HTEXT) as file:
        for line in file:          #Recorre cada línea del archivo
            line = line.strip()
            if line.startswith('J'):        #Verifica el nivel de taxonomía deseado
                set = line.split()
                taxonomy = (set[1])
                set.remove(taxonomy)
                #Selecciona todos los strings que contienen algún código RS
                RS_codes = []
                for string in set[:]:

                    if "NC" in string:          # Selecciona strings con código RS
                        RS_codes.append(string)
                        set.remove(string)
                    elif "TAX" in string:
                        set.remove(string)        #Elimina de la lista a la taxonomía
                pass
                sep = ","
                RS = sep.join(RS_codes)
                in_id = RS.find("RS:")          #Índice de inicio del código RS
                fin_id = RS.find("]")           #Índice del final del código RS
                RS = RS[in_id + 3:fin_id]
                set.pop(0)          #Elimina la letra de jerarquía
                table_sep = " "
                name = table_sep.join(set)
                out_file.write(tab.join([name, RS, taxonomy, '\n']))
        pass












