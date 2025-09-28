# htext_to_table
Script que convierte archivos de clasificación taxonómica viral KEGG en una tabla

## Tutorial de uso

Este programa convierte un archivo jerárquico en formato `.htext` a un archivo tabulado `.tsv`.

### 1. Requisitos

* Python 3 instalado en el sistema.
* Un archivo de entrada en formato `.htext`.


### 2. Ejecución
1. Descargue el archivo de entrada desde https://www.kegg.jp/kegg-bin/get_htext?Viruses
2. Modifique la extension del archivo a ".htext"
3. Guarde el script como `convert_to_tsv.py` en el mismo directorio que el archivo de entrada
4. Ejecúte el script en la terminal con:
```bash
python Viral_hierarchies.py
```
