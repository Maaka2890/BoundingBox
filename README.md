# BoundingBox
This plugin returns the xmin, ymin, xmax, ymax of the current view window in Qgis and the GetMap request of the selected WMS.
Coppy the folder "BoundingBox" to C:\Users\[USERNAME]\.qgis2\python\plugins and the plugin will be available in Qgis. 

Developers of web services often need bounding boxes of specific areas during trouble shooting, for test calls or for communication. 
The goal of this plugin is to, with one click, provide the bounding box of the current view window and the GetMap request of the selected WMS. You can copy this for your tests. 
With this plugin you can pan to a new location and press "Get BBOX" to updated the bounding box and GetMap request. Making it the quickest way of getting the needed information. 
No more need for different software, python commands, or copying xmin, ymin etc. one by one. Your bounding box is only 2 clicks away. 

Note that, in this plugin, the order will be xmin, ymin, xmax, ymax. This corresponds to the gml simple features point geometry encoding. Depending on the EPSG code you might need ymin, xmin, ymax, xmax in your tests.

This plugin was created using Plugin Builder, Qt Creator and python. 
For more information, see the PyQGIS Developer Cookbook at:
http://www.qgis.org/pyqgis-cookbook/index.html

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.