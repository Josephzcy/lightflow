import numpy as np
import cv2 as cv
path='C:\Dump_light_stream\OpticalFlow-190705-142119\\1813\\FlowGroundTruth'
path_image_1813='C:\Dump_light_stream\OpticalFlow-190705-142119\out\BaseColor\BaseColor1813.png'
path_image_1801='C:\Dump_light_stream\OpticalFlow-190705-142119\out\BaseColor\BaseColor1801.png'

def get_flow_img_np(in_file, height, width):         # height：y轴长度；width x轴长度
    flow_img = np.fromfile(in_file, np.float32)
    assert len(flow_img.shape) == 1
    assert flow_img.shape[0] == height * width * 2
    flow_img = np.reshape(flow_img, (height, width, 2))
    return flow_img

#读取原图像
src_1813=cv.imread(path_image_1813)
src_1801=cv.imread(path_image_1801)

src_1813_height = src_1813.shape[0]
src_1813_weight = src_1813.shape[1]
src_1813_channels = src_1813.shape[2]
print("weight : %s, height : %s, channel : %s" % (src_1813_height, src_1813_weight, src_1813_channels))

# for row in range(src_1813_height):  # 遍历高
#     for col in range(src_1813_weight):  # 遍历宽
#         for c in range(src_1813_channels):  # 便利通道
#             pv = src_1813[row, col, c]
#             src_1813[row, col, c] = 255 - pv  # 全部像素取反，实现一个反向效果
# cv.imshow("fanxiang", src_1813)



#图片ROI区域截取
src_1813=cv.imread(path_image_1813)
src_1801=cv.imread(path_image_1801)
cv.imshow('input_image_1813', src_1813)
#cropImg = src[350:380, 50:100]                            #截取对应的部分，第一组值对应heigjt,第二组值对应windth
cropImg_1813= src_1813[370:375, 80:85]                     #截取5*5的区域
cropImg_1801= src_1801[370:375, 80:85]                     #截取5*5的区域


#将图片转为灰度图
cropImg_1813_gray = cv.cvtColor(cropImg_1813,cv.COLOR_RGB2GRAY)
cropImg_1801_gray = cv.cvtColor(cropImg_1801,cv.COLOR_RGB2GRAY)
cv.imshow("cropImg_1813_gray",cropImg_1813_gray)
#图像像素值和原图像灰度值
print('下面是1813的像素值')
print(cropImg_1813)
print('下面是1813图像灰度值')
print(cropImg_1813_gray)

print('下面是1801的像素值')
print(cropImg_1801)
print('下面是1801的图像灰度值')
print(cropImg_1801_gray)

#将图片转为灰度图
flow_img=get_flow_img_np(path, 1080, 1920)                  #读取并显示流
Intercept_flow_img = flow_img[370:375, 80:85]               #先取出需要的行和列

print('显示流数据')
print(Intercept_flow_img)
print('取流数据')
print(Intercept_flow_img[0,0])
print(Intercept_flow_img[0,0,0])


# #获取图像的高度和宽度
# cropImg_1813_size=cropImg_1813.shape
# cropImg_1813_size=cropImg_1801.shape
# cropImg_1813_height=cropImg_1813[0]
# cropImg_1813_Width=cropImg_1813[1]
# cropImg_1813_channels=cropImg_1813[2]
#
# cropImg_1801_height=cropImg_1813[0]
# cropImg_1801_Width=cropImg_1813[1]
# cropImg_1801_channels=cropImg_1813[2]
#
# print(type(cropImg_1813_Width))
# print(len(cropImg_1813_Width))
#
# #循环比较
# print('获取每个像素点的每个通道的数值')
# # for row in range(cropImg_1813_height):
# #     for col in range(cropImg_1813_Width):
# #         for c in range(cropImg_1813_channels):
# #               pv = cropImg_1813[row, col, c]
# #               print(pv)
#
#
#
# # for row in range(5):
# #     for col in range(5):
# #         Intercept_flow_img[0,0]
# #          #print(cropImg_1813_gray[row,col])


cv.waitKey(0)





















cv.waitKey(0)











# 取对应的列
# for i in range(870,1400,1):
#         row_flow_img.append(flow_img[i])
# #取对应的行
# for i in row_flow_img:
#         row_flow_img.append(flow_img[i])
#         column_flow_img

