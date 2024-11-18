# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1047, 821)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_robo = QPushButton(self.frame_top_menus)
        self.btn_page_robo.setObjectName(u"btn_page_robo")
        self.btn_page_robo.setMinimumSize(QSize(0, 40))
        self.btn_page_robo.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	font-size: 12px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_robo)

        self.btn_page_config = QPushButton(self.frame_top_menus)
        self.btn_page_config.setObjectName(u"btn_page_config")
        self.btn_page_config.setMinimumSize(QSize(0, 40))
        self.btn_page_config.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"font-size: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_config)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"	font-size: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"border: none")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border: none;")
        self.page_robo = QWidget()
        self.page_robo.setObjectName(u"page_robo")
        self.verticalLayout_7 = QVBoxLayout(self.page_robo)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.page_robo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 10, 71, 51))
        self.label_3.setStyleSheet(u"font: 81 27px \"AirbnbCereal_W_XBd ExtBd\";\n"
"color: #fff;")
        self.page_robo_log_field = QTextEdit(self.frame_2)
        self.page_robo_log_field.setObjectName(u"page_robo_log_field")
        self.page_robo_log_field.setGeometry(QRect(20, 70, 871, 541))
        self.page_robo_log_field.setStyleSheet(u"font: 81 12px\"AirbnbCereal_W_Light\";\n"
"background: #000;\n"
"border: none;\n"
"border-radius: 8px;\n"
"color: #fff;")
        self.page_robo_stop_button = QPushButton(self.frame_2)
        self.page_robo_stop_button.setObjectName(u"page_robo_stop_button")
        self.page_robo_stop_button.setGeometry(QRect(230, 660, 201, 41))
        self.page_robo_stop_button.setStyleSheet(u"color: #fff;\n"
"background: red;\n"
"border: none;\n"
"font: 81 14px\"AirbnbCereal_W_XBd ExtBd\";\n"
"border-radius: 8px;\n"
)
        self.page_robo_start_button = QPushButton(self.frame_2)
        self.page_robo_start_button.setObjectName(u"page_robo_start_button")
        self.page_robo_start_button.setGeometry(QRect(520, 660, 201, 41))
        self.page_robo_start_button.setStyleSheet(u"color: #fff;\n"
"background: #1F6AA5;\n"
"border: none;\n"
"font: 81 14px\"AirbnbCereal_W_XBd ExtBd\";\n"
"border-radius: 8px;\n"
)

        self.verticalLayout_7.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_robo)
        self.page_config = QWidget()
        self.page_config.setObjectName(u"page_config")
        self.verticalLayout_6 = QVBoxLayout(self.page_config)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_config)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: none")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(10, 10, 191, 51))
        self.label_2.setStyleSheet(u"font: 81 27px \"AirbnbCereal_W_XBd ExtBd\";\n"
"color: #fff;")
        self.page_config_save_button = QPushButton(self.frame)
        self.page_config_save_button.setObjectName(u"page_config_save_button")
        self.page_config_save_button.setGeometry(QRect(370, 670, 201, 41))
        self.page_config_save_button.setStyleSheet(u"color: #fff;\n"
"background: #1F6AA5;\n"
"border: none;\n"
"font: 81 14px\"AirbnbCereal_W_XBd ExtBd\";\n"
"border-radius: 8px;\n"
)
        self.page_config_file_button = QPushButton(self.frame)
        self.page_config_file_button.setObjectName(u"page_config_file_button")
        self.page_config_file_button.setGeometry(QRect(90, 110, 251, 31))
        self.page_config_file_button.setStyleSheet(u"color: #fff;\n"
"background: #1F6AA5;\n"
"border: none;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"border-radius: 8px;\n"
)
        self.page_config_effecti_button = QPushButton(self.frame)
        self.page_config_effecti_button.setObjectName(u"page_config_effecti_button")
        self.page_config_effecti_button.setGeometry(QRect(600, 110, 251, 31))
        self.page_config_effecti_button.setStyleSheet(u"color: #fff;\n"
"background: #1F6AA5;\n"
"border: none;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"border-radius: 8px;\n"
)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 90, 41, 16))
        self.label_4.setStyleSheet(u"color: #fff;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(690, 90, 91, 20))
        self.label_5.setStyleSheet(u"color: #fff;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"")
        self.page_config_declaracao_button = QPushButton(self.frame)
        self.page_config_declaracao_button.setObjectName(u"page_config_declaracao_button")
        self.page_config_declaracao_button.setGeometry(QRect(90, 200, 251, 31))
        self.page_config_declaracao_button.setStyleSheet(u"color: #fff;\n"
"background: #1F6AA5;\n"
"border: none;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"border-radius: 8px;\n"
)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(180, 180, 71, 16))
        self.label_6.setStyleSheet(u"color: #fff;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"")
        self.page_config_proposta_button = QPushButton(self.frame)
        self.page_config_proposta_button.setObjectName(u"page_config_proposta_button")
        self.page_config_proposta_button.setGeometry(QRect(600, 200, 251, 31))
        self.page_config_proposta_button.setStyleSheet(u"color: #fff;\n"
"background: #1F6AA5;\n"
"border: none;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"border-radius: 8px;\n"
)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(670, 180, 121, 20))
        self.label_7.setStyleSheet(u"color: #fff;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"")
        self.page_config_log_field = QTextEdit(self.frame)
        self.page_config_log_field.setObjectName(u"page_config_log_field")
        self.page_config_log_field.setGeometry(QRect(90, 340, 761, 301))
        self.page_config_log_field.setStyleSheet(u"background: #000;\n"
"color: #fff;\n"
"font: 81 12px\"AirbnbCereal_W_Light\";\n"
"border-radius: 8px;\n"
"border: none")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 260, 81, 20))
        self.label_8.setStyleSheet(u"color: #fff;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"")
        self.page_config_documentos_button = QPushButton(self.frame)
        self.page_config_documentos_button.setObjectName(u"page_config_documentos_button")
        self.page_config_documentos_button.setGeometry(QRect(90, 280, 251, 31))
        self.page_config_documentos_button.setStyleSheet(u"color: #fff;\n"
"background: #1F6AA5;\n"
"border: none;\n"
"font: 81 14px\"AirbnbCereal_W_Light\";\n"
"border-radius: 8px;\n"
)

        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_config)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #FFF;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"EXPANDIR", None))
        self.btn_page_robo.setText(QCoreApplication.translate("MainWindow", u"Rob\u00f4", None))
        self.btn_page_config.setText(QCoreApplication.translate("MainWindow", u"Config.", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"EM BREVE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rob\u00f4", None))
        self.page_robo_stop_button.setText(QCoreApplication.translate("MainWindow", u"PARAR", None))
        self.page_robo_start_button.setText(QCoreApplication.translate("MainWindow", u"COME\u00c7AR", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.page_config_save_button.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.page_config_file_button.setText(QCoreApplication.translate("MainWindow", u"Escolher o caminho para salvar", None))
        self.page_config_effecti_button.setText(QCoreApplication.translate("MainWindow", u"Escolher o arquivo HTML Effecti", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pasta", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Arquivo HTML", None))
        self.page_config_declaracao_button.setText(QCoreApplication.translate("MainWindow", u"Escolher o arquivo de declara\u00e7\u00e3o", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Declara\u00e7\u00e3o", None))
        self.page_config_proposta_button.setText(QCoreApplication.translate("MainWindow", u"Escolher o arquivo da planilha", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Planilha de Proposta", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Documentos", None))
        self.page_config_documentos_button.setText(QCoreApplication.translate("MainWindow", u"Escolher os arquivos da documenta\u00e7\u00e3o", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"EM BREVE", None))
    # retranslateUi

