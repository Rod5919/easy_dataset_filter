import os

class Os_script:
    def __init__(self, input_folder='data/images', output_folder='public/images'):
        self.__current_folder = dir_path = os.path.dirname(os.path.realpath(__file__))
        self.__input_folder = os.path.join(self.__current_folder, input_folder)
        self.__output_folder = os.path.join(self.__current_folder, output_folder)
        print("Os_script imported")

    def move_file(self, path, destination):
        #TODO: move_file
        pass

    def move_xml_file(self, path, destination):
        #TODO: move_xml_file
        pass

    def setInputfolder(self, path):
        #TODO: setInputfolder
        pass

    def setOutputfolder(self, path):
        #TODO: setOutputfolder
        pass

    def setCurrentfolder(self, path):
        #TODO: setCurrentfolder
        pass
    
    def getInputfolder(self):
        return self.__input_folder
    
    def getCurrentfolder(self):
        return self.__current_folder

    def getOutputfolder(self):
        return self.__output_folder