"""
def Rename_func(inp,Replace_Dict):
    
    output_list = []
    for entry in inp:
        if "," in entry:
            working_entry = entry.split(",")
        else:
            working_entry = [entry]
        NewString = ""
        redudantlist = []
        for element in working_entry:
            try:
                replaced_element = Replace_Dict[element]
            except:
                raise AttributeError(element+ " is not present in the specified dict.")
            if replaced_element not in redudantlist:
                redudantlist.append(replaced_element)
                NewString = NewString + str(replaced_element) + ","
                
        if len(NewString) != 0:
            NewString = NewString[:-1]
        output_list.append(NewString)
    return(output_list)



"""

def Rename_func(inp,Replace_Dict):
    
    output_list = []

    
    for entry in inp:
        if "," in entry:
            working_entry = entry.split(",")
        else:
            working_entry = [entry]
        NewStringList = []
        redudantlist = []

        for element in working_entry:
            try:
                replaced_element = Replace_Dict[element]
            except:
                replaced_element = element
            if replaced_element not in redudantlist:
                redudantlist.append(replaced_element)#So if Gene A is in there twice, the second time this wont execute.
                NewStringList.append(str(replaced_element))
   
         
        NewString = ",".join(sorted(NewStringList))
        #If we do not do this sort above, then if you have {'1':"A",'2':"B",'3':"A"}, "1,2" will be converted to "A,B" and "2,3" will be converted to "B,A".
      

        output_list.append(NewString)
    return(output_list)