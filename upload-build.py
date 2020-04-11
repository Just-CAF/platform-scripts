import os
import subprocess

build_dirs = ['out/target/product/cheeseburger', 'out/target/product/dumpling']

for device_dir in build_dirs:
    newest = ""
    for file in os.listdir(device_dir):
        if file.endswith(".zip"):
            filename = file

    device = device_dir.split('/')[3]
    command = "scp {} rautamak@frs.sourceforge.net:/home/frs/project/just-caf-releases/custom_prerelease/{}".format(device_dir + "/" + filename, device.capitalize())
    subprocess.call(command, shell=True)
