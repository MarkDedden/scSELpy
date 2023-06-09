"""
Created on Tue Oct 12 17:55:21 2021

@author: Mark Dedden
"""

from ..config import settings

import numpy as np

import scanpy as sc
#from scanpy.plotting._tools import scatterplots as scsp
from scanpy import logging as logger

import matplotlib
from matplotlib.backend_bases import MouseButton as MouseButton
from matplotlib import pyplot as plt 
from matplotlib import path as mpltPath
import sys
import os  
import atexit



def is_notebook() -> bool: #code in this function is borrowed from https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter


def logger_info(msg,warning=False): #I do not want to change the scanpy verbosity settings, but I would like to use its logger to display information.
    current_settings = sc.settings.verbosity # To revert to this setting after the info has been printed
    sc.settings.verbosity = settings.verbosity #scSELpy internal verbosity setting, mimics Scanpy's but starts with 2 (info) on initializion. 
    if warning:
        
        logger.warning(msg)
    else:
        logger.info(msg)
    sc.settings.verbosity = current_settings

def log_scale(VarDict,returned):
            if VarDict['return_fig_backup'] == True:
                ax_ref = returned.gca()
            else:
                ax_ref = returned
            ax_ref.set_yscale('log')
            ax_ref.set_xscale('log')

def getXY(cordlist,scat_plot,returnVar,lc,colorline,ls,custom_lines):


    x = [p[0] for p in cordlist]
    x = x+[x[0]] # We want to have the last dot connect back to the first placed dot, so we add it to the list.
    y = [p[1] for p in cordlist]
    y = y+[y[0]] 

    if colorline == None:
        inp_color = None
    else:
        inp_color = colorline[lc%len(colorline)]
        
    if type(ls) == str:
        inp_style = ls
    else:
        inp_style = ls[lc%len(ls)]
    
    if scat_plot == "scat":
        hh = returnVar.plot(x,y,color=inp_color,linestyle=inp_style)
    else:
        hh = plt.plot(x,y,color=inp_color,linestyle=inp_style)
    if custom_lines != None: # Here we catch the line handles for the legends and return it. This is only required for plotting in the REMAP function.
        custom_lines = custom_lines + hh
        return (custom_lines)
    else: #In the other sections, we do not care about the legends. Here we want to calculate the polygons and therefore return the cordinates.
        return([(p[0],p[1]) for p in cordlist])


def draw_line(Amount_of_inp,scat_plot,returnVar,Mock,lc,colorline,linestyle,printcords,timeout,plot_is_open):
    class Track_openness:
        is_open = plot_is_open
    def on_close(event):

 

        event.canvas.stop_event_loop()
        Track_openness.is_open = False
    
        """
        This section needs some explaining. When the matplotlib plot is closed by pressing the X/cross in the top corner or by using a key of plt.rcParams["keymap.quit"], ginput stays active for two reasons:
            1) The matplotlib event loop is not terminated on a close_event.
            2) As this current draw_line() function is called in a while loop, closing the plot will never have the draw_line() function return None (returning None will break the while loop), therefore after closing the plot, this function and thus also ginput() will be called again, causing an unresponsive program. 
                Since plt.fignum_exists(plt.gcf().number), a function to check if the plot is still open, will return True even on a closed plot, the only way I could fix it is by defining on_close() as an inner function with Track_openness as an inner class. 
                Therefore when the plot is closed and the close_event is invoked in the matplotlib interactive backend, Track_opennes.is_open will be set to False. Returning this to the interactive_plot_selecting_cells will lead to breaking of the whileloop. 
            
        If this fix is not added to scSELpy, the program becomes unresponsive, which in most cases leads to forcefully ending the entire python session, with the risk of losing all data.
        To make sure Track_opennes is changed on closing the plot, we link on_close to the canvas using "mpl_connect". 
        When the plot is closed while running ginput, this on_close() function will be called.

        If the user closes the ginput normally, using key presses or mouse button clicks, the mpl_disconnect() function will be called before the plot is closed and therefore this function will never be called. Also the ginput() function will return None, which is returned by draw_line() aswell, resulting in a break of the while loop and everything concluding nominal.

        """
    ax = plt.gca()

    if Mock is not None: #If we passed a mock, we do not want to call ginput. Instead, we just assign the mock to xy.
        xy = Mock
        
    else:
        cid = returnVar.figure.canvas.mpl_connect('close_event', on_close) #In the event that someone closes the plot, we want to call on_close().

        try:
            


            xy = plt.ginput(n=Amount_of_inp,mouse_add=MouseButton.LEFT, mouse_pop=MouseButton.MIDDLE, mouse_stop=MouseButton.RIGHT,timeout=timeout) #matplotlib.ginput() is responsible for recording the user input. Each click is stored in a tuple as (x,y). All coordinates for a single polygon are stored in a list [(x1,y1),(x2,y2)].
 
        except Exception as except_error:
            returnVar.figure.canvas.mpl_disconnect(cid)
            logger_info("Drawing of polygon not concluded correctly. Exception: "+str(except_error),warning=True)
            return(None)
        if printcords:
            if len(xy) != 0:
                logger_info(xy)
        returnVar.figure.canvas.mpl_disconnect(cid)


    if len(xy) == 0:
        return(None,Track_openness.is_open)

        
    polygon = getXY(xy,scat_plot,returnVar,lc,colorline,linestyle,None)
    ax.figure.canvas.draw()


    
    return(polygon,Track_openness.is_open)
    
