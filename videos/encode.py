import os

newFiles = []
directory = os.path.dirname(os.path.realpath(__file__))
destinationDirectory = os.path.join(directory, 'encoded')

if not os.path.exists(destinationDirectory):
	os.mkdir(destinationDirectory)

for videofile in os.listdir(directory):
	if videofile.lower().endswith('.mp4'):
		newFiles.append(videofile)

for video in newFiles:
	videoName = os.path.splitext(video)[0]
	newFile = '%s.mp4' % videoName
	i = os.path.join(directory, video)
	o = os.path.join(destinationDirectory, newFile)
	if os.path.isfile(o):
		continue
	encodeCommand = 'ffmpeg -i "%s" -vf scale=-1:480 -c:v libx264 -profile:v baseline -level 3.0 -preset fast -crf 23 -pix_fmt yuv420p "%s"' % (i, o)
	print 'Encoding %s' % video
	encode = os.popen(encodeCommand).read()
