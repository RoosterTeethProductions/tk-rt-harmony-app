# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 392)
        self.form_layout = QtGui.QVBoxLayout(Dialog)
        self.header_widget = QtGui.QWidget(Dialog)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_example = QtGui.QLabel(Dialog)
        self.logo_example.setText("")
        self.logo_example.setPixmap(QtGui.QPixmap(":/res/sg_logo.png"))
        self.logo_example.setObjectName("logo_example")
        self.horizontalLayout.addWidget(self.logo_example)
        self.context = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context.sizePolicy().hasHeightForWidth())
        self.context.setSizePolicy(sizePolicy)
        self.context.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.context.setObjectName("context")
        self.horizontalLayout.addWidget(self.context)
        self.header_widget.setLayout(self.horizontalLayout)
        self.form_layout.addWidget(self.header_widget)
        
        self.user_label = QtGui.QLabel(Dialog)
        self.user_label.setSizePolicy(sizePolicy)
        self.context.setAlignment(QtCore.Qt.AlignCenter)
        self.user_label.setObjectName("user_label")
        self.form_layout.addWidget(self.user_label)

        # { Start main body
        self.main_body = QtGui.QWidget(Dialog)
        self.main_body_layout = QtGui.QVBoxLayout(Dialog)
        #   { Start options
        self.options_widget = QtGui.QWidget(Dialog)
        self.options_layout = QtGui.QHBoxLayout(Dialog)

        #       { Start selection options
        self.selection_options_widget = QtGui.QWidget(Dialog)
        self.selection_options_layout = QtGui.QVBoxLayout(Dialog)
        
        self.render_format = QtGui.QComboBox(Dialog)
        self.render_format.addItems([".MOV", ".PNG"])
        self.selection_options_layout.addWidget(self.render_format)

        self.selection_options_widget.setLayout(self.selection_options_layout)
        self.options_layout.addWidget(self.selection_options_widget)
        #       } end selection options

        #       { Start resolution options
        self.resolution_options_widget = QtGui.QWidget(Dialog)
        self.resolution_options_layout = QtGui.QVBoxLayout(Dialog)

        #           { Start resolution x
        self.res_x_widget = QtGui.QWidget(Dialog)
        self.res_x_layout = QtGui.QHBoxLayout(Dialog)
        self.res_x_label = QtGui.QLabel("Resolution X: ")
        self.res_x_edit = QtGui.QLineEdit("1920")
        self.res_x_layout.addWidget(self.res_x_label)
        self.res_x_layout.addWidget(self.res_x_edit)
        self.res_x_widget.setLayout(self.res_x_layout)
        self.resolution_options_layout.addWidget(self.res_x_widget)
        #           } End resolution x

        #           { Start resolution y
        self.res_y_widget = QtGui.QWidget(Dialog)
        self.res_y_layout = QtGui.QHBoxLayout(Dialog)
        self.res_y_label = QtGui.QLabel("Resolution Y: ")
        self.res_y_edit = QtGui.QLineEdit("1080")
        self.res_y_layout.addWidget(self.res_y_label)
        self.res_y_layout.addWidget(self.res_y_edit)
        self.res_y_widget.setLayout(self.res_y_layout)
        self.resolution_options_layout.addWidget(self.res_y_widget)
        #           } End resolution y

        self.resolution_options_widget.setLayout(self.resolution_options_layout)
        self.options_layout.addWidget(self.resolution_options_widget)
        #       } end resolution options

        self.options_widget.setLayout(self.options_layout)
        self.main_body_layout.addWidget(self.options_widget)
        #   } end options
        
        self.main_body.setLayout(self.main_body_layout)
        self.form_layout.addWidget(self.main_body)
        # } end main body

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.context.setText(QtGui.QApplication.translate("Dialog", "Your Current Context: ", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
