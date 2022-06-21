import os
import glob
import json

class Tmp_script:
    def __init__(self, dir_path= os.path.join(os.path.dirname(os.path.realpath(__file__)),'tmp')):
        self.__dir_path = dir_path
        self.__checkpoints = glob.glob(os.path.join(dir_path,"*.json"))

    def create_checkpoint(self, attributes):
        with open(os.path.join(self.__dir_path,f"checkpoint{(len(self.__checkpoints)+1)}.json"), 'w') as f:
            f.write(json.dumps(attributes, indent = 4))
        print("checkpoint created successfully")
    
    def load_checkpoint(self, index):
        with open(self.__checkpoints[index], 'r') as f:  
            return json.load(f)
    
    def save_checkpoint(self):
        try:
            with open(self.__checkpoints[index], 'w') as f:
                f.write(json.dumps(attributes, indent = 4))
            return "Saved"
        except Exception as e:
            return e
    
    def getCheckpoints(self):
        return self.__checkpoints
    
    def getDirpath(self):
        return self.__dir_path