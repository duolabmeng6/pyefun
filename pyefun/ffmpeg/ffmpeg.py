#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-06-12 23:33
# @Author : Nuonuo
# @Site : 
# @File : ffmpeg.py
# @Software: PyCharm

'''
ffmeg下载地址
http://www.ffmpeg.org/download.html
'''

import ffmpy3
import datetime
from moviepy.editor import *
import os


def 获取_视频_信息(path):
    data = 运行2(r'ffprobe -i ' + path)
    # Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p, 960x540, 1008 kb/s, 25 fps, 25 tbr, 25k tbn, 50 tbc (default)
    # 第一个流是视频流，编码格式是H264格式(封装格式为AVC1)，每一帧的数据表示为yuv420p，分辨率为960x540，这路流的比特率为1108Kbit/s，帧率为每秒钟25帧。

    # Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 92 kb/s (default)
    # 这行信息表示第二个流是音频流，编码方式为ACC（封装格式为MP4A），并且采用的Profile是LC规格，采样率是44.1KHz，声道是立体声，这路流的比特率92Kbit/s。
    print(data)
    print('*' * 20)
    print('Duration: 持续时间,开始时间,比特率')
    print('Stream  编码格式,每一帧的数据表示,分辨率,这路流的比特率,帧率为每秒钟*帧')
    print('视频:Video 音频:Audio')


def 视频_压缩(path, 音频比特率, 视频比特率, 保存地址):
    '''
    改变码率  比特率
    ffmpeg -i 01.mp4 -b:a 100k -b:v 3000k nnn.mp4
    ffmpeg -i Desktop/1.mov -b:v 1.5M  Desktop/1.mp4
    改变分辨率
    ffmpeg -i Desktop/1.mov -s vga Desktop/1.mp4
    -s vga : 指定分辨率， vga 代表 600*480，也可以换成其他的值
    指定文件大小(不建议使用)
    ffmpeg -i Desktop/吉他.mp4  -fs 15MB  Desktop/output1.mp4
    #fs 20 : 表示文件大小最大值为15MB
    改变帕率
    ffmpeg -i Desktop/吉他.mp4  -r 20  Desktop/output1.mp4
    -r 20：表示帧率设置为 20fps
    ----------------------------
    一般 根据原来视频控制 比率
    '''
    ff = ffmpy3.FFmpeg(
        inputs={path: None},
        outputs={保存地址: f'-b:a {音频比特率}k -b:v {视频比特率}k'}
    )
    # print(ff.cmd)
    ff.run()


def 视频_切片_ts(path, 保存m3u8地址):
    # ffmpeg -i XXX.mp4 -c:v libx264 -c:a copy -f hls XXX.m3u8
    ff = ffmpy3.FFmpeg(
        inputs={path: None},
        outputs={保存m3u8地址: f' -c:v libx264 -c:a copy -f hls'}
    )
    # print(ff.cmd)
    ff.run()


def 视频_截取(path, 截取时间, 结束时间, 保存地址):
    '''
    path:截取视频文件
    截取时间:从第几分钟开始截取 1分钟1:00
    截取时长:需要截取多长时间
    保存地址:保存地址
    ---
    ffmpeg -ss 00:03:00 -i video.mp4 -to 00:02:00 -c copy cut.mp4
    去除片头 ffmpeg -ss 00:03:00 -i video.mp4 -c copy cut.mp4
    '''
    截取时长 = minNums(截取时间, 结束时间)
    ff = ffmpy3.FFmpeg(
        inputs={path: None},
        outputs={保存地址: f' -ss {截取时间} -t {截取时长} '}
    )
    # print(ff.cmd)
    ff.run()


def 视频_截取_快速(path, 截取时间, 截取时长, 保存地址):
    # 不推荐使用  文件大 嗯嗯嗯 视频不太稳  快是快
    ff = ffmpy3.FFmpeg(
        inputs={path: '-ss 截取时间'},
        outputs={保存地址: '-t 截取时长 -c:v copy -c:a copy'}
    )
    # print(ff.cmd)
    ff.run()


def 视频_提取音频(path, 保存地址):
    '音频默认m4a格式'
    # ffmpeg -i 16.mp4 -vn -codec copy out.m4a
    ff = ffmpy3.FFmpeg(
        inputs={path: None},
        outputs={保存地址: ' -vn -codec copy '}
    )
    # print(ff.cmd)
    ff.run()


