# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'designerfnPgWO.ui'
##
# Created by: Qt User Interface Compiler version 5.14.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from Modelo import NIMFA, Graph

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
from matplotlib import pyplot as plt




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.Graph = None
        self.Model = None
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(255, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionNuevo = QAction(MainWindow)
        self.actionNuevo.setObjectName(u"actionNuevo")
        self.actionCargar = QAction(MainWindow)
        self.actionCargar.setObjectName(u"actionCargar")
        self.actionAyuda_sobre_el_uso_del_app = QAction(MainWindow)
        self.actionAyuda_sobre_el_uso_del_app.setObjectName(u"actionAyuda_sobre_el_uso_del_app")
        self.actionAcerca_de_ka_Aoo = QAction(MainWindow)
        self.actionAcerca_de_ka_Aoo.setObjectName(u"actionAcerca_de_ka_Aoo")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionCerrar = QAction(MainWindow)
        self.actionCerrar.setObjectName(u"actionCerrar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TazaContagioSlider = QSlider(self.centralwidget)
        self.TazaContagioSlider.setObjectName(u"TazaContagioSlider")
        self.TazaContagioSlider.setGeometry(QRect(20, 280, 191, 22))
        font = QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.TazaContagioSlider.setFont(font)
        self.TazaContagioSlider.setFocusPolicy(Qt.StrongFocus)
        self.TazaContagioSlider.setMaximum(12)
        self.TazaContagioSlider.setSingleStep(1)
        self.TazaContagioSlider.setPageStep(2)
        self.TazaContagioSlider.setValue(0)
        self.TazaContagioSlider.setSliderPosition(0)
        self.TazaContagioSlider.setTracking(True)
        self.TazaContagioSlider.setOrientation(Qt.Horizontal)
        self.TazaContagioSlider.setInvertedAppearance(False)
        self.TazaContagioSlider.setInvertedControls(False)
        self.TazaContagioSlider.setTickPosition(QSlider.TicksBelow)
        self.TazaContagioSlider.setTickInterval(2)
        self.TituloTazaCon = QLabel(self.centralwidget)
        self.TituloTazaCon.setObjectName(u"TituloTazaCon")
        self.TituloTazaCon.setGeometry(QRect(40, 240, 161, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.TituloTazaCon.setFont(font1)
        self.TituloTazaCon.setAlignment(Qt.AlignCenter)
        self.Separador1 = QFrame(self.centralwidget)
        self.Separador1.setObjectName(u"Separador1")
        self.Separador1.setGeometry(QRect(10, 220, 221, 16))
        self.Separador1.setFrameShape(QFrame.HLine)
        self.Separador1.setFrameShadow(QFrame.Sunken)
        self.Num2TCon = QLabel(self.centralwidget)
        self.Num2TCon.setObjectName(u"Num2TCon")
        self.Num2TCon.setGeometry(QRect(160, 310, 47, 13))
        font2 = QFont()
        font2.setPointSize(11)
        self.Num2TCon.setFont(font2)
        self.Num2TCon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Num1TCon = QLabel(self.centralwidget)
        self.Num1TCon.setObjectName(u"Num1TCon")
        self.Num1TCon.setGeometry(QRect(70, 310, 47, 13))
        self.Num1TCon.setFont(font2)
        self.Num1TCon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Num0TCon = QLabel(self.centralwidget)
        self.Num0TCon.setObjectName(u"Num0TCon")
        self.Num0TCon.setGeometry(QRect(-20, 310, 51, 16))
        self.Num0TCon.setFont(font2)
        self.Num0TCon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.TituloTazaCur = QLabel(self.centralwidget)
        self.TituloTazaCur.setObjectName(u"TituloTazaCur")
        self.TituloTazaCur.setGeometry(QRect(30, 340, 161, 31))
        self.TituloTazaCur.setFont(font1)
        self.TituloTazaCur.setAlignment(Qt.AlignCenter)
        self.TazaCuraSlider = QSlider(self.centralwidget)
        self.TazaCuraSlider.setObjectName(u"TazaCuraSlider")
        self.TazaCuraSlider.setGeometry(QRect(20, 380, 191, 22))
        self.TazaCuraSlider.setFont(font)
        self.TazaCuraSlider.setFocusPolicy(Qt.StrongFocus)
        self.TazaCuraSlider.setMaximum(12)
        self.TazaCuraSlider.setSingleStep(1)
        self.TazaCuraSlider.setPageStep(2)
        self.TazaCuraSlider.setValue(0)
        self.TazaCuraSlider.setSliderPosition(0)
        self.TazaCuraSlider.setTracking(True)
        self.TazaCuraSlider.setOrientation(Qt.Horizontal)
        self.TazaCuraSlider.setInvertedAppearance(False)
        self.TazaCuraSlider.setInvertedControls(False)
        self.TazaCuraSlider.setTickPosition(QSlider.TicksBelow)
        self.TazaCuraSlider.setTickInterval(2)
        self.Num0TCon_2 = QLabel(self.centralwidget)
        self.Num0TCon_2.setObjectName(u"Num0TCon_2")
        self.Num0TCon_2.setGeometry(QRect(-20, 410, 51, 16))
        self.Num0TCon_2.setFont(font2)
        self.Num0TCon_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Num1TCur = QLabel(self.centralwidget)
        self.Num1TCur.setObjectName(u"Num1TCur")
        self.Num1TCur.setGeometry(QRect(70, 410, 47, 13))
        self.Num1TCur.setFont(font2)
        self.Num1TCur.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Num2TCura = QLabel(self.centralwidget)
        self.Num2TCura.setObjectName(u"Num2TCura")
        self.Num2TCura.setGeometry(QRect(160, 410, 47, 13))
        self.Num2TCura.setFont(font2)
        self.Num2TCura.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Separador2 = QFrame(self.centralwidget)
        self.Separador2.setObjectName(u"Separador2")
        self.Separador2.setGeometry(QRect(10, 440, 221, 16))
        self.Separador2.setFrameShape(QFrame.HLine)
        self.Separador2.setFrameShadow(QFrame.Sunken)
        self.Correr = QPushButton(self.centralwidget)
        self.Correr.setObjectName(u"Correr")
        self.Correr.setGeometry(QRect(20, 470, 201, 31))
        self.Cargar = QPushButton(self.centralwidget)
        self.Cargar.setObjectName(u"Cargar")
        self.Cargar.setGeometry(QRect(20, 80, 201, 31))
        self.Guardar = QPushButton(self.centralwidget)
        self.Guardar.setObjectName(u"Guardar")
        self.Guardar.setGeometry(QRect(20, 130, 201, 31))
        self.NuevoGrafo = QPushButton(self.centralwidget)
        self.NuevoGrafo.setObjectName(u"NuevoGrafo")
        self.NuevoGrafo.setGeometry(QRect(20, 180, 201, 31))
        self.TituloTazaCon_2 = QLabel(self.centralwidget)
        self.TituloTazaCon_2.setObjectName(u"TituloTazaCon_2")
        self.TituloTazaCon_2.setGeometry(QRect(30, 30, 181, 31))
        font3 = QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        font3.setWeight(75)
        self.TituloTazaCon_2.setFont(font3)
        self.TituloTazaCon_2.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(240, 0, 20, 521))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 801, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionCargar)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuAyuda.addAction(self.actionAyuda_sobre_el_uso_del_app)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de_ka_Aoo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Tesis", None))
        self.actionNuevo.setText(
            QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.actionCargar.setText(
            QCoreApplication.translate("MainWindow", u"Cargar", None))
        self.actionAyuda_sobre_el_uso_del_app.setText(
            QCoreApplication.translate("MainWindow", u"Ayuda sobre el uso del app", None))
        self.actionAcerca_de_ka_Aoo.setText(
            QCoreApplication.translate("MainWindow", u"Acerca de la App", None))
        self.actionGuardar.setText(
            QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionCerrar.setText(
            QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.TituloTazaCon.setText(QCoreApplication.translate(
            "MainWindow", u"Taza de Contagio", None))
        self.Num2TCon.setText(
            QCoreApplication.translate("MainWindow", u"2", None))
        self.Num1TCon.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        self.Num0TCon.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.TituloTazaCur.setText(QCoreApplication.translate(
            "MainWindow", u"Taza de Cura", None))
        self.Num0TCon_2.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
        self.Num1TCur.setText(
            QCoreApplication.translate("MainWindow", u"1", None))
        self.Num2TCura.setText(
            QCoreApplication.translate("MainWindow", u"2", None))

        self.Correr.setText(QCoreApplication.translate(
            "MainWindow", u"Correr Simulaci\u00f3n", None))
        self.Correr.clicked.connect(self.runModel)

        self.Cargar.setText(QCoreApplication.translate(
            "MainWindow", u"Cargar Simulaci\u00f3n", None))
        self.Cargar.clicked.connect(self.loadGraph)

        self.Guardar.setText(QCoreApplication.translate(
            "MainWindow", u"Guardar Simulaci\u00f3n", None))
        self.Guardar.clicked.connect(self.saveGraph)

        self.NuevoGrafo.setText(QCoreApplication.translate(
            "MainWindow", u"Generar un Nuevo Grafo", None))
        self.NuevoGrafo.clicked.connect(self.newGraph)


        self.TituloTazaCon_2.setText(
            QCoreApplication.translate("MainWindow", u"Parametros", None))
        self.menuArchivo.setTitle(
            QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(
            QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

    def newGraph(self):
        dialog = QDialog()
        ui = Ui_NuevoGrafo()
        ui.setupUi(dialog)
        dialog.show()
        resp = dialog.exec_()
        val = ui.spinBox.value()

        if resp:
            self.Graph = Graph(2,str(val))
            self.Graph.plot()

    def loadGraph(self):
        dialog = QDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(dialog,"Cargar Grafo", "","All Files (*);;JSON files (*.json)", options=options)
        if fileName:
            self.Graph = Graph(1,fileName)
            self.Graph.plot()

    def saveGraph(self):
        dialog = QDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(dialog,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
            self.Graph.save_graph(fileName)

    def runModel(self):
        print("La simulacion iniciara")
        self.Model = NIMFA(self.Graph.adjM,self.Graph)
        beta = self.TazaContagioSlider.value()/6
        delta = self.TazaCuraSlider.value()/6
        self.Model.setRates(beta,delta)
        self.Model.run()
        self.Model.plotTime()

    


class Ui_NuevoGrafo(object):
    def setupUi(self, NuevoGrafo):
        if not NuevoGrafo.objectName():
            NuevoGrafo.setObjectName(u"NuevoGrafo")
        self.buttonBox = QDialogButtonBox(NuevoGrafo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(110, 70, 161, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(NuevoGrafo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 241, 51))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.spinBox = QSpinBox(NuevoGrafo)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(30, 70, 71, 31))
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBox.setMinimum(2)

        self.retranslateUi(NuevoGrafo)
        self.buttonBox.accepted.connect(NuevoGrafo.accept)
        self.buttonBox.rejected.connect(NuevoGrafo.reject)

        QMetaObject.connectSlotsByName(NuevoGrafo)
    # setupUi

    def retranslateUi(self, NuevoGrafo):
        NuevoGrafo.setWindowTitle(QCoreApplication.translate("NuevoGrafo", u"Nuevo Grafo", None))
        self.label.setText(QCoreApplication.translate("NuevoGrafo", u"Ingrese el numero de nodos", None))
    # retranslateUi



class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__=="__main__":
    app = QApplication()
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
