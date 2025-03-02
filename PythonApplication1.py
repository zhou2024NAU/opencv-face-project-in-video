import os
import cv2
from PIL import Image
import numpy as np
def getImageAndLabels(path):
    
if-_name_-==__main_-:
#图片路径
path='./data/jm/
#获取图像数组和1d标签数组和姓名
faces,ids=getImageAndLabels(path)
#加载识别器
recognizer=cv2.face.LBPHFaceRecognizer_create()
#训练
recognizer.train(faces,np.array(ids))
#保存文件
recognizer.write('trainer/trainer.yml')
