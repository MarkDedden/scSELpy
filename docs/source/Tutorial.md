# Tutorial
```{eval-rst}
.. role:: small
```

```{eval-rst}
.. role:: smaller
```
## Getting started

After installation of scSELpy, lets load scSELpy as scS. scSELpy does not use dependencies that scanpy does not use, if scanpy runs fine on your system, scSELpy should also work.


```python
 
#If plots are not being shown on Jupyter Notebook, try using:
#%matplotlib inline
#Do not use it on ipython.

import scanpy as sc 
import scselpy as scS 
adata = scS.generate.adata()
```


```python
sc.pl.umap(adata,color='CellType1')
sc.pl.scatter(adata,"x_scat","y_scat",color='CellType2') #in scatter plot, x_scat and y_scat could be e.g. n_genes and n_counts in a real anndata object.
```


    
![png](Tutorial_files/Tutorial_3_0.png)
    



    
![png](Tutorial_files/Tutorial_3_1.png)
    


## Selecting cells on UMAP

We will now select our cells using scSELpy.
### Some tips before:
Left click to select.<br>
Middle button to erase last selected point.<br>
Right click once when you are done selecting.<br>
Right click twice when you want to exit. <b>Do not use the X(cross)</b> in the top right corner to exit.

### Running scSELpy
Lets run scSELpy. Since we imported scSELpy as scS, we can basically copy paste the code of scanpy imported as sc, and change sc to scS.

A window should popup, in which you can select your cells. Left click a few times on the plot, afterwards right click two times to exit. 


```python
scS.pl.umap(adata,color="CellType1")#,helpbox=True 
```


    
![png](Tutorial_files/Tutorial_7_0.png)
    


## Ploting selected cells

The selected cells are annotated and stored as ```Anndata observations```. By default, it is stored as REMAP_1. The second time your run scSELpy, it will be stored as REMAP_2 and so on. If scSELpy.settings.verbosity is atleast 2 (2 by default), the stored observation name will be output after it is added by scSELpy.


```python
sc.pl.umap(adata,color="REMAP_1")
```


    
![png](Tutorial_files/Tutorial_10_0.png)
    


Lets say we are only interested in our select cells, we can remove the other cells.


```python
adata_selected = adata[adata.obs["REMAP_1"] != "Other"]
sc.pl.umap(adata_selected,color="REMAP_1")
```


    
![png](Tutorial_files/Tutorial_12_0.png)
    


Or the inverse, only keep other.


```python
adata_unselected = adata[adata.obs["REMAP_1"] == "Other"]#Lets say we are only interested in our select cells, we can remove the other cells.
sc.pl.umap(adata_unselected,color="REMAP_1")
```


    
![png](Tutorial_files/Tutorial_14_0.png)
    


Replot the selection with the CellTypes as background. 


```python
scS.pl.umap(adata_unselected,color="CellType1",replot_lines="REMAP_1")
```


    
![png](Tutorial_files/Tutorial_16_0.png)
    


The coordinates of the polygons are stored in ```Anndata Unstructured annotation```. By running adata.uns, we can see the coordinates of the polygon. Alternatively, we can run scSELpy.pl.umap(adata,printcords=True), to print the coordinates of the polygon. These coordinates can be added to the mock parameter, to automatically redraw the polygons. More on the mock parameter in the ```Mock toturial```.


```python

```

## Selecting cells on Scatter plots.

Besides UMAP, we can also select on PCA, TSNE and Scatter plots. It is basically all the same. Here we demonstrate the cell selection on Scatter plots. 

This time, lets make multiple overlapping selections. 
After you made your selection with left click, right click once and make a new selection with left click. After you are done, right click twice


```python
scS.pl.scatter(adata,"x_scat","y_scat",color='CellType2') 
```


    
![png](Tutorial_files/Tutorial_21_0.png)
    


For the consequetive scatter plot, the selected cells were stored as REMAP_2


```python
sc.pl.scatter(adata,"x_scat","y_scat",color='REMAP_2')
```


    
![png](Tutorial_files/Tutorial_23_0.png)
    


Lets use the selection from above and add an extra selection to it, using the load parameter. 


```python
scS.pl.scatter(adata,"x_scat","y_scat",color='REMAP_2',load="REMAP_2",replot_lines="REMAP_2")

```


    
![png](Tutorial_files/Tutorial_25_0.png)
    


Revisualize using scanpy. Now we have an extra selection.


```python
sc.pl.scatter(adata,"x_scat","y_scat",color='REMAP_2')
```


    
![png](Tutorial_files/Tutorial_27_0.png)
    



```python

```

It is also possible to totally overwrite any existing cluster.


```python

scS.pl.scatter(adata,"x_scat","y_scat",color='REMAP_2',load="REMAP_2",overwrite=True)
sc.pl.scatter(adata,"x_scat","y_scat",color='REMAP_2')
```


    
![png](Tutorial_files/Tutorial_30_0.png)
    



    
![png](Tutorial_files/Tutorial_30_1.png)
    



```python

```


```python
from scanpy.plotting import palettes
color_pal = palettes.vega_20
#color_pal = palettes.default_102

```

scSELpy is not made for more than one input for the color parameter. If this is done, the lines will always be shown on the right most plot. Example:


