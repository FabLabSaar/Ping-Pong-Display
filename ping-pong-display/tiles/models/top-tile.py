doc = FreeCAD.newDocument("Top-Tile")
tile = doc.addObject("Part::Box","Tile")
tile.Width = 80.0
tile.Length = 80.0
tile.Height = 3.0

sphere_locations = [(x,y) for x in [20.0,60.0] for y in [20.0,60.0]]
for (i,(x,y)) in enumerate(sphere_locations):
  s = doc.addObject("Part::Sphere","Sphere{0}".format(i+1))
  s.Radius = '19.0 mm'
  s.Placement = App.Placement(App.Vector(x,y,16), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
  c = doc.addObject("Part::Cut","CutS{0}".format(i+1))
  c.Base = tile
  c.Tool = s
  tile = c

rabbet_locations = [(x,y) for x in [0.0,75.0] for y in [35.0]]
for (i,(x,y)) in enumerate(rabbet_locations):
  r = doc.addObject("Part::Box","Rabbet{0}".format(i+1))
  r.Width = 10.0
  r.Length = 5.0
  r.Height = 3.0
  r.Placement = App.Placement(App.Vector(x,y,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
  c = doc.addObject("Part::Cut","CutR{0}".format(i+1))
  c.Base = tile
  c.Tool = r
  tile = c

doc.recompute()