def tryPass(inp):
    try:

        inp

    except:

        pass
    
def floatCheck(inp,instance,warn=False):
    
    if type(inp[0]) == list or type(inp[0]) == np.ndarray:
        usevar = inp[0][0]
    else:
        usevar = inp[0]
        
    
    retvar = isinstance(usevar,np.floating) or isinstance(usevar,float)
    
    if retvar == False:
        try:
            if isinstance(usevar[0],np.floating) or isinstance(usevar[0],float):
                retvar = True
        except:
            pass
        
    if retvar == False and warn:
        logger_info("Your "+instance+" are not floats. While running a scatter plot, consider converting them float if the labels are numeric",warning=True)
    elif retvar == False:
        raise ValueError("scSELpy ERROR: The entered values for the "+instance+" parameter are not floats. Please convert them to floats to avoid serious errors. In case you want to run the program without conversion, please run skip_float_check = True")

def CheckParamType(VarDict,ParamDict):
    for x in VarDict:
        if x not in ParamDict:
            continue
        if "skip" not in ParamDict[x][1]:
            if type(VarDict[x]) not in ParamDict[x][1]:
                raise AttributeError("Parameter \""+str(x)+"\" can only be one of these types: " + str(ParamDict[x][1]).replace("<class ","").replace("'","").replace("[","").replace("]","").replace(">",""))

def InitiateParamDict():
    ParamDict={}
    ParamDict['map_attr'] = ["umap",[str],""]
    ParamDict['x_scat'] = [None,[type(None),str],"The x coordinate for scatter plot"]
    ParamDict['y_scat'] = [None,[type(None),str],"The y coordinate for scatter plot"]
    
    ParamDict['line_palette'] = [None,[type(None),list],"A list with colors for the lines of the drawn polygons."] 
    ParamDict['line_labels'] = [None,[type(None),str,list],"Labels for the polygon on the plot. The labels given will not rename the polygon. This has to be done after running scSELpy. See <code>Renaming scSELpy annotations</code>"] 
    ParamDict['linestyle'] = ["-",[type(None),str,list],"Specify the style of the polygon lines. Options are <code>-</code>, <code>.</code>,<code>--</code> and <code>-.</code>. If you want to select 3 polygons, you can pass [\".\",\"-\",\"--\"]"] 
    ParamDict['line_loc'] = ['upper left',[type(None),str],"Handles the legend location of the second legend, namely the one of the line labels for the polygons. See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html for more information"]
    ParamDict['line_bbox_to_anchor'] = [(1, 1),[type(None),tuple],"Same as the line_loc parameter."]
    ParamDict['line_handlelength'] = [None,[type(None),int,float],"Handles the line length of the lines in the second legend. Can be usefull when changing plt.rcParams['font.size']"]
    
    ParamDict['unselected_cells'] = ["Other",[str],"All cells that are not located within a polygon will be denominated as \"Other\" by default. Changing this parameter will denominate all unselected cells to the name given here. If an integer in string format will be given here, scSELpy might not work properly."]
    ParamDict['load'] = [None,[type(None),str],"Load an <code>Anndata obvservation</code>, on which annotations will be added. For example, load=\"REMAP_1\" (default scSELpy output) or load=\"leiden_r0.5\". For concrete examples please check the toturial."]
    ParamDict['replot_lines'] = [None,[type(None),str],"Using this parameter can replot polygons drawn from previous scSELpy invocations. Takes an <code>Unstructured Anndata annotation</code> stored by an earlier invocation of scSELpy. When this parameter is used, the user can not draw new lines, with the exception for when used together with the load parameter. In the latter case, all previously and newly drawn polygons will be annotated on the loaded <code>Anndata obvservation</code>."]
    ParamDict['overwrite'] = [False,[bool],"While <code>overwrite = False</code>, multiple polygons that overlap the same cell, will have the name annotated to that cell. For example \"1,2,3\" when Polygon 1, 2 and 3 overlap this cell. In the case that <code>overwrite = True</code>, only the last Polygon will be annotated. Therefore the output will be \"3\", even when Polygon 1, 2 and 3 overlap it."]
    ParamDict['printcords'] = [False,[bool],"Print out the coordinates of the selected lines. These can be used for the <code>mock</code> parameter."]    
    ParamDict["use_log_scale"] = [False,[bool],"If you wish to use the log scale in plots. Could be used e.g. for selecting antibody data in scatter plots in combination with use_raw=True."]
                                  
    ParamDict['skip_float_check'] = [False,[bool],"When running scatter plots, scSELpy will automatically check if the input is float. If this is not the case, it will return an error. To disable this error, run <code>skip_float_check = True</code>"]
    ParamDict['mock'] = [None,[type(None),dict],"Automatically runs scSELpy with preset coordinates, the user will not be able to make a selection. This can be handy when rerunning pipelines. For usage instructions please check the <code>Mock</code> section in the documentation."]# Load tests
    
    ParamDict['save'] = [None,[type(None),str],"Saves figure in provided path+filename. If only a filename is provided, will save in \"figures/\"+filename. Does not work the same as in scanpy. <code>scanpy.set_figure_params</code> should still work."]
    #ParamDict['interactive_backend'] = ["Qt5agg" if "win" in sys.platform else "TkAgg",[str],"For the drawing of polygons, an interactive backend will be used. If a default back-end does not work propperly on your computer, you can change it. More information at https://matplotlib.org/stable/users/explain/backends.html"] 
    ParamDict['interactive_backend'] = [None if is_notebook() == False else "Qt5Agg" ,[str,type(None)],"Default: None if not running on Jupyter Notebook (In this case, backend will only switch if you specify this parameter). If running on Jupyter: Qt5Agg. If running scSELpy on Jupyter Notebook, the drawing of polygons requires the use of an interactive backend. If the default back-end does not work propperly on your computer, you can change it. More information at https://matplotlib.org/stable/users/explain/backends.html"]
    ParamDict['timeout'] = [60,[float,int],"Amount of seconds until the drawing of the polygons will automatically stop."]
    ParamDict['helpbox'] = [False,[bool],"Before drawing, shows some text that gives instructions for drawing polygons"]
    
    ParamDict['components'] = [None,[type(None),str],""]
    ParamDict['layer'] = [None,["skip"],""]
    ParamDict['layers'] = [None,["skip"],""]
    return(ParamDict)
                                     
