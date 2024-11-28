include <_constants.scad>
include <_lid.scad>
include <_walls.scad>
include <_legs.scad>

module main(){  
  // For best quality print this part with infill 100%
  translate([0,0,-0.5])
  difference(){
    walls_with_connectors();
    mounting_holes(r_offset=-0.1);
  }
}

main();
