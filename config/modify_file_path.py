from pathlib import PureWindowsPath,PurePosixPath


class ModifyFilePath:
    def __init__(self,filepath:str) -> None:
        self.filepath = filepath

    # action -> function that converts the file's path from windows to WLS
    def convert_filepath(self):
        try:
            if PureWindowsPath(self.filepath).is_absolute() == False:
                return self.filepath
            else:
                wpath = PureWindowsPath(self.filepath).parts #  receives the windows file path and convert its elements in a tuple
                lpath = PurePosixPath("/mnt/c",*wpath[1:]) # adds the prefix "/mnt/c" and take elements of the tuple from position 1 to end [1:]
                return lpath
        except SyntaxError:
            print("Syntax Error, windows file path format, adding 'r'")