def setup(adata,**kwargs):
    """
    In this section we create VarDict, that keeps track of all scSELpy parameters and the parameters of scanpy that we have to modify.
    """

    tryPass(plt.close())#Close old plots.
    

    ParamDict=InitiateParamDict() # In here, we will store all variables we will use. If any of them are in the kwargs, we will copy them and remove them from the **kwargs.
    kwargs_copy = kwargs.copy() # Create a copy, so we can safely delete. The copy will be sent to the sc.pl.*() function.

    if 'return_fig' in kwargs:
        ParamDict['return_fig_backup'] = [kwargs['return_fig'],[bool],""]
    else:
        ParamDict['return_fig_backup'] = [False,[bool],""]
    #ParamDict['parameter_name'] = ['parameter_input',['list','with','all','acceptable','types'],"info"]

    
    VarDict = {x:ParamDict[x][0] for x in ParamDict}


    for x in kwargs: #Check all args, if it is in the VarDict, remove them from the copy. We will pass the copy to sc.pl.*
        if x in VarDict:
            VarDict[x] = kwargs[x]
            if x.lower() not in ["components","layer","layers"]:
                del kwargs_copy[x]
    
     




       
    if VarDict['replot_lines'] == True:
        if VarDict['load'] != None:
            if VarDict['load'] in adata.uns:
            
                VarDict['replot_lines'] = VarDict['load']
            else:
                VarDict['replot_lines'] = None 
            
        else:
            raise AttributeError("The replot_lines parameter can only be true if the load parameter is not None")

    
    if "show" in kwargs: # We need show to be false.
        VarDict['show_backup'] = kwargs_copy['show'] 
        kwargs_copy["show"] = False
    else:
        kwargs_copy["show"] = False
        VarDict['show_backup'] = None
    
    if "basis" in kwargs:
        VarDict['basis'] = kwargs_copy['basis']
        del kwargs_copy['basis']
    else:
        VarDict['basis'] = "X_"+VarDict['map_attr'].lower()
        
    if VarDict['layers'] != None or VarDict['layer'] != None:
        raise AttributeError("Layers are not supported by scSELpy. Please assign the layer to a variable and run scSELpy again.")
        
        

    if VarDict['x_scat'] != None and VarDict['y_scat'] != None:
           
            if 'use_raw' in kwargs_copy:
                
                
                if kwargs_copy["use_raw"] == True:
                
                    if hasattr(adata, "raw"):
                        if type(adata.raw) == type(None):
                            raise AttributeError("use_raw is passed, but anndata.raw has NoneType.")
                        
                    else:
                        raise AttributeError("use_raw is passed, but anndata has no .raw.")


                DoUseRaw = kwargs_copy['use_raw']
            else: #Scat has use_raw = None, but defaults to True if .raw is present. Automatically assiging None gives a problem in the _get_color_source_vector function, as it uses an "if True" statement. Which is a problem if passing None, as it will have the same result asif use_raw would be false. 
                
                if hasattr(adata, "raw"):
                    if type(adata.raw) == type(None):
                        DoUseRaw = None
                    else:
                        DoUseRaw = True
                else:
                    DoUseRaw = None
            from scanpy.plotting._tools import scatterplots as scsp
            VarDict['xscat_matrix'] = scsp._get_color_source_vector(adata,VarDict['x_scat'],use_raw=DoUseRaw)
            VarDict['yscat_matrix'] = scsp._get_color_source_vector(adata,VarDict['y_scat'],use_raw=DoUseRaw)

    CheckParamType(VarDict,ParamDict)
    
    return(kwargs_copy,VarDict)

