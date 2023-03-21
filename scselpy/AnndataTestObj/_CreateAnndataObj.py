import pandas as pd
import scanpy as sc
import numpy as np


def updatelist(inplist,val):
    outplist = [inplist[out+(out%val)] if out < 600-val else (600-out)%val for num,out in enumerate(inplist)]
    return(outplist)

def CreateList(n1,n2,n3,n4,n5,n6): #Looks random enough, but creates a dataset that should be the same everywhere. 
	alist = [a for a in range(0,600)]
	blist = [b for b in range(0,600)]
	clist = [c for c in range(0,600)]

	for k in range(n2,n1,-2):
		alist = updatelist(alist,k)
	for r in range(n4,n2,-3):
		blist = updatelist(blist,r)
	for e in range(n6,n5,-4):
		clist = updatelist(clist,e)
	returnlist = [float(np.mean([a,b,c])-(min([a,b,c]))-c%7)-a%3 for a,b,c in zip(alist,blist,clist)]
	return(returnlist)


def adata_gen():

	
	#Since its about the X_* objects, we can make an anndata with 600 cells and only 1 gene, all having an expression of 0.
	adataDict = {}

	adataDict = {"Cell_"+str(x):[0,265643] if x%12==0 or x%23 == 0 or x%7 == 0 or x > 550 or x < 70 else [x%5,35732] if x < 100 or x > 300 else [x%4,231435] if x%9 == 0 else [x%3,65784] for x in range(0,600)}
	adata = pd.DataFrame(adataDict)
	adata = np.float32(adata)
	adata = sc.AnnData(adata)
	adata = adata.T
	adata.var_names = ["ENSG00000075624","ENSG00000146192"]
	adata.var["Genes"] = ["ACTB","FGD2"]


	ylist = CreateList(23,41,31,54,17,23)
	xlist = CreateList(17,31,11,27,33,47)
	adata.obsm['X_umap'] = np.array([[x,y] for x,y in zip(xlist,ylist)])
	adata.obsm['X_tsne'] = adata.obsm['X_umap'].copy()

	#We use the same data for tsne and umap.
	#We also use the same data from pca and scatter

	ylist = CreateList(10,14,11,57,33,67)
	xlist = []
	a = 9
	for num,x in enumerate(ylist):
		a = (num%2)
		if a == 0:
			b = -1
		else:
			b = 1
		xlist.append(float(x+((num%40)*b)))

	adata.obsm['X_pca'] = np.array([[x,y] for x,y in zip(xlist,ylist)])
	adata.obs['x_scat'] = xlist
	adata.obs['y_scat'] = ylist

	adata.obs['CellType1'] = [str(int(x[0]/50)) for x in adata.obsm['X_umap']]
	adata.obs['CellType2'] = [str(int(x[0]/50)) for x in adata.obsm['X_pca']]



	return (adata)
