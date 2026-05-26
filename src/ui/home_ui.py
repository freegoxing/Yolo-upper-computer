# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QSplitter,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 540)
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        self.Main_QF = QFrame(self.MainWidget)
        self.Main_QF.setObjectName(u"Main_QF")
        self.Main_QF.setGeometry(QRect(-10, 0, 1011, 541))
        self.Main_QF.setStyleSheet(u"QFrame#Main_QF {\n"
"    background-color: rgb(18, 22, 30);\n"
"    border-radius: 18px;\n"
"}")
        self.main_qframe = QHBoxLayout(self.Main_QF)
        self.main_qframe.setSpacing(0)
        self.main_qframe.setObjectName(u"main_qframe")
        self.main_qframe.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuBg = QFrame(self.Main_QF)
        self.LeftMenuBg.setObjectName(u"LeftMenuBg")
        self.LeftMenuBg.setMinimumSize(QSize(68, 0))
        self.LeftMenuBg.setMaximumSize(QSize(68, 16777215))
        self.LeftMenuBg.setStyleSheet(u"QFrame#LeftMenuBg {\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:0 rgba(42, 52, 65, 245),\n"
"        stop:1 rgba(28, 36, 48, 245)\n"
"    );\n"
"\n"
"    border: 1px solid rgba(100, 140, 180, 90);\n"
"}")
        self.LeftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.LeftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.ToggleBox = QFrame(self.LeftMenuBg)
        self.ToggleBox.setObjectName(u"ToggleBox")
        self.ToggleBox.setMinimumSize(QSize(200, 80))
        self.ToggleBox.setMaximumSize(QSize(200, 80))
        self.ToggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.ToggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ToggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.ToggleBotton = QPushButton(self.ToggleBox)
        self.ToggleBotton.setObjectName(u"ToggleBotton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToggleBotton.sizePolicy().hasHeightForWidth())
        self.ToggleBotton.setSizePolicy(sizePolicy)
        self.ToggleBotton.setMinimumSize(QSize(0, 45))
        self.ToggleBotton.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.ToggleBotton.setFont(font)
        self.ToggleBotton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ToggleBotton.setMouseTracking(True)
        self.ToggleBotton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton.setAutoFillBackground(False)
        self.ToggleBotton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        icon = QIcon()
        iconThemeName = u"zoom-out"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../Ultralytics-PySide6", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.ToggleBotton.setIcon(icon)
        self.ToggleBotton.setAutoDefault(False)
        self.ToggleBotton.setFlat(False)

        self.verticalLayout_4.addWidget(self.ToggleBotton)


        self.verticalLayout_2.addWidget(self.ToggleBox)

        self.MenuBox = QFrame(self.LeftMenuBg)
        self.MenuBox.setObjectName(u"MenuBox")
        self.MenuBox.setMinimumSize(QSize(200, 0))
        self.MenuBox.setMaximumSize(QSize(200, 16777215))
        self.MenuBox.setFrameShape(QFrame.Shape.NoFrame)
        self.MenuBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.MenuBox)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.src_file_button = QPushButton(self.MenuBox)
        self.src_file_button.setObjectName(u"src_file_button")
        self.src_file_button.setMinimumSize(QSize(0, 45))
        self.src_file_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.src_file_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/file.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        self.src_file_button.setCheckable(False)

        self.verticalLayout_5.addWidget(self.src_file_button)

        self.src_cam_button = QPushButton(self.MenuBox)
        self.src_cam_button.setObjectName(u"src_cam_button")
        self.src_cam_button.setMinimumSize(QSize(0, 45))
        self.src_cam_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.src_cam_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/cam.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        self.src_cam_button.setCheckable(False)

        self.verticalLayout_5.addWidget(self.src_cam_button)

        self.src_rtsp_button = QPushButton(self.MenuBox)
        self.src_rtsp_button.setObjectName(u"src_rtsp_button")
        self.src_rtsp_button.setMinimumSize(QSize(0, 45))
        self.src_rtsp_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.src_rtsp_button.setAutoFillBackground(False)
        self.src_rtsp_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/RTSP.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.verticalLayout_5.addWidget(self.src_rtsp_button)

        self.src_udp_button = QPushButton(self.MenuBox)
        self.src_udp_button.setObjectName(u"src_udp_button")
        self.src_udp_button.setMinimumSize(QSize(0, 45))
        self.src_udp_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.src_udp_button.setAutoFillBackground(False)
        self.src_udp_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/RTSP.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")

        self.verticalLayout_5.addWidget(self.src_udp_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.MenuBox)


        self.main_qframe.addWidget(self.LeftMenuBg)

        self.ContentBox = QFrame(self.Main_QF)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setStyleSheet(u"QFrame#ContentBox {\n"
"\n"
"    background-color: rgb(34, 42, 54);\n"
"\n"
"    border: 1px solid rgba(120, 160, 200, 40);\n"
"\n"
"}")
        self.ContentBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.ContentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.ContentBox)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 30))
        self.top.setMaximumSize(QSize(16777215, 30))
        self.top.setStyleSheet(u"QFrame#top{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}")
        self.top.setFrameShape(QFrame.Shape.StyledPanel)
        self.top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, -1, 0)
        self.explain_title = QLabel(self.top)
        self.explain_title.setObjectName(u"explain_title")
        self.explain_title.setMinimumSize(QSize(0, 30))
        self.explain_title.setMaximumSize(QSize(16777215, 30))
        self.explain_title.setStyleSheet(u"color: rgb(245, 248, 252);\n"
"\n"
"padding-left: 10px;\n"
"\n"
"font-family: \"Microsoft YaHei UI\";\n"
"font-size: 12pt;\n"
"font-weight: 700;")
        self.explain_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.explain_title)

        self.buttons_sf = QFrame(self.top)
        self.buttons_sf.setObjectName(u"buttons_sf")
        self.buttons_sf.setMinimumSize(QSize(120, 30))
        self.buttons_sf.setMaximumSize(QSize(120, 30))
        self.buttons_sf.setFrameShape(QFrame.Shape.NoFrame)
        self.buttons_sf.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_sf)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.min_sf = QPushButton(self.buttons_sf)
        self.min_sf.setObjectName(u"min_sf")
        self.min_sf.setMinimumSize(QSize(14, 14))
        self.min_sf.setMaximumSize(QSize(14, 14))
        self.min_sf.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(4, 180, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.min_sf)

        self.max_sf = QPushButton(self.buttons_sf)
        self.max_sf.setObjectName(u"max_sf")
        self.max_sf.setMinimumSize(QSize(14, 14))
        self.max_sf.setMaximumSize(QSize(14, 14))
        self.max_sf.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(227, 199, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.max_sf)

        self.close_button = QPushButton(self.buttons_sf)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(14, 14))
        self.close_button.setMaximumSize(QSize(14, 14))
        self.close_button.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(240, 108, 96);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.close_button)


        self.horizontalLayout.addWidget(self.buttons_sf)


        self.verticalLayout_6.addWidget(self.top)

        self.content = QStackedWidget(self.ContentBox)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.widget_2 = QWidget()
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.content.addWidget(self.widget_2)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_46 = QHBoxLayout(self.widget)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(9, 0, 0, 0)
        self.content.addWidget(self.widget)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy1)
        self.home.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_24 = QHBoxLayout(self.home)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 0, 0, 0)
        self.main_content_cam = QVBoxLayout()
        self.main_content_cam.setSpacing(5)
        self.main_content_cam.setObjectName(u"main_content_cam")
        self.QF_Group_cam = QFrame(self.home)
        self.QF_Group_cam.setObjectName(u"QF_Group_cam")
        self.QF_Group_cam.setMinimumSize(QSize(0, 100))
        self.QF_Group_cam.setMaximumSize(QSize(16777215, 100))
        self.QF_Group_cam.setStyleSheet(u"QFrame#QF_Group_cam {\n"
"\n"
"    background-color: rgb(56, 66, 82);\n"
"\n"
"    border: 1px solid rgba(160, 200, 255, 70);\n"
"\n"
"    border-radius: 12px;\n"
"}")
        self.QF_Group_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.QF_Group_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.QF_Group_cam)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 9, -1, 15)
        self.Class_QF_cam = QFrame(self.QF_Group_cam)
        self.Class_QF_cam.setObjectName(u"Class_QF_cam")
        self.Class_QF_cam.setMinimumSize(QSize(170, 80))
        self.Class_QF_cam.setMaximumSize(QSize(170, 80))
        palette = QPalette()
        brush = QBrush(QColor(245, 248, 250, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        gradient = QLinearGradient(0, 0, 1, 1)
        gradient.setSpread(QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(58, 88, 120, 255))
        gradient.setColorAt(1, QColor(42, 65, 92, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 1, 1)
        gradient1.setSpread(QGradient.Spread.PadSpread)
        gradient1.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(58, 88, 120, 255))
        gradient1.setColorAt(1, QColor(42, 65, 92, 255))
        brush2 = QBrush(gradient1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        gradient2 = QLinearGradient(0, 0, 1, 1)
        gradient2.setSpread(QGradient.Spread.PadSpread)
        gradient2.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(58, 88, 120, 255))
        gradient2.setColorAt(1, QColor(42, 65, 92, 255))
        brush3 = QBrush(gradient2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        brush4 = QBrush(QColor(245, 248, 250, 128))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 1, 1)
        gradient3.setSpread(QGradient.Spread.PadSpread)
        gradient3.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(58, 88, 120, 255))
        gradient3.setColorAt(1, QColor(42, 65, 92, 255))
        brush5 = QBrush(gradient3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 1, 1)
        gradient4.setSpread(QGradient.Spread.PadSpread)
        gradient4.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(58, 88, 120, 255))
        gradient4.setColorAt(1, QColor(42, 65, 92, 255))
        brush6 = QBrush(gradient4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush6)
        gradient5 = QLinearGradient(0, 0, 1, 1)
        gradient5.setSpread(QGradient.Spread.PadSpread)
        gradient5.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(58, 88, 120, 255))
        gradient5.setColorAt(1, QColor(42, 65, 92, 255))
        brush7 = QBrush(gradient5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        gradient6 = QLinearGradient(0, 0, 1, 1)
        gradient6.setSpread(QGradient.Spread.PadSpread)
        gradient6.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(58, 88, 120, 255))
        gradient6.setColorAt(1, QColor(42, 65, 92, 255))
        brush8 = QBrush(gradient6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush8)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        gradient7 = QLinearGradient(0, 0, 1, 1)
        gradient7.setSpread(QGradient.Spread.PadSpread)
        gradient7.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(58, 88, 120, 255))
        gradient7.setColorAt(1, QColor(42, 65, 92, 255))
        brush9 = QBrush(gradient7)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        gradient8 = QLinearGradient(0, 0, 1, 1)
        gradient8.setSpread(QGradient.Spread.PadSpread)
        gradient8.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(58, 88, 120, 255))
        gradient8.setColorAt(1, QColor(42, 65, 92, 255))
        brush10 = QBrush(gradient8)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        self.Class_QF_cam.setPalette(palette)
        self.Class_QF_cam.setToolTipDuration(0)
        self.Class_QF_cam.setStyleSheet(u"QFrame#Class_QF_cam {\n"
"    color: rgb(245, 248, 250);\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:1,\n"
"        stop:0 rgb(58, 88, 120),\n"
"        stop:1 rgb(42, 65, 92)\n"
"    );\n"
"\n"
"    border: 1px solid rgb(95, 170, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.Class_QF_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Class_QF_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.Class_QF_cam)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.Class_top_cam = QFrame(self.Class_QF_cam)
        self.Class_top_cam.setObjectName(u"Class_top_cam")
        self.Class_top_cam.setStyleSheet(u"border:none")
        self.Class_top_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Class_top_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Class_top_cam)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 3, 0, 3)
        self.label_9 = QLabel(self.Class_top_cam)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans CJK SC"])
        font1.setPointSize(14)
        font1.setWeight(QFont.DemiBold)
        font1.setItalic(False)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: rgb(235, 240, 245);\n"
