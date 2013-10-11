**********************
Automating 3D printing
**********************

..  code-block:: text

    #!/bin/bash   
   openscad -s $1.stl  $1.scad   
   slic3r --load ~/projects/mechanical/Slic3rConfigs/yellow_abs.INI --gcode-arcs $1.stl   

Next, make this script runnable from the command line using this:

..  code-block:: text

    ln -s full_path_to_oss /usr/local/bin/oss   
