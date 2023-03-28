#!/usr/bin/env python3
import os

# Check if QNMData/ exists
if not os.path.exists("QNMData"):
    os.makedirs("QNMData")   

if not os.path.exists("tmp"):
    os.makedirs("tmp")

# Unzip, paste in QNMData/ and delete the .zip
for l in [2,3,4,5,6,7]:
    if not os.path.exists("QNMData/l" + str(l)):
        print("Un-compressing l = " + str(l) + "...")
        os.system("unzip -q CompressedData/l" + str(l) + ".zip -d tmp/")
        os.system("rm -r tmp/__MACOSX")
        os.system("mv tmp/* " + "QNMData/l" + str(l))
        # os.system("rm CompressedData/l" + str(l) + ".zip")
    else:
        print("l = " + str(l) + " already downloaded.")
    # os.system("rm -r QNMData/__MACOSX")

# Delete tmp/
os.system("rm -r tmp")