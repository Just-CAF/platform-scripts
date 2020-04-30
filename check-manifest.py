from urllib.request import urlopen

TAG = ""

c = open("manifest/codeaurora.xml", "r")
for line in c.readlines():
    if '<default revision="' in line:
        TAG = line.split('"')[1].split("/")[2]
        print("Update to " + TAG)

        break

c.close()


URL = "https://source.codeaurora.org/quic/la/platform/manifest/plain/{}.xml?h=release".format(TAG)
caf = urlopen(URL)

not_found = []

for line in caf.readlines():
    line = line.decode('utf-8')
    if "<project " not in line:
        continue

    name = line.split('name="')[1].split('"')[0]
    path = line.split('path="')

    if len(path) > 1:
        path = path[1].split('"')[0]

    with open("manifest/codeaurora.xml") as our:
        if not name in our.read():
            print(name, " not found in current manifest")
            entry = '<project name="{}" path="{}" />'.format(name, path)
            print(entry)
            print()

caf.close()
