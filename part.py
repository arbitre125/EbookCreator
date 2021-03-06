#############################################################################
# Copyright (C) 2019 Olaf Japp
#
# This file is part of EbookCreator.
#
#  EbookCreator is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  EbookCreator is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with EbookCreator.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import os
from PyQt5.QtCore import QObject, pyqtProperty


class Part(QObject):

    def __init__(self, parent = None):
        super().__init__(parent)
        self._name = ""
        self._src = ""
        self._pdfOnly = False

    @pyqtProperty('QString')
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @pyqtProperty('QString')
    def src(self):
        return self._src

    @src.setter
    def src(self, src):
        self._src = src

    @pyqtProperty('bool')
    def pdfOnly(self):
        return self._pdfOnly

    @pdfOnly.setter
    def pdfOnly(self, pdfOnly):
        self._pdfOnly = pdfOnly