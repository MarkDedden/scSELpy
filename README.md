# scSELpy 
scSELpy (**S**ingle-**c**ell **sel**ection in **Py**thon) is a manual cell selection tool to support Scanpy-based pipelines. It calls Scanpy generated plots and allows to user to draw polygons on top of them, in order to select cells. The cells located within these drawn polygons are assigned an identity, which will be stored in the Anndata object as an observation. Cells located within multiple Polygons will have multiple identities for in the same observation, separated by a comma.  

## Installation
Python3-7+  
  
```pip install scselpy```  
  
Installation and import are fully in lower-case.

## Backend
When running scSELpy on Jupyter Notebook, the backend will temprary change to an interactive backend. The default interactive backend is Qt5Agg. If you are getting this error:  ```ImportError: Failed to import any of the following Qt binding modules: PyQt6, PySide6, PyQt5, PySide2``` please install PyQt5 with ```pip install PyQt5```. 

If the backend does not work on your computer, try using to a different one by running ```scselpy.pl.umap(adata,interactive_backend="TkAgg")```. All matplotlib supported backends can be found [here].

While running scSELpy in a Python shell such as ipython the default backend is usually interactive and therefore a switch will not be conducted, however, if you are experiencing troubles, it is possible to temporary switch the interactive backend to e.g. Qt5Agg or TkAgg by using the command above.

## Running scSELpy
In order to get started with scSELpy, please refer to the [documentation].
The Tutorial can also be found as a notebook on this github/folder. 


[documentation]: https://scselpy.readthedocs.io/
[here]: https://matplotlib.org/stable/users/explain/backends.html

