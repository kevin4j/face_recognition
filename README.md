参考
https://github.com/ageitgey/face_recognition	人脸识别
https://blog.csdn.net/cgy233/article/details/105521718/ 	  Windows10安装dlib失败的几点原因


1. 本机环境
windows 10
python 3.6.5

2. 在C盘用户下增加pip镜像（阿里云）配置
如：
1）在用户目录C:\Users\guang\  下创建文件夹pip
2）在文件夹pip下创建配置文件pip.ini，内容如下
`[global]`
`index-url = http://mirrors.aliyun.com/pypi/simple/`
`[install]`
`trusted-host=mirrors.aliyun.com`

3. 创建项目
    1）创建项目目录， 如D:\python_workspace\face_recognition
  2）创建项目虚拟环境
    `python -m venv D:\python_workspace\face_recognition\venv`
  
  3）后续的安装都在虚拟环境中操作
    `cd D:\python_workspace\face_recognition\venv\Scripts`
  
4. 升级pip版本
     可以查看pip版本，显示9.0.3
       `pip --version`

     升级pip
       `python -m pip install --upgrade pip`

5. 安装第三方包

     pip install cmake

     pip install boost

6. 使用pip命令安装face_recognition

     `pip install face_recognition`

     会自动安装所依赖的包，如 Click, Pillow, numpy, face-recognition-models, dlib, face-recognition

7.  编写识别程序recognize_faces.py

8.  运行测试

完整说明 http://note.youdao.com/noteshare?id=27996355a4be481fec26bf56e1b8ac79&sub=113A66ACED7A4EE386EFD4DDFAAA0B74

