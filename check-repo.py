import subprocess

build_top = "/root/caf10/"

custom_repos = {
    'build/core': 'platform/build/core',
    'build/soong': 'platform/build/soong',
    'external/libunwind_llvm': 'platform/external/libunwind_llvm',
    'hardware/libhardware': 'platform/hardware/libhardware',
    'packages/apps/Settings': 'platform/packages/apps/settings',
    'bionic': 'platform/bionic',
    'external/selinux': 'platform/external/selinux',
    'frameworks/av': 'platform/frameworks/av',
    'system/core': 'platform/system/core',
    'vendor/qcom/opensource/audio-hal/primary-hal': 'platform/hardware/qcom/audio',
    'vendor/qcom/opensource/commonsys/cryptfs_hw': 'platform/vendor/qcom-opensource/cryptfs_hw/',
    'vendor/qcom/opensource/interfaces': 'platform/vendor/qcom-opensource/interfaces/',
    'hardware/qcom/media': 'platform/hardware/qcom/media',
    'frameworks/base': 'platform/frameworks/base',
    'packages/services/telephony': 'platform/packages/services/telephony',
    'vendor/codeaurora/commonsys/telephony': 'platform/vendor/codeaurora/commonsys/telephony',
    'frameworks/opt/telephony': 'platform/frameworks/opt/telephony',
    'frameworks/opt/net/wifi': 'platform/frameworks/opt/net/wifi',
    'vendor/qcom/opensource/audio-hal/primary-hal': 'platform/hardware/qcom/audio',
    'hardware/qcom/media': 'platform/hardware/qcom/media',
    'packages/apps/Messaging': 'platform/packages/apps/Messaging'
}

for path, repo in custom_repos.items():
    print("repo:", path)
    full_path = "{}{}".format(build_top, path)
    print subprocess.call("git status", shell=True, cwd=full_path)
    raw_input("Press Enter to continue...")
    print("")
