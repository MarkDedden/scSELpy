from collections import Counter
import numpy as np

def cells_per_cluster(adata,obs_inp):
    Abs_dict = Counter(adata.obs[obs_inp])
    Perc_dict = {ob:round((Abs_dict[ob]/len(adata.obs))*100,2) for ob in sorted(Abs_dict, key=Abs_dict.get, reverse=True)}
    return(Perc_dict)
    
    
    
def update_dict(sub_adata,cluster,Output_dict,which_var,gene):
    if which_var == "var_names":
        Output_dict[cluster] = round(((np.count_nonzero(sub_adata.X[:,list(sub_adata.var_names).index(gene)]))/len(sub_adata.obs))*100,2)
    else:
        Output_dict[cluster] = round(((np.count_nonzero(sub_adata.X[:,list(sub_adata.var[which_var]).index(gene)]))/len(sub_adata.obs))*100,2)

    return(Output_dict)

def cells_expressing_gene(adata,obs_inp,gene,which_var="var_names"):
    Output_dict = {}
    if obs_inp == None:
        Output_dict = update_dict(adata,"All",Output_dict,which_var,gene)
        return(Output_dict)
    
    for cluster in sorted(set(adata.obs[obs_inp])):
        sub_adata = adata[adata.obs[obs_inp] == cluster]
        Output_dict = update_dict(sub_adata,cluster,Output_dict,which_var,gene)
        
    return(Output_dict)



def add_TPM(sub_adata,cluster,Output_dict,which_var,gene,layer_key):
    if layer_key == None:
        array = sub_adata.X
    else:
        array = sub_adata.layers[layer_key]
    
    if which_var == "var_names":
        Output_dict[cluster] = round(np.float32((np.sum(array[:,list(sub_adata.var_names).index(gene)]))/np.sum(array))*1000000,2)
    else:
        Output_dict[cluster] = round(np.float32((np.sum(array[:,list(sub_adata.var[which_var]).index(gene)]))/np.sum(array))*1000000,2)
    return(Output_dict)

def calculate_TPM(adata,obs_inp,gene,which_var="var_names",use_raw=True,layer_key=None):
    Output_dict = {}
    
    if use_raw==True:
        
        if hasattr(adata, "raw"):
            if type(adata.raw) == type(None):
                raise AttributeError("use_raw is passed, but anndata.raw has NoneType.")
            else:
                anndata = adata.raw
        else:
            raise AttributeError("use_raw is passed, but anndata has no .raw.")

  
        
    else:
        anndata = adata
    
    if layer_key != None:
        if hasattr(anndata, "layers"):
            if layer_key not in anndata.layers:
                raise AttributeError(str(layer_key)+" is not found in anndata.layers. Please be aware that use_raw == True by default and that the raw object might not have this specific layer.")
        else:
            raise AttributeError(str(layer_key)+" is not found in anndata.layers. Please be aware that use_raw == True by default and that the raw object might not have layers.")
            
    for cluster in sorted(set(anndata.obs[obs_inp])):
        sub_adata = anndata[anndata.obs[obs_inp] == cluster]
        Output_dict = add_TPM(sub_adata,cluster,Output_dict,which_var,gene,layer_key)
        
    return(Output_dict)
