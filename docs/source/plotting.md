# Plotting
```{eval-rst}
.. role:: small
```

```{eval-rst}
.. role:: smaller
```

scSELpy can be employed to manual select and annotate cells on scanpy generated plots. The following plots are supported: UMAP, TSNE, PCA and scatter plots. All these plots take the normal scanpy parameters, with additonal scSELpy parameters. The scSELpy parameters are the same for all 4, unless specified otherwise.

If none of the above mentioned embeddings work, scSELpy also supports scanpy's ```embedding``` plotting parameter.  

## UMAP
scselpy.pl.umap(adata,*kwargs)

## TSNE
scselpy.pl.tsne(adata,*kwargs)

## PCA
scselpy.pl.pca(adata,*kwargs)

## Scatter plot
scselpy.pl.scatter(adata,x,y,*kwargs)
<br>For example:<br>
```scselpy.pl.scatter(adata,'n_genes','n_counts',color="ATCB")``` 

## Embedding
scselpy.pl.embedding(adata,basis=arg,*kwargs)
<br>For example, in order to run umap:<br>
```scselpy.pl.embedding(adata,basis="X_umap",color="ATCB")``` 

## Parameters
```{include} generated_markdown/Parameters.md

```

## Removed or changed parameters

In general, all scanpy plotting parameters can be passed to the scselpy.pl.* functions, with the exception of:

- ```Layers``` or ```Layer``` 

The following parameters have been changed:

- ```components``` in scSELpy, you can only have 2 dimensions. e.g. the 3rd and 4th component.
- ```save``` As shown in parameters, scSELpy has its own saving function implemented. 




## Running other commands (Not supported)
In case the user would like to use scSELpy with other commands, it is technically possible by calling scSELpy's Remap() function directly and set its internal parameter ```override``` to True:

```
scselpy.pl._scselpy.Remap(adata,override=True,scat_plot=False,basis=<input from obsm>,plotattr=<function>,remove_show_override=True)
```
<br>

```scat_plot``` defines if the entry is a scatter plot. If passing a scatterplot, use the arguments "x_scat" and "y_scat". Options: "scat","embedding" and anything else, e.g. False<br><br>
```plotattr``` passes the function that we want to run. e.g. sc.pl.umap, sc.pl.draw_graph or maybe even a function that does not stem from scanpy.<br><br>
```remove_show_override``` disables the scSELpy internal override which always passes show=False to scanpy. The default of remove_show_override=True, this is probabaly the best if not running scanpy directly.<br><br>

With the following command we run a scatter plot this way:


```
scselpy.pl._scselpy.Remap(adata,x_scat="n_counts",y_scat="n_genes",override=True,scat_plot="scat",plotattr=sc.pl.scatter,remove_show_override=False)
```

To run this on e.g. Scanpy's draw_graph:<br>
```
scselpy.pl._scselpy.Remap(adata,override=True,scat_plot=False,basis="X_draw_graph_fa",plotattr=sc.pl.draw_graph,remove_show_override=False)
```

To try this on an external Scanpy-based package, such as [Scirpy]:<br>
```
import scirpy as ir
df, dst, lk = ir.tl.repertoire_overlap(adata, "CD4_and_CD8_cells", inplace=False)
dfT = df.T
First = "CD8"
Second = "CD4"
adata.obsm['X_Repertoire'] = np.array([[dfT[First][ID],dfT[Second][ID]] if np.isnan(float(ID)) == False else [0.0,0.0] for ID in list(adata.obs["clone_id"])])
scselpy.pl._scselpy.Remap(adata,override=True,remove_show_override=True,scat_plot=False,basis="X_Repertoire",plotattr=ir.pl.repertoire_overlap,...)
```
<br><br>
This function only works on scanpy-based packages and if the Anndata object is the only non-keyword argument.




[Scirpy]: https://scverse.org/scirpy/











