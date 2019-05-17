doc = FreeCAD.newDocument("Bottom-Tile")
tile = doc.addObject("Part::Box","Tile")
tile.Width = 80.0
tile.Length = 80.0
tile.Height = 5.0

rabbet_locations = [(x,y) for x in [0.0,75.0] for y in [35.0]]
for (i,(x,y)) in enumerate(rabbet_locations):
  r = doc.addObject("Part::Box","Rabbet{0}".format(i+1))
  r.Width = 10.0
  r.Length = 5.0
  r.Height = 3.0
  r.Placement = App.Placement(App.Vector(x,y,5), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
  # c = doc.addObject("Part::Cut","CutR{0}".format(i+1))
  # c.Base = lastCut
  # c.Tool = r
  # lastCut = c

doc.recompute()