import sys
import getpass
import os
import shutil

if len(sys.argv) < 2:
    if len(sys.argv) < 3:
        basetexturedir = "textures/"
    else:
        print("Custom argument for base temporary textures folder detected. Setting custom CR mod directory based on it...")
        basetexturedir = sys.argv[2]
    
    username = getpass.getuser()

    if os.name == "nt":
        moddir = "C:/Users/" + username + "/AppData/Local/cosmic-reach/mods/assets/"
    else:
        moddir = "/home/" + username + "/.local/share/cosmic-reach/"
else:
    print("Custom argument detected. Setting custom CR mod directory based on it...")
    moddir = sys.argv[1]

blockdir = moddir + "blocks/"
modeldir = moddir + "models/blocks/"
texturedir = moddir + "textures/blocks/"
print("Mod base directory (enter an argument to change it): " + moddir)
print("Mod block directory: " + blockdir)
print("Mod model directory: " + modeldir)
print("Mod texture directory: " + texturedir)

if not os.path.exists(blockdir):
    os.makedirs(blockdir)
if not os.path.exists(modeldir):
    os.makedirs(modeldir)
if not os.path.exists(texturedir):
    os.makedirs(texturedir)

if os.path.exists("textures"):
    if not os.listdir("textures"): 
        print("Please populate the generated textures folder in the same directory as the program with 16x16 PNG textures and restart the program.")
        sys.exit(1)
else:
    print("The textures folder for the textures to add doesn't exist. \nIt has been created, please populate the generated textures folder in the same directory as the program with 16x16 PNG textures and restart the program.")
    os.makedirs("textures")
    sys.exit(1)

texturelist = os.listdir("textures")
texturelistlen = len(texturelist)
if texturelistlen == 1:
    print(str(texturelistlen) + " texture to add detected.")
else:
    print(str(texturelistlen) + " textures to add detected.")

for i in range(texturelistlen):
    name, ext = os.path.splitext(texturelist[i])
    if ext != ".png":
        print("Invalid file extension for texture " + texturelist[i] + "! Skipping texture...")
    else:
        print("Writing block json for " + texturelist[i])
        f = open(blockdir + name + "_block.json", "w")
        f.write("{\n")
        f.write("\t\"stringId\": \"crbulktexturegen:" + name + "\",\n")
        f.write("\t\"blockStates\": {\n")
        f.write("\t\t\"" + name + "\": {\n")
        f.write("\t\t\t\"modelName\": \"" + name + "_model\",\n")
        f.write("\t\t\t\"generateSlabs\": false\n")
        f.write("\t\t}\n")
        f.write("\t}\n")
        f.write("}\n")
        f.close()

        print("Writing model json for " + texturelist[i])
        f = open(modeldir + name + "_model.json", "w")
        f.write("{\n")
        f.write("\t\"parent\": \"cube\",\n")
        f.write("\t\"textures\": {\n")
        f.write("\t\t\"all\": {\n")
        f.write("\t\t\t\"fileName\": \"" + texturelist[i] + "\"\n")
        f.write("\t\t}\n")
        f.write("\t}\n")
        f.write("}\n")
        f.close()

        print("Copying texture for " + texturelist[i])
        shutil.copyfile("textures/" + texturelist[i], texturedir + texturelist[i])

        print(texturelist[i] + " was added.")
