import os

images = os.listdir("./get_paintings/retrieved_paintings")
imageNames = [each.split(".")[0] for each in images]

cwd = os.getcwd()
for (index, imageName) in enumerate(imageNames):
    if images[index].endswith("webp"):
        continue
    os.system(
        f"~/Downloads/libwebp-0.4.1-mac-10.8/bin/cwebp -q 80 {cwd}/get_paintings/retrieved_paintings/{images[index]} -o {cwd}/paintings/{imageName}.webp"
    )
