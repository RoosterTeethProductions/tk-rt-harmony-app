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

        # { Start main body
        self.main_body = QtGui.QWidget(Dialog)
        self.main_body_layout = QtGui.QVBoxLayout(Dialog)
        #   { Start options
        self.options_widget = QtGui.QWidget(Dialog)
        self.options_layout = QtGui.QHBoxLayout(Dialog)

        #       { Start selection options
        self.selection_options_widget = QtGui.QWidget(Dialog)
        self.selection_options_layout = QtGui.QVBoxLayout(Dialog)

        self.options_label = QtGui.QLabel("Render Options")
        self.selection_options_layout.addWidget(self.options_label)
        
        #           { Start start_frame
        self.start_frame_widget = QtGui.QWidget(Dialog)
        self.start_frame_layout = QtGui.QHBoxLayout(Dialog)
        self.start_frame_label = QtGui.QLabel(Dialog)
        self.start_frame_label.setText("Start Frame:")
        self.start_frame = QtGui.QLineEdit("0")
        self.start_frame_layout.addWidget(self.start_frame_label)
        self.start_frame_layout.addWidget(self.start_frame)
        self.start_frame_widget.setLayout(self.start_frame_layout)
        self.selection_options_layout.addWidget(self.start_frame_widget)
        #           } End start_frame

        #           { Start end_frame
        self.end_frame_widget = QtGui.QWidget(Dialog)
        self.end_frame_layout = QtGui.QHBoxLayout(Dialog)
        self.end_frame_label = QtGui.QLabel(Dialog)
        self.end_frame_label.setText("End Frame:")
        self.end_frame = QtGui.QLineEdit("0")
        self.end_frame_layout.addWidget(self.end_frame_label)
        self.end_frame_layout.addWidget(self.end_frame)
        self.end_frame_widget.setLayout(self.end_frame_layout)
        self.selection_options_layout.addWidget(self.end_frame_widget)
        #           } End end_frame

        self.with_sound = QtGui.QCheckBox("With sound", Dialog)
        self.selection_options_layout.addWidget(self.with_sound)
        self.generate_thumbnail = QtGui.QCheckBox("Generate thumbnail", Dialog)
        self.selection_options_layout.addWidget(self.generate_thumbnail)

        #           { Start thumbnail_frame
        self.thumb_frame_widget = QtGui.QWidget(Dialog)
        self.thumb_frame_layout = QtGui.QHBoxLayout(Dialog)
        self.thumb_frame_label = QtGui.QLabel(Dialog)
        self.thumb_frame_label.setText("Thumbnail Frame:")
        self.thumb_frame = QtGui.QLineEdit("0")
        self.thumb_frame_layout.addWidget(self.thumb_frame_label)
        self.thumb_frame_layout.addWidget(self.thumb_frame)
        self.thumb_frame_widget.setLayout(self.thumb_frame_layout)
        self.selection_options_layout.addWidget(self.thumb_frame_widget)
        #           } End thumb_frame

        self.white_background = QtGui.QCheckBox("White background", Dialog)
        self.selection_options_layout.addWidget(self.white_background)

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

        #           { Start shotgun
        self.send_to_shotgun = QtGui.QCheckBox("Send to ShotGrid", Dialog)
        self.task_select = QtGui.QComboBox(Dialog)
        self.resolution_options_layout.addWidget(self.send_to_shotgun)
        self.resolution_options_layout.addWidget(self.task_select)
        self.task_status_widget = QtGui.QWidget(Dialog)
        self.task_status_layout = QtGui.QHBoxLayout(Dialog)
        self.status_label = QtGui.QLabel("Task Status")
        self.task_status_drop = QtGui.QComboBox(Dialog)
        self.task_status_layout.addWidget(self.status_label)
        self.task_status_layout.addWidget(self.task_status_drop)
        self.task_status_widget.setLayout(self.task_status_layout)
        self.resolution_options_layout.addWidget(self.task_status_widget)
        #           } End shotgun

        self.resolution_options_widget.setLayout(self.resolution_options_layout)
        self.options_layout.addWidget(self.resolution_options_widget)
        #       } end resolution options

        self.options_widget.setLayout(self.options_layout)
        self.main_body_layout.addWidget(self.options_widget)
        #   } end options

        self.save_label = QtGui.QLabel("Save Location:")
        self.main_body_layout.addWidget(self.save_label)

        #   { Start save location
        self.save_widget = QtGui.QWidget(Dialog)
        self.save_layout = QtGui.QHBoxLayout(Dialog)
        self.save_edit = QtGui.QLineEdit(Dialog)
        self.file_dialog = QtGui.QPushButton("...")
        self.save_layout.addWidget(self.save_edit)
        self.save_layout.addWidget(self.file_dialog)
        self.save_widget.setLayout(self.save_layout)
        self.main_body_layout.addWidget(self.save_widget)
        #   } end save location

        self.make_playblast_button = QtGui.QPushButton("Make Playblast")
        self.main_body_layout.addWidget(self.make_playblast_button)
        
        self.main_body.setLayout(self.main_body_layout)
        self.form_layout.addWidget(self.main_body)
        # } end main body

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