def CheckRaw(adata,VarDict,**kwargs):
    Raw = False
    if "use_raw" in kwargs:
        Raw = kwargs["use_raw"]
    else: #By default, scatter uses raw.
        if VarDict['map_attr'].lower() == "scatter" or VarDict['map_attr'].lower() == "scat":
            Raw = True
        else:
            Raw = False
    if Raw:
        return(adata.raw)
    else: #False or None
        return(adata)

def checks(adata,VarDict,**kwargs):
    if False:
        if VarDict['load'] != None:
            if list(set(adata.obs[VarDict['load']])) == ['Other']: # For some reason, the loaded list is completely empty. We will just set the parameters asif its a new entry and then overwrite the adata.obs entry using the VarDict['number'].
                
                VarDict['store_load_parameter'] = VarDict['load']
                VarDict['load'] = None
                VarDict['replot_lines'] = None
                #We cant delete adata.obs[VarDict['load']] now, because then its gives an error when using the color parameter for the same obj.
                
            
    if VarDict['mock'] is not None and type(VarDict['mock']) != dict:

        raise AttributeError("Mock parameter is for testing purposes only.")
        
    if VarDict['components'] != None:
        if str(VarDict['components']).lower() == "all" or type(VarDict['components']) == list or str(VarDict['components']).count(",") > 1:
            raise AttributeError("Passing components in scSELpy can only be done as a single string, e.g. \"3,4\", with only 2 dimensions at most.")

    if VarDict['load'] != None:
        if VarDict['load'] not in adata.obs:
            raise AttributeError("The load parameter \""+str(VarDict['load'])+"\" has to be present in anndata.obs")
    if VarDict['skip_float_check'] == False: # Here we check if all values we are going to need are floats. 
    
    #if "color" in kwargs:
        if False: #This sections checks if the obs passed in the color parameter are float, but it might not be that important. For now disabled.
            if "scat" in VarDict['map_attr'].lower():

                    floatCheck(adata.obs[kwargs['color']],".obs[\'"+kwargs['color']+"\']",warn=True)

            
                
        if "scat" not in VarDict['map_attr'].lower():

                floatCheck(adata.obsm[VarDict['basis']],".obsm[\'"+VarDict['basis']+"\']") 

        else:
            

            floatCheck(VarDict['xscat_matrix'],VarDict['x_scat'])
            floatCheck(VarDict['yscat_matrix'],VarDict['y_scat'])

    return(VarDict)  
    


# Below, we decide which attribute we will plot, e.g. umap, tsne etc. Based on the "map_attr" arg.
def set_map_attr(adata,VarDict,**kwargs):

    avail_atr = "\"umap\",\"tsne\",\"pca\", \"scatter\" or \"embedding\""
    scat_plot = False
    
    if VarDict['map_attr'].lower() == "scatter" or VarDict['map_attr'].lower() == "scat": 
        if VarDict['x_scat'] is None or VarDict['y_scat'] is None:
            raise AttributeError('When choosing the scatter plot, please make sure the y_scat and x_scat args are defined.')
        scat_plot = "scat"
        plotattr = sc.pl.scatter
    else:
        if "basis" not in VarDict:
            raise AttributeError("The basis parameter is not found")
        elif VarDict['basis'] not in adata.obsm:
            raise AttributeError(str(VarDict['basis'])+" not found in anndata.obsm")


        if VarDict['map_attr'].lower() == "umap": 
            plotattr = sc.pl.umap
            
        elif VarDict['map_attr'].lower() == "tsne": 
            plotattr = sc.pl.tsne
            
        elif VarDict['map_attr'].lower() == "pca": 
            plotattr = sc.pl.pca

        elif VarDict['map_attr'].lower() == "embedding":
            scat_plot = "embedding"
            plotattr = sc.pl.embedding

        else: #If the input of map_attr differs from what we have listed above, raise an error.
            raise ValueError('The attribute '+VarDict['basis']+' entered is not whitelisted. The following attributes are available: '+avail_atr+'. e.g. Remap(adata,map_attr="umap"). If you meant to override this whitelist, please check if you specified Remap(adata,override=True).')



    return(scat_plot,plotattr)





