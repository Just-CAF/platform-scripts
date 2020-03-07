import subprocess
import sys
import os

kernel_base     = "https://source.codeaurora.org/quic/la/kernel/msm-4.4"
qcacld_base     = "https://source.codeaurora.org/quic/la/platform/vendor/qcom-opensource/wlan/qcacld-3.0"
fw_api_base     = "https://source.codeaurora.org/quic/la/platform/vendor/qcom-opensource/wlan/fw-api"
qca_wifi_base   = "https://source.codeaurora.org/quic/la/platform/vendor/qcom-opensource/wlan/qca-wifi-host-cmn"

path = "{}/{}".format(os.getcwd(), "kernel/oneplus/msm8998")

def merge_tag(repo, tag):
    staging = repo.split("/")[-1];
    print subprocess.call("git fetch {} refs/tags/{}".format(repo, tag), shell=True, cwd=path)
    msg = subprocess.check_output(["git merge", "--no-commit", "-X", "subtree=drivers/staging/{} FETCH_HEAD".format(staging)],
            shell=True, cwd=path)

    if ("Automatic merge failed" in msg):
        print("MANUAL MERGE NEEDED")
        quit()

    print subprocess.call("git add drivers/staging; git commit -m \"staging: update {} from {}\" ".format(staging, tag),
            shell=True, cwd=path)

# First argument is the CAF-tag
CAF_TAG = sys.argv[1]

merge_tag(qcacld_base, CAF_TAG)
merge_tag(fw_api_base, CAF_TAG)
merge_tag(qca_wifi_base, CAF_TAG)
