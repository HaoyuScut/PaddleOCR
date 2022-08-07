# -*- coding: utf-8 -*-
#########################批量旋转图片####################
# mv ./* "/home/admin503/why/PaddleOCR/Crop_img/"
import os
from PIL import Image
def rotate_pic():
    input_path = "/home/admin503/why/yolov5-6.0/runs/detect/exp3/crops/device_yellow_v/"
    #input_path = "/home/admin503/why/yolov5-6.0/runs/detect/exp3/crops/wire_white_v/"
    
    output_path = "/home/admin503/why/PaddleOCR/Crop_img/"  # 输出文件夹名�?

    filelist=os.listdir(input_path) #返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序�?

    for img in filelist:
        img_name = os.path.splitext(img)[0]  # 获取不加后缀名的文件�?
        
        img_path = os.path.join(input_path, img)
        print(img_path)  # 打印查看文件�?
        im = Image.open(img_path)
        im = im.convert("RGB")  # 把PNG格式转换成的四通道转成RGB的三通道
        im_rotate = im.rotate(90, expand=1)  # 逆时针旋�?0�?expand=1表示原图直接旋转
        # 判断输出文件夹是否已存在，不存在则创建�?
        folder = os.path.exists(output_path)
        if not folder:
            os.makedirs(output_path)
        # 把旋转后的图片存入输出文件夹
        #im_rotate.save(output_path + '/' + img_name + '_rotated' + '.jpg')
        im_rotate.save(output_path + '/' + img_name + '.jpg')
    print('所有图片均已旋转完毕，并存入输出文件夹')
rotate_pic()

#########################################文件批量重命�?####################################
# import os
# def rename():
#     count=920 #初始文件编号�?
#     path=r"E:\Wire_Project\Data_set\After Rename\Yellow_dataset\yellow" #需要重命名的文件目录，注意目录的写�?
#     # path1 = r"E:\Wire_Project\Data_set\After Rename\Yellow_dataset\label"
#     filelist=os.listdir(path) #返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序�?
#     for files in filelist:  #循环列出文件
#         Olddir=os.path.join(path,files)  #将多个路径组合后返回
#         if os.path.isdir(Olddir): #判断路径是否为目录，isfile判断是否为文�?
#             continue #是的话继�?
#         filename=os.path.splitext(files)[0]  #文件�?
#         filetype=os.path.splitext(files)[1]  #文件后缀
#         Newdir=os.path.join(path,'wire_'+str(count)+filetype)
#         os.rename(Olddir,Newdir)  #重命名文件或目录
#         count+=1   #文件编号�?
# rename()
###########################################################################################

###########################label重命�?最终格�?########################################################
# import os
#
# label_path = r"E:\Wire_Project\Data_set\Four\All\labels"
# label_path_new = r"E:\Wire_Project\Data_set\Four\All\labels_new"
# label_list = os.listdir(label_path)
# count = 0
#
# for label_file in label_list:
#     if label_file.endswith(".txt"):
#         with open(os.path.join(label_path, label_file), "r", encoding="utf-8") as f1, open(
#                 os.path.join(label_path_new, label_file), "w", encoding="utf-8") as f2:
#             for line in f1:
#                 items = line.split(" ")
#                 if items[0] == "0":
#                     items[0] = "1"
#                 elif items[0] == "1":
#                     items[0] = "0"
#                 elif items[0] == "2":
#                     items[0] = "2"
#                 elif items[0] == "3":
#                     items[0] = "4"
#                 elif items[0] == "4":
#                     items[0] = "5"
#
#                 line = " ".join(items)
#                 f2.write(line)
###############################################################################################

