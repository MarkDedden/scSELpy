
#https://docs.python.org/3/library/unittest.html
import unittest
from . import utils as util
from .. import plotting as scSpl
from ..AnndataTestObj import _CreateAnndataObj as gen


filestr = str(__file__)
file_path = str(filestr[:-len(filestr.split("/")[-1])])



def GenerateMockDict():
	Mock = {'umap':[
	    [(140.0, 215.0), (140.0, 110.0), (200, 110)],
	    [(190.0, 205.0), (190.0, 85.0), (260.0, 85.0), (260.0, 205.0)],
	    [(170.0, 150.0), (169.85012495834079, 152.99500249940485), (169.40199733523724, 155.96007992385182), (168.66009467376819, 158.8656061998402), (167.63182982008655, 161.6825502692595), (166.32747685671117, 164.3827661581261), (164.76006844729034, 166.93927420185105), (162.94526561853465, 169.32653061713074), (160.90120128041497, 171.52068272698568), (158.64829904811992, 173.4998072888245), (156.20906917604418, 175.2441295442369), (153.60788364276732, 176.73622080184305), (150.8707326343002, 177.9611725790168), (148.02496485873763, 178.9067455625158), (145.09901428700724, 179.5634918996538), (142.12211605003108, 179.92484959812163), (139.12401433096133, 179.98720809124515), (136.13466517113426, 179.74994431357405), (133.18393715920737, 179.21542892634585), (130.30131299409487, 178.38900263062243), (127.51559490358572, 177.27892280477045), (124.85461686200426, 175.8962809994662), (122.34496648233961, 174.2548921145877), (120.01171936160526, 172.3711563653016), (117.87818853376262, 170.26389541653452), (115.96569153359198, 167.95416432311868), (114.29333739893157, 165.4650411546439), (112.87783573948815, 162.82139640701487), (111.73332977994025, 160.0496445046771), (110.87125504551227, 157.17747987641943), (110.30022510198663, 154.23360024179598), (110.02594549180162, 151.24741987299868), (110.05115672615742, 148.24877569717256), (110.37560690273406, 145.2676291757025), (110.99605422261618, 142.33376693919502), (111.90629938127613, 139.47650316931134), (113.09724750997562, 136.72438670115437), (114.55699904868779, 134.10491577274516), (116.27096864256754, 131.6442632717184), (118.22203087399583, 129.36701522448075), (120.39069137409169, 127.29592514076212), (122.75528160400196, 125.45168666806765), (125.29217535977904, 123.85272682759233), (127.97602483760076, 122.51502189751633), (130.78001390064742, 121.45193778331452), (133.6761260170766, 120.67409647004709), (136.63542419194835, 120.18926989099607), (139.62834009611325, 120.00230227307698), (142.62496950318337, 120.11506173492478), (145.59537108267722, 120.52642162127002), (148.50986556389674, 121.23227176010583), (151.33933228138935, 122.225559530168), (154.05550013901126, 123.49636032839537), (156.63123008537477, 125.03197673328292), (159.04078627827897, 126.81706537332032), (161.26009322873773, 128.83379023288816), (163.2669763553074, 131.06200086383026), (165.0413835451747, 133.47943372207075), (166.5655855082395, 136.06193461758716), (167.82435292232103, 138.78370005509277), (168.80510859951093, 141.61753505403206), (169.4980531532775, 144.53512487183696), (169.89626291069652, 147.5073179154749)]
	],
	'pca':[
	    [(136.463281561131, 204.38811626195732), (141.9917562724014, 73.01946284032377), (226.30099561927517, 78.49315673289183), (220.7725209080047, 271.8970076036302)],
	    [(35.568618080446015, 140.52835418199658), (126.78845081640776, 16.457959283787105), (150.284468339307, 147.82661270542067)],
	    [(170.0, 150.0), (169.85012495834079, 152.99500249940485), (169.40199733523724, 155.96007992385182), (168.66009467376819, 158.8656061998402), (167.63182982008655, 161.6825502692595), (166.32747685671117, 164.3827661581261), (164.76006844729034, 166.93927420185105), (162.94526561853465, 169.32653061713074), (160.90120128041497, 171.52068272698568), (158.64829904811992, 173.4998072888245), (156.20906917604418, 175.2441295442369), (153.60788364276732, 176.73622080184305), (150.8707326343002, 177.9611725790168), (148.02496485873763, 178.9067455625158), (145.09901428700724, 179.5634918996538), (142.12211605003108, 179.92484959812163), (139.12401433096133, 179.98720809124515), (136.13466517113426, 179.74994431357405), (133.18393715920737, 179.21542892634585), (130.30131299409487, 178.38900263062243), (127.51559490358572, 177.27892280477045), (124.85461686200426, 175.8962809994662), (122.34496648233961, 174.2548921145877), (120.01171936160526, 172.3711563653016), (117.87818853376262, 170.26389541653452), (115.96569153359198, 167.95416432311868), (114.29333739893157, 165.4650411546439), (112.87783573948815, 162.82139640701487), (111.73332977994025, 160.0496445046771), (110.87125504551227, 157.17747987641943), (110.30022510198663, 154.23360024179598), (110.02594549180162, 151.24741987299868), (110.05115672615742, 148.24877569717256), (110.37560690273406, 145.2676291757025), (110.99605422261618, 142.33376693919502), (111.90629938127613, 139.47650316931134), (113.09724750997562, 136.72438670115437), (114.55699904868779, 134.10491577274516), (116.27096864256754, 131.6442632717184), (118.22203087399583, 129.36701522448075), (120.39069137409169, 127.29592514076212), (122.75528160400196, 125.45168666806765), (125.29217535977904, 123.85272682759233), (127.97602483760076, 122.51502189751633), (130.78001390064742, 121.45193778331452), (133.6761260170766, 120.67409647004709), (136.63542419194835, 120.18926989099607), (139.62834009611325, 120.00230227307698), (142.62496950318337, 120.11506173492478), (145.59537108267722, 120.52642162127002), (148.50986556389674, 121.23227176010583), (151.33933228138935, 122.225559530168), (154.05550013901126, 123.49636032839537), (156.63123008537477, 125.03197673328292), (159.04078627827897, 126.81706537332032), (161.26009322873773, 128.83379023288816), (163.2669763553074, 131.06200086383026), (165.0413835451747, 133.47943372207075), (166.5655855082395, 136.06193461758716), (167.82435292232103, 138.78370005509277), (168.80510859951093, 141.61753505403206), (169.4980531532775, 144.53512487183696), (169.89626291069652, 147.5073179154749)]
	]
	}


	Mock['tsne'] = Mock['umap']
	Mock['scat'] = Mock['pca']
	Mock['scatter'] = Mock['pca']


	return(Mock)


