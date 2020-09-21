from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from System.IO import Directory

not_found = []

def replace_node(node, folder_path):
    new_node_path = Directory.GetFiles(folder_path, node.Name + ".*")
    if new_node_path:
        node.Replace(new_node_path[0])
    else:
        not_found.append(node.Name)

if BrawlAPI.RootNode != None:
    children = BrawlAPI.RootNode.GetChildrenRecursive()
    models = filter(lambda c: isinstance(c, MDL0Node), children)
    folder_path = BrawlAPI.OpenFolderDialog("Open materials/shaders folder")
    for model in models:
        for shader in model.ShaderList: replace_node(shader, folder_path)
        for mat in model.MaterialList: replace_node(mat, folder_path)
        model.Rebuild(True) # force rebuild because brawlcrate is shit
    if not_found:
        BrawlAPI.ShowMessage("File not found for: " + ", ".join(not_found), "")