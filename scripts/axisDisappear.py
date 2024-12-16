# Loop through all objects in the active document
for o in App.ActiveDocument.Objects:
    # Check if the object is a Link
    if "App::Link" in o.TypeId:
        # Access the linked document
        linked_doc = o.LinkedObject.Document
        # Loop through all objects in the linked document
        for linked_o in linked_doc.Objects:
            # Check if the object label starts with "Axis_"
            if linked_o.Label.startswith("Axis_"):
                # Hide the linked object
                linked_o.ViewObject.Visibility = False
