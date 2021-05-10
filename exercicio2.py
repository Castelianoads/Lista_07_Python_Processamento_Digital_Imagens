import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QToolTip, QGridLayout, QWidget
from PyQt5.QtCore import QSize

class Janela(QMainWindow): #MainWindow
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
        #Criar os componentes (Label, Button, Text, Image)
        #Criando um imagem
        self.imagem1 = QLabel(self) 
        self.endereco1 = 'imagens/ave.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(800, 700, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        #Imagem 2
        self.imagem2 = QLabel(self) 
        self.endereco2 = 'imagens/ave_cinza.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(800, 700, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        #Criando botao
        self.botao1 = QtWidgets.QPushButton(self)
        self.botao1.setText("Original") 

        #Botao 2
        self.botao2 = QtWidgets.QPushButton(self)
        self.botao2.setText("Transformação") 

        #Organizando os componentes Widgets dentro do GridLayout
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.addWidget(self.botao1, 2, 0)
        self.layout.addWidget(self.botao2, 2, 1)

aplicacao = QApplication(sys.argv)        
j = Janela() #MainWindow
j.show()
sys.exit(aplicacao.exec_())
       
