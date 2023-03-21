from ._RenameAnno import Rename_func
from ._GenerateDict import gen_dict

def rename(inp,Replace_Dict):
	return(Rename_func(inp,Replace_Dict))


def generate_replace_dict(inp):
    return(gen_dict(inp))