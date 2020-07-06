# tubedownloader
A fancy Youtube Video Downloader

## Installation

Install the dependencies via `pip3`:

```bash
pip3 install -r requirements.txt
```

- Install required [ffmpeg](https://ffmpeg.org/download.html) binaries. For [Mac](http://mac-tutorials.net/2019/12/30/step-by-step-ffmpeg-mac-10-15-catalina-installation-easy-guide/).
- Apply [workaround](https://github.com/nficano/pytube/issues/661#issuecomment-650766403) to fix the `cipher` issue.
- For mac users have to execute [Certificates.command](https://github.com/gap-decoder/gapdecoder/issues/16#issuecomment-559572502).

**Tip**: See [pytube](https://github.com/nficano/pytube/blob/master/README.md) to get more information.

## Usage

See help:
```bash
./viddownloader.py --help
usage: viddownloader.py [-h] -u YOUTUBE [-o OUTPUT] [-s SKIP]

optional arguments:
  -h, --help            show this help message and exit
  -u YOUTUBE, --youtube YOUTUBE
                        Youtube URL. Example: 'https://www.youtube.com/watch?v=huTUOek4LgU' (default: None)
  -o OUTPUT, --output OUTPUT
                        Output filename (default: out.mp4)
  -s SKIP, --skip SKIP  Skip existing (default: False)
```

## Example

```bash
./viddownloader.py --youtube 'https://www.youtube.com/watch?v=2STPr1Taaw8' 
```

Output:

```bash
* Title: YouTube
* Author: The B1M
* Desciption: Rising 435 metres from a small site on Manhattan's Billionaire's Row, 111W57 is the thinnest skyscraper ever constructed. For more by The B1M subscribe now - http://ow.ly/GxW7y  

Full story here - https://www.theb1m.com/video/building-the-worlds-thinnest-skyscraper

Go Behind The B1M. Click "JOIN" here - https://bit.ly/2Ru3M6O

The B1M Merch store - https://teespring.com/stores/theb1m

Narrated by Fred Mills. Additional footage and images courtesy of The Dronalist, Max Touhey, JDS Development Group, SHoP Architects, Google Earth, Landmark Preservation Commission, James Durkin, JE Dolci, Michael Young, and Dan Cortese.

For more from The Dronalist visit - https://bit.ly/3dCW0iM

For more from Max Touhey visit - http://www.metouhey.com/

View this video and more at - https://www.TheB1M.com 
Follow us on Twitter - http://www.twitter.com/TheB1M
Like us on Facebook - http://www.facebook.com/TheB1M
Follow us on LinkedIn - https://www.linkedin.com/company/the-b1m-ltd
Follow us on Instagram - http://instagram.com/theb1m/

#construction #architecture #NewYork

We welcome you sharing our content to inspire others, but please be nice and play by our rules: http://www.theb1m.com/guidelines-for-sharing

Our content may only be embedded onto third party websites by arrangement. We have established partnerships with domains to share our content and help it reach a wider audience. If you are interested in partnering with us please contact Enquiries@TheB1M.com.

Ripping and/or editing this video is illegal and will result in legal action. 

© 2020 The B1M Limited
* Is age Restictred?  False
* Views: 734686

Downloading video part:
<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">
Downloading audio part:
<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">


Merging..
ffmpeg version git-2020-06-28-4cfcfb3 Copyright (c) 2000-2020 the FFmpeg developers
  built with Apple clang version 11.0.0 (clang-1100.0.33.8)
  configuration: --enable-gpl --enable-version3 --enable-sdl2 --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libdav1d --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libsrt --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvo-amrwbenc --enable-libmysofa --enable-libspeex --enable-libxvid --enable-libaom --enable-libgsm --enable-appkit --enable-avfoundation --enable-coreimage --enable-audiotoolbox
  libavutil      56. 55.100 / 56. 55.100
  libavcodec     58. 93.100 / 58. 93.100
  libavformat    58. 47.100 / 58. 47.100
  libavdevice    58. 11.100 / 58. 11.100
  libavfilter     7. 86.100 /  7. 86.100
  libswscale      5.  8.100 /  5.  8.100
  libswresample   3.  8.100 /  3.  8.100
  libpostproc    55.  8.100 / 55.  8.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'tmp/audio.mp4':
  Metadata:
    major_brand     : dash
    minor_version   : 0
    compatible_brands: iso6mp41
    creation_time   : 2020-07-01T21:04:52.000000Z
  Duration: 00:06:55.75, start: 0.000000, bitrate: 129 kb/s
    Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 3 kb/s (default)
    Metadata:
      creation_time   : 2020-07-01T21:04:52.000000Z
      handler_name    : ISO Media file produced by Google Inc.
Input #1, mov,mp4,m4a,3gp,3g2,mj2, from 'tmp/video.mp4':
  Metadata:
    major_brand     : dash
    minor_version   : 0
    compatible_brands: iso6avc1mp41
    creation_time   : 2020-07-01T21:25:42.000000Z
  Duration: 00:06:55.70, start: 0.000000, bitrate: 2222 kb/s
    Stream #1:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1920x1080 [SAR 1:1 DAR 16:9], 37 kb/s, 30 fps, 30 tbr, 15360 tbn, 60 tbc (default)
    Metadata:
      creation_time   : 2020-07-01T21:25:42.000000Z
      handler_name    : ISO Media file produced by Google Inc.
File 'out.mp4' already exists. Overwrite? [y/N] y
Stream mapping:
  Stream #0:0 -> #0:0 (aac (native) -> aac (native))
  Stream #1:0 -> #0:1 (h264 (native) -> h264 (libx264))
Press [q] to stop, [?] for help
[libx264 @ 0x7faebf835c00] using SAR=1/1
[libx264 @ 0x7faebf835c00] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2 AVX FMA3 BMI2 AVX2
[libx264 @ 0x7faebf835c00] profile High, level 4.0, 4:2:0, 8-bit
[libx264 @ 0x7faebf835c00] 264 - core 160 - H.264/MPEG-4 AVC codec - Copyleft 2003-2020 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=12 lookahead_threads=2 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=25 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
Output #0, mp4, to 'out.mp4':
  Metadata:
    major_brand     : dash
    minor_version   : 0
    compatible_brands: iso6mp41
    encoder         : Lavf58.47.100
    Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 128 kb/s (default)
    Metadata:
      creation_time   : 2020-07-01T21:04:52.000000Z
      handler_name    : ISO Media file produced by Google Inc.
      encoder         : Lavc58.93.100 aac
    Stream #0:1(und): Video: h264 (libx264) (avc1 / 0x31637661), yuv420p, 1920x1080 [SAR 1:1 DAR 16:9], q=-1--1, 30 fps, 15360 tbn, 30 tbc (default)
    Metadata:
      creation_time   : 2020-07-01T21:25:42.000000Z
      handler_name    : ISO Media file produced by Google Inc.
      encoder         : Lavc58.93.100 libx264
    Side data:
      cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
frame=12471 fps= 41 q=-1.0 Lsize=  167937kB time=00:06:55.75 bitrate=3309.0kbits/s speed=1.36x    
video:160968kB audio:6530kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.261837%
[aac @ 0x7faebf809e00] Qavg: 288.988
[libx264 @ 0x7faebf835c00] frame I:73    Avg QP:18.01  size:173902
[libx264 @ 0x7faebf835c00] frame P:3609  Avg QP:22.02  size: 31795
[libx264 @ 0x7faebf835c00] frame B:8789  Avg QP:25.11  size:  4254
[libx264 @ 0x7faebf835c00] consecutive B-frames:  3.3%  6.5%  5.3% 85.0%
[libx264 @ 0x7faebf835c00] mb I  I16..4: 15.4% 58.4% 26.3%
[libx264 @ 0x7faebf835c00] mb P  I16..4:  3.0%  6.1%  0.4%  P16..4: 33.6% 11.4%  7.0%  0.0%  0.0%    skip:38.5%
[libx264 @ 0x7faebf835c00] mb B  I16..4:  0.3%  0.4%  0.0%  B16..8: 31.3%  1.3%  0.2%  direct: 0.7%  skip:65.8%  L0:44.8% L1:50.6% BI: 4.6%
[libx264 @ 0x7faebf835c00] 8x8 transform intra:61.9% inter:75.3%
[libx264 @ 0x7faebf835c00] coded y,uvDC,uvAC intra: 27.6% 31.3% 4.9% inter: 7.0% 5.7% 0.1%
[libx264 @ 0x7faebf835c00] i16 v,h,dc,p: 33% 35% 10% 22%
[libx264 @ 0x7faebf835c00] i8 v,h,dc,ddl,ddr,vr,hd,vl,hu: 30% 23% 33%  2%  2%  2%  3%  2%  3%
[libx264 @ 0x7faebf835c00] i4 v,h,dc,ddl,ddr,vr,hd,vl,hu: 41% 21% 10%  4%  5%  5%  5%  4%  5%
[libx264 @ 0x7faebf835c00] i8c dc,h,v,p: 59% 22% 16%  3%
[libx264 @ 0x7faebf835c00] Weighted P-Frames: Y:6.1% UV:4.5%
[libx264 @ 0x7faebf835c00] ref P L0: 62.2% 16.9% 16.5%  4.3%  0.1%
[libx264 @ 0x7faebf835c00] ref B L0: 92.0%  6.8%  1.3%
[libx264 @ 0x7faebf835c00] ref B L1: 97.7%  2.3%
[libx264 @ 0x7faebf835c00] kb/s:3172.11


Check out: out.mp4
```

Now, you can open `out.mp4` with your favourite player. And don't forget to rename it!?

**Bonus**: You can find the `audio` file in the `tmp` folder.