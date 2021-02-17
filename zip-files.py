#!/usr/bin/env python
import os
import zipfile

# Compress the folder 'sample-data' creating 'output/example.zip'

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

zipf = zipfile.ZipFile('output/example.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('sample-data/', zipf)
zipf.close()
