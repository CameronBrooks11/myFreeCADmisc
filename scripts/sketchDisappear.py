# Loop through all objects in the active document
for o in App.ActiveDocument.Objects:
    # Check if the object is a Sketch
    if "Sketcher::SketchObject" in o.TypeId:
        # Hide the object in the active document
        o.ViewObject.Visibility = False
    # Check if the object is a Link
    elif "App::Link" in o.TypeId:
        # Access the linked document
        linked_doc = o.LinkedObject.Document
        # Loop through all objects in the linked document
        for linked_o in linked_doc.Objects:
            # Check if the object is a Sketch
            if "Sketcher::SketchObject" in linked_o.TypeId:
                # Hide the linked object
                linked_o.ViewObject.Visibility = False
