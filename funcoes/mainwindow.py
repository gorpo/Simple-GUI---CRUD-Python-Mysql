# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 699)
        self.janela_pai = QtWidgets.QWidget(MainWindow)
        self.janela_pai.setObjectName("janela_pai")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.janela_pai)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuTopo = QtWidgets.QFrame(self.janela_pai)
        self.menuTopo.setMaximumSize(QtCore.QSize(16777215, 45))
        self.menuTopo.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.menuTopo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menuTopo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuTopo.setObjectName("menuTopo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menuTopo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_informacoes = QtWidgets.QFrame(self.menuTopo)
        self.frame_informacoes.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_informacoes.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_informacoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_informacoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_informacoes.setObjectName("frame_informacoes")
        self.label_6 = QtWidgets.QLabel(self.frame_informacoes)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.label_6.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"font: 20px Segoe UI, bold;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.frame_informacoes)
        self.frame_minimizar = QtWidgets.QFrame(self.menuTopo)
        self.frame_minimizar.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_minimizar.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_minimizar.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_minimizar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_minimizar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_minimizar.setObjectName("frame_minimizar")
        self.botao_minimizar = QtWidgets.QPushButton(self.frame_minimizar)
        self.botao_minimizar.setGeometry(QtCore.QRect(10, 0, 50, 50))
        self.botao_minimizar.setStyleSheet("QPushButton {\n"
"    background-image: url(:/minimizar/images/minimize.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_minimizar.setText("")
        self.botao_minimizar.setObjectName("botao_minimizar")
        self.horizontalLayout_2.addWidget(self.frame_minimizar)
        self.frame_fechar = QtWidgets.QFrame(self.menuTopo)
        self.frame_fechar.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_fechar.setMaximumSize(QtCore.QSize(50, 50))
        self.frame_fechar.setStyleSheet("background-color: rgb(31,31,31);")
        self.frame_fechar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_fechar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fechar.setObjectName("frame_fechar")
        self.botao_fechar = QtWidgets.QPushButton(self.frame_fechar)
        self.botao_fechar.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.botao_fechar.setStyleSheet("QPushButton {\n"
"    background-image: url(:/fechar/images/icons8-delete-24.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_fechar.setText("")
        self.botao_fechar.setObjectName("botao_fechar")
        self.horizontalLayout_2.addWidget(self.frame_fechar)
        self.verticalLayout.addWidget(self.menuTopo)
        self.conteiner_central = QtWidgets.QFrame(self.janela_pai)
        self.conteiner_central.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.conteiner_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_central.setObjectName("conteiner_central")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.conteiner_central)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.janela_central = QtWidgets.QFrame(self.conteiner_central)
        self.janela_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.janela_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.janela_central.setObjectName("janela_central")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.janela_central)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.janela_central)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.banco_de_dados = QtWidgets.QWidget()
        self.banco_de_dados.setObjectName("banco_de_dados")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.banco_de_dados)
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_13.setSpacing(9)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame = QtWidgets.QFrame(self.banco_de_dados)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.input_db = QtWidgets.QLineEdit(self.frame)
        self.input_db.setMinimumSize(QtCore.QSize(0, 40))
        self.input_db.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.input_db.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_db.setClearButtonEnabled(False)
        self.input_db.setObjectName("input_db")
        self.horizontalLayout_3.addWidget(self.input_db)
        self.input_host = QtWidgets.QLineEdit(self.frame)
        self.input_host.setMinimumSize(QtCore.QSize(0, 40))
        self.input_host.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.input_host.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_host.setClearButtonEnabled(False)
        self.input_host.setObjectName("input_host")
        self.horizontalLayout_3.addWidget(self.input_host)
        self.input_usuario = QtWidgets.QLineEdit(self.frame)
        self.input_usuario.setMinimumSize(QtCore.QSize(0, 40))
        self.input_usuario.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.input_usuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_usuario.setClearButtonEnabled(False)
        self.input_usuario.setObjectName("input_usuario")
        self.horizontalLayout_3.addWidget(self.input_usuario)
        self.input_senha = QtWidgets.QLineEdit(self.frame)
        self.input_senha.setMinimumSize(QtCore.QSize(0, 40))
        self.input_senha.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.input_senha.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_senha.setClearButtonEnabled(False)
        self.input_senha.setObjectName("input_senha")
        self.horizontalLayout_3.addWidget(self.input_senha)
        self.btn_enviar = QtWidgets.QPushButton(self.frame)
        self.btn_enviar.setMinimumSize(QtCore.QSize(90, 40))
        self.btn_enviar.setStyleSheet("QPushButton {\n"
"    background-color:rgb(0,0,0);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.btn_enviar.setObjectName("btn_enviar")
        self.horizontalLayout_3.addWidget(self.btn_enviar)
        self.verticalLayout_13.addWidget(self.frame)
        self.barra_menus_banco_dados = QtWidgets.QFrame(self.banco_de_dados)
        self.barra_menus_banco_dados.setMinimumSize(QtCore.QSize(0, 300))
        self.barra_menus_banco_dados.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.barra_menus_banco_dados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.barra_menus_banco_dados.setObjectName("barra_menus_banco_dados")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.barra_menus_banco_dados)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.conteiner_esquerda_db = QtWidgets.QFrame(self.barra_menus_banco_dados)
        self.conteiner_esquerda_db.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteiner_esquerda_db.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_esquerda_db.setObjectName("conteiner_esquerda_db")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.conteiner_esquerda_db)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.db_texto_titulo = QtWidgets.QLineEdit(self.conteiner_esquerda_db)
        self.db_texto_titulo.setMinimumSize(QtCore.QSize(0, 40))
        self.db_texto_titulo.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.db_texto_titulo.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.db_texto_titulo.setClearButtonEnabled(False)
        self.db_texto_titulo.setObjectName("db_texto_titulo")
        self.verticalLayout_15.addWidget(self.db_texto_titulo)
        self.db_texto_codigo = QtWidgets.QTextEdit(self.conteiner_esquerda_db)
        self.db_texto_codigo.setStyleSheet("QTextEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QTextEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTextEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.db_texto_codigo.setOverwriteMode(False)
        self.db_texto_codigo.setPlaceholderText("")
        self.db_texto_codigo.setObjectName("db_texto_codigo")
        self.verticalLayout_15.addWidget(self.db_texto_codigo)
        self.horizontalLayout_17.addWidget(self.conteiner_esquerda_db)
        self.conteiner_direita_db = QtWidgets.QFrame(self.barra_menus_banco_dados)
        self.conteiner_direita_db.setMaximumSize(QtCore.QSize(400, 16777215))
        self.conteiner_direita_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_direita_db.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_direita_db.setObjectName("conteiner_direita_db")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.conteiner_direita_db)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.db_texto_link = QtWidgets.QLineEdit(self.conteiner_direita_db)
        self.db_texto_link.setMinimumSize(QtCore.QSize(0, 40))
        self.db_texto_link.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.db_texto_link.setObjectName("db_texto_link")
        self.verticalLayout_14.addWidget(self.db_texto_link)
        self.db_texto_observacao = QtWidgets.QTextEdit(self.conteiner_direita_db)
        self.db_texto_observacao.setMaximumSize(QtCore.QSize(16777215, 250))
        self.db_texto_observacao.setStyleSheet("QTextEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Courier New;\n"
"}\n"
"QTextEdit:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTextEdit:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.db_texto_observacao.setObjectName("db_texto_observacao")
        self.verticalLayout_14.addWidget(self.db_texto_observacao)
        self.conteiner_menus_db = QtWidgets.QFrame(self.conteiner_direita_db)
        self.conteiner_menus_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_menus_db.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_menus_db.setObjectName("conteiner_menus_db")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.conteiner_menus_db)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.botao_db_adiciona = QtWidgets.QPushButton(self.conteiner_menus_db)
        self.botao_db_adiciona.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_db_adiciona.setObjectName("botao_db_adiciona")
        self.horizontalLayout_18.addWidget(self.botao_db_adiciona)
        self.botao_db_atualiza = QtWidgets.QPushButton(self.conteiner_menus_db)
        self.botao_db_atualiza.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_db_atualiza.setObjectName("botao_db_atualiza")
        self.horizontalLayout_18.addWidget(self.botao_db_atualiza)
        self.botao_db_deleta = QtWidgets.QPushButton(self.conteiner_menus_db)
        self.botao_db_deleta.setStyleSheet("QPushButton {\n"
"    background-color:transparent;\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 20px SegoeUIl, bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(30,144,255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(1,84,149);\n"
"}")
        self.botao_db_deleta.setObjectName("botao_db_deleta")
        self.horizontalLayout_18.addWidget(self.botao_db_deleta)
        self.verticalLayout_14.addWidget(self.conteiner_menus_db)
        self.horizontalLayout_17.addWidget(self.conteiner_direita_db)
        self.verticalLayout_13.addWidget(self.barra_menus_banco_dados)
        self.conteiner_dados_db = QtWidgets.QFrame(self.banco_de_dados)
        self.conteiner_dados_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conteiner_dados_db.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteiner_dados_db.setObjectName("conteiner_dados_db")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.conteiner_dados_db)
        self.horizontalLayout_16.setContentsMargins(9, 0, 9, 9)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tabela_dados_db = QtWidgets.QTableView(self.conteiner_dados_db)
        self.tabela_dados_db.setStyleSheet("QHeaderView {\n"
"background: rgb(30, 30, 30);\n"
"}\n"
"QHeaderView::section{\n"
"    color: rgb(255, 255, 255);\n"
"background: rgb(35,35,35);\n"
"}\n"
"QTableCornerButton::section{\n"
"background: rgb(35,35,35);\n"
"}\n"
"QHeaderView::section:pressed{\n"
"background: rgb(30,144,255);\n"
"}\n"
"QTableCornerButton::section:pressed{\n"
"background: rgb(30,144,255);\n"
"}\n"
"\n"
"\n"
"\n"
"QTableView{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 10px;\n"
"background-color: rgb(30,30,30);\n"
"    color: rgb(203, 203, 203);\n"
"font: 15px Segoe UI, bold;\n"
"}\n"
"QTableView:hover{\n"
"border: 2px solid rgb(55,55,55);\n"
"}\n"
"QTableView:focus{\n"
"border: 2px solid  rgb(85, 170, 255);\n"
"    color: rgb(85, 170, 255);\n"
"}\n"
"* { gridline-color: gray }")
        self.tabela_dados_db.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabela_dados_db.setGridStyle(QtCore.Qt.SolidLine)
        self.tabela_dados_db.setObjectName("tabela_dados_db")
        self.tabela_dados_db.horizontalHeader().setDefaultSectionSize(150)
        self.horizontalLayout_16.addWidget(self.tabela_dados_db)
        self.verticalLayout_13.addWidget(self.conteiner_dados_db)
        self.stackedWidget.addWidget(self.banco_de_dados)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.rodape = QtWidgets.QFrame(self.janela_central)
        self.rodape.setMinimumSize(QtCore.QSize(0, 17))
        self.rodape.setStyleSheet("background-color: rgb(31, 31, 31);")
        self.rodape.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rodape.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rodape.setObjectName("rodape")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.rodape)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rodape_desenvolvedor = QtWidgets.QLabel(self.rodape)
        self.rodape_desenvolvedor.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.rodape_desenvolvedor.setObjectName("rodape_desenvolvedor")
        self.horizontalLayout_7.addWidget(self.rodape_desenvolvedor)
        self.rodape_versao = QtWidgets.QLabel(self.rodape)
        self.rodape_versao.setStyleSheet("QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(98, 103, 111);\n"
"font: 10px ,Segoe UI;\n"
"margin-right: 5px;\n"
"}\n"
"\n"
"")
        self.rodape_versao.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rodape_versao.setObjectName("rodape_versao")
        self.horizontalLayout_7.addWidget(self.rodape_versao)
        self.redimensionador = QtWidgets.QFrame(self.rodape)
        self.redimensionador.setMaximumSize(QtCore.QSize(20, 20))
        self.redimensionador.setStyleSheet("QSizeGrip {\n"
"    \n"
"    background-image: url(:/redimensiona/images/cil-move.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}")
        self.redimensionador.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redimensionador.setFrameShadow(QtWidgets.QFrame.Raised)
        self.redimensionador.setObjectName("redimensionador")
        self.horizontalLayout_7.addWidget(self.redimensionador)
        self.verticalLayout_4.addWidget(self.rodape)
        self.horizontalLayout.addWidget(self.janela_central)
        self.verticalLayout.addWidget(self.conteiner_central)
        MainWindow.setCentralWidget(self.janela_pai)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "CRUD MYSQL"))
        self.input_db.setText(_translate("MainWindow", "database"))
        self.input_host.setText(_translate("MainWindow", "host"))
        self.input_usuario.setText(_translate("MainWindow", "usuário"))
        self.input_senha.setText(_translate("MainWindow", "senha"))
        self.btn_enviar.setText(_translate("MainWindow", "enviar"))
        self.db_texto_titulo.setText(_translate("MainWindow", "titulo"))
        self.db_texto_codigo.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px;\">codigo</span></p></body></html>"))
        self.db_texto_link.setText(_translate("MainWindow", "link"))
        self.db_texto_observacao.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15px;\">observações</span></p></body></html>"))
        self.botao_db_adiciona.setText(_translate("MainWindow", "adiciona"))
        self.botao_db_atualiza.setText(_translate("MainWindow", "atualiza"))
        self.botao_db_deleta.setText(_translate("MainWindow", "deleta"))
        self.rodape_desenvolvedor.setText(_translate("MainWindow", "manicomio | 2020"))
        self.rodape_versao.setText(_translate("MainWindow", "v1.0  "))


import files_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
