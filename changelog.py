from datetime import datetime
import subprocess
import os

BUILD_TOP = "/root/caf10/"
MANIFEST = BUILD_TOP + "manifest/default.xml"
CHANGELOG_FILENAME = BUILD_TOP + "releases/changelog_{}.txt".format(datetime.today().strftime("%Y%m%d_%H%M%S"))

print("Changelog to file {}".format(CHANGELOG_FILENAME))
custom_repos = []

with open(MANIFEST, "r") as manifest:
    m = manifest.readlines()

    for row in m:
        row = row.strip()
        if row.startswith("<project name="):
            custom_repos.append(row.split(" ")[2].split('"')[1])

# Get last changelog to only log changes after it
dates = []
for file in os.listdir(BUILD_TOP + "releases/"):
    if file.startswith("changelog") and file.endswith(".txt"):
        date = (file.split("_")[1] + file.split("_")[2]).split(".")[0]
        dates.append(datetime.strptime(date, "%Y%m%d%H%M%S"))

previous = str(max(dates)).replace(" ", "T")

# Write changelog
changelog_file = open(CHANGELOG_FILENAME, "w+")
for repo in custom_repos:
    full_path = "{}{}".format(BUILD_TOP, repo)
    log = subprocess.Popen("git log --after={} --pretty='format:%h %<(10)%an %s'".format(previous), shell=True, cwd=full_path, stdout=subprocess.PIPE)
    output = log.stdout.read().decode('utf-8')
    if output != "":
        print(output)
        changelog_file.write("{}\n\n{}\n\n".format(repo, output))
