..  _testing-openscad:

################
Testing OpenSCAD
################

..  include::   /references.inc

In this note, we will generate a simple object and test the program to make
sure it will create the output products we need in building a robot.

***************
Output Products
***************

OpenSCAD_ can generate a few different output products from a script. One is a
simple image of the object as viewed from a camera we need to place so it can
"see" the object.

Here is a list of the available output formats:

* `stl` - a file suitable for importing into Google SketchUp
* `dxf` - an industry standard drawing format used by many CAD tools
  `
