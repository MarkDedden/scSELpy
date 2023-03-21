# Usage Principles
```{eval-rst}
.. role:: small
```

```{eval-rst}
.. role:: smaller
```

We wrote scSELpy to run with [Scanpy]-based pipelines, making use of [AnnData]. We tried to make it as easy as possible to switch between plotting in Scanpy and plotting/drawing with scSELpy. 
The idea is to run umap, tsne, pca and scatter plots the same way as run they are executed in scanpy, changing sc.pl to scS.pl.

## Import
Import scSELpy as:
```import scselpy as scS```



[Scanpy]: https://scanpy.readthedocs.io/
[AnnData]: https://anndata.readthedocs.io/
