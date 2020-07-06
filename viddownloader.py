#!/usr/bin/env python3

import ffmpeg
import argparse

from pytube import YouTube

parser = argparse.ArgumentParser(
                    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-u", "--youtube", help = "Youtube URL. Example: 'https://www.youtube.com/watch?v=huTUOek4LgU'", type = str, required= True)
parser.add_argument("-o", "--output", help = "Output filename", type = str, required= False, default='out.mp4')
parser.add_argument("-s", "--skip", help = "Skip existing tmp", type = bool, required= False, default=False)
args = parser.parse_args()

yt = YouTube(args.youtube)

print("Downloading video part:")
print(yt.streams.filter(file_extension='mp4',type="video").order_by('resolution')[-1])
yt.streams.filter(file_extension='mp4',type="video").order_by('resolution')[-1].download( output_path='tmp', filename='video', skip_existing=args.skip)

print("Downloading audio part:")
print(yt.streams.get_audio_only("mp4"))
yt.streams.get_audio_only("mp4").download(output_path='tmp', filename='audio', skip_existing=args.skip)

print("Merging")
video_stream = ffmpeg.input('tmp/video.mp4')
audio_stream = ffmpeg.input('tmp/audio.mp4')
ffmpeg.output(audio_stream, video_stream, args.output).run()

print("Check out: " + args.output)