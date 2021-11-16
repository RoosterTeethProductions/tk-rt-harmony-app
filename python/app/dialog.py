# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from posixpath import normpath
import sgtk
import os
import sys
import threading

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

# standard toolkit logger
logger = sgtk.platform.get_logger(__name__)



def show_dialog(app_instance):
    """
    Shows the main dialog window.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
    app_instance.engine.show_dialog("Playblast Maker", app_instance, AppDialog)


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """

    def __init__(self):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this.
        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - An Sgtk API instance, via self._app.sgtk
        self.dcc_app = sgtk.platform.current_engine().app
        self._app = sgtk.platform.current_bundle()
        self._sg = self._app.shotgun
        self.project = self._app.context.project
        self.user = sgtk.util.get_current_user(sgtk)
        

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        

        # logging happens via a standard toolkit logger
        logger.info("Launching Playblast Maker...")

       

        # lastly, set up our very basic UI
        #self.ui.context.setText("Current Context: %s" % self._app.context)
        #self.ui.user_label.setText("Current User: {}".format(self.user["name"]))
        
        start_frame = self.dcc_app.get_start_frame()
        end_frame = self.dcc_app.get_stop_frame()
        self.ui.start_frame.setText(str(start_frame))
        self.ui.end_frame.setText(str(end_frame))
        self.ui.thumb_frame.setText(str(start_frame))
        self.tasks = self.get_assigned_tasks()
        for task in self.tasks:
            self.ui.task_select.addItem("{} {}".format(task["entity"]["name"], task["content"]))
        self.ui.with_sound.setChecked(True)
        self.ui.send_to_shotgun.setChecked(True)
        self.bind_connections()

    def bind_connections(self):
        #self.ui.render_format.currentTextChanged.connect(self.on_render_format_change)
        self.ui.task_select.currentIndexChanged.connect(self.task_select_changed)
        self.ui.file_dialog.clicked.connect(self.file_dialog_popup)
        self.ui.send_to_shotgun.stateChanged.connect(self.shotgun_selection_changed)
        self.ui.make_playblast_button.clicked.connect(self.make_playblast)
        
    def on_render_format_change(self, text):
        if text == ".MOV":
            self.ui.with_sound.setEnabled(True)
            self.ui.generate_thumbnail.setEnabled(True)
            self.ui.thumb_frame.setEnabled(True)
            self.ui.thumb_frame_label.setEnabled(True)

            self.ui.white_background.setEnabled(False)
        else:
            self.ui.white_background.setEnabled(True)

            self.ui.with_sound.setEnabled(False)
            self.ui.generate_thumbnail.setEnabled(False)
            self.ui.thumb_frame.setEnabled(False)
            self.ui.thumb_frame_label.setEnabled(False)

    def file_dialog_popup(self):
        file_path = QtGui.QFileDialog().getExistingDirectory(None, "Select Folder", "",
                                                             QtGui.QFileDialog.ShowDirsOnly)
        self.ui.save_edit.setText(file_path)

    def get_assigned_tasks(self):
        filters = [["project", 'is', self.project], ["task_assignees", "in", self.user]]
        fields = ["id", "content", "entity", "sg_status_list"]
        results = self._sg.find("Task", filters, fields)
        return results

    def task_select_changed(self):
        #self.ui.save_edit.setText(str(self.tasks[self.ui.task_select.currentIndex()]))
        pass

    def shotgun_selection_changed(self):
        if self.ui.send_to_shotgun.isChecked():
            self.ui.task_select.setEnabled(True)
        else:
            self.ui.task_select.setEnabled(False)

    def make_playblast(self):
        task = self.tasks[self.ui.task_select.currentIndex()]
        self.dcc_app.render_to_quicktime(self.ui.save_edit.text(), self.ui.start_frame.text(),
                                         self.ui.end_frame.text(), self.ui.with_sound.isChecked(),
                                         self.ui.res_x_edit.text(), self.ui.res_y_edit.text(),
                                         self.ui.generate_thumbnail.isChecked(), self.ui.thumb_frame.text())
        #norm_path = os.path.normpath(result)
        version_name = self.dcc_app.current_version_name()
        logger.debug(version_name)
        # if os.path.exists(norm_path) and self.ui.send_to_shotgun.isChecked():
        #     logger.debug("Submitting to Shotgrid")
        #     # upload to sg
        #     data = {
        #         "version_name": os.path.basename(norm_path),
        #         "task": task,
        #         "entity": task["entity"]
        #     }
        #     sg_result = self._sg.create("Version", data)
        #     self._sg.upload("Version", sg_result["id"], result, field_name="sg_uploaded_movie", 
        #                     display_name=os.path.basename(norm_path))

