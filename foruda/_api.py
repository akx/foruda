import os

from foruda.entry import Entry


def get_entries(root):
    def _get_entries(dir, parent, out_list):
        dent: os.DirEntry
        for dent in os.scandir(dir):
            ent = Entry(dent=dent, root=root, parent=parent, children=[])
            out_list.append(ent)
            if dent.is_dir():
                _get_entries(dent.path, parent=ent, out_list=ent.children)

    root_ents = []
    _get_entries(root, None, root_ents)
    return root_ents


def walk(root):
    if isinstance(root, Entry):
        yield root
    for ent in getattr(root, "children", root):
        yield from walk(ent)
