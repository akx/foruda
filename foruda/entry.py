# -- encoding: UTF-8 --
import os
import pathlib
from typing import List

import attr


@attr.s(auto_attribs=True)
class Entry:
    dent: os.DirEntry
    root: str
    parent: "Entry"
    children: List["Entry"]

    @property
    def path(self) -> pathlib.PurePath:
        return pathlib.PurePath(self.dent.path)

    @property
    def relpath(self) -> pathlib.PurePath:
        return self.path.relative_to(self.root)

    @property
    def name(self) -> str:
        return self.dent.name

    @property
    def ext(self) -> str:
        return self.name.rpartition(".")[-1].lower()

    @property
    def isdir(self) -> bool:
        return self.dent.is_dir()

    def __str__(self):
        return f'<{self.relpath}>'
