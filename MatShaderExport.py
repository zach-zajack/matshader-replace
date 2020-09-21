from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from System.IO import Path

def export_node(node, folder_path):
    node.Export(Path.Combine(folder_path, node.Name))

if BrawlAPI.RootNode != None:
    children = BrawlAPI.RootNode.GetChildrenRecursive()
    models = filter(lambda c: isinstance(c, MDL0Node), children)
    folder_path = BrawlAPI.OpenFolderDialog("Open materials/shaders folder")
    for model in models:
        for shader in model.ShaderList: export_node(shader, folder_path)
        for mat in model.MaterialList: export_node(mat, folder_path)