def Get_Max_val_from_list_with_commas(list_with_comma_containing_strings): #It is possible that the last selected region (thus the highest number), is within another region and therefore is only present within commas. This function should check for that.
    NumberList = []
    for entry1 in list_with_comma_containing_strings:

        if "," in entry1:
            for entry2 in entry1.split(","):

                if str(entry2).isdigit():

                    NumberList.append(int(entry2))#Sometimes we can have commas, so split them and get all numbers.
        else:
            if str(entry1).isdigit():
                NumberList.append(int(entry1))


    if len(NumberList) != 0: 
        HighestNumber = max(NumberList)
        return(HighestNumber)
    else:
        return(0) #It could be the case that a list is passed with only strings. In that case, nothing has been appended.


def prepare(adata,VarDict):
    if VarDict['load'] == None: 
        counts = 0
    else: # If 'load' has an object name stored for anndata.obs, get the highest number in that list, but filter out any string.
            


        counts = Get_Max_val_from_list_with_commas(adata.obs[VarDict['load']])

    if VarDict['mock'] is None and VarDict['interactive_backend'] != None:
        matplotlib.use(VarDict['interactive_backend'], force=True) # We have to switch to a different matplotlib backend in order to be able to interact with the plot on Jupyter Notebook.


    return(counts)
    
def AddTextBox(txt,y,ret):
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    return(ret.text(0.05, y, txt, transform=ret.transAxes, fontsize=14,
                  verticalalignment='top', bbox=props))
def interactive_plot_selecting_cells(adata,VarDict,scat_plot,plotattr,counts,MainmlpBackend,unsError,**kwargs_copy):
    if VarDict['replot_lines'] != None:
        try:

            ShapeDict = adata.uns[VarDict['replot_lines']].copy()

        except:
            
            raise AttributeError(unsError)
    else:

        ShapeDict = {} # This dict will store the cordinates of each shape. We will use it to replot it after switching matplotlib backend and to determine which obsm coordinates are located within the shape.
    try:

        if scat_plot == "scat":
            returned = plotattr(adata,VarDict['x_scat'],VarDict['y_scat'], **kwargs_copy) 
        elif scat_plot == "embedding":
            returned = plotattr(adata,basis=VarDict['basis'], **kwargs_copy) #The "show" parameter will always be false, even if user puts it on True.

        else:
            returned = plotattr(adata, **kwargs_copy) # Here we plot. plotattr is e.g. sc.pl.umap. As we switched the back-end, this plot will be interactive.
            
        
    except: #In the case that we cannot make the interactive plot, we need to switch back to the original backend in the case that we use Jupyter Notebook and switched to an interactive backend.
        plt.close()
        if VarDict['interactive_backend'] != None:
            matplotlib.use(MainmlpBackend, force=True)

        
      

        raise AttributeError("Unexpected error:", sys.exc_info()[1])
        
        
    try:
        if type(returned) == list:
            returned = returned[-1]   
        if type(returned) == dict: #In cases of heatmap. Other cases were dict is returned are not supported.
            returned = returned['heatmap_ax']
        

        
        if VarDict["use_log_scale"] == True:
            log_scale(VarDict,returned)
        
        if VarDict['helpbox']:
            StoreTxtObjs = {}
            returned.plot()
            textlist = ["Left click to select","Right click when done","Right click twice to exit","Don't close the window any other way","helpbox=False to disable this help message (=default)","Press any key to continue"]
            curY = 1.05
            for enum,txt in enumerate(textlist):
                curY = curY-0.15
                StoreTxtObjs[enum] = AddTextBox(txt,curY,returned)


            plt.waitforbuttonpress(0)
            for removekey in StoreTxtObjs:
                StoreTxtObjs[removekey].set_visible(False)
            ax = plt.gca()
            ax.figure.canvas.draw()
            
        
       
        lc = len(ShapeDict)-1        
        mock_int = -1
        if VarDict['replot_lines'] != None and VarDict['load'] != None:
            for iteration,ShapeKey in enumerate(adata.uns[VarDict['replot_lines']]):
                getXY(adata.uns[VarDict['replot_lines']][ShapeKey],scat_plot,returned,iteration,VarDict['line_palette'],VarDict['linestyle'],None)

        plot_is_open = True 
        while True:
            
            
            lc = lc + 1
           
            mock_int = mock_int + 1
            if VarDict['mock'] != None:
                if len(VarDict['mock'][VarDict['map_attr']]) == mock_int:
                    break
                mock_inp = VarDict['mock'][VarDict['map_attr']][mock_int]
            else:
                mock_inp = None
            counts = counts + 1
            outp,plot_is_open = draw_line(100000,scat_plot,returned,mock_inp,lc,VarDict['line_palette'],VarDict['linestyle'],VarDict['printcords'],VarDict["timeout"],plot_is_open) 

            if plot_is_open == False:
                break
            if outp != None:
                ShapeDict[str(counts)] = outp
            else:
                break


        plt.close()
    except: #In the case that we cannot make the interactive plot, we need to switch back to the original backend in the case that we use Jupyter Notebook and switched to an interactive backend.
        plt.close()
        if VarDict['interactive_backend'] != None:
            matplotlib.use(MainmlpBackend, force=True)



        
    
        raise AttributeError("Unexpected error:", sys.exc_info()[1])
        
    tryPass(plt.close()) # We do not want to continue with the plot we drawn. We will draw a new one later.
    if VarDict['interactive_backend'] != None:
        matplotlib.use(MainmlpBackend, force=True)

        
    return(ShapeDict)  
                

