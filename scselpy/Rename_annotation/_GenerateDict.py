def gen_dict(inp):
    AllEntriesList = []
    for entry in inp:
        if "," in entry:
            for sub_entry in entry.split(","):
                AllEntriesList.append(sub_entry)
        else:
            AllEntriesList.append(entry)
    
    
    
    return({Name:Name for Name in list(set(AllEntriesList))})
    
    
    
    