def GenerateMockDict2():
    Mock = {'umap':[
        [(116.6675428116288, 56.62557027225898), (121.88608124253284, 178.02825607064014), (121.88608124253284, 241.2944444444444), (169.89663480684982, 239.5845474613686), (170.94034249303064, 195.12722590139802), (164.6780963759458, 95.95320088300218), (160.50326563122258, 49.78598233995584)],
        [(141.71652727996812, 99.37299484915377), (212.6886499402628, 176.31835908756435), (277.39852648347266, 85.69381898454745), (214.77606531262444, 36.1068064753495)]
    ],
	'pca':[
        [(133.6990442054958, 27.405347068923234), (111.58514536041415, 142.3529188128526), (77.03217841497408, 288.3180892813343), (115.73150139386695, 244.52853814078983), (183.45531660692944, 133.2300956585725), (274.67514934289125, 34.70360559234733)],
        [(229.06523297491037, 308.3883002207506), (180.69107925129424, 127.75640176600444), (310.6102349661489, 260.94961981849406)]    
    	]
    	}
    
    Mock['tsne'] = Mock['umap']
    Mock['scat'] = Mock['pca']
    Mock['scatter'] = Mock['pca']
    
    
    return(Mock)
def GenerateMockDict3():
    Mock = {'umap':[
        [(78.05035842293904, 123.31155261221483), (175.11517323775385, 114.76206769683589), (245.04358821186776, 179.73815305371593), (232.5190959776981, 261.8132082413539), (155.28472720031857, 282.3319720382633), (111.44900438072477, 253.2637233259749)]
    	],
        'pca':[
        [(168.25201115093586, 321.1602526367427), (211.09769016328153, 178.84421142997306), (284.3499800876144, 129.58096639686045), (345.16320191158894, 169.72138827569293), (336.87048984468333, 273.7215722344862), (280.20362405416165, 326.63394652931083)]
        ]
    	}
    
    Mock['tsne'] = Mock['umap']
    Mock['scat'] = Mock['pca']
    Mock['scatter'] = Mock['pca']
    
    
    return(Mock)
