#!/usr/bin/env python3
import os

# Check if QNMData/ exists
if not os.path.exists("QNMData"):
    os.makedirs("QNMData")

URLs = {
    2: "https://github.com/jredondoyuste/MathematicaQNM/blob/main/l2.zip"
}    

# Download the files from the URLs, unzip, paste in QNMData/ and delete the .zip
for l in URLs:
    if not os.path.exists("QNMData/l" + str(l)):
        print("Downloading l = " + str(l) + "...")
        os.system("wget " + URLs[l] + " -O l" + str(l) + ".zip")
        os.system("unzip l" + str(l) + ".zip -d QNMData/")
        os.system("rm l" + str(l) + ".zip")
    else:
        print("l = " + str(l) + " already downloaded.")