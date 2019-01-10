import os,sys
import logging
from ffmpy import FFmpeg
from natsort import natsorted

logger = logging.getLogger(__name__)


def hls_dir_to_mp4(in_path_dir, out_path_file):
    """
    将hls文件夹里面分片的视频转化为单个MP4文件
    ffmpeg -i "concat:file001.ts|file002.ts|file003.ts|file004.ts......n.ts" -acodec copy -vcodec copy -absf aac_adtstoasc out.mp4
    :param in_path:
    :param out_path:
    :return:
    """
    # 获取"concat:file001.ts|file002.ts|file003.ts|file004.ts......n.ts"列表参数
    out_files = []
    for dir in natsorted([val for val in os.listdir(in_path_dir) if val.startswith(in_path_dir.split("/")[-1])]):
        dirPath = os.path.join(in_path_dir, dir)
        print(dirPath)

        for root, dirs, files in os.walk(dirPath):
            files = natsorted(files)
            for file in files:
                if os.path.splitext(file)[1] == '.ts':
                    # 拼接成完整路径
                    filePath = os.path.join(root, file)
                    out_files.append(filePath)

    cmd = '|'.join(out_files)
    print(out_files)
    cmd = 'concat:' + "\"" + cmd + "\""
    cmd = 'ffmpeg -i ' + cmd + ' -acodec copy -vcodec copy -absf aac_adtstoasc ' + out_path_file
    print(execCmd(cmd))


def videoCurv():
    """
    转换视频格式
    :return:
    """
    # 转换input.mp4 为 output.avi
    FFmpeg(inputs={in_path: None}, outputs={out_path: None}).run()


def execCmd(cmd):
    """
    执行计算命令时间
    """
    r = os.popen(cmd)
    text = r.read().strip()
    r.close()
    return text


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 3:
        hls_dir_to_mp4(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        hls_dir_to_mp4(sys.argv[1], 'tmp.mp4')
    else:
        print('请输入视频所在目录path')
    # hls_dir_to_mp4(
    #     in_path_dir='/Users/bunny/Library/Containers/com.tencent.tenvideo/Data/Library/Application Support/Download/video/g00208rhr0m.320092.hls',
    #     out_path_file='1.mp4');
