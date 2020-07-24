import shutil
from typing import List
from pathlib import Path


class Parser():
    def __init__(self):
        pass

    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplimentedError

    def read(self, path):
        with open(path, 'r') as file:
            return file.read()

    def write(self, path, dest, content, ext='.xml'):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(self, path, source , dest):
        shutil.copy2(path, dest / path.relativeto(source))


class ResourceParser(Parser):
    def __init__(self):
        super().__init__(self)

    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)