"font: 14pt \"Noto Sans CJK SC\";\n"
"padding-left: 14px;\n"
"font-weight: 600;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9.setIndent(0)

        self.horizontalLayout_16.addWidget(self.label_9)


        self.verticalLayout_17.addWidget(self.Class_top_cam)

        self.line_6 = QFrame(self.Class_QF_cam)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMaximumSize(QSize(16777215, 1))
        self.line_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_6)

        self.Class_bottom_cam = QFrame(self.Class_QF_cam)
        self.Class_bottom_cam.setObjectName(u"Class_bottom_cam")
        self.Class_bottom_cam.setStyleSheet(u"border:none")
        self.Class_bottom_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Class_bottom_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.Class_bottom_cam)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 6, 0, 6)
        self.Class_num_cam = QLabel(self.Class_bottom_cam)
        self.Class_num_cam.setObjectName(u"Class_num_cam")
        self.Class_num_cam.setMinimumSize(QSize(0, 30))
        self.Class_num_cam.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans CJK SC"])
        font2.setPointSize(17)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.Class_num_cam.setFont(font2)
        self.Class_num_cam.setStyleSheet(u"color: rgb(235, 240, 245);\n"
"font: 17pt \"Noto Sans CJK SC\";\n"
"")
        self.Class_num_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.Class_num_cam, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_17.addWidget(self.Class_bottom_cam)

        self.verticalLayout_17.setStretch(1, 2)
        self.verticalLayout_17.setStretch(2, 1)

        self.horizontalLayout_15.addWidget(self.Class_QF_cam)

        self.Fps_QF_cam = QFrame(self.QF_Group_cam)
        self.Fps_QF_cam.setObjectName(u"Fps_QF_cam")
        self.Fps_QF_cam.setMinimumSize(QSize(170, 80))
        self.Fps_QF_cam.setMaximumSize(QSize(170, 80))
        self.Fps_QF_cam.setToolTipDuration(0)
        self.Fps_QF_cam.setStyleSheet(u"QFrame#Fps_QF_cam {\n"
"    color: rgb(245, 248, 250);\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:1,\n"
"        stop:0 rgb(48, 92, 76),\n"
"        stop:1 rgb(34, 68, 58)\n"
"    );\n"
"\n"
"    border: 1px solid rgb(90, 210, 140);\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Fps_QF_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fps_QF_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.Fps_QF_cam)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.Fps_top_cam = QFrame(self.Fps_QF_cam)
        self.Fps_top_cam.setObjectName(u"Fps_top_cam")
        self.Fps_top_cam.setStyleSheet(u"border:none")
        self.Fps_top_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fps_top_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.Fps_top_cam)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 3, 7, 3)
        self.label_11 = QLabel(self.Fps_top_cam)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(235, 240, 245);\n"
