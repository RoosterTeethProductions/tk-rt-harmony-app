# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.


from sgtk.platform import Application
import sgtk


class StgkStarterApp(Application):
    """
    The app entry point. This class is responsible for initializing and tearing down
    the application, handle menu registration etc.
    """

    def init_app(self):
        """
        Called as the application is being initialized
        """

        # first, we use the special import_module command to access the app module
        # that resides inside the python folder in the app. This is where the actual UI
        # and business logic of the app is kept. By using the import_module command,
        # toolkit's code reload mechanism will work properly.
        app_payload = self.import_module("app")

        # now register a *command*, which is normally a menu entry of some kind on a Shotgun
        # menu (but it depends on the engine). The engine will manage this command and
        # whenever the user requests the command, it will call out to the callback.

        # first, set up our callback, calling out to a method inside the app module contained
        # in the python folder of the app
        menu_callback = lambda: app_payload.dialog.show_dialog(self)

        # now register the command with the engine
        self.engine.register_command("Playblast Maker", menu_callback)
        self.engine.register_command("Some other thing", menu_callback)

    @property
    def shotgun(self):
        """
        Subclassing of the shotgun property on the app base class.
        This is a temporary arrangement to be able to time some of the shotgun calls.
        """
        # get the real shotgun from the application base class
        app_shotgun = sgtk.platform.Application.shotgun.fget(self)
        return DebugWrapperShotgun(app_shotgun, self.log_debug)

class DebugWrapperShotgun(object):
    def __init__(self, sg_instance, log_fn):
        self._sg = sg_instance
        self._log_fn = log_fn
        self.config = sg_instance.config

    def find(self, *args, **kwargs):
        self._log_fn("SG API find start: %s %s" % (args, kwargs))
        data = self._sg.find(*args, **kwargs)
        self._log_fn("SG API find end")
        return data

    def find_one(self, *args, **kwargs):
        self._log_fn("SG API find_one start: %s %s" % (args, kwargs))
        data = self._sg.find_one(*args, **kwargs)
        self._log_fn("SG API find_one end")
        return data

    def create(self, *args, **kwargs):
        self._log_fn("SG API create start: %s %s" % (args, kwargs))
        data = self._sg.create(*args, **kwargs)
        self._log_fn("SG API create end")
        return data

    def update(self, *args, **kwargs):
        self._log_fn("SG API update start: %s %s" % (args, kwargs))
        data = self._sg.update(*args, **kwargs)
        self._log_fn("SG API update end")
        return data

    def upload(self, *args, **kwargs):
        self._log_fn("SG API upload start: %s %s" % (args, kwargs))
        data = self._sg.upload(*args, **kwargs)
        self._log_fn("SG API upload end")
        return data

    def insert(self, *args, **kwargs):
        self._log_fn("SG API insert start: %s %s" % (args, kwargs))
        data = self._sg.insert(*args, **kwargs)
        self._log_fn("SG API insert end")
        return data