def 视频_删除音频():
    pass
    '''
    去掉原视频音轨
    E:\anzhuangbao\ffmpeg\bin\ffmpeg -i G:\hi.mp4 -c:v copy -an G:\nosound.mp4
    添加背景音乐
    E:\anzhuangbao\ffmpeg\bin\ffmpeg -i G:\nosound.mp4 -i G:\songs.mp3 -t 7.1 -c y copy G:\output.mp4
    方法2
    合并音频和视频，保留视频原声（此时需要将mp3文件放在前面，MP4文件放在后面）否则会没有背景音乐
    E:\anzhuangbao\ffmpeg\bin\ffmpeg.exe -i G:\songs.mp3 -i G:\hi.mp4  -t 7.1 -y G:\new1.mp4
    -t后面跟时长 -y表示覆盖
    :return:
    '''


def minNums(startTime, endTime):
    '''计算两个时间点之间的分钟数'''
    # 处理格式,加上秒位
    startTime1 = startTime
    endTime1 = endTime
    # 计算分钟数
    startTime2 = datetime.datetime.strptime(startTime1, "%M:%S")
    endTime2 = datetime.datetime.strptime(endTime1, "%M:%S")
    seconds = (endTime2 - startTime2).seconds
    # 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分的和，并没有包含时间差的天数（既是两个时间点不是同一天，失效）
    total_seconds = (endTime2 - startTime2).total_seconds()
    # 来获取准确的时间差，并将时间差转换为秒
    mins = total_seconds / 60
    s = total_seconds % 60

    if mins < 10:
        resu = '0' + str(int(mins))
    else:
        resu = '' + str(int(mins))
    if s < 10:
        resu += ':0' + str(int(s))
    else:
        resu += ':' + str(int(s))
    return resu


def 音频_MP3转WAV(path, 保存地址):
    # ffmpeg -i music.mp3 music.wav
    ff = ffmpy3.FFmpeg(
        inputs={path: None},
        outputs={保存地址: None}
    )
    # print(ff.cmd)
    ff.run()


def 音频_截取(path, 开始时间, 截取时长, 保存地址):
    # ffmpeg -i music.wav -ss 0 -t 37 musicshort.wav
    ff = ffmpy3.FFmpeg(
        inputs={path: None},
        outputs={保存地址: f' -ss {开始时间} -t {截取时长} '}
    )
    ff.run()


def 视频_音频_混合(音频地址, 视频地址, 保存地址):
    # ffmpeg -i musicshort.wav -i movie.avi final_video.avi
    ff = ffmpy3.FFmpeg(
        inputs={音频地址: None},
        outputs={保存地址: f'-i {视频地址} '}
    )
    ff.run()


def 视频_合成(filelist, 保存文件名):
    # file '10.mp4' 先生成txt文件
    # 操作目录默认桌面
    系统.修改当前操作路径(系统.取桌面目录())
    # ffmpeg -f concat -i filelist.txt -c copy out.mp4
    ff = ffmpy3.FFmpeg(
        inputs={None: "-f concat -i"},
        outputs={保存文件名: f' {filelist} -c copy '}
    )
    ff.run()


def 视频_合成多个(合成文件夹, 保存地址):
    # 注意某些视频可能因为分辨率问题影响视频合成

    # 主要是需要moviepy这个库
    # 定义一个数组
    L = []
    # 访问 video 文件夹 (假设视频都放在这里面)
    for root, dirs, files in os.walk(合成文件夹):
        # 遍历所有文件
        # 按文件名排序
        rq = []
        for i in files:
            rq.append(int(i[:-4]))
        rq.sort()
        for file in rq:
            # 如果后缀名为 .mp4
            # if os.path.splitext(file)[1] == '.mp4':
            # 拼接成完整路径
            filePath = os.path.join(root, str(file) + '.mp4')
            # 载入视频
            video = VideoFileClip(filePath)
            # 添加到数组
            L.append(video)
    # 拼接视频
    final_clip = concatenate_videoclips(L)
    # 生成目标视频文件
    final_clip.to_videofile(r"C:\Users\Erin\Desktop\\" + 保存地址, fps=24, remove_temp=False)


def 视频_合成单个(视频1, 视频2, 保存地址):
    系统.修改当前操作路径(系统.取桌面目录())
    # 修改视频帕高度和宽度 后合并
    video = VideoFileClip(视频1)
    video2 = VideoFileClip(视频2).resize(video.size)
    video_new = concatenate_videoclips([video2, video])
    video_new.write_videofile(r"C:\Users\Erin\Desktop\\" + 保存地址)


def 运行2(cmd):
    '运行cmd命令 并返回结果'
    return os.popen(cmd).read()
