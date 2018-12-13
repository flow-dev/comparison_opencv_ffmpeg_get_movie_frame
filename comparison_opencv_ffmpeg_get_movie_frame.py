
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
comparison_opencv_ffmpeg_get_movie_frame.py
"""

# conda install -c mrinaljain17 ffmpeg-python
# conda install -c conda-forge ffmpeg
# https://github.com/kkroening/ffmpeg-python/tree/master/examples

__author__ = "flow_dev"

import numpy as np
import cv2
import os
#import matplotlib.pyplot as plt
import ffmpeg

def ffmpeg_movie():
    
    FILE_NAME = 'GreenBackCat.mov'
    
    # 動画ファイルの情報を取得
    probe = ffmpeg.probe(FILE_NAME)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    width = int(video_stream['width'])
    height = int(video_stream['height'])
    nb_frames = int(video_stream['nb_frames'])
    #print (video_stream)
    print (nb_frames)

    # ffmpegで読み込み.
    out, _ = (
        ffmpeg
        .input(FILE_NAME)
        .output('pipe:', format='rawvideo', pix_fmt='rgb24')
        .run(capture_stdout=True)
    )
    
    # numpy配列で出力.
    video = (
        np
        .frombuffer(out, np.uint8)
        .reshape([-1, height, width, 3])
    )

    print (video.shape)
    # numpy配列をRGBのpngで書き出し.
    frame_num = (nb_frames - 1)
    video_img = cv2.cvtColor(video[frame_num], cv2.COLOR_RGB2BGR)
    # Resolve同等のpngにするには,[cv2.IMWRITE_PNG_COMPRESSION, 0]で圧縮率を指定.
    cv2.imwrite(str(frame_num) + '_ffmpeg_rgb.png', video_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

def opencv_movie():

    # 動画ファイルの読み込み
    cap = cv2.VideoCapture('GreenBackCat.mov')
    cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)
    print (cap.get(cv2.CAP_PROP_CONVERT_RGB))

    all_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print (all_count,fps)

    # 連番ファイルに展開
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            count_padded = '%05d' % count
            if(count == (all_count -1)):
                # Resolve同等のpngにするには,[cv2.IMWRITE_PNG_COMPRESSION, 0]で圧縮率を指定.
                cv2.imwrite(count_padded + '_opencv_rgb.png', frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])
                print (count_padded)                
            count += 1
        else:
            break

    cap.release()

if __name__ == '__main__':
    opencv_movie()
    ffmpeg_movie()
    # ffmpeg.exe -i .\GreenBackCat.mov -vcodec png image_%03d.png
