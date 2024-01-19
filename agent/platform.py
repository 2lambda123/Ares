import os
import shutil


def is_linux():
    return os.name == 'posix'

def is_windows():
    return os.name == 'nt'

def copy_file(source, destination):
    shutil.copy2(source, destination)

def copy_directory(source, destination):
    shutil.copytree(source, destination)

def move_file(source, destination):
    shutil.move(source, destination)
