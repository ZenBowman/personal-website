import os, sys
import shutil

def process(fn):
    input = open(fn)
    output = open("target/" + fn, "w")
    for line in input.readlines():
        if line.strip().startswith("#"):
            inclusion = line.strip().strip("#")
            includer = open(inclusion)
            output.writelines(includer.readlines())
            includer.close()
        else:
            output.write(line)
            if (not line.strip().startswith("<")):
                output.write("<br/>")
    input.close()
    output.close()

def setup_target():
    if os.path.isdir("target"):
        shutil.rmtree("target")
    os.mkdir("target")
    shutil.copytree("pictures", "target/pictures")

if __name__ == "__main__":
    setup_target()
    for f in os.listdir("."):
        if f.startswith("."):
            continue
        if f.endswith("html"):
            process(f)
        elif f.endswith("css"):
            shutil.copy(f, "target")
