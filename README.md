# comparison_opencv_ffmpeg_get_movie_frame
comparison_opencv_ffmpeg_get_movie_frame

## Installation

* conda install -c mrinaljain17 ffmpeg-python (ffmpegのラッパー)
* conda install -c conda-forge ffmpeg (最新のffmpeg(4.1))

## Documentation

* https://github.com/kkroening/ffmpeg-python/tree/master/examples

## memo

* 動画ファイルからResolve_15.2と同じpngを出力したい.
* cv2.VideoCaptureだと,カラースペースが"yuv420"から変更できないので色ずれ.(Resovle_15_2_rgb.png VS 00118_opencv_rgb.png)
* ffmpeg-pythonを使えば,"rawvideo"でnumpy配列に全フレームを格納できる.
* cv2.imwrite前に,cv2.COLOR_RGB2BGRする必要あり.
* cv2.imwrite時に,[cv2.IMWRITE_PNG_COMPRESSION, 0]を付けないと,Resolve_15.2に対して圧縮率が高すぎる
* Resovle_15_2_rgb.pngが,Resolve_15.2で出力したpng
* 00118_opencv_rgb.pngが,cv2.VideoCaptureで出力したpng
* 118_ffmpeg_rgb.pngが,ffmpeg-pythonで出力したpng
