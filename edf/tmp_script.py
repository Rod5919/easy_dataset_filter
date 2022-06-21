import os
import glob

class Tmp_script:
    def __init__(self, dir_path= os.path.join(os.path.dirname(os.path.realpath(__file__)),'tmp')):
        self.dir_path = dir_path
        self.__checkpoints = glob.glob(os.path.join(dir_path,"*"))

    def create_checkpoint(self):
        #TODO: create_checkpoint
        pass
    
    def load_checkpoint(self):
        #TODO: load_checkpoint
        pass
    
    def save_checkpoint(self):
        #TODO: save_checkpoint
        pass
    
    def getCheckpoints(self):
        return self.__checkpoints