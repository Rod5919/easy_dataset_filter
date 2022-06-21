import glob

class Tmp_script:
    def __init__(self, dir_path):
        self.checkpoints = glob.glob(dir_path)
        print("Tmp_script imported")

    def create_checkpoint(self):
        #TODO: create_checkpoint
        pass
    
    def load_checkpoint(self):
        #TODO: load_checkpoint
        pass
    
    def save_checkpoint(self):
        #TODO: save_checkpoint
        pass