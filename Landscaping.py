import clr
import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
import System
from System import Array
from System.Collections.Generic import *
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

# The inputs to this node will be stored as a list in the IN variables.
doc = DocumentManager.Instance.CurrentDBDocument # Current Document opened
uiapp = DocumentManager.Instance.CurrentUIApplication 
app = uiapp.Application 
uidoc = uiapp.ActiveUIDocument

# Place your code below this line
fec = FilteredElementCollector(doc).WherePasses(AreaFilter()).ToElements() # Area elements array
bbox = [BoundingBoxContainsPointFilter(e.Location.Point) for e in fec] # bounding box filter by point of Area element
fec2 = [FilteredElementCollector(doc).OfClass(FamilyInstance).WherePasses(box).ToElements() for box in bbox] # array of family instances where they match filter


# Assign your output to the OUT variable.
OUT = fec2
