#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:57:04 2022

@author: bioinformatics
"""

#import sys
import os
#sys.path.append('../scselpy/plotting')#If run directly from docs. However, we run it from setup.py.

#from _scselpy import InitiateParamDict as IPD


from scselpy.plotting._scselpy import InitiateParamDict as IPD # When running from setup.py

        
def ReturnTypes(inp):
    outp = []
    for xinp in inp:
        if xinp == type(None):
            outp.append("None")
        else:
            outp.append(str(xinp)[8:-2])
        
    return(outp)

def check_if_string(inp):
    

    if type(inp) == str:
        inp = "\'"+inp+"\'" 
    
    
    
    
    return("default:  <code>"+str(inp)+"</code>")


def Create_parameters_html():
    pwd = os.path.dirname(os.path.abspath(__file__))
    
    Params_initiate = IPD()
    Params = {}
    
    for param in Params_initiate:
    
        if 'scat' in param or "layer" in param or "map_attr" in param or "components" in param:
            continue
        else:
            Params[param] = Params_initiate[param]
    
    background_color_html = "<div style=\"background-color:rgba(0, 0, 0, 0.0470588); text-align:left; vertical-align: middle; padding:8px 0;\">"
    
    
    write_Parameters = "  ".join([background_color_html+"<b>&nbsp;"+str(x)+": <code>"+", ".join(ReturnTypes(Params[x][1]))+"</code></b> ("+check_if_string(Params[x][0])+")</div>  &nbsp;&nbsp;&nbsp; "+str(Params[x][2])+" <br><br>" for x in Params])
    if not os.path.exists(pwd+"/source/generated_markdown"):
        os.makedirs(pwd+"/source/generated_markdown")
    with open(pwd+"/source/generated_markdown/Parameters.md","w+") as f:
        f.write(write_Parameters)
        
    
    
    
    

