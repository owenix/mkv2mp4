import subprocess, os, sys

FFMPEG_PATH = '/usr/bin/ffmpeg'

def process():
    cwd = os.getcwd()
 
    # get a list of files that have the extension mkv
    filelist = filter(
        lambda f: f.split('.')[-1] == 'mkv', 
        os.listdir(cwd)
    )
 
    # encode each file
    for file in filelist:
        encode(file)

def encode(file):
	name = ''.join(file.split('.')[:-1])
	
	output = '{}.mp4'.format(name)

	subprocess.call([FFMPEG_PATH, '-i', file, '-vcodec', 'copy', 
		'-acodec', 'copy', output])

if __name__ == "__main__":
		process()
				