###################判断label文件夹和img文件夹的不同文件##################################
# -*- coding: utf-8 -*-
# import os
# def file_name(image_dir,label_dir):
#     jpg_list = []
#     label_list = []
#     for root, dirs, files in os.walk(image_dir):
#         for file in files:
#             jpg_list.append(os.path.splitext(file)[0])
#     for root, dirs, files in os.walk(label_dir):
#         for file in files:
#             label_list.append(os.path.splitext(file)[0])
#     print(len(jpg_list))
#     diff = set(label_list).difference(set(jpg_list))  # 差集，在a中但不在b中的元素
#     for name in diff:
#         print("no jpg", name + ".txt")
#     diff2 = set(jpg_list).difference(set(label_list))  # 差集，在b中但不在a中的元素
#     print(len(diff2))
#     for name in diff2:
#         print("no label", name + ".jpg")
# if __name__ == '__main__':
#     path1 = r"E:\Wire_Project\Data_set\After Rename\Yellow_dataset\yellow"
#     path2 = r"E:\Wire_Project\Data_set\After Rename\Yellow_dataset\labels"
#     file_name(path1,path2)

######################################################################################


####################################xml格式label转txt########################################
# #法一
# import random
# import os
# import argparse
#
#
# # annotations_path and save_txt_path
# def get_opt():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--xml_path', default='D:/shuichi_test/VOC2007/Annotations/',
#                         type=str, help='input xml file ')
#     parser.add_argument('--txt_path', default="D:/shuichi_test/VOC2007/ImageSets/Main/",
#                         type=str, help='output txt file')
#     opt = parser.parse_args()
#     return opt
#
#
# opt = get_opt()
# # xml_path
# xml_file = opt.xml_path
# # save_txt_path
# save_txt_file = opt.txt_path
# # 若save_txt_path不存在，则手动创�?
# if not os.path.exists(save_txt_file):
#     os.makedirs(save_txt_file)
# # 迭代xml_path路径下所有的文件返回包含该目录下所有文件的list(无序)
# total_xml = os.listdir(xml_file)
# # 获取包含所有数据list的长�?
# num = len(total_xml)
# # list的范围，后续用于迭代向txt文件中写入数�?image)
# list_index = range(num)
# # 采集的数据集中训练数据和验证数据的总占�?
# train_val_percent = 1
# # 训练数据的占�?
# train_percent = 0.99
# # 采集的数据集中训练数据和验证数据的数�?
# tv = int(num * train_val_percent)
# # 训练数据的数�?int()向下取整
# tr = int(tv * train_percent)
# # 从总数据中随机抽取训练集和验证集数�?
# train_val = random.sample(list_index, tv)
# # 从训练集和验证集中随机抽取训练集数据
# train = random.sample(train_val, tr)
#
# # 创建train_val.txt,train.txt,test.txt,val.txt
# file_train_vale = open(save_txt_file + 'train_val.txt', 'w')
# file_train = open(save_txt_file + "train.txt", 'w')
# file_test = open(save_txt_file + "test.txt", 'w')
# file_val = open(save_txt_file + "val.txt", 'w')
# # train_val.txt将训练集和验证集数据写入
# # train.txt将训练集数据写入
# # test.txt将测试集数据写入
# # val.txt将验证集数据写入
# for i in list_index:
#     # [:-4]将图片格式去掉，比如.jpg
#     data_name = total_xml[i][:-4] + '\n'
#     # 若该index存在于train_val中，则写�?
#     if i in train_val:
#         file_train_vale.write(data_name)
#         if i in train:
#             file_train.write(data_name)
#         else:
#             file_val.write(data_name)
#     else:
#         file_test.write(data_name)
#
# # 文件流关�?
# file_train_vale.close()
# file_train.close()
# file_test.close()
# file_val.close()
##################################################################################


# #法二
# import os
# import cv2
# import glob
# import random
# #
# train_txt_path = 'train.txt'
# val_txt_path = 'val.txt'
# #全部的txt
# path_imgs = 'your_data_path/*.txt'
# #glob.glob返回所有匹配的文件路径列表�?
# image_list = glob.glob(path_imgs)
# #打乱
# random.shuffle(image_list)
# #这里是划分，我设置的�?.85�?.15  可以根据自己情况划分
# num = len(image_list)
# train_list = image_list[:int(0.85*num)]
# val_list = image_list[int(0.85*num):]
# #写入，CV2的判断语句是因为有些图片CV2无法读取，会返回none，导致报错，所以我们直接跳过这样的图片
# with open(train_txt_path,'w') as f:
#     for line in train_list:
#         jpg_name = line.replace('txt','jpg')
#         img = cv2.imread(jpg_name)
#         if img is not None:
#             f.write(jpg_name + '\n')
# #写入验证�?
# with open(val_txt_path,'w') as f:
#     for line in val_list:
#         jpg_name = line.replace('txt','jpg')
#         img = cv2.imread(jpg_name)
#         if img is not None:
#             f.write(jpg_name + '\n')