"font: 14pt \"Noto Sans CJK SC\";\n"
"padding-left: 14px;\n"
"font-weight: 600;")
        self.label_11.setMidLineWidth(-1)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setIndent(0)

        self.horizontalLayout_18.addWidget(self.label_11)


        self.verticalLayout_26.addWidget(self.Fps_top_cam)

        self.line_8 = QFrame(self.Fps_QF_cam)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMaximumSize(QSize(16777215, 1))
        self.line_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_26.addWidget(self.line_8)

        self.Fps_bottom_cam = QFrame(self.Fps_QF_cam)
        self.Fps_bottom_cam.setObjectName(u"Fps_bottom_cam")
        self.Fps_bottom_cam.setStyleSheet(u"border:none")
        self.Fps_bottom_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Fps_bottom_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.Fps_bottom_cam)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 6, 0, 6)
        self.fps_label_cam = QLabel(self.Fps_bottom_cam)
        self.fps_label_cam.setObjectName(u"fps_label_cam")
        self.fps_label_cam.setMinimumSize(QSize(0, 30))
        self.fps_label_cam.setMaximumSize(QSize(16777215, 30))
        self.fps_label_cam.setFont(font2)
        self.fps_label_cam.setStyleSheet(u"color: rgb(235, 240, 245);\n"
"font: 17pt \"Noto Sans CJK SC\";\n"
"")
        self.fps_label_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_27.addWidget(self.fps_label_cam)


        self.verticalLayout_26.addWidget(self.Fps_bottom_cam)

        self.verticalLayout_26.setStretch(1, 2)
        self.verticalLayout_26.setStretch(2, 1)

        self.horizontalLayout_15.addWidget(self.Fps_QF_cam)

        self.Target_QF_cam = QFrame(self.QF_Group_cam)
        self.Target_QF_cam.setObjectName(u"Target_QF_cam")
        self.Target_QF_cam.setMinimumSize(QSize(170, 80))
        self.Target_QF_cam.setMaximumSize(QSize(170, 80))
        self.Target_QF_cam.setToolTipDuration(0)
        self.Target_QF_cam.setStyleSheet(u"QFrame#Target_QF_cam {\n"
"    color: rgb(250, 250, 250);\n"
"\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:1,\n"
"        stop:0 rgb(115, 72, 48),\n"
"        stop:1 rgb(82, 52, 38)\n"
"    );\n"
"\n"
"    border: 1px solid rgb(255, 165, 90);\n"
"    border-radius: 10px;\n"
"}")
        self.Target_QF_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Target_QF_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.Target_QF_cam)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.Target_top_cam = QFrame(self.Target_QF_cam)
        self.Target_top_cam.setObjectName(u"Target_top_cam")
        self.Target_top_cam.setStyleSheet(u"border:none")
        self.Target_top_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Target_top_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Target_top_cam)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 3, 0, 3)
        self.label_10 = QLabel(self.Target_top_cam)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 30))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"color: rgb(235, 240, 245);\n"
