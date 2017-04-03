# BoundingBox
This plugin returns the xmin, ymin, xmax ,ymax of the current view window in Qgis
Coppy the folder "BoundingBox" to C:\Users\[USERNAME]\.qgis2\python\plugins and the plugin will be available in Qgis. 

Developers of web services often need to test calls in which a bounding box is nescesary. The goal of this plugin is to (with one click) provide the bouning box of the current view window. which you can coppy for your tests. 

Note that, in this plugin, the order will be xmin, ymin, xmax, ymax. This corresponds to the gml simple features point geometry encoding. But depending on the EPSG code your might need ymin, xmin, ymax, xmax in your tests. 

This plugin was created using Plugin Builder, Qt Creator and python. 
For more information, see the PyQGIS Developer Cookbook at:
http://www.qgis.org/pyqgis-cookbook/index.html

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.