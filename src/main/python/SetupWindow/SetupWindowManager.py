#!/usr/bin/env python
# coding=utf-8

# Copyright (C) 2015 Pâris Quentin

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from com.playonlinux.framework import SetupWizard

class SetupWindowManager(object):

    def __init__(self, wizard):
        """:type : dict[int, SetupWizard] """
        self.managedWindows = {}
        self.wizard = wizard

    def getWindow(self, windowId):
        """
            :param windowId: int
            :rtype: SetupWizard
        """
        return self.managedWindows[windowId]

    def newWindow(self, windowId, title):
        self.managedWindows[windowId] = SetupWizard(title)
        self.managedWindows[windowId].init()
        return self.managedWindows[windowId]

    def closeAll(self):
        for windowId in self.managedWindows:
            self.managedWindows[windowId].close()