def Save(VarDict,scat_plot,returnVar):
    if VarDict['save'] == False:
        pass
    else:
               
        
        
        if VarDict['save'] == True: #If True, no name has been given

            savename = VarDict['map_attr']+".pdf" # e.g. umap.pdf
        else:
            savename = VarDict['save'] # Name has been given
        
        #In scanpy, they save everything in ./figures/
        #We do the same, but before, we check if the given string contains a valid path.
        snlen = len(savename.split("/")[-1]) #split on / and check for the length of the last string. Remove this from the savename string, to get entire path.
        if snlen == 0:
            raise AttributeError("Did you specify a name for the save parameter, or just a path that ends with a slash? Please specify a filename")
        if os.path.isdir(savename[:-snlen]): #If the dir exists, save here.
            pass
        else:

            try: # TryPass() function doesnt work here.
                os.mkdir(os.getcwd()+"/figures")
            except:
                pass
                

            savename = os.getcwd()+"/figures/"+savename
        
        if scat_plot == "scat":
            returnVar.figure.savefig(savename,bbox_inches='tight')
        else:
            plt.savefig(savename,bbox_inches='tight')


def input_for_poly(adata,VarDict):
    if VarDict['components'] == None:

        poly_inp = adata.obsm[VarDict['basis']][:,[0,1]]
    else:

        comps = VarDict['components'].split(",")
        poly_inp = adata.obsm[VarDict['basis']][:,[int(comps[0])-1,int(comps[1])-1]]# Passing the dimensions. 

    return(poly_inp)