```python
scS.pl.umap(adata,color=["CellType2","CellType1"],replot_lines="REMAP_2",line_palette=palettes.default_102[5:8],line_labels=["A","B","C"])

```


    
![png](Tutorial_files/Tutorial_34_0.png)
    


With line_palette, we can specify the colors of the lines


```python
scS.pl.umap(adata,line_palette=palettes.default_102) 
```


    
![png](Tutorial_files/Tutorial_36_0.png)
    


We can also add a legend


```python
scS.pl.umap(adata,replot_lines="REMAP_3",line_palette=palettes.default_102[5:8],line_labels=["A","B","C"])
```


    
![png](Tutorial_files/Tutorial_38_0.png)
    


Or change the position of the legend


```python
scS.pl.umap(adata,replot_lines="REMAP_3",line_palette=palettes.default_102[12:15],line_labels=["A","B","C"],line_loc='upper right',line_bbox_to_anchor=(-0.05,1))
```


    
![png](Tutorial_files/Tutorial_40_0.png)
    


Or not show all labels


```python
scS.pl.umap(adata,replot_lines="REMAP_3",line_palette=palettes.default_102[12:14],line_labels=["A","B","_nolegend_"],line_loc='upper right',line_bbox_to_anchor=(-0.05,1))

```


    
![png](Tutorial_files/Tutorial_42_0.png)
    



```python

```

## Changing annotation names


```python
sc.pl.umap(adata,color="REMAP_3")
```


    
![png](Tutorial_files/Tutorial_45_0.png)
    


We are going to rename the annotations. Number 1 and 2 will be part of "gene A" and number 3 will be "gene B"
Lets generate a dictionary in which we can assign the names we want to replace for REMAP_3.


```python
scS.annotate.gen_dict(adata.obs['REMAP_3'])
```




    {'1': '1', '3': '3', '2': '2', 'Other': 'Other'}



Lets copy the dict above and rename:


```python
input_dict = {'2': 'Gene B',
 '3': 'Gene A',
 'Other': 'Other',
 '1': 'Gene A'}
```


```python
adata.obs['REMAP_3_renamed'] = scS.annotate.rename(adata.obs['REMAP_3'],input_dict)
```


```python
sc.pl.umap(adata,color="REMAP_3_renamed")
```


    
![png](Tutorial_files/Tutorial_51_0.png)
    


Now the annotations are renamed. 
If we would load REMAP_3_renamed and plot more lines, the reannotated names would not change. 
If we however used replot_lines parameter together with the load parameter, the old numeric names would reappear and be added to the new annotations. Please be aware of this.


```python

```

## Selection tools

scSELpy has a function to:
1) calculate the % of cells in each selection 





```python
scS.tl.cells_per_cluster(adata,"REMAP_3_renamed")
```




    {'Other': 57.17, 'Gene A': 25.5, 'Gene B': 11.67, 'Gene A,Gene B': 5.67}



2) to calculate the % of cells expressing a certain gene in each selection 


```python
scS.tl.cells_expressing_gene(adata,"REMAP_3_renamed","ENSG00000075624")
```




    {'Gene A': 49.02, 'Gene A,Gene B': 50.0, 'Gene B': 58.57, 'Other': 46.36}



In the case that the gene name is not stored in anndata.var_names, but e.g. in ``anndata.var["Genes"]``, we can run: 


```python
scS.tl.cells_expressing_gene(adata,"REMAP_3_renamed","ACTB",which_var="Genes")
```




    {'Gene A': 49.02, 'Gene A,Gene B': 50.0, 'Gene B': 58.57, 'Other': 46.36}



3) Calculate the Transcripts per Million:


```python
scS.tl.calculate_TPM(adata,"REMAP_3_renamed","ACTB",which_var="Genes",use_raw=False)
```




    {'Gene A': 7.33, 'Gene A,Gene B': 6.2, 'Gene B': 11.82, 'Other': 6.87}




```python

```

## Tips and tricks

If you do not want to store to REMAP_1, you can also create your own name.


```python
adata.obs['Own_name'] = ['Other']*len(adata.obs)
scS.pl.umap(adata,load="Own_name",printcords=True)
sc.pl.umap(adata,color="Own_name")
```


    
![png](Tutorial_files/Tutorial_66_0.png)
    



    
![png](Tutorial_files/Tutorial_66_1.png)
    


If you want to show a subcluster but not move the entire plot, you can draw a line around it and change the line_palette parameter to a color with a transparancy setting of 0, e.g. (0,0,0,0). 


```python
scS.pl.umap(adata,color='CellType1')
```


    
![png](Tutorial_files/Tutorial_68_0.png)
    



```python
for ct in sorted(set(adata.obs['CellType1'])):
    print(ct)
    scS.pl.umap(adata[adata.obs['CellType1'] == ct],color="CellType1",replot_lines="REMAP_4",line_palette=[(0,0,0,0)],size=200)
```

    0



    
![png](Tutorial_files/Tutorial_69_1.png)
    


    1



    
![png](Tutorial_files/Tutorial_69_3.png)
    


    2



    
![png](Tutorial_files/Tutorial_69_5.png)
    


    3



    
![png](Tutorial_files/Tutorial_69_7.png)
    


    4



    
![png](Tutorial_files/Tutorial_69_9.png)
    


    5



    
![png](Tutorial_files/Tutorial_69_11.png)
    


    6



    
![png](Tutorial_files/Tutorial_69_13.png)
    



```python

```
