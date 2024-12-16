# Loop through all objects in the active document
for o in App.ActiveDocument.Objects:
    # Hide objects in the active document based on their label or type
    if o.Label.startswith("LCS_") or "Sketcher::SketchObject" in o.TypeId:
        o.ViewObject.Visibility = False

    # Check if the object is a Link to go through its linked document
    elif "App::Link" in o.TypeId:
        # Access the linked document
        linked_doc = o.LinkedObject.Document
        # Loop through all objects in the linked document
        for linked_o in linked_doc.Objects:
            # Hide linked objects based on their label or type
            if linked_o.Label.startswith("Axis_") or linked_o.Label.startswith("LCS_") or "Sketcher::SketchObject" in linked_o.TypeId:
                linked_o.ViewObject.Visibility = False
