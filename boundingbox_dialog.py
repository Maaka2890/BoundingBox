# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BoundingBoxDialog
                                 A QGIS plugin
 This plugin returns the xmin, ymin, xmax, ymax of the current view window, 
 and the GetMap request of the selected WMS. 
                             -------------------
        begin                : 2017-04-03
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Maaka2890
        email                : kkj_15@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys
import re
from PyQt4 import QtCore, QtGui, uic

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'boundingbox_dialog_base.ui'))


class BoundingBoxDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(BoundingBoxDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.GetBB.clicked.connect(self.CalculateBB)
    def CalculateBB(self):
        xmin=iface.mapCanvas().extent().xMinimum()
        xmax=iface.mapCanvas().extent().xMaximum()
        ymin=iface.mapCanvas().extent().yMinimum()
        ymax=iface.mapCanvas().extent().yMaximum()
        bb1= str(xmin) + ","+str(ymin) + "," +str(xmax) + "," +str(ymax)
        bb=str(bb1)
        self.textOutput.setText(bb)
        layer = iface.activeLayer()
        urlsearch = "<tr><td>GetCapabilitiesUrl</td><td>(.+?)</td>"
        urlresult = re.search(urlsearch, layer.metadata())
        url = urlresult.group(1)
        versionsearch = "<tr><td>WMS Version</td><td>(.+?)</td>"
        versionresult = re.search(versionsearch, layer.metadata())
        version = versionresult.group(1)
        crs = iface.activeLayer().crs().authid()
        crs = re.search('(.*)', crs)
        crs= crs.group(1)
        namesearch = "<tr><td>Name</td><td>(.+?)</td>"
        nameresult = re.search(namesearch, layer.metadata())
        name= nameresult.group(1)
        width=iface.mapCanvas().size().width()
        width=str(width)
        height=iface.mapCanvas().size().height()
        height=str(height)
        formatsearch = "<tr><td>Image Formats</td><td>(.+?)</td>"
        formatresult = re.search(formatsearch, layer.metadata())
        format = formatresult.group(1)
        format = format.split('<')[0]
        getmap= url + "service=WMS&request=GetMap&version="+version +"&BGCOLOR=0xFFFFFF"+"&crs="+crs+"&bbox=" +bb +"&layers=" +name +"&width=" +width +"&height=" +height +"&format=" +format
        self.textOutput_2.setText(getmap)