def GetValidateLists(filename):
	with open(filename) as g: # Did not use pickle or other libs, to make scSELpy use as minimal libs as possible.
		ReadMocks = g.read().splitlines()
	MockDict = {}
	for l in ReadMocks:
		if l[0] == "<" and l[-1] == ">":
			MockDict[l[1:-1]] = []
			AppName = l[1:-1]
		else:
			MockDict[AppName].append(l)

	MockDict['tsne'] = MockDict['umap']
	MockDict['scat'] = MockDict['pca']


	return (MockDict)


