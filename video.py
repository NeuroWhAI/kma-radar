import os
from os import walk

list_file = "img_paths.txt"

for (_, _, filenames) in walk("img"):
    with open(list_file, "w") as f:
        f.writelines(map(lambda name: f"file img/{name}\n", filenames))
    break

#imgs_per_second = 12
imgs_per_second = 24
os.popen(f"ffmpeg -y -r {imgs_per_second} -f concat -safe 0 -i {list_file} "\
    "-vf \"yadif,format=yuv420p,scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2\" "\
    "-force_key_frames \"expr:gte(t,n_forced/2)\" -use_editlist 0 -movflags +faststart "\
    "-preset slow -crf 20 -bf 2 -c:v libx264 -b:v 50M out.mp4").read()

os.remove(list_file)
