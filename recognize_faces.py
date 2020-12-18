import face_recognition
import os

# 本项目https://github.com/ageitgey/face_recognition是世界上最简洁的人脸识别库，你可以使用Python和命令行工具提取、识别、操作人脸。
# 本项目的人脸识别是基于业内领先的C++开源库 dlib中的深度学习模型，用Labeled Faces in the Wild人脸数据集进行测试，有高达99.38%的准确率。
# 但对小孩和亚洲人脸的识别准确率尚待提升
# 默认的容错率是0.6，容错率越低，识别越严格准确


# 已知的人脸库
know_face_dir = "know_faces"
know_faces_names = []
know_faces = []
imageNames = os.listdir(know_face_dir)
for imageName in imageNames:
    image = face_recognition.load_image_file(know_face_dir+"/"+imageName)
    image_encoding = face_recognition.face_encodings(image)[0]
    know_faces.append(image_encoding)
    know_faces_names.append(imageName)

# 待识别的人脸
unknow_face_dir = "unknow_faces"
unknow_imageNames = os.listdir(unknow_face_dir)
for unknow_imageName in unknow_imageNames:
    unknow_image = face_recognition.load_image_file(unknow_face_dir+"/"+unknow_imageName)
    unknow_image_encoding = face_recognition.face_encodings(unknow_image)[0]
    # 从已知的人脸库中识别当前图片，容错率设置为0.5
    results = face_recognition.compare_faces(know_faces, unknow_image_encoding, 0.5)
    print(unknow_imageName+":")
    for index in range(len(results)):
        # 打印匹配的人脸
        if results[index] == True:
            print(know_faces_names[index])