class TestStringMethods(unittest.TestCase):

    def GetHighestRemap(self):
        HighestRemap = max([int(xlx.split("_")[-1]) if xlx[:5] == "REMAP" else 0 for xlx in list(self.adata.obs)]) # Everytime we run our sc.pl.*, we return "REMAP_x" in adata.obs. Where x is an increasing number (increase by 1). This code checks the highest number (latest addition).
        return(HighestRemap)
    def UpdateCreatedRemap(self,attr):
        
        HighestRemap = self.GetHighestRemap()
        
        self.CreatedRemap[attr] = list(self.adata.obs['REMAP_'+str(HighestRemap)])


    def Run_scselpy(self,**params):
        scSpl.umap(self.adata,mock=self.Mock,**params)
        self.UpdateCreatedRemap("umap")        
        scSpl.pca(self.adata,mock=self.Mock,**params)
        self.UpdateCreatedRemap("pca")
        scSpl.tsne(self.adata,mock=self.Mock,**params)
        self.UpdateCreatedRemap("tsne")


        

    def setUp(self):

        
        self.Mock = GenerateMockDict()
        self.ValidateREMAP = util.GetValidateLists(file_path+"REMAP_val.txt")
        
         
        self.adata = gen.adata_gen() 
        
        self.CreatedRemap = {}



                
        
    def test_all_mocks_in_one_run(self): #If all runs where only Mock1 are loaded pass, but this one fails, the Mock data in Mock2 or Mock3 is incorrect.
        self.ValidateREMAP_3rd = util.GetValidateLists(file_path+"REMAP_val3.txt")

        self.Mock2 = GenerateMockDict2()
        self.Mock3 = GenerateMockDict3()
        self.Mock4 = {key:self.Mock[key] + self.Mock2[key] + self.Mock3[key] for key in self.Mock}

        scSpl.umap(self.adata,mock=self.Mock4)

        self.UpdateCreatedRemap("umap")        
        scSpl.pca(self.adata,mock=self.Mock4)

        self.UpdateCreatedRemap("pca")
        scSpl.tsne(self.adata,mock=self.Mock4)

        self.UpdateCreatedRemap("tsne")

        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock4)

        
        self.UpdateCreatedRemap("scat")

        
        
        
        #for attr in ['scat']:
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP_3rd[attr]) 



    def test_load(self): #Check if loading works correctly.
        self.ValidateREMAP_2nd = util.GetValidateLists(file_path+"REMAP_val2.txt")
        self.Mock2 = GenerateMockDict2()


        
        scSpl.umap(self.adata,mock=self.Mock)
        scSpl.umap(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()))

        self.UpdateCreatedRemap("umap")        
        scSpl.pca(self.adata,mock=self.Mock)
        scSpl.pca(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()))

        self.UpdateCreatedRemap("pca")
        scSpl.tsne(self.adata,mock=self.Mock)
        scSpl.tsne(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("tsne")
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()))
        
        self.UpdateCreatedRemap("scat")

        
        
        
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP_2nd[attr])
        
    def test_load2(self): #I have had some bugs where the first load works, but when you load again it fails. Therefore a double load test.
        self.ValidateREMAP_3rd = util.GetValidateLists(file_path+"REMAP_val3.txt")
        self.Mock2 = GenerateMockDict2()
        self.Mock3 = GenerateMockDict3()


        scSpl.umap(self.adata,mock=self.Mock)
        scSpl.umap(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()))
        scSpl.umap(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("umap")        
        scSpl.pca(self.adata,mock=self.Mock)
        scSpl.pca(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()))
        scSpl.pca(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("pca")
        scSpl.tsne(self.adata,mock=self.Mock)
        scSpl.tsne(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()))
        scSpl.tsne(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("tsne")

        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()))
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()))
        
        self.UpdateCreatedRemap("scat")

        
        
        
        for attr in ['scat']:
        #for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP_3rd[attr])
    def test_load3(self): 
        self.ValidateREMAP_3rd = util.GetValidateLists(file_path+"REMAP_val3.txt")

        self.Mock2 = GenerateMockDict2()
        self.Mock3 = GenerateMockDict3()
        self.Mock4 = {key:self.Mock2[key] + self.Mock3[key] for key in self.Mock}
        

        scSpl.umap(self.adata,mock=self.Mock)

        scSpl.umap(self.adata,mock=self.Mock4,load='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("umap")        
        scSpl.pca(self.adata,mock=self.Mock)

        scSpl.pca(self.adata,mock=self.Mock4,load='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("pca")
        scSpl.tsne(self.adata,mock=self.Mock)

        scSpl.tsne(self.adata,mock=self.Mock4,load='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("tsne")

        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock)

        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock4,load='REMAP_'+str(self.GetHighestRemap()))
        
        self.UpdateCreatedRemap("scat")

        
        
        
        #for attr in ['scat']:
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP_3rd[attr])            
            
    def test_load_replot(self):
        self.ValidateREMAP_3rd = util.GetValidateLists(file_path+"REMAP_val3.txt")
        self.Mock2 = GenerateMockDict2()
        self.Mock3 = GenerateMockDict3()

        
        scSpl.umap(self.adata,mock=self.Mock)
        scSpl.umap(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()))
        scSpl.umap(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("umap")        
        scSpl.pca(self.adata,mock=self.Mock)
        scSpl.pca(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()))
        scSpl.pca(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("pca")
        scSpl.tsne(self.adata,mock=self.Mock)
        scSpl.tsne(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()))
        scSpl.tsne(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()))
        self.UpdateCreatedRemap("tsne")
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()))
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()))
        
        self.UpdateCreatedRemap("scat")

        
        
        
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP_3rd[attr])

    def test_param0(self):


        parameters={}
        scatparams={}
        self.Run_scselpy(**parameters)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock,**scatparams)
        self.UpdateCreatedRemap("scat")
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP[attr])

    def test_param1(self):


        parameters = {'legend_loc':'upper left','sort_order':False,'legend_fontsize':'xx-small','na_in_legend':False,'vmax':3.1,'vmin':0.2,'wspace':0.4,'hspace':0.4,'title':'test','legend_fontoutline':4}
        scatparams={'legend_loc':'upper left','sort_order':False,'legend_fontsize':'xx-small','title':'test','legend_fontoutline':4}
        self.Run_scselpy(**parameters)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock,**scatparams)
        self.UpdateCreatedRemap("scat")
        
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP[attr])


    def test_return_fig(self):


        parameters={'return_fig':True}
        scatparams={}
        self.Run_scselpy(**parameters)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock,**scatparams)
        self.UpdateCreatedRemap("scat")
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP[attr])

    def test_show_false(self):


        parameters={'show':False}
        scatparams={'show':False}
        self.Run_scselpy(**parameters)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock,**scatparams)
        self.UpdateCreatedRemap("scat")
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP[attr])


    def test_save(self):

        
        scSpl.umap(self.adata,mock=self.Mock,save="test_umap.png")
        self.UpdateCreatedRemap("umap")        
        scSpl.pca(self.adata,mock=self.Mock,save="test_pca.png")
        self.UpdateCreatedRemap("pca")
        scSpl.tsne(self.adata,mock=self.Mock,save="test_tsne.png")
        self.UpdateCreatedRemap("tsne")
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock,save="test_scat.png")
        self.UpdateCreatedRemap("scat")
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP[attr])
            
    def test_line_colors(self): 
        

        parameters={'line_palette':[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)]}
        scatparams={'line_palette':[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)]}
        self.Run_scselpy(**parameters)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock,**scatparams)
        self.UpdateCreatedRemap("scat")
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP[attr])



    def test_load_replot_line_colors(self):
        self.ValidateREMAP_3rd = util.GetValidateLists(file_path+"REMAP_val3.txt")
        self.Mock2 = GenerateMockDict2()
        self.Mock3 = GenerateMockDict3()

        scSpl.umap(self.adata,mock=self.Mock)
        scSpl.umap(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()),line_palette=[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)])
        scSpl.umap(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()),line_palette=[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)])
        self.UpdateCreatedRemap("umap")     
        scSpl.pca(self.adata,mock=self.Mock)
        scSpl.pca(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()),line_palette=[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)])
        scSpl.pca(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()),line_palette=[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)])
        self.UpdateCreatedRemap("pca")
        scSpl.tsne(self.adata,mock=self.Mock)
        scSpl.tsne(self.adata,mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()),line_palette=[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)])
        scSpl.tsne(self.adata,mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()),line_palette=[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)])
        self.UpdateCreatedRemap("tsne")
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock)
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock2,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()),line_palette=[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)])
        scSpl.scatter(self.adata,'x_scat','y_scat',mock=self.Mock3,load='REMAP_'+str(self.GetHighestRemap()),replot_lines='REMAP_'+str(self.GetHighestRemap()),line_palette=[(0.8, 0.4, 0.8, 1),(0, 0, 1, 1),(1, 0, 0, 1),(0.7, 0.7, 0.7, 1)])
        
        self.UpdateCreatedRemap("scat")

        
        
        
        
        for attr in ['tsne','scat','pca','umap']:

            self.assertEqual(self.CreatedRemap[attr], self.ValidateREMAP_3rd[attr])


def run():


    
	if __name__ == '__main__':
	    unittest.main()


#python -m unittest scselpy/tests/scselpy_tests.py


