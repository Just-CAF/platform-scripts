import subprocess

TAG = "LA.UM.8.4.r1-04700-8x98.0"
codeaurora_base = "https://source.codeaurora.org/quic/la"
build_top = "/root/caf10/"
upstreamable_tag = 'upstream="caf"'
custom_repos = {}

f = open("manifest/default.xml", "r")
for line in f.readlines():
    if upstreamable_tag in line:
        name = line.split('"')[1].replace("_", "/")
        path = line.split('"')[3]


        # Handling exceptions..
        if name == "platform/vendor/qcom-opensource/commonsys/cryptfs/hw":
            name = "platform/vendor/qcom-opensource/cryptfs_hw"

        if name == "platform/external/libunwind/llvm":
            name = "platform/external/libunwind_llvm"

        print(codeaurora_base + "/" + name)
        custom_repos[path] = name

for path, repo in custom_repos.items():
    print("repo:", path)
    full_path = "{}{}".format(build_top, path)
    subprocess.Popen("git checkout custom || git checkout q", shell=True, cwd=full_path)
    print subprocess.call("git remote add caf {}/{}".format(codeaurora_base, repo), shell=True, cwd=full_path)
    print subprocess.call("git pull caf refs/tags/{}".format(TAG), shell=True, cwd=full_path)
    print subprocess.call("git push aosp-caf q", shell=True, cwd=full_path)
