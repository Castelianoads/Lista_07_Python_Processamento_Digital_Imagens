import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QToolTip, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_main_window()
        self.carregarJanela() #initUI

    def setup_main_window(self):
        self.x = 800
        self.y = 600
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagens")
        self.wid = QWidget(self) #Cria o widget
        self.setCentralWidget(self.wid) #Fica no centro da janela
        self.layout = QGridLayout() #Cria o layout em grid
        self.wid.setLayout(self.layout) #Aplica o layout grid no widget

    def carregarJanela(self): #initUI
        #Criar um label
        self.texto = QLabel("0", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        #Criando botao
        self.botao1 = QtWidgets.QPushButton(self)
        self.botao1.setText("+ Incrementa") 
        self.botao1.clicked.connect(self.botao1Click) 

        self.botao2 = QtWidgets.QPushButton(self)
        self.botao2.setText("- Decrementa") 
        self.botao2.clicked.connect(self.botao2Click)

        self.botao3 = QtWidgets.QPushButton(self)
        self.botao3.setText("- Reset") 
        self.botao3.clicked.connect(self.botao3Click)

        #Organizando os componentes Widgets dentro do GridLayout
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.botao1, 1, 0, 1, 2)     
        self.layout.addWidget(self.botao2, 2, 0, 1, 2)          
        self.layout.addWidget(self.botao3, 3, 0, 1, 2)          
    
    def botao1Click(self): 
        self.texto.setText("Carlos Eduardo Casteliano de Paula")

    def botao2Click(self): 
        self.texto.setText("Carlos Eduardo Casteliano de Paula")

    def botao3Click(self): 
        self.texto.setText("Carlos Eduardo Casteliano de Paula")               

aplicacao = QApplication(sys.argv)
j = Janela()
j.show()
sys.exit(aplicacao.exec_())