# 法三
# 将图片和标注数据按比例切分为 训练集和测试�?
# import shutil
# import random
# import os
#
# # 原始路径
# image_original_path = 'E:/Wire_Project/Data_set/Four/All/images/'
# label_original_path = 'E:/Wire_Project/Data_set/Four/All/labels_new/'
# # 训练集路�?
# train_image_path = 'E:/Wire_Project/Data_set/Four/Divide/train/images/'
# train_label_path = 'E:/Wire_Project/Data_set/Four/Divide/train/labels/'
# # 验证集路�?
# val_image_path = 'E:/Wire_Project/Data_set/Four/Divide/val/images/'
# val_label_path = 'E:/Wire_Project/Data_set/Four/Divide/val/labels/'
# # 测试集路�?
# test_image_path = 'E:/Wire_Project/Data_set/Four/Divide/test/images/'
# test_label_path = 'E:/Wire_Project/Data_set/Four/Divide/test/labels/'
#
# # 数据集划分比例，训练�?5%，验证集15%，测试集15%
# train_percent = 0.7
# val_percent = 0.15
# test_percent = 0.15
#
#
# # 检查文件夹是否存在
# def mkdir():
#     if not os.path.exists(train_image_path):
#         os.makedirs(train_image_path)
#     if not os.path.exists(train_label_path):
#         os.makedirs(train_label_path)
#
#     if not os.path.exists(val_image_path):
#         os.makedirs(val_image_path)
#     if not os.path.exists(val_label_path):
#         os.makedirs(val_label_path)
#
#     if not os.path.exists(test_image_path):
#         os.makedirs(test_image_path)
#     if not os.path.exists(test_label_path):
#         os.makedirs(test_label_path)
#
#
# def main():
#     mkdir()
#
#     total_txt = os.listdir(label_original_path)
#     num_txt = len(total_txt)
#     list_all_txt = range(num_txt)  # 范围 range(0, num)
#
#     num_train = int(num_txt * train_percent)
#     num_val = int(num_txt * val_percent)
#     num_test = num_txt - num_train - num_val
#
#     train = random.sample(list_all_txt, num_train)
#     # train从list_all_txt取出num_train个元�?
#     # 所以list_all_txt列表只剩下了这些元素：val_test
#     val_test = [i for i in list_all_txt if not i in train]
#     # 再从val_test取出num_val个元素，val_test剩下的元素就是test
#     val = random.sample(val_test, num_val)
#     # 检查两个列表元素是否有重合的元�?
#     # set_c = set(val_test) & set(val)
#     # list_c = list(set_c)
#     # print(list_c)
#     # print(len(list_c))
#
#     print("训练集数目：{}, 验证集数目：{},测试集数目：{}".format(len(train), len(val), len(val_test) - len(val)))
#     for i in list_all_txt:
#         name = total_txt[i][:-4]
#
#         srcImage = image_original_path + name + '.jpg'
#         srcLabel = label_original_path + name + '.txt'
#
#         if i in train:
#             dst_train_Image = train_image_path + name + '.jpg'
#             dst_train_Label = train_label_path + name + '.txt'
#             shutil.copyfile(srcImage, dst_train_Image)
#             shutil.copyfile(srcLabel, dst_train_Label)
#         elif i in val:
#             dst_val_Image = val_image_path + name + '.jpg'
#             dst_val_Label = val_label_path + name + '.txt'
#             shutil.copyfile(srcImage, dst_val_Image)
#             shutil.copyfile(srcLabel, dst_val_Label)
#         else:
#             dst_test_Image = test_image_path + name + '.jpg'
#             dst_test_Label = test_label_path + name + '.txt'
#             shutil.copyfile(srcImage, dst_test_Image)
#             shutil.copyfile(srcLabel, dst_test_Label)
#
#
# if __name__ == '__main__':
#     main()



