# from gui.py import Gui
from .os_script import Os_script as osp
# from tmp_script import Tmp_script as tsp

class EDF:
    def __init__(self, input_folder='data/images/', output_folder='public/images'):
        self.osp = osp(input_folder=input_folder, output_folder=output_folder)
        print(self.osp.getInputfolder())
    
