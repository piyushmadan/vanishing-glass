# vanishing.py
# Python that controls an ArcGIS webmap

# import essential JS objects
map = JSObject(main_map)
console = JSObject(console)
esri = JSObject(esri)
Point = JSObject(pointmaker)
PictureMarkerSymbol = JSObject(picturemaker)
Graphic = JSObject(graphicmaker)
SpatialReference = JSObject(srmaker)

# re-center map
map.centerAndZoom( [ -71, 42 ], 8 )

# test creating a point, adding a marker

pt = Point( [-71, 42], SpatialReference({ "wkid": 4326 } ) )
console.log(pt)

symbol = PictureMarkerSymbol( "marker.png", 40, 40 )
console.log(symbol)

gr = Graphic( pt, symbol )
console.log(gr)

map.graphics.add( gr )

# test output to console
console.log( map )