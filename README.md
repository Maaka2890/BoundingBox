# BoundingBox
This plugin return the xmin, ymin, xmax ,ymax of the current view window in Qgis

This plugin is still in development!

Developers of web services often need to test calls in which a bounding box is nescesary. The goal of this plugin is to (with one click) provide the bouning box of the current view window. which you can coppy for your tests. 

Note that, in this plugin, the order will be xmin, ymin, xmax, ymax. This corresponds to the gml simple features point geometry encoding. But depending on the EPSG code your might need ymin, xmin, ymax, xmax in your tests. 
