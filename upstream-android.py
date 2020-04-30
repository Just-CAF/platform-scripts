import subprocess
import os

TAG = ""
codeaurora_base = "https://source.codeaurora.org/quic/la"
build_top = os.getcwd() + "/"
upstreamable_tag = 'upstream="caf"'
custom_repos = {}

caf = open("manifest/codeaurora.xml", "r")
for line in caf.readlines():
    if '<default revision="' in line:
        TAG = line.split('"')[1].split("/")[2]
        print("Update to " + TAG)

        break

caf.close()

manifest = open("manifest/default.xml", "r")
for line in manifest.readlines():
    if upstreamable_tag in line:
        name = line.split('"')[1].replace("_", "/")
        path = line.split('"')[3]


        # Handling exceptions..
        if name == "platform/vendor/qcom-opensource/commonsys/cryptfs/hw":
            name = "platform/vendor/qcom-opensource/cryptfs_hw"

        if name == "platform/external/libunwind/llvm":
            name = "platform/external/libunwind_llvm"

        custom_repos[path] = name

manifest.close()

for path, repo in custom_repos.items():
    print("repo: " + path)
    full_path = "{}{}".format(build_top, path)
    subprocess.Popen("git checkout custom 2>/dev/null || git checkout q", shell=True, cwd=full_path)
    print(subprocess.call("git fetch {}/{} refs/tags/{}".format(codeaurora_base, repo, TAG), shell=True, cwd=full_path))
    print(subprocess.call("git merge FETCH_HEAD", shell=True, cwd=full_path))
    print(subprocess.call("git push aosp-caf HEAD", shell=True, cwd=full_path))
    print("")
