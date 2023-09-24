import os
import argparse

parser = argparse.ArgumentParser(description='Video encoding script')
parser.add_argument('-l', '--language', default='eng', help='Language code for audio selection (default: eng)')
args = parser.parse_args()

newFiles = []
directory = os.path.dirname(os.path.realpath(__file__))
destinationDirectory = os.path.join(directory, 'encoded')

if not os.path.exists(destinationDirectory):
    os.mkdir(destinationDirectory)

def isVideo(videofile):
    video_extensions = ['.mp4', '.mkv', '.mov', '.avi']
    return any(videofile.lower().endswith(ext) for ext in video_extensions)

newFiles = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if isVideo(f)]

for filepath in newFiles:
    video = os.path.basename(filepath)
    videoName = os.path.splitext(video)[0]
    newFile = '%s.mp4' % videoName
    i = filepath
    o = os.path.join(destinationDirectory, newFile)
    if os.path.isfile(o):
        continue

    # Use ffprobe to get information about audio streams in the input file
    ffprobe_command = 'ffprobe -v error -select_streams a -show_entries stream=index:stream_tags=language -of csv=p=0 "%s"' % i
    ffprobe_output = os.popen(ffprobe_command).read()

    audio_streams = ffprobe_output.strip().split('\n')
    for line in audio_streams:
        values = line.split(',')
        if len(values) == 2:
            index, tags = values
            if args.language in tags:
                # Encode the video and specify the English audio stream by index
                encodeCommand = 'ffmpeg -i "%s" -vf scale=-2:480 -c:v libx264 -profile:v baseline -level 3.0 -preset fast -crf 23 -pix_fmt yuv420p -map "0:0" -map "0:%s" -c:a copy "%s"' % (i, index, o)
                print('Encoding %s with English audio' % newFile)
                encode = os.popen(encodeCommand).read()
                break  # Break the loop after the first English audio stream is found
    else:
        # If no English audio stream is found, encode without specifying an audio stream
        encodeCommand = 'ffmpeg -i "%s" -vf scale=-2:480 -c:v libx264 -profile:v baseline -level 3.0 -preset fast -crf 23 -pix_fmt yuv420p "%s"' % (i, o)
        print('Encoding %s without specifying audio stream' % newFile)
        encode = os.popen(encodeCommand).read()