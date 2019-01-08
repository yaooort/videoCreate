# videoCreate
将腾讯视频缓存文件转换为.mp4

> **腾讯视频mac版本下载的视频缓存目录为/Users/oort/Library/Containers/com.tencent.tenvideo/Data/Library/Application Support/Download/video/**

> **将其文件夹下视频文件.dt进行合并为单个MP4文件**

> **使用ffmpeg**

> **可以直接使用该脚本**


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
    execCmd(cmd)
