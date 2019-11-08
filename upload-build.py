import os
import subprocess

build_dirs = ['out/target/product/cheeseburger', 'out/target/product/dumpling']
newest = ""

for device_dir in build_dirs:
    for file in os.listdir(device_dir):
        if file.endswith(".zip"):
            filename = file.split("-")
	    newest = file

            if filename[4] > newest:
		newest = filename

    device = device_dir.split('/')[3]
    command = "scp {} rautamak@frs.sourceforge.net:/home/frs/project/just-caf-releases/{}".format(device_dir + "/" + newest, device.capitalize())
    subprocess.call(command, shell=True)
