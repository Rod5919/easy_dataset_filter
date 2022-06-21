import os
import shutil

class Os_script:
    def __init__(self, input_folder, output_folder, current_folder):
        self.__current_folder = current_folder
        self.__input_folder = os.path.join(self.__current_folder, input_folder)
        self.__output_folder = os.path.join(self.__current_folder, output_folder)

    def move_file(self, path, destination):
        shutil.copyfile(path, destination)

    def move_xml_file(self, path, destination):
        try:
            shutil.copyfile(path.split('.')[0]+"xml", destination)
            print(f"{path} moved to {destination}")
        except FileNotFoundError:
            print(f"{path} has no xml file")

    def has_xml_file(self, path):
        return os.path.exists(path.split('.')[0]+"xml")

    def setInputfolder(self, path):
        self.__input_folder = path

    def setOutputfolder(self, path):
        self.__output_folder = path
    
    def getInputfolder(self):
        return self.__input_folder
    
    def getCurrentfolder(self):
        return self.__current_folder

    def getOutputfolder(self):
        return self.__output_folder