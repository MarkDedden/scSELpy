# Tools
```{eval-rst}
.. role:: small
```

```{eval-rst}
.. role:: smaller
```

Calculate basic cell statistics of selected regions.

## Percentage cells in each region
```scselpy.tl.cells_per_cluster(adata,obs_inp)```
Calculates the percentage of cells in each selected region. 



<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;adata: <code>AnnData</code></b> </div>  &nbsp;&nbsp;&nbsp; Annotated data matrix. <br><br>  


<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;obs_inp: <code> str</code></b> </div> &nbsp;&nbsp;&nbsp; Keys for annotations of observations/cells from <code>AnnData</code>.  <br><br>  


## Percentage cells expressing a certain gene
```scselpy.tl.cells_expressing_gene(adata,obs_inp,gene,which_var="var_names")```
Calculates the percentage of cells expressing a certain gene.



<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;adata: <code>AnnData</code></b> </div>  &nbsp;&nbsp;&nbsp; Annotated data matrix. <br><br>  


<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;obs_inp: <code> str</code></b> </div> &nbsp;&nbsp;&nbsp; Keys for annotations of observations/cells from <code>AnnData</code>.  <br><br>  

<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;gene: <code> str</code></b> </div> &nbsp;&nbsp;&nbsp; The gene name that should be used for the calculation.  <br><br>  

<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;which_var: <code> str</code></b> (default:  <code>'var_names'</code>) </div> &nbsp;&nbsp;&nbsp; Key in the <code>Anndata</code> variable that habors the given gene name. The default will use <code>anndata.var_names</code> <br><br>  


## Calculating Transcripts per Million
```scselpy.tl.calculate_TPM(adata,obs_inp,gene,which_var="var_names",use_raw=True,layer_key=None)```
Calculates the transcripts per million of a certain gene within a region of cells.

<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;adata: <code>AnnData</code></b> </div>  &nbsp;&nbsp;&nbsp; Annotated data matrix. <br><br>  


<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;obs_inp: <code> str</code></b> </div> &nbsp;&nbsp;&nbsp; Keys for annotations of observations/cells from <code>AnnData</code>.  <br><br>  

<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;gene: <code> str</code></b> </div> &nbsp;&nbsp;&nbsp; The gene name that should be used for the calculation.  <br><br>  

<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;which_var: <code> str</code></b> (default:  <code>'var_names'</code>) </div> &nbsp;&nbsp;&nbsp; Key in the <code>Anndata</code> variable that habors the given gene name. The default will use <code>anndata.var_names</code> <br><br>  

<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;use_raw: <code> bool</code></b> (default:  <code>True</code>) </div> &nbsp;&nbsp;&nbsp; It is recommended to use unnormalized and unscaled values for calculating the TPM. Therefore, by default the script will use anndata.raw. If the unnormalized values are not stored here, please pass <code>use_raw=False</code> <br><br>  

<div style="background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;"><b>&nbsp;layer_key: <code> str</code></b> (default:  <code>None</code>) </div> &nbsp;&nbsp;&nbsp; If the unnormalized counts are stored in layers, please specify the layer key. <br><br>  
