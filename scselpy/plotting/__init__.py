from ._scselpy import Remap


def umap(adata,**args):
    ReturnVar = Remap(adata,remove_show_override=False,map_attr="umap",**args)

    if ReturnVar is None:
        pass
    else:
        return(ReturnVar)
    
def tsne(adata,**args):
    ReturnVar = Remap(adata,remove_show_override=False,map_attr="tsne",**args)
    if ReturnVar is None:
        pass
    else:
        return(ReturnVar)
    
def pca(adata,**args):
    ReturnVar = Remap(adata,remove_show_override=False,map_attr="pca",**args)
    if ReturnVar is None:
        pass
    else:
        return(ReturnVar)
    
def scatter(adata, x=None, y=None,**args):
    if x == None or y == None:
        raise AttributeError("Please run as *.scatter(adata,x,y,...). e.g. *.scatter(adata,'n_genes','n_counts',...)")
        
    #elif x not in adata.obs or y not in adata.obs:
        #raise AttributeError("Second and third arguments should be members of anndata.obs")

    ReturnVar = Remap(adata,x_scat=x,y_scat=y,remove_show_override=False,map_attr="scatter",**args)
    if ReturnVar is None:
        pass
    else:
        return(ReturnVar)

def embedding(adata,basis,**args):
    ReturnVar = Remap(adata,basis=basis,remove_show_override=False,map_attr="embedding",**args)
    if ReturnVar is None:
        pass
    else:
        return(ReturnVar)
