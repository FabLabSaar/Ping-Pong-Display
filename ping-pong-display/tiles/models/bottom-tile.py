doc = FreeCAD.newDocument("Bottom-Tile")
tile = doc.addObject("Part::Box","Tile")
tile.Width = 80.0
tile.Length = 80.0
tile.Height = 3.0

chamber_locations = [(x,y) for x in [20.0 - 7.0, 60.0 - 7.0] for y in [3.5]]
for (i,(x,y)) in enumerate(chamber_locations):
  ch = doc.addObject("Part::Box","Chamber{0}".format(i+1))
  ch.Width = 73.0
  ch.Length = 14.0
  ch.Height = 2.0
  ch.Placement.Base = (x,y,1.0)
  c = doc.addObject("Part::Cut","CutCh{0}".format(i+1))
  c.Base = tile
  c.Tool = ch
  tile = c

floor_locations = [(x,y) for x in [20.0 - 6.0, 60.0 - 6.0] for y in [0.0]]
for (i,(x,y)) in enumerate(floor_locations):
  f = doc.addObject("Part::Box","Floor{0}".format(i+1))
  f.Width = 80.0
  f.Length = 12.0
  f.Height = 2.0
  f.Placement.Base = (x,y,1.0)
  c = doc.addObject("Part::Cut","CutF{0}".format(i+1))
  c.Base = tile
  c.Tool = f
  tile = c

tunnel_locations = [(x,y) for x in [0.0] for y in [0.0, 80.0 - 2.5]]
for (i,(x,y)) in enumerate(tunnel_locations):
  t = doc.addObject("Part::Box","Chamber{0}".format(i+1))
  t.Width = 2.5
  t.Length = 80.0
  t.Height = 2.0
  t.Placement.Base = (x,y,1.0)
  c = doc.addObject("Part::Cut","CutT{0}".format(i+1))
  c.Base = tile
  c.Tool = t
  tile = c

nose_locations = [(x,y) for x in [0.0,75.0] for y in [35.0]]
for (i,(x,y)) in enumerate(nose_locations):
  n = doc.addObject("Part::Box","Nose{0}".format(i+1))
  n.Width = 10.0
  n.Length = 5.0
  n.Height = 3.0
  n.Placement.Base = (x,y,3.0)
  f = doc.addObject("Part::MultiFuse","Fusion{0}".format(i))
  f.Shapes = [n, tile]
  tile = f

d = doc.addObject("Part::Cylinder","Cylinder")
d.Radius = 1.5
d.Placement.Base = (40.0, 40.0, 0.0)
c = doc.addObject("Part::Cut","CutD")
c.Base = tile
c.Tool = d
tile = c

doc.recompute()

Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewIsometric()
