import os

images = os.listdir("./paintings")
imageNames = [each.split(".")[0] for each in images]

cwd = os.getcwd()
for (index, imageName) in enumerate(imageNames):
    os.system(
        f"~/Downloads/libwebp-0.4.1-mac-10.8/bin/cwebp -q 80 {cwd}/paintings/{images[index]} -o {cwd}/paintingswebp/{imageName}.webp"
    )