def Store_obj(VarDict,adata,ShapeDict):
    if VarDict['load'] != None: 
        applist = list(adata.obs[VarDict['load']])
        SkipThese = set([item for sublist in [ID.split(",") for ID in set(adata.obs[VarDict['load']])] for item in sublist]) # [ID.split(",") for ID in set(adata.obs[VarDict['load'])] creates from ["1,2,3","3,4","5"] the following list: [[1,2,3],[3,4],[5]]. The rest of the list comprehension Makes it into [1,2,3,3,4,5]. The set of this removes the doubles.
        #SkipThese exists of all IDs in the load parameter object. We can skip them in the for loop.
                                      
    else:
        
        applist = [VarDict['unselected_cells']] * len(adata.obs) # This list we will add to adata.obs['REMAP_x'] afterwards. At the start, we fill all entries with "Other" ("Other" is the default of VarDict['unselected_cells']) and repalce it later.
        SkipThese = []
    for counts in ShapeDict.copy():
        if counts in SkipThese:
            continue
        polygon = mpltPath.Path(ShapeDict[counts]) # Create the polygon of the returned coordinates.
        if VarDict['map_attr'].lower() == "scat" or VarDict['map_attr'].lower() == "scatter": #If scatterplot
            
            inside = polygon.contains_points(np.column_stack((VarDict['xscat_matrix'],VarDict['yscat_matrix']))) # Returns a boolean list, if each points is inside the shape/polygon.       

            
        else:

            poly_inp = input_for_poly(adata,VarDict)
            inside = polygon.contains_points(poly_inp)
        

        if VarDict['overwrite']:
            applist = [ str(counts) if i else j for i,j in zip(inside,applist) ] #Overwrites the existing IDs in the polygon. e.g. if a third line is drawn over a cell with ID "1,2", the updated ID without overwrite becomes "1,2,3", but mere "3" with overwrite on. 
        else:
            applist = [ str(counts) if i and j == VarDict['unselected_cells'] else j+","+str(counts) if i else j for i,j in zip(inside,applist) ] # If i for inside == True, add the current variable. If the previous variable is "Other" and therefore no number, VarDict['unselected_cells'] ("Other" by default) will be replaced by the number. If a number already exist, the new number will be updated. 
        

    if VarDict['load'] != None and VarDict['replot_lines'] == None: 
        
        
        
        replot_lines = VarDict['load'] #ShapeDict is already stored. replot_lines and load are paired by default.

        if replot_lines in adata.uns: #If true, the uns was generated by scSELpy and the old existing uns should be pooled with the new ShapeDict, in order to concatenate the old and new lines.

            adata.uns[replot_lines] = dict(adata.uns[replot_lines], **ShapeDict) # add the old uns dict with the new Shapedict together into the new uns.
            
        else: #The load object was generated by other algorithm.
            #Check if value in obj is number and if its number, get the highest. 

            HighestNumber = Get_Max_val_from_list_with_commas(adata.obs[VarDict['load']])
            replot_lines = VarDict['load']
            ReNumberedDict = {str(int(key)+HighestNumber):ShapeDict[key] for key in ShapeDict}
            adata.uns[replot_lines] = ReNumberedDict
            logger_info(str(replot_lines)+' was added to anndata.uns.')

            
        adata.obs[VarDict['load']] = applist

    elif VarDict['load'] != None and VarDict['replot_lines'] != None:
        adata.obs[VarDict['load']] = applist
        adata.uns[VarDict['replot_lines']] = ShapeDict
    elif 'store_load_parameter' in VarDict: # This is in case the checks() function found that the 'load' parameter was empty and asigned VarDict['load'] to Nonetype.
        adata.obs[str(VarDict['store_load_parameter'])] = applist    
        adata.uns[str(VarDict['store_load_parameter'])] = ShapeDict
    else:
        REMAP_count_var = 0
        while True: # In this loop, we add "REMAP_1", but if REMAP_1 is already in adata, we add _2, _3 etc.
            REMAP_count_var = REMAP_count_var + 1
            if "REMAP_"+str(REMAP_count_var) in adata.obs: # If REMAP_1 already in adata.obs, continue to REMAP_2 etc.
                continue
            else: # We finally found one that is not in adata.obs. Lets add this one.
                logger_info('REMAP_'+str(REMAP_count_var)+' was added to anndata.obs.')

                logger_info('REMAP_'+str(REMAP_count_var)+' was added to anndata.uns.')
                adata.obs['REMAP_'+str(REMAP_count_var)] = applist    
                adata.uns['REMAP_'+str(REMAP_count_var)] = ShapeDict #We will also store the shapedict in anndata.uns, so it can be replot_lines later with scanpy.

                break
    
    
    
    
    #To be able to use sc.pl.*, we need to remove the 'REMAP_*_colors' uns entry.
    if str(VarDict['load'])+"_colors" in adata.uns:
        del adata.uns[VarDict['load']+"_colors"]   


def ReturnToNormalBackend(mlpb,VarDict):
    if VarDict['interactive_backend'] != None:
        matplotlib.use(mlpb, force=True)



    try:
        plt.close()
    except:
        pass
    
