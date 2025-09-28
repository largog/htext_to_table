# htext_to_table
Script que convierte archivos de clasificación taxonómica viral KEGG en una tabla

## Tutorial de uso

Este programa convierte un archivo jerárquico en formato `.htext` a un archivo tabulado `.tsv`.

### 1. Requisitos

* Python 3 instalado en el sistema.
* Un archivo de entrada en formato `.htext`.

El archivo de entrada debe tener esta estructura:

```bash
+J
#<h2><a href="/kegg/brite.html"><img src="/Fig/bget/kegg3.gif" align="middle" border=0></a>&nbsp; KEGG Viruses in Taxonomic Ranks</h2>
!
AdsDNA-RT viruses
B  Riboviria
C    Pararnavirae
D      Artverviricota
E        Revtraviricetes
F          Blubervirales
G            Hepadnaviridae
H              Avihepadnavirus
I                Avihepadnavirus anatigruidae
J                  12639  Duck hepatitis B virus [TAX:12639] [RS:NC_001344]
J                  259931  Ross's goose hepatitis B virus [TAX:259931] [RS:NC_005888]
```

### 2. Ejecución
1. Descargue el archivo de entrada desde este repositorio
2. Guarde el script  `Viral_hierarchies.py` en el mismo directorio que el archivo de entrada
3. Ejecúte el script en la terminal con:
```bash
python Viral_hierarchies.py
```