"font: 14pt \"Noto Sans CJK SC\";\n"
"padding-left: 14px;\n"
"font-weight: 600;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10.setIndent(0)

        self.horizontalLayout_17.addWidget(self.label_10)


        self.verticalLayout_24.addWidget(self.Target_top_cam)

        self.line_7 = QFrame(self.Target_QF_cam)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(16777215, 1))
        self.line_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_24.addWidget(self.line_7)

        self.Target_bottom_cam = QFrame(self.Target_QF_cam)
        self.Target_bottom_cam.setObjectName(u"Target_bottom_cam")
        self.Target_bottom_cam.setStyleSheet(u"border:none")
        self.Target_bottom_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Target_bottom_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.Target_bottom_cam)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 6, 0, 6)
        self.Target_num_cam = QLabel(self.Target_bottom_cam)
        self.Target_num_cam.setObjectName(u"Target_num_cam")
        self.Target_num_cam.setMinimumSize(QSize(0, 30))
        self.Target_num_cam.setMaximumSize(QSize(16777215, 30))
        self.Target_num_cam.setFont(font2)
        self.Target_num_cam.setStyleSheet(u"color: rgb(235, 240, 245);\n"
"font: 17pt \"Noto Sans CJK SC\";\n"
"")
        self.Target_num_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.Target_num_cam)


        self.verticalLayout_24.addWidget(self.Target_bottom_cam)

        self.verticalLayout_24.setStretch(1, 2)
        self.verticalLayout_24.setStretch(2, 1)

        self.horizontalLayout_15.addWidget(self.Target_QF_cam)


        self.main_content_cam.addWidget(self.QF_Group_cam)

        self.Result_QF_cam = QFrame(self.home)
        self.Result_QF_cam.setObjectName(u"Result_QF_cam")
        self.Result_QF_cam.setStyleSheet(u"QFrame#Result_QF_cam {\n"
"\n"
"    background-color: rgb(56, 66, 82);\n"
"\n"
"    border: 1px solid rgba(160, 200, 255, 70);\n"
"\n"
"    border-radius: 12px;\n"
"}")
        self.Result_QF_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Result_QF_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.Result_QF_cam)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.splitter_cam = QSplitter(self.Result_QF_cam)
        self.splitter_cam.setObjectName(u"splitter_cam")
        self.splitter_cam.setStyleSheet(u"#splitter_cam::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter_cam.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_cam.setHandleWidth(2)
        self.pre_cam = QLabel(self.splitter_cam)
        self.pre_cam.setObjectName(u"pre_cam")
        self.pre_cam.setMinimumSize(QSize(200, 100))
        self.pre_cam.setStyleSheet(u"QFrame#QF_Group_cam {\n"
"\n"
"    background-color: rgb(56, 66, 82);\n"
"\n"
"    border: 1px solid rgba(160, 200, 255, 70);\n"
"\n"
"    border-radius: 12px;\n"
"}")
        self.pre_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_cam.addWidget(self.pre_cam)
        self.res_cam = QLabel(self.splitter_cam)
        self.res_cam.setObjectName(u"res_cam")
        self.res_cam.setMinimumSize(QSize(200, 100))
        self.res_cam.setStyleSheet(u"QFrame#QF_Group_cam {\n"
"\n"
"    background-color: rgb(52, 62, 78);\n"
"\n"
"    border: 1px solid rgba(140, 180, 220, 55);\n"
"\n"
"    border-radius: 12px;\n"
"}")
        self.res_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.splitter_cam.addWidget(self.res_cam)

        self.verticalLayout_30.addWidget(self.splitter_cam)


        self.main_content_cam.addWidget(self.Result_QF_cam)

        self.Defect_QF_cam = QFrame(self.home)
        self.Defect_QF_cam.setObjectName(u"Defect_QF_cam")
        self.Defect_QF_cam.setMinimumSize(QSize(0, 70))
        self.Defect_QF_cam.setMaximumSize(QSize(16777215, 70))
        self.Defect_QF_cam.setStyleSheet(u"QFrame#Defect_QF_cam {\n"
"    background-color: rgba(56, 66, 82, 100);\n"
"    border: 1px solid rgba(160, 200, 255, 30);\n"
"    border-radius: 10px;\n"
"}")
        self.defect_layout = QHBoxLayout(self.Defect_QF_cam)
        self.defect_layout.setSpacing(10)
        self.defect_layout.setObjectName(u"defect_layout")
        self.defect_layout.setContentsMargins(10, 5, 10, 5)
        self.card_crazing = QFrame(self.Defect_QF_cam)
        self.card_crazing.setObjectName(u"card_crazing")
        self.card_crazing.setStyleSheet(u"QFrame { background-color: rgba(70, 80, 100, 120); border: 1px solid rgba(160, 200, 255, 40); border-radius: 6px; }")
        self.v_layout_crazing = QVBoxLayout(self.card_crazing)
        self.v_layout_crazing.setObjectName(u"v_layout_crazing")
        self.label_crazing = QLabel(self.card_crazing)
        self.label_crazing.setObjectName(u"label_crazing")
        self.label_crazing.setStyleSheet(u"color: #A0C8FF; font-size: 10pt; font-weight: bold;")
        self.label_crazing.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_crazing.addWidget(self.label_crazing)

        self.count_crazing = QLabel(self.card_crazing)
        self.count_crazing.setObjectName(u"count_crazing")
        self.count_crazing.setStyleSheet(u"color: white; font-size: 13pt; font-weight: bold;")
        self.count_crazing.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_crazing.addWidget(self.count_crazing)


        self.defect_layout.addWidget(self.card_crazing)

        self.card_inclusion = QFrame(self.Defect_QF_cam)
        self.card_inclusion.setObjectName(u"card_inclusion")
        self.card_inclusion.setStyleSheet(u"QFrame { background-color: rgba(70, 80, 100, 120); border: 1px solid rgba(160, 200, 255, 40); border-radius: 6px; }")
        self.v_layout_inclusion = QVBoxLayout(self.card_inclusion)
        self.v_layout_inclusion.setObjectName(u"v_layout_inclusion")
        self.label_inclusion = QLabel(self.card_inclusion)
        self.label_inclusion.setObjectName(u"label_inclusion")
        self.label_inclusion.setStyleSheet(u"color: #A0C8FF; font-size: 10pt; font-weight: bold;")
        self.label_inclusion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_inclusion.addWidget(self.label_inclusion)

        self.count_inclusion = QLabel(self.card_inclusion)
        self.count_inclusion.setObjectName(u"count_inclusion")
        self.count_inclusion.setStyleSheet(u"color: white; font-size: 13pt; font-weight: bold;")
        self.count_inclusion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_inclusion.addWidget(self.count_inclusion)


        self.defect_layout.addWidget(self.card_inclusion)

        self.card_patches = QFrame(self.Defect_QF_cam)
        self.card_patches.setObjectName(u"card_patches")
        self.card_patches.setStyleSheet(u"QFrame { background-color: rgba(70, 80, 100, 120); border: 1px solid rgba(160, 200, 255, 40); border-radius: 6px; }")
        self.v_layout_patches = QVBoxLayout(self.card_patches)
        self.v_layout_patches.setObjectName(u"v_layout_patches")
        self.label_patches = QLabel(self.card_patches)
        self.label_patches.setObjectName(u"label_patches")
        self.label_patches.setStyleSheet(u"color: #A0C8FF; font-size: 10pt; font-weight: bold;")
        self.label_patches.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_patches.addWidget(self.label_patches)

        self.count_patches = QLabel(self.card_patches)
        self.count_patches.setObjectName(u"count_patches")
        self.count_patches.setStyleSheet(u"color: white; font-size: 13pt; font-weight: bold;")
        self.count_patches.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_patches.addWidget(self.count_patches)


        self.defect_layout.addWidget(self.card_patches)

        self.card_pitted = QFrame(self.Defect_QF_cam)
        self.card_pitted.setObjectName(u"card_pitted")
        self.card_pitted.setStyleSheet(u"QFrame { background-color: rgba(70, 80, 100, 120); border: 1px solid rgba(160, 200, 255, 40); border-radius: 6px; }")
        self.v_layout_pitted = QVBoxLayout(self.card_pitted)
        self.v_layout_pitted.setObjectName(u"v_layout_pitted")
        self.label_pitted = QLabel(self.card_pitted)
        self.label_pitted.setObjectName(u"label_pitted")
        self.label_pitted.setStyleSheet(u"color: #A0C8FF; font-size: 10pt; font-weight: bold;")
        self.label_pitted.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_pitted.addWidget(self.label_pitted)

        self.count_pitted_surface = QLabel(self.card_pitted)
        self.count_pitted_surface.setObjectName(u"count_pitted_surface")
        self.count_pitted_surface.setStyleSheet(u"color: white; font-size: 13pt; font-weight: bold;")
        self.count_pitted_surface.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_pitted.addWidget(self.count_pitted_surface)


        self.defect_layout.addWidget(self.card_pitted)

        self.card_rolled = QFrame(self.Defect_QF_cam)
        self.card_rolled.setObjectName(u"card_rolled")
        self.card_rolled.setStyleSheet(u"QFrame { background-color: rgba(70, 80, 100, 120); border: 1px solid rgba(160, 200, 255, 40); border-radius: 6px; }")
        self.v_layout_rolled = QVBoxLayout(self.card_rolled)
        self.v_layout_rolled.setObjectName(u"v_layout_rolled")
        self.label_rolled = QLabel(self.card_rolled)
        self.label_rolled.setObjectName(u"label_rolled")
        self.label_rolled.setStyleSheet(u"color: #A0C8FF; font-size: 10pt; font-weight: bold;")
        self.label_rolled.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_rolled.addWidget(self.label_rolled)

        self.count_rolled_in_scale = QLabel(self.card_rolled)
        self.count_rolled_in_scale.setObjectName(u"count_rolled_in_scale")
        self.count_rolled_in_scale.setStyleSheet(u"color: white; font-size: 13pt; font-weight: bold;")
        self.count_rolled_in_scale.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_rolled.addWidget(self.count_rolled_in_scale)


        self.defect_layout.addWidget(self.card_rolled)

        self.card_scratches = QFrame(self.Defect_QF_cam)
        self.card_scratches.setObjectName(u"card_scratches")
        self.card_scratches.setStyleSheet(u"QFrame { background-color: rgba(70, 80, 100, 120); border: 1px solid rgba(160, 200, 255, 40); border-radius: 6px; }")
        self.v_layout_scratches = QVBoxLayout(self.card_scratches)
        self.v_layout_scratches.setObjectName(u"v_layout_scratches")
        self.label_scratches = QLabel(self.card_scratches)
        self.label_scratches.setObjectName(u"label_scratches")
        self.label_scratches.setStyleSheet(u"color: #A0C8FF; font-size: 10pt; font-weight: bold;")
        self.label_scratches.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_scratches.addWidget(self.label_scratches)

        self.count_scratches = QLabel(self.card_scratches)
        self.count_scratches.setObjectName(u"count_scratches")
        self.count_scratches.setStyleSheet(u"color: white; font-size: 13pt; font-weight: bold;")
        self.count_scratches.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.v_layout_scratches.addWidget(self.count_scratches)


        self.defect_layout.addWidget(self.card_scratches)


        self.main_content_cam.addWidget(self.Defect_QF_cam)

        self.Pause_QF_cam = QFrame(self.home)
        self.Pause_QF_cam.setObjectName(u"Pause_QF_cam")
        self.Pause_QF_cam.setMinimumSize(QSize(0, 30))
        self.Pause_QF_cam.setMaximumSize(QSize(16777215, 30))
        self.Pause_QF_cam.setStyleSheet(u"QFrame#Pause_Group_cam {\n"
"\n"
"    background-color: rgb(56, 66, 82);\n"
"\n"
"    border: 1px solid rgba(160, 200, 255, 70);\n"
"\n"
"    border-radius: 12px;\n"
"}")
        self.Pause_QF_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.Pause_QF_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.Pause_QF_cam)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 3, 0)
        self.run_button_cam = QPushButton(self.Pause_QF_cam)
        self.run_button_cam.setObjectName(u"run_button_cam")
        self.run_button_cam.setMinimumSize(QSize(0, 30))
        self.run_button_cam.setMaximumSize(QSize(16777215, 30))
        self.run_button_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.run_button_cam.setMouseTracking(True)
        self.run_button_cam.setStyleSheet(u"QPushButton{\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/all/img/begin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/all/img/pause.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.run_button_cam.setIcon(icon1)
        self.run_button_cam.setIconSize(QSize(30, 30))
        self.run_button_cam.setCheckable(True)
        self.run_button_cam.setChecked(False)

        self.horizontalLayout_20.addWidget(self.run_button_cam)

        self.progress_bar_cam = QProgressBar(self.Pause_QF_cam)
        self.progress_bar_cam.setObjectName(u"progress_bar_cam")
        self.progress_bar_cam.setMinimumSize(QSize(0, 20))
        self.progress_bar_cam.setMaximumSize(QSize(16777215, 20))
        self.progress_bar_cam.setStyleSheet(u"QProgressBar{\n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(253, 143, 134);\n"
"text-align:center;\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgba(215, 215, 215,100);\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"border-radius:0px;\n"
"background: rgba(119, 111, 252, 200);\n"
"border-radius: 7px;\n"
"}")
        self.progress_bar_cam.setMaximum(1000)
        self.progress_bar_cam.setValue(0)

        self.horizontalLayout_20.addWidget(self.progress_bar_cam)

        self.stop_button_cam = QPushButton(self.Pause_QF_cam)
        self.stop_button_cam.setObjectName(u"stop_button_cam")
        self.stop_button_cam.setMinimumSize(QSize(0, 30))
        self.stop_button_cam.setMaximumSize(QSize(16777215, 30))
        self.stop_button_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stop_button_cam.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/stop.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")

        self.horizontalLayout_20.addWidget(self.stop_button_cam)


        self.main_content_cam.addWidget(self.Pause_QF_cam)


        self.horizontalLayout_24.addLayout(self.main_content_cam)

        self.prm_page_cam = QFrame(self.home)
        self.prm_page_cam.setObjectName(u"prm_page_cam")
        self.prm_page_cam.setMinimumSize(QSize(0, 0))
        self.prm_page_cam.setMaximumSize(QSize(0, 16777215))
        self.prm_page_cam.setStyleSheet(u"QFrame#prm_page_cam{\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(0, 0, 100),  stop:1 rgb(10, 50, 200));\n"
"border-top-left-radius:30px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"}")
        self.prm_page_cam.setFrameShape(QFrame.Shape.StyledPanel)
        self.prm_page_cam.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.prm_page_cam)
        self.verticalLayout_31.setSpacing(15)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(15, 15, -1, -1)
        self.label_cam = QLabel(self.prm_page_cam)
        self.label_cam.setObjectName(u"label_cam")
        self.label_cam.setStyleSheet(u"padding-left: 0px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 240);\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_cam.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_cam)

        self.Model_QF_cam_2 = QWidget(self.prm_page_cam)
        self.Model_QF_cam_2.setObjectName(u"Model_QF_cam_2")
        self.Model_QF_cam_2.setMinimumSize(QSize(190, 90))
        self.Model_QF_cam_2.setMaximumSize(QSize(190, 90))
        self.Model_QF_cam_2.setStyleSheet(u"QWidget#Model_QF_cam_2{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_32 = QVBoxLayout(self.Model_QF_cam_2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_10 = QPushButton(self.Model_QF_cam_2)
        self.ToggleBotton_10.setObjectName(u"ToggleBotton_10")
        sizePolicy.setHeightForWidth(self.ToggleBotton_10.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_10.setSizePolicy(sizePolicy)
        self.ToggleBotton_10.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_10.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Nirmala UI"])
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setItalic(False)
        self.ToggleBotton_10.setFont(font3)
        self.ToggleBotton_10.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ToggleBotton_10.setMouseTracking(True)
        self.ToggleBotton_10.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_10.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_10.setAutoFillBackground(False)
        self.ToggleBotton_10.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/model.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_10.setIcon(icon)
        self.ToggleBotton_10.setAutoDefault(False)
        self.ToggleBotton_10.setFlat(False)

        self.verticalLayout_32.addWidget(self.ToggleBotton_10)

        self.model_box_cam = QComboBox(self.Model_QF_cam_2)
        self.model_box_cam.setObjectName(u"model_box_cam")
        self.model_box_cam.setMinimumSize(QSize(170, 20))
        self.model_box_cam.setMaximumSize(QSize(170, 20))
        self.model_box_cam.setStyleSheet(u"\n"
"QComboBox {\n"
"            background-color: rgba(255,255,255,90);\n"
"			color: rgba(0, 0, 0, 200);\n"
"			font: 600 9pt \"Segoe UI\";\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 10px;\n"
"            padding-left: 15px;\n"
"        }\n"
"\n"
"        QComboBox:on {\n"
"            border: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
"            width: 22px;\n"
"            border-left: 1px solid lightgray;\n"
"            border-top-right-radius: 15px;\n"
"            border-bottom-right-radius: 15px;\n"
"        }\n"
"\n"
"        QComboBox::drop-down:on {\n"
"            border-left: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            width: 16px;\n"
"            height: 16px;\n"
"            image: url(:/all/img/box_down.png);\n"
"        }\n"
"\n"
"        QComboBox::down-arrow:on {\n"
"            image: url(:/all/img/box_up.png);\n"
"        }\n"
"\n"
"        QComboBox QAbstractItemView {\n"
"  "
                        "          border: none;\n"
"            outline: none;\n"
"			padding: 10px;\n"
"            background-color: rgb(223, 188, 220);\n"
"        }\n"
"\n"
"\n"
"        QComboBox QScrollBar:vertical {\n"
"            width: 2px;\n"
"           background-color: rgba(255,255,255,150);\n"
"        }\n"
"\n"
"        QComboBox QScrollBar::handle:vertical {\n"
"            background-color: rgba(255,255,255,90);\n"
"        }")
        self.model_box_cam.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.model_box_cam.setMinimumContentsLength(0)

        self.verticalLayout_32.addWidget(self.model_box_cam)


        self.verticalLayout_31.addWidget(self.Model_QF_cam_2)

        self.IOU_QF_cam = QFrame(self.prm_page_cam)
        self.IOU_QF_cam.setObjectName(u"IOU_QF_cam")
        self.IOU_QF_cam.setMinimumSize(QSize(190, 90))
        self.IOU_QF_cam.setMaximumSize(QSize(190, 90))
        self.IOU_QF_cam.setStyleSheet(u"QFrame#IOU_QF_cam{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.IOU_QF_cam)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.ToggleBotton_9 = QPushButton(self.IOU_QF_cam)
        self.ToggleBotton_9.setObjectName(u"ToggleBotton_9")
        sizePolicy.setHeightForWidth(self.ToggleBotton_9.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_9.setSizePolicy(sizePolicy)
        self.ToggleBotton_9.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_9.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_9.setFont(font3)
        self.ToggleBotton_9.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ToggleBotton_9.setMouseTracking(True)
        self.ToggleBotton_9.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_9.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_9.setAutoFillBackground(False)
        self.ToggleBotton_9.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/IOU.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_9.setIcon(icon)
        self.ToggleBotton_9.setAutoDefault(False)
        self.ToggleBotton_9.setFlat(False)

        self.verticalLayout_33.addWidget(self.ToggleBotton_9)

        self.frame_4 = QFrame(self.IOU_QF_cam)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(0, 20))
        self.frame_4.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_21 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(8, 0, 10, 0)
        self.iou_spinbox_cam = QDoubleSpinBox(self.frame_4)
        self.iou_spinbox_cam.setObjectName(u"iou_spinbox_cam")
        self.iou_spinbox_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.iou_spinbox_cam.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.iou_spinbox_cam.setMinimum(0.010000000000000)
        self.iou_spinbox_cam.setMaximum(1.000000000000000)
        self.iou_spinbox_cam.setSingleStep(0.050000000000000)
        self.iou_spinbox_cam.setValue(0.450000000000000)

        self.horizontalLayout_21.addWidget(self.iou_spinbox_cam)

        self.iou_slider_cam = QSlider(self.frame_4)
        self.iou_slider_cam.setObjectName(u"iou_slider_cam")
        self.iou_slider_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.iou_slider_cam.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.iou_slider_cam.setMinimum(1)
        self.iou_slider_cam.setMaximum(100)
        self.iou_slider_cam.setValue(45)
        self.iou_slider_cam.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_21.addWidget(self.iou_slider_cam)


        self.verticalLayout_33.addWidget(self.frame_4)


        self.verticalLayout_31.addWidget(self.IOU_QF_cam)

        self.Conf_QF_cam = QFrame(self.prm_page_cam)
        self.Conf_QF_cam.setObjectName(u"Conf_QF_cam")
        self.Conf_QF_cam.setMinimumSize(QSize(190, 90))
        self.Conf_QF_cam.setMaximumSize(QSize(190, 90))
        self.Conf_QF_cam.setStyleSheet(u"QFrame#Conf_QF_cam{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_34 = QVBoxLayout(self.Conf_QF_cam)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.ToggleBotton_7 = QPushButton(self.Conf_QF_cam)
        self.ToggleBotton_7.setObjectName(u"ToggleBotton_7")
        sizePolicy.setHeightForWidth(self.ToggleBotton_7.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_7.setSizePolicy(sizePolicy)
        self.ToggleBotton_7.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_7.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_7.setFont(font3)
        self.ToggleBotton_7.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ToggleBotton_7.setMouseTracking(True)
        self.ToggleBotton_7.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_7.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_7.setAutoFillBackground(False)
        self.ToggleBotton_7.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/conf.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_7.setIcon(icon)
        self.ToggleBotton_7.setAutoDefault(False)
        self.ToggleBotton_7.setFlat(False)

        self.verticalLayout_34.addWidget(self.ToggleBotton_7)

        self.frame_5 = QFrame(self.Conf_QF_cam)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(0, 20))
        self.frame_5.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_22 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(8, 0, 10, 0)
        self.conf_spinbox_cam = QDoubleSpinBox(self.frame_5)
        self.conf_spinbox_cam.setObjectName(u"conf_spinbox_cam")
        self.conf_spinbox_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.conf_spinbox_cam.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.conf_spinbox_cam.setMinimum(0.010000000000000)
        self.conf_spinbox_cam.setMaximum(1.000000000000000)
        self.conf_spinbox_cam.setSingleStep(0.050000000000000)
        self.conf_spinbox_cam.setValue(0.250000000000000)

        self.horizontalLayout_22.addWidget(self.conf_spinbox_cam)

        self.conf_slider_cam = QSlider(self.frame_5)
        self.conf_slider_cam.setObjectName(u"conf_slider_cam")
        self.conf_slider_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.conf_slider_cam.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.conf_slider_cam.setMinimum(1)
        self.conf_slider_cam.setMaximum(100)
        self.conf_slider_cam.setValue(25)
        self.conf_slider_cam.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_22.addWidget(self.conf_slider_cam)


        self.verticalLayout_34.addWidget(self.frame_5)


        self.verticalLayout_31.addWidget(self.Conf_QF_cam)

        self.Delay_QF_cam = QFrame(self.prm_page_cam)
        self.Delay_QF_cam.setObjectName(u"Delay_QF_cam")
        self.Delay_QF_cam.setMinimumSize(QSize(190, 90))
        self.Delay_QF_cam.setMaximumSize(QSize(190, 90))
        self.Delay_QF_cam.setStyleSheet(u"QFrame#Delay_QF_cam{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_35 = QVBoxLayout(self.Delay_QF_cam)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.ToggleBotton_8 = QPushButton(self.Delay_QF_cam)
        self.ToggleBotton_8.setObjectName(u"ToggleBotton_8")
        sizePolicy.setHeightForWidth(self.ToggleBotton_8.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_8.setSizePolicy(sizePolicy)
        self.ToggleBotton_8.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_8.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_8.setFont(font3)
        self.ToggleBotton_8.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ToggleBotton_8.setMouseTracking(True)
        self.ToggleBotton_8.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_8.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_8.setAutoFillBackground(False)
        self.ToggleBotton_8.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/delay.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_8.setIcon(icon)
        self.ToggleBotton_8.setAutoDefault(False)
        self.ToggleBotton_8.setFlat(False)

        self.verticalLayout_35.addWidget(self.ToggleBotton_8)

        self.frame_6 = QFrame(self.Delay_QF_cam)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(0, 20))
        self.frame_6.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_23 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(8, 0, 10, 0)
        self.speed_spinbox_cam = QSpinBox(self.frame_6)
        self.speed_spinbox_cam.setObjectName(u"speed_spinbox_cam")
        self.speed_spinbox_cam.setStyleSheet(u"QSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.speed_spinbox_cam.setMaximum(50)
        self.speed_spinbox_cam.setValue(10)

        self.horizontalLayout_23.addWidget(self.speed_spinbox_cam)

        self.speed_slider_cam = QSlider(self.frame_6)
        self.speed_slider_cam.setObjectName(u"speed_slider_cam")
        self.speed_slider_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.speed_slider_cam.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(253, 139, 133),  stop:1 rgb(248, 194, 152));\n"
"border-radius: 5px;\n"
"}")
        self.speed_slider_cam.setMaximum(50)
        self.speed_slider_cam.setValue(10)
        self.speed_slider_cam.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_23.addWidget(self.speed_slider_cam)


        self.verticalLayout_35.addWidget(self.frame_6)


        self.verticalLayout_31.addWidget(self.Delay_QF_cam)

        self.Save_QF_cam = QFrame(self.prm_page_cam)
        self.Save_QF_cam.setObjectName(u"Save_QF_cam")
        self.Save_QF_cam.setMinimumSize(QSize(190, 120))
        self.Save_QF_cam.setMaximumSize(QSize(190, 120))
        self.Save_QF_cam.setStyleSheet(u"QFrame#Save_QF_cam{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_36 = QVBoxLayout(self.Save_QF_cam)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_11 = QPushButton(self.Save_QF_cam)
        self.ToggleBotton_11.setObjectName(u"ToggleBotton_11")
        sizePolicy.setHeightForWidth(self.ToggleBotton_11.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_11.setSizePolicy(sizePolicy)
        self.ToggleBotton_11.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_11.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_11.setFont(font3)
        self.ToggleBotton_11.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ToggleBotton_11.setMouseTracking(True)
        self.ToggleBotton_11.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.ToggleBotton_11.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ToggleBotton_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ToggleBotton_11.setAutoFillBackground(False)
        self.ToggleBotton_11.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/save.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_11.setIcon(icon)
        self.ToggleBotton_11.setAutoDefault(False)
        self.ToggleBotton_11.setFlat(False)

        self.verticalLayout_36.addWidget(self.ToggleBotton_11)

        self.save_res_button_cam = QCheckBox(self.Save_QF_cam)
        self.save_res_button_cam.setObjectName(u"save_res_button_cam")
        self.save_res_button_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_res_button_cam.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_36.addWidget(self.save_res_button_cam)

        self.save_txt_button_cam = QCheckBox(self.Save_QF_cam)
        self.save_txt_button_cam.setObjectName(u"save_txt_button_cam")
        self.save_txt_button_cam.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_txt_button_cam.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_36.addWidget(self.save_txt_button_cam)


        self.verticalLayout_31.addWidget(self.Save_QF_cam)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_3)


        self.horizontalLayout_24.addWidget(self.prm_page_cam)

        self.content.addWidget(self.home)

        self.verticalLayout_6.addWidget(self.content)

        self.below = QFrame(self.ContentBox)
        self.below.setObjectName(u"below")
        self.below.setMinimumSize(QSize(0, 30))
        self.below.setMaximumSize(QSize(16777215, 30))
        self.below.setFrameShape(QFrame.Shape.NoFrame)
        self.below.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.below)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, 2, 0, 4)
        self.status_bar = QLabel(self.below)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"\n"
"color: rgb(245, 248, 252);\n"
"\n"
"padding-left: 10px;\n"
"")

        self.horizontalLayout_13.addWidget(self.status_bar)


        self.verticalLayout_6.addWidget(self.below)

        self.content.raise_()
        self.top.raise_()
        self.below.raise_()

        self.main_qframe.addWidget(self.ContentBox)

        MainWindow.setCentralWidget(self.MainWidget)

        self.retranslateUi(MainWindow)

        self.ToggleBotton.setDefault(False)
        self.content.setCurrentIndex(2)
        self.ToggleBotton_10.setDefault(False)
        self.ToggleBotton_9.setDefault(False)
        self.ToggleBotton_7.setDefault(False)
        self.ToggleBotton_8.setDefault(False)
        self.ToggleBotton_11.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ToggleBotton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u8fb9\u680f", None))
        self.src_file_button.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934", None))
        self.src_cam_button.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934", None))
        self.src_rtsp_button.setText(QCoreApplication.translate("MainWindow", u"RTSP", None))
        self.src_udp_button.setText(QCoreApplication.translate("MainWindow", u"UDP", None))
        self.explain_title.setText(QCoreApplication.translate("MainWindow", u"\u667a\u68c0\u5fae\u94a2\u961f", None))
        self.min_sf.setText("")
        self.max_sf.setText("")
        self.close_button.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u522b\u6570\u91cf", None))
        self.Class_num_cam.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u79d2\u5e27\u6570", None))
        self.fps_label_cam.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u7f3a\u9677\u603b\u6570", None))
        self.Target_num_cam.setText("")
        self.pre_cam.setText("")
        self.res_cam.setText("")
        self.label_crazing.setText(QCoreApplication.translate("MainWindow", u"\u9f9f\u88c2", None))
        self.count_crazing.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_inclusion.setText(QCoreApplication.translate("MainWindow", u"\u5939\u6742", None))
        self.count_inclusion.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_patches.setText(QCoreApplication.translate("MainWindow", u"\u6591\u5757", None))
        self.count_patches.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_pitted.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u8680", None))
        self.count_pitted_surface.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_rolled.setText(QCoreApplication.translate("MainWindow", u"\u6c27\u5316\u76ae", None))
        self.count_rolled_in_scale.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_scratches.setText(QCoreApplication.translate("MainWindow", u"\u5212\u75d5", None))
        self.count_scratches.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.run_button_cam.setText("")
        self.stop_button_cam.setText("")
        self.label_cam.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.ToggleBotton_10.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.model_box_cam.setPlaceholderText("")
        self.ToggleBotton_9.setText(QCoreApplication.translate("MainWindow", u"IoU\u9608\u503c", None))
        self.ToggleBotton_7.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u4fe1\u5ea6\u9608\u503c", None))
        self.ToggleBotton_8.setText(QCoreApplication.translate("MainWindow", u"\u5ef6\u8fdf(ms)", None))
        self.ToggleBotton_11.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.save_res_button_cam.setText(QCoreApplication.translate("MainWindow", u"Save MP4/JPG", None))
        self.save_txt_button_cam.setText(QCoreApplication.translate("MainWindow", u"Save Labels(.txt)", None))
        self.status_bar.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
    # retranslateUi