def Remap(adata,override=False,remove_show_override=True,**kwargs): # Here is where it all starts. 
       
    #plt.rcParams["keymap.quit"] = [""]
    MainmlpBackend = matplotlib.get_backend() # Get the current backend. This should happen before the prepare() function is executed. 
    
    
    
    
    kwargs_copy,VarDict = setup(adata,**kwargs) # Create VarDict to keep track of scSELpy native args.
    if remove_show_override == True:
        del kwargs_copy["show"]
    

    VarDict = checks(adata,VarDict,**kwargs) # Perform some checks
    if override == False:
        scat_plot,plotattr = set_map_attr(adata,VarDict,**kwargs) #umap, tsne, pca or scatter.
    else:  #Not supported, but if a user would want to run anything outside of umap, tsne, pca or scatter, I give them the option to by running: 
        scat_plot = kwargs['scat_plot']
        plotattr = kwargs['plotattr']
        del kwargs_copy['plotattr']
        del kwargs_copy['scat_plot']
        
    unsError = "The replot_lines parameter should only be invoked with the name of an anndata.uns. e.g. in case of adata.uns[\"REMAP_1\"], run scSELpy.pl.umap(adata,replot_lines=\"REMAP_1\",kwargs**). Current input: "+str(VarDict['replot_lines']) 

        
    #PRE-plotting before backend switch. To make sure all parameters are working.
    if scat_plot == "scat":
        returned = plotattr(adata,VarDict['x_scat'],VarDict['y_scat'], **kwargs_copy) 
    elif scat_plot == "embedding":
        returned = plotattr(adata,basis=VarDict['basis'], **kwargs_copy) #The "show" parameter will always be false, even if user puts it on True.

    else:
        returned = plotattr(adata, **kwargs_copy) # Here we plot. plotattr is e.g. sc.pl.umap. As we switched the back-end, this plot will be interactive.


        
    if VarDict['replot_lines'] != None and VarDict['load'] == None: #In this case, we can skip the interactive part. Just replotting the already drawn.
        try:
            ShapeDict = adata.uns[VarDict['replot_lines']].copy()
        except:
            
            raise AttributeError(unsError)

    else:
        atexit.register(ReturnToNormalBackend,mlpb=MainmlpBackend,VarDict=VarDict) #In case the user closes the plot window during the other backend, this function would revert to the normal backend on exit
        counts = prepare(adata,VarDict) # Switch matplotlib backend to interactive plot.
        #Now it is time to run the interactive plot and select the cells.
        ShapeDict = interactive_plot_selecting_cells(adata,VarDict,scat_plot,plotattr,counts,MainmlpBackend,unsError,**kwargs_copy)
        atexit.unregister(ReturnToNormalBackend)
    if scat_plot == "scat":
        returnVar = plotattr(adata,VarDict['x_scat'],VarDict['y_scat'], **kwargs_copy) #The "show" parameter will always be false, even if user puts it on True.
    elif scat_plot == "embedding":
        returnVar = plotattr(adata,basis=VarDict['basis'], **kwargs_copy) #The "show" parameter will always be false, even if user puts it on True.

    else:
        returnVar = plotattr(adata, **kwargs_copy) 
    

    
    if VarDict["use_log_scale"] == True:
        log_scale(VarDict,returnVar)
    
    
    #-------reploting the lines on the plot, so the plot can be printed and saved----------
    custom_lines = []

  
    for itere,counts in enumerate(ShapeDict):
        
        custom_lines = getXY(ShapeDict[counts],scat_plot,returnVar,itere,VarDict['line_palette'],VarDict['linestyle'],custom_lines)
    
    if VarDict['line_labels'] != None:

        if len(ShapeDict) < len(VarDict['line_labels']):
            line_labels = VarDict['line_labels'][:len(ShapeDict)]
        else:
            line_labels = VarDict['line_labels']

        #handles.append(custom_lines)
        #labels.append(line_labels)
        
        if type(returnVar) == list: #Multiple variables have been passed to the scanpy color argument.
            ax2 = returnVar[-1].twinx()
            #scSELpy is not made to support multiple plots in one go, so we just add the legend to the last plot.
        else:    
            ax2 = returnVar.twinx() # We create a copy of the axes to add another legend. Using add_artist for adding legend is buggy.
        ax2.legend(custom_lines,line_labels,loc=VarDict['line_loc'],bbox_to_anchor=VarDict['line_bbox_to_anchor'],handlelength=VarDict['line_handlelength']) # Plotting the line legend. In getXY(), the labels are added.
        ax2.axis('off')
    

        
    #--------- SAVING -----------------
    if VarDict['save'] != None: # We did not want the plots being saved while drawing. Now we can save it manually with the plt.savefig()
        Save(VarDict,scat_plot,returnVar) #Should automatically take the settings from scanpy.set_figure_params, as that function updated matplotlib.rcParams.
            
 
    #-----------Storing object with selected cells----------    
    # e.g. anndata.obs['Remap_1']    
    if VarDict['replot_lines'] != None: 
        if VarDict['load'] == None:# No need to store "REMAP_" when we did not draw anything.
            pass
        else:
            Store_obj(VarDict,adata,ShapeDict)
    else:
        Store_obj(VarDict,adata,ShapeDict)

    if is_notebook(): #Running this on Ipython will crash Ipython. Not running this on Jupyter Notebook will only output the last plot.
        plt.pause(0.0001) #If we do not execute this micropause on Jupyter notebook, it will only show the last plot only, in the case that multiple instances of scSELpy are ran in the same jupyter notebook cell.

    if VarDict['return_fig_backup'] == False and VarDict['show_backup'] != False:

        pass
    else:

        return(returnVar)
