# scSELpy
```{eval-rst}
.. role:: small
```

```{eval-rst}
.. role:: smaller
```
With scSELpy, the user can draw polygons on two-dimensional Scanpy plots in order to select cells. Any cell located within one or more polygons are annotated as belonging to these polygons. Cell annotations are added to ```AnnData``` observations. The coordinates of the polygons are added the ```AnnData.uns```.  

```{include} tree.md
```
