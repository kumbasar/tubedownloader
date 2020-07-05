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

Example:

```bash
./viddownloader.py --youtube 'http://youtube.com/watch?v=9bZkp7q19f0'
```

Output example:

```bash
Downloading video part:
<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">
Downloading audio part:
<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
Merging
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
    creation_time   : 2020-01-13T16:32:54.000000Z
  Duration: 00:04:12.26, start: 0.000000, bitrate: 129 kb/s
    Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 5 kb/s (default)
    Metadata:
      creation_time   : 2020-01-13T16:32:54.000000Z
      handler_name    : ISO Media file produced by Google Inc.
Input #1, mov,mp4,m4a,3gp,3g2,mj2, from 'tmp/video.mp4':
  Metadata:
    major_brand     : dash
    minor_version   : 0
    compatible_brands: iso6avc1mp41
    creation_time   : 2020-01-13T16:46:24.000000Z
  Duration: 00:04:12.17, start: 0.000000, bitrate: 3283 kb/s
    Stream #1:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1920x1080 [SAR 1:1 DAR 16:9], 15 kb/s, 23.98 fps, 23.98 tbr, 24k tbn, 47.95 tbc (default)
    Metadata:
      creation_time   : 2020-01-13T16:46:24.000000Z
      handler_name    : ISO Media file produced by Google Inc.
File 'out.mp4' already exists. Overwrite? [y/N] y
Stream mapping:
  Stream #0:0 -> #0:0 (aac (native) -> aac (native))
  Stream #1:0 -> #0:1 (h264 (native) -> h264 (libx264))
Press [q] to stop, [?] for help
[libx264 @ 0x7fd495809a00] using SAR=1/1
[libx264 @ 0x7fd495809a00] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2 AVX FMA3 BMI2 AVX2
[libx264 @ 0x7fd495809a00] profile High, level 4.0, 4:2:0, 8-bit
[libx264 @ 0x7fd495809a00] 264 - core 160 - H.264/MPEG-4 AVC codec - Copyleft 2003-2020 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=12 lookahead_threads=2 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=23 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
Output #0, mp4, to 'out.mp4':
  Metadata:
    major_brand     : dash
    minor_version   : 0
    compatible_brands: iso6mp41
    encoder         : Lavf58.47.100
    Stream #0:0(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 128 kb/s (default)
    Metadata:
      creation_time   : 2020-01-13T16:32:54.000000Z
      handler_name    : ISO Media file produced by Google Inc.
      encoder         : Lavc58.93.100 aac
    Stream #0:1(und): Video: h264 (libx264) (avc1 / 0x31637661), yuv420p, 1920x1080 [SAR 1:1 DAR 16:9], q=-1--1, 23.98 fps, 24k tbn, 23.98 tbc (default)
    Metadata:
      creation_time   : 2020-01-13T16:46:24.000000Z
      handler_name    : ISO Media file produced by Google Inc.
      encoder         : Lavc58.93.100 libx264
    Side data:
      cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
frame= 6046 fps= 30 q=-1.0 Lsize=  143680kB time=00:04:12.26 bitrate=4665.9kbits/s speed=1.26x
video:139599kB audio:3907kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.121689%
[aac @ 0x7fd495808800] Qavg: 1219.834
[libx264 @ 0x7fd495809a00] frame I:173   Avg QP:19.87  size: 77797
[libx264 @ 0x7fd495809a00] frame P:3346  Avg QP:23.22  size: 27598
[libx264 @ 0x7fd495809a00] frame B:2527  Avg QP:25.09  size: 14699
[libx264 @ 0x7fd495809a00] consecutive B-frames: 35.2% 20.6% 20.0% 24.2%
[libx264 @ 0x7fd495809a00] mb I  I16..4: 17.9% 75.1%  7.1%
[libx264 @ 0x7fd495809a00] mb P  I16..4:  6.7% 19.9%  1.0%  P16..4: 33.9%  7.0%  2.0%  0.0%  0.0%    skip:29.5%
[libx264 @ 0x7fd495809a00] mb B  I16..4:  1.5%  5.0%  0.4%  B16..8: 30.5%  5.0%  0.8%  direct: 1.8%  skip:55.1%  L0:51.3% L1:43.3% BI: 5.3%
[libx264 @ 0x7fd495809a00] 8x8 transform intra:72.7% inter:87.1%
[libx264 @ 0x7fd495809a00] coded y,uvDC,uvAC intra: 42.4% 49.6% 11.1% inter: 10.0% 12.2% 0.3%
[libx264 @ 0x7fd495809a00] i16 v,h,dc,p: 24% 33%  9% 33%
[libx264 @ 0x7fd495809a00] i8 v,h,dc,ddl,ddr,vr,hd,vl,hu: 27% 23% 21%  4%  5%  5%  6%  5%  5%
[libx264 @ 0x7fd495809a00] i4 v,h,dc,ddl,ddr,vr,hd,vl,hu: 30% 24% 13%  4%  8%  7%  7%  5%  4%
[libx264 @ 0x7fd495809a00] i8c dc,h,v,p: 49% 23% 21%  8%
[libx264 @ 0x7fd495809a00] Weighted P-Frames: Y:1.8% UV:1.6%
[libx264 @ 0x7fd495809a00] ref P L0: 74.0% 14.7%  8.0%  3.2%  0.0%
[libx264 @ 0x7fd495809a00] ref B L0: 90.1%  8.5%  1.4%
[libx264 @ 0x7fd495809a00] ref B L1: 98.5%  1.5%
[libx264 @ 0x7fd495809a00] kb/s:4535.01
Check out: out.mp4
```

Now, you can open `out.mp4` with your favourite player. And don't forget to rename it!?

**Bonus**: You can find the `audio` file in the `tmp` folder.