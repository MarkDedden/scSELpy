# scSELpy - **S**ingle-**c**ell **sel**ection **Py**thon 
scSELpy is a manual cell selection tool to support Scanpy-based pipelines. It calls Scanpy generated plots and allows to user to draw polygons on top of them, in order to select cells. The cells located within these drawn polygons are assigned an identity, which will be stored in the Anndata object as an observation. Cells located within multiple Polygons will have multiple identities for in the same observation, separated by a comma.  

## Installation
Python3-7+  
```pip install scselpy```  
Installation and import are fully in lower-case.

## Running scSELpy
In order to get started with scSELpy, please refer to the [documentation].
The Tutorial can also be found as a notebook on this github/folder. 


[documentation]: https://scselpy.readthedocs.io/
