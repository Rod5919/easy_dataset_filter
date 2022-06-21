from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import glob

from .os_script import Os_script as osp
from .tmp_script import Tmp_script as tsp

from PyQt5 import QtCore, QtGui, QtWidgets
class EDF:
    def __init__(self,
                 input_folder='data', 
                 output_folder='public',
                 current_folder=os.path.join(os.path.dirname(os.path.realpath(__file__)),'..'),
                 checkpoint_directory=None,
                 image_extension="jpg"):
        # Current directory for the checkpoint_directory
        checkpoint_directory = os.path.join(current_folder,'tmp') if checkpoint_directory is None else checkpoint_directory
        # PyQt5
        self.app = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.show()
        
        # Imports
        self.osp = osp(input_folder=input_folder, output_folder=output_folder, current_folder=current_folder)
        self.tsp = tsp(checkpoint_directory)
        print(checkpoint_directory)
        print(self.tsp.getCheckpoints())
        
        # Variables
        self.files = glob.glob(os.path.join(self.osp.getInputfolder(),f"*.{image_extension}"))
        self.moved = []
        self.discarted = 0
                
        # SetupUi
        self.setupUi()
        sys.exit(self.app.exec_())
    
    
    def setupUi(self):
        self.main_window.setObjectName("self.MainWindow")
        self.main_window.resize(640, 480)
        
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(30, 60, 30, 180))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.prevImage)

        self.imageButton = QtWidgets.QPushButton(self.centralwidget)
        self.imageButton.setGeometry(QtCore.QRect(60, 60, 250, 150))
        self.imageButton.setObjectName("imageButton")
        self.imageButton.setIcon(QtGui.QIcon('/home/rodri/Documents/easy_dataset_filter/Screenshot from 2022-05-18 17-26-54.png'))
        self.imageButton.setIconSize(QtCore.QSize(250, 180))

        self.xml_badge = QtWidgets.QLabel(self.centralwidget)
        self.xml_badge.setObjectName("xml_badge")
        self.xml_badge.setText("xml")
        self.xml_badge.setGeometry(QtCore.QRect(270, 70, 25, 17))

        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(310, 60, 30, 180))
        self.nextButton.setObjectName("nextButton")
        
        self.rejectButton = QtWidgets.QPushButton(self.centralwidget)
        self.rejectButton.setGeometry(QtCore.QRect(60, 210, 121, 31))
        self.rejectButton.setObjectName("rejectButton")
        
        self.acceptButton = QtWidgets.QPushButton(self.centralwidget)
        self.acceptButton.setGeometry(QtCore.QRect(180, 210, 131, 31))
        self.acceptButton.setObjectName("acceptButton")
        
        self.pwd_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pwd_lbl.setGeometry(QtCore.QRect(40, 310, 291, 17))
        self.pwd_lbl.setObjectName("pwd_lbl")
        
        self.card_1 = QtWidgets.QLabel(self.centralwidget)
        self.card_1.setGeometry(QtCore.QRect(380, 60, 201, 141))
        self.card_1.setObjectName("card_1")
        
        self.card_2 = QtWidgets.QLabel(self.centralwidget)
        self.card_2.setGeometry(QtCore.QRect(380, 210, 211, 151))
        self.card_2.setObjectName("card_2")
        
        self.in_lbl = QtWidgets.QLabel(self.centralwidget)
        self.in_lbl.setGeometry(QtCore.QRect(40, 350, 111, 17))
        self.in_lbl.setObjectName("in_lbl")
        
        self.out_lbl = QtWidgets.QLabel(self.centralwidget)
        self.out_lbl.setGeometry(QtCore.QRect(40, 380, 111, 17))
        self.out_lbl.setObjectName("out_lbl")
        
        self.tmp_lbl = QtWidgets.QLabel(self.centralwidget)
        self.tmp_lbl.setGeometry(QtCore.QRect(40, 410, 111, 17))
        self.tmp_lbl.setObjectName("tmp_lbl")
        
        self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input.setGeometry(QtCore.QRect(160, 350, 211, 20))
        self.lineEdit_input.setObjectName("lineEdit_input")
        
        self.lineEdit_output = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_output.setGeometry(QtCore.QRect(160, 380, 211, 20))
        self.lineEdit_output.setObjectName("lineEdit_output")
        
        self.lineEdit_check = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_check.setGeometry(QtCore.QRect(160, 410, 211, 20))
        self.lineEdit_check.setObjectName("lineEdit_check")
        
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(380, 410, 61, 21))
        self.loadButton.setObjectName("pushButton")
        self.loadButton.clicked.connect(self.load_checkpoint)
        
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        self.title_lbl.setGeometry(QtCore.QRect(0, 0, 641, 41))
        self.title_lbl.setObjectName("title_lbl")
        
        self.main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        
        self.main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def acceptImage(self, path, destination):
        self.osp.move_file(path, destination)        
        self.osp.move_xml_file(path, destination)
    
    def rejectImage(self):
        #TODO: rejectImage
        pass

    def nextImage(self):
        #TODO: nextImage
        pass
        
    def prevImage(self):
        #TODO: prevImage
        print("Previous image")
        
    def load_checkpoint(self):
        #TODO: load_checkpoint
        print(self.tsp.dir_path)
        print(self.tsp.getCheckpoints())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("self.MainWindow", "self.MainWindow"))
        self.backButton.setText(_translate("self.MainWindow", "<"))
        self.nextButton.setText(_translate("self.MainWindow", ">"))
        self.rejectButton.setText(_translate("self.MainWindow", "Reject"))
        self.acceptButton.setText(_translate("self.MainWindow", "Accept"))
        self.pwd_lbl.setText(_translate("self.MainWindow", "Current folder: ../.../../../.../"))
        self.card_1.setText(_translate("self.MainWindow", 
        "File: ##/#####\n"
        "\n"
        "Files moved: #####\n"
        "\n"
        "Files discarted: #####"))
        self.card_2.setText(_translate("MainWindow", 
        "FILES MOVED\n"
        "\n"
        "\n"
        "\n"
        "With xml: #####\n"
        "\n"
        "Without xml: #####"))
        self.in_lbl.setText(_translate("MainWindow", "Input folder:"))
        self.out_lbl.setText(_translate("MainWindow", "Output folder:"))
        self.tmp_lbl.setText(_translate("MainWindow", "Checkpoint file:"))
        self.loadButton.setText(_translate("MainWindow", "Load"))
        self.title_lbl.setText(_translate("MainWindow", "Easy Dataset Filter"))
    