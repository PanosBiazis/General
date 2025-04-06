# Computer Vision is a way of teaching intelligenc to machines and making them see things just like humans do.

# OpenCV is a massiv open-sourrce library for the vision , machine learning , and processing of images.
# OpenCV is a Python library which is used for Image and Video Processing.

# #It can process pictures and videos to recognise objects ,faces, or even texts.
# import cv2#OpenCV

# print(cv2.__version__)

# # OpenCV imread() suports different PNG,JPEG etc file formats.
# # This function view a picture in a browser.
# # The window matches the pcture scale automatically.

# # imwrite() function it helps to show a picture is written.

# # image=cv2.imread('C:\Users\panag\Pictures\Screenshots\Screenshot 2024-05-20 102555.png')
# # # Showing the image
# # cv2.imshow('image',image)


# import cv2 as cv

# print(cv.__version__)

# # Raw string to handle backslashes
# image = cv.imread(r'C:\Users\panag\Pictures\Screenshots\Screenshot 2024-05-20 102555.png')
# # Showing the image
# cv.imshow('image', image)
# cv.waitKey(0)  # Wait for a key press to close the window
# cv.destroyAllWindows()

# resized_image=cv.resize(image,(750,1080))
# # Showing the image
# cv.imshow('image', resized_image)

# # Conversion of the image from one color code to another is done using the cvtColor() function

# cv.waitKey(0)  # Wait for a key press to close the window
# cv.destroyAllWindows()

# gray_image=cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)

# cv.imshow('gray image',gray_image)

# cv.waitKey(0)  # Wait for a key press to close the window
# cv.destroyAllWindows()

# import sys

# img=cv.imread(r'F:\panag\Pictures\Saved Pictures\starry_night.jpg')

# if img is None:
#     sys.exit("Could not read the image.")

# cv.imshow("Display window", img)
# k=cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("starry_night.png",img)


# # imread_color
# # imread_grayscale
# # imread_unchanged
# # cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected.
# # cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# # cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
# # cv2.IMREAD_COLOR is the default flag.
# # cv2.IMREAD_GRAYSCALE is used to convert image to grayscale.
# # cv2.IMREAD_UNCHANGED is used to convert image to such including alpha channel.

# import numpy as np

# cap=cv.VideoCapture(0)

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
    
# else:
#     while True:
#     # Capture frame-by-frame
#         ret, frame = cap.read()

#     # If frame is read correctly re is True
#         if not ret:
#             print("Can't receive frame (stream end?). Exiting ...")
#             break
#     # Our operations on the frame come here
#         gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     # Display the resulting frame
#         cv.imshow('frame', gray)

#         if cv.waitKey(1) == ord('q'):
#             break

# # When everything done, release the capture
# cap.release()
# cv.destroyAllWindows()

# # cap.get(propld) where propld is a number from 0 to 18

# # Create a black image

# img=np.zeros((512,512,3),np.uint8)

# # Draw a diagonal blue line with thickness of 5 px
# cv.line(img,(0,0),(511,511),(255,0,0),5)

# # Drawing Rectangle
# cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# # Drawing circle
# cv.circle(img,(447,63), 63, (0,0,255), -1)

# # Display image
# cv.imshow('image',img)

# cv.waitKey(0)

# cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np
# import sys

# print(cv.__version__)

# # Reading and displaying an image using a raw string for the file path
# image_path = r'C:\Users\panag\Pictures\Screenshots\Screenshot 2024-05-20 102555.png'
# image = cv.imread(image_path)

# if image is None:
#     sys.exit(f"Could not read the image from {image_path}")

# cv.imshow('Original Image', image)
# cv.waitKey(0)  # Wait for a key press to close the window
# cv.destroyAllWindows()

# # Resizing the image
# resized_image = cv.resize(image, (750, 1080))
# cv.imshow('Resized Image', resized_image)
# cv.waitKey(0)  # Wait for a key press to close the window
# cv.destroyAllWindows()

# # Converting the image to grayscale
# gray_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray_image)
# cv.waitKey(0)  # Wait for a key press to close the window
# cv.destroyAllWindows()

# # Reading and displaying another image (ensure the file path is correct)
# image_path2 = r'F:\panag\Pictures\Saved Pictures\starry_night.jpg'
# img = cv.imread(image_path2)

# if img is None:
#     sys.exit(f"Could not read the image from {image_path2}")

# cv.imshow("Display window", img)
# k = cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("starry_night.png", img)
# cv.destroyAllWindows()

# # Capturing video from the camera
# cap = cv.VideoCapture(0)

# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# else:
#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         # If frame is read correctly ret is True
#         if not ret:
#             print("Can't receive frame (stream end?). Exiting ...")
#             break

#         # Convert frame to grayscale
#         gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#         # Display the resulting frame
#         cv.imshow('Video Frame', gray)

#         # Break the loop if 'q' key is pressed
#         if cv.waitKey(1) == ord('q'):
#             break

# # When everything done, release the capture and destroy all windows
# cap.release()
# cv.destroyAllWindows()

# # Drawing shapes on an image
# img = np.zeros((512, 512, 3), np.uint8)

# # Draw a diagonal blue line with thickness of 5 px
# cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# # Drawing Rectangle
# cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# # Drawing circle
# cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# # Display image with drawings
# cv.imshow('Drawn Image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np
import sys

print(cv.__version__)

# Reading and displaying an image using a raw string for the file path
image_path =r'/run/media/panos/SAMSUNG T7/panag/Pictures/Saved Pictures/upscayl/images_upscayl.png' #r'C:\Users\panag\Pictures\Screenshots\Screenshot 2024-05-20 102555.png'
image = cv.imread(image_path)

if image is None:
   sys.exit(f"Could not read the image from {image_path}")

cv.imshow('Original Image', image)
cv.waitKey(0)  # Wait for a key press to close the window
cv.destroyAllWindows()

# Resizing the image
resized_image = cv.resize(image, (750, 1080))
cv.imshow('Resized Image', resized_image)
cv.waitKey(0)  # Wait for a key press to close the window
cv.destroyAllWindows()

# Converting the image to grayscale
gray_image = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray_image)
cv.waitKey(0)  # Wait for a key press to close the window
cv.destroyAllWindows()

# Reading and displaying another image (ensure the file path is correct)
image_path2 = r'/run/media/panos/SAMSUNG T7/panag/Pictures/Saved Pictures/starry_night.jpg'
img = cv.imread(image_path2)

if img is None:
  sys.exit(f"Could not read the image from {image_path2}")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_night.png", img)
cv.destroyAllWindows()

# Function to handle mouse events
def mouse_callback(event, x, y, flags, param):
    global capturing
    if event == cv.EVENT_LBUTTONDOWN:
        # Check if the click is within the button area
        if 0 <= x <= 100 and 0 <= y <= 50:
            capturing = False

# Capturing video from the camera
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    sys.exit()

# Create a named window and set mouse callback
cv.namedWindow('Video Frame')
cv.setMouseCallback('Video Frame', mouse_callback)

capturing = True
while capturing:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Draw a button (rectangle) in the top left corner
    cv.rectangle(gray, (0, 0), (100, 50), (255, 255, 255), -1)
    cv.putText(gray, 'STOP', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv.LINE_AA)

    # Display the resulting frame
    cv.imshow('Video Frame', gray)

    # Break the loop if 'q' key is pressed
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture and destroy all windows
cap.release()
cv.destroyAllWindows()

# Drawing shapes on an image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Drawing Rectangle
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# Drawing circle
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Display image with drawings
cv.imshow('Drawn Image', img)
cv.waitKey(0)
cv.destroyAllWindows()


# Accessing ad Modifying pixel values

img=cv.imread(r'/run/media/panos/SAMSUNG T7/panag/Pictures/Saved Pictures/my_image.png')
px=img[100,100]
print(px)

# Access only blue pixel

blue=img[100,100,0]
print(blue)

# Modifying the pixel values in the same way
img[100,100]=[255,255,255]
print(img[100,100])

# Accessing image Properties
print(img.shape)

# Image ROI
# If you want to play with some certain regions of images.
# you can use it for eye detection and face detection

ball=img[280:340,330:390]
img[273:333,100:160] = ball 

# Arithmetic Operations
x=np.uint8([250])
y=np.uint8([10])
print(cv.add(x,y))# 250+10=260 => 255 [[255]]
print(x+y)

# Measurement performance
e1=cv.getTickCount()
print(e1)
# your code execution
e2=cv.getTickCount()
print(e2)
time=(e2-e1)/cv.getTickFrequency()
print(time)

img1=cv.imread(r'/run/media/panos/SAMSUNG T7/panag/Pictures/Saved Pictures/my_image.png')
e1=cv.getTickCount()
for i in range(5,49,2):
    img1=cv.medianBlur(img1,i)
e2=cv.getTickCount()
t=(e2-e1)/cv.getTickFrequency()
print(t)



# For color conversion, use the cv.cvtColor(input_image,flag)

# For BGR, bgr_image = cv.cvtColor(input_image, cv.COLOR_BGR2RGB)

# For BGR GREY conversion, cv.COLOR_BGR2GRAY FOR FLAG

# Similarly for BGR HSV, cv.COLOR_BGR2HSV

# Getting flags
flags=[i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)


# ['COLOR_BAYER_BG2BGR', 'COLOR_BAYER_BG2BGRA', 'COLOR_BAYER_BG2BGR_EA', 'COLOR_BAYER_BG2BGR_VNG', 'COLOR_BAYER_BG2GRAY', 'COLOR_BAYER_BG2RGB', 'COLOR_BAYER_BG2RGBA', 'COLOR_BAYER_BG2RGB_EA', 'COLOR_BAYER_BG2RGB_VNG', 'COLOR_BAYER_BGGR2BGR',
# 'COLOR_BAYER_BGGR2BGRA', 'COLOR_BAYER_BGGR2BGR_EA', 'COLOR_BAYER_BGGR2BGR_VNG', 'COLOR_BAYER_BGGR2GRAY', 'COLOR_BAYER_BGGR2RGB', 'COLOR_BAYER_BGGR2RGBA', 'COLOR_BAYER_BGGR2RGB_EA', 'COLOR_BAYER_BGGR2RGB_VNG', 'COLOR_BAYER_GB2BGR', 'COLOR_BAYER_GB2BGRA',
# 'COLOR_BAYER_GB2BGR_EA', 'COLOR_BAYER_GB2BGR_VNG', 'COLOR_BAYER_GB2GRAY', 'COLOR_BAYER_GB2RGB', 'COLOR_BAYER_GB2RGBA', 'COLOR_BAYER_GB2RGB_EA', 'COLOR_BAYER_GB2RGB_VNG', 'COLOR_BAYER_GBRG2BGR', 'COLOR_BAYER_GBRG2BGRA', 'COLOR_BAYER_GBRG2BGR_EA',
# 'COLOR_BAYER_GBRG2BGR_VNG', 'COLOR_BAYER_GBRG2GRAY', 'COLOR_BAYER_GBRG2RGB', 'COLOR_BAYER_GBRG2RGBA', 'COLOR_BAYER_GBRG2RGB_EA', 'COLOR_BAYER_GBRG2RGB_VNG', 'COLOR_BAYER_GR2BGR', 'COLOR_BAYER_GR2BGRA', 'COLOR_BAYER_GR2BGR_EA', 'COLOR_BAYER_GR2BGR_VNG',
# 'COLOR_BAYER_GR2GRAY', 'COLOR_BAYER_GR2RGB', 'COLOR_BAYER_GR2RGBA', 'COLOR_BAYER_GR2RGB_EA', 'COLOR_BAYER_GR2RGB_VNG', 'COLOR_BAYER_GRBG2BGR', 'COLOR_BAYER_GRBG2BGRA', 'COLOR_BAYER_GRBG2BGR_EA', 'COLOR_BAYER_GRBG2BGR_VNG', 'COLOR_BAYER_GRBG2GRAY',
# 'COLOR_BAYER_GRBG2RGB', 'COLOR_BAYER_GRBG2RGBA', 'COLOR_BAYER_GRBG2RGB_EA', 'COLOR_BAYER_GRBG2RGB_VNG', 'COLOR_BAYER_RG2BGR', 'COLOR_BAYER_RG2BGRA', 'COLOR_BAYER_RG2BGR_EA', 'COLOR_BAYER_RG2BGR_VNG', 'COLOR_BAYER_RG2GRAY', 'COLOR_BAYER_RG2RGB',
# 'COLOR_BAYER_RG2RGBA', 'COLOR_BAYER_RG2RGB_EA', 'COLOR_BAYER_RG2RGB_VNG', 'COLOR_BAYER_RGGB2BGR', 'COLOR_BAYER_RGGB2BGRA', 'COLOR_BAYER_RGGB2BGR_EA', 'COLOR_BAYER_RGGB2BGR_VNG', 'COLOR_BAYER_RGGB2GRAY', 'COLOR_BAYER_RGGB2RGB', 'COLOR_BAYER_RGGB2RGBA',
# 'COLOR_BAYER_RGGB2RGB_EA', 'COLOR_BAYER_RGGB2RGB_VNG', 'COLOR_BGR2BGR555', 'COLOR_BGR2BGR565', 'COLOR_BGR2BGRA', 'COLOR_BGR2GRAY', 'COLOR_BGR2HLS', 'COLOR_BGR2HLS_FULL', 'COLOR_BGR2HSV', 'COLOR_BGR2HSV_FULL',
# 'COLOR_BGR2LAB', 'COLOR_BGR2LUV', 'COLOR_BGR2Lab', 'COLOR_BGR2Luv', 'COLOR_BGR2RGB', 'COLOR_BGR2RGBA', 'COLOR_BGR2XYZ', 'COLOR_BGR2YCR_CB', 'COLOR_BGR2YCrCb', 'COLOR_BGR2YUV',
# 'COLOR_BGR2YUV_I420', 'COLOR_BGR2YUV_IYUV', 'COLOR_BGR2YUV_UYNV', 'COLOR_BGR2YUV_UYVY', 'COLOR_BGR2YUV_Y422', 'COLOR_BGR2YUV_YUNV', 'COLOR_BGR2YUV_YUY2', 'COLOR_BGR2YUV_YUYV', 'COLOR_BGR2YUV_YV12', 'COLOR_BGR2YUV_YVYU',
# 'COLOR_BGR5552BGR', 'COLOR_BGR5552BGRA', 'COLOR_BGR5552GRAY', 'COLOR_BGR5552RGB', 'COLOR_BGR5552RGBA', 'COLOR_BGR5652BGR', 'COLOR_BGR5652BGRA', 'COLOR_BGR5652GRAY', 'COLOR_BGR5652RGB', 'COLOR_BGR5652RGBA',
# 'COLOR_BGRA2BGR', 'COLOR_BGRA2BGR555', 'COLOR_BGRA2BGR565', 'COLOR_BGRA2GRAY', 'COLOR_BGRA2RGB', 'COLOR_BGRA2RGBA', 'COLOR_BGRA2YUV_I420', 'COLOR_BGRA2YUV_IYUV', 'COLOR_BGRA2YUV_UYNV', 'COLOR_BGRA2YUV_UYVY',
# 'COLOR_BGRA2YUV_Y422', 'COLOR_BGRA2YUV_YUNV', 'COLOR_BGRA2YUV_YUY2', 'COLOR_BGRA2YUV_YUYV', 'COLOR_BGRA2YUV_YV12', 'COLOR_BGRA2YUV_YVYU', 'COLOR_BayerBG2BGR', 'COLOR_BayerBG2BGRA', 'COLOR_BayerBG2BGR_EA', 'COLOR_BayerBG2BGR_VNG',
# 'COLOR_BayerBG2GRAY', 'COLOR_BayerBG2RGB', 'COLOR_BayerBG2RGBA', 'COLOR_BayerBG2RGB_EA', 'COLOR_BayerBG2RGB_VNG', 'COLOR_BayerBGGR2BGR', 'COLOR_BayerBGGR2BGRA', 'COLOR_BayerBGGR2BGR_EA', 'COLOR_BayerBGGR2BGR_VNG', 'COLOR_BayerBGGR2GRAY',
# 'COLOR_BayerBGGR2RGB', 'COLOR_BayerBGGR2RGBA', 'COLOR_BayerBGGR2RGB_EA', 'COLOR_BayerBGGR2RGB_VNG', 'COLOR_BayerGB2BGR', 'COLOR_BayerGB2BGRA', 'COLOR_BayerGB2BGR_EA', 'COLOR_BayerGB2BGR_VNG', 'COLOR_BayerGB2GRAY', 'COLOR_BayerGB2RGB',
# 'COLOR_BayerGB2RGBA', 'COLOR_BayerGB2RGB_EA', 'COLOR_BayerGB2RGB_VNG', 'COLOR_BayerGBRG2BGR', 'COLOR_BayerGBRG2BGRA', 'COLOR_BayerGBRG2BGR_EA', 'COLOR_BayerGBRG2BGR_VNG', 'COLOR_BayerGBRG2GRAY', 'COLOR_BayerGBRG2RGB', 'COLOR_BayerGBRG2RGBA',
# 'COLOR_BayerGBRG2RGB_EA', 'COLOR_BayerGBRG2RGB_VNG', 'COLOR_BayerGR2BGR', 'COLOR_BayerGR2BGRA', 'COLOR_BayerGR2BGR_EA', 'COLOR_BayerGR2BGR_VNG', 'COLOR_BayerGR2GRAY', 'COLOR_BayerGR2RGB', 'COLOR_BayerGR2RGBA', 'COLOR_BayerGR2RGB_EA',
# 'COLOR_BayerGR2RGB_VNG', 'COLOR_BayerGRBG2BGR', 'COLOR_BayerGRBG2BGRA', 'COLOR_BayerGRBG2BGR_EA', 'COLOR_BayerGRBG2BGR_VNG', 'COLOR_BayerGRBG2GRAY', 'COLOR_BayerGRBG2RGB', 'COLOR_BayerGRBG2RGBA', 'COLOR_BayerGRBG2RGB_EA', 'COLOR_BayerGRBG2RGB_VNG',
# 'COLOR_BayerRG2BGR', 'COLOR_BayerRG2BGRA', 'COLOR_BayerRG2BGR_EA', 'COLOR_BayerRG2BGR_VNG', 'COLOR_BayerRG2GRAY', 'COLOR_BayerRG2RGB', 'COLOR_BayerRG2RGBA', 'COLOR_BayerRG2RGB_EA', 'COLOR_BayerRG2RGB_VNG', 'COLOR_BayerRGGB2BGR', 'COLOR_BayerRGGB2BGRA',
# 'COLOR_BayerRGGB2BGR_EA', 'COLOR_BayerRGGB2BGR_VNG', 'COLOR_BayerRGGB2GRAY', 'COLOR_BayerRGGB2RGB', 'COLOR_BayerRGGB2RGBA', 'COLOR_BayerRGGB2RGB_EA', 'COLOR_BayerRGGB2RGB_VNG', 'COLOR_COLORCVT_MAX', 'COLOR_GRAY2BGR', 'COLOR_GRAY2BGR555', 'COLOR_GRAY2BGR565',
# 'COLOR_GRAY2BGRA', 'COLOR_GRAY2RGB', 'COLOR_GRAY2RGBA', 'COLOR_HLS2BGR', 'COLOR_HLS2BGR_FULL', 'COLOR_HLS2RGB', 'COLOR_HLS2RGB_FULL', 'COLOR_HSV2BGR', 'COLOR_HSV2BGR_FULL', 'COLOR_HSV2RGB', 'COLOR_HSV2RGB_FULL', 'COLOR_LAB2BGR', 'COLOR_LAB2LBGR', 'COLOR_LAB2LRGB',
# 'COLOR_LAB2RGB', 'COLOR_LBGR2LAB', 'COLOR_LBGR2LUV', 'COLOR_LBGR2Lab', 'COLOR_LBGR2Luv', 'COLOR_LRGB2LAB', 'COLOR_LRGB2LUV', 'COLOR_LRGB2Lab', 'COLOR_LRGB2Luv', 'COLOR_LUV2BGR', 'COLOR_LUV2LBGR', 'COLOR_LUV2LRGB', 'COLOR_LUV2RGB', 'COLOR_Lab2BGR', 'COLOR_Lab2LBGR',
# 'COLOR_Lab2LRGB', 'COLOR_Lab2RGB', 'COLOR_Luv2BGR', 'COLOR_Luv2LBGR', 'COLOR_Luv2LRGB', 'COLOR_Luv2RGB', 'COLOR_M_RGBA2RGBA', 'COLOR_RGB2BGR', 'COLOR_RGB2BGR555', 'COLOR_RGB2BGR565', 'COLOR_RGB2BGRA', 'COLOR_RGB2GRAY', 'COLOR_RGB2HLS', 'COLOR_RGB2HLS_FULL',
# 'COLOR_RGB2HSV', 'COLOR_RGB2HSV_FULL', 'COLOR_RGB2LAB', 'COLOR_RGB2LUV', 'COLOR_RGB2Lab', 'COLOR_RGB2Luv', 'COLOR_RGB2RGBA', 'COLOR_RGB2XYZ', 'COLOR_RGB2YCR_CB', 'COLOR_RGB2YCrCb', 'COLOR_RGB2YUV', 'COLOR_RGB2YUV_I420', 'COLOR_RGB2YUV_IYUV', 'COLOR_RGB2YUV_UYNV',
# 'COLOR_RGB2YUV_UYVY', 'COLOR_RGB2YUV_Y422', 'COLOR_RGB2YUV_YUNV', 'COLOR_RGB2YUV_YUY2', 'COLOR_RGB2YUV_YUYV', 'COLOR_RGB2YUV_YV12', 'COLOR_RGB2YUV_YVYU', 'COLOR_RGBA2BGR', 'COLOR_RGBA2BGR555', 'COLOR_RGBA2BGR565', 'COLOR_RGBA2BGRA', 'COLOR_RGBA2GRAY',
# 'COLOR_RGBA2M_RGBA', 'COLOR_RGBA2RGB', 'COLOR_RGBA2YUV_I420', 'COLOR_RGBA2YUV_IYUV', 'COLOR_RGBA2YUV_UYNV', 'COLOR_RGBA2YUV_UYVY', 'COLOR_RGBA2YUV_Y422', 'COLOR_RGBA2YUV_YUNV', 'COLOR_RGBA2YUV_YUY2', 'COLOR_RGBA2YUV_YUYV', 'COLOR_RGBA2YUV_YV12',
# 'COLOR_RGBA2YUV_YVYU', 'COLOR_RGBA2mRGBA', 'COLOR_XYZ2BGR', 'COLOR_XYZ2RGB', 'COLOR_YCR_CB2BGR', 'COLOR_YCR_CB2RGB', 'COLOR_YCrCb2BGR', 'COLOR_YCrCb2RGB', 'COLOR_YUV2BGR', 'COLOR_YUV2BGRA_I420', 'COLOR_YUV2BGRA_IYUV', 'COLOR_YUV2BGRA_NV12', 'COLOR_YUV2BGRA_NV21',
# 'COLOR_YUV2BGRA_UYNV', 'COLOR_YUV2BGRA_UYVY', 'COLOR_YUV2BGRA_Y422', 'COLOR_YUV2BGRA_YUNV', 'COLOR_YUV2BGRA_YUY2', 'COLOR_YUV2BGRA_YUYV', 'COLOR_YUV2BGRA_YV12', 'COLOR_YUV2BGRA_YVYU', 'COLOR_YUV2BGR_I420', 'COLOR_YUV2BGR_IYUV', 'COLOR_YUV2BGR_NV12',
# 'COLOR_YUV2BGR_NV21', 'COLOR_YUV2BGR_UYNV', 'COLOR_YUV2BGR_UYVY', 'COLOR_YUV2BGR_Y422', 'COLOR_YUV2BGR_YUNV', 'COLOR_YUV2BGR_YUY2', 'COLOR_YUV2BGR_YUYV', 'COLOR_YUV2BGR_YV12', 'COLOR_YUV2BGR_YVYU', 'COLOR_YUV2GRAY_420', 'COLOR_YUV2GRAY_I420', 'COLOR_YUV2GRAY_IYUV',
# 'COLOR_YUV2GRAY_NV12', 'COLOR_YUV2GRAY_NV21', 'COLOR_YUV2GRAY_UYNV', 'COLOR_YUV2GRAY_UYVY', 'COLOR_YUV2GRAY_Y422', 'COLOR_YUV2GRAY_YUNV', 'COLOR_YUV2GRAY_YUY2', 'COLOR_YUV2GRAY_YUYV', 'COLOR_YUV2GRAY_YV12', 'COLOR_YUV2GRAY_YVYU', 'COLOR_YUV2RGB',
# 'COLOR_YUV2RGBA_I420', 'COLOR_YUV2RGBA_IYUV', 'COLOR_YUV2RGBA_NV12', 'COLOR_YUV2RGBA_NV21', 'COLOR_YUV2RGBA_UYNV', 'COLOR_YUV2RGBA_UYVY', 'COLOR_YUV2RGBA_Y422', 'COLOR_YUV2RGBA_YUNV', 'COLOR_YUV2RGBA_YUY2', 'COLOR_YUV2RGBA_YUYV', 'COLOR_YUV2RGBA_YV12', 
# 'COLOR_YUV2RGBA_YVYU', 'COLOR_YUV2RGB_I420', 'COLOR_YUV2RGB_IYUV', 'COLOR_YUV2RGB_NV12', 'COLOR_YUV2RGB_NV21', 'COLOR_YUV2RGB_UYNV', 'COLOR_YUV2RGB_UYVY', 'COLOR_YUV2RGB_Y422', 'COLOR_YUV2RGB_YUNV', 'COLOR_YUV2RGB_YUY2', 'COLOR_YUV2RGB_YUYV', 'COLOR_YUV2RGB_YV12',
# 'COLOR_YUV2RGB_YVYU', 'COLOR_YUV420P2BGR', 'COLOR_YUV420P2BGRA', 'COLOR_YUV420P2GRAY', 'COLOR_YUV420P2RGB', 'COLOR_YUV420P2RGBA', 'COLOR_YUV420SP2BGR', 'COLOR_YUV420SP2BGRA', 'COLOR_YUV420SP2GRAY', 'COLOR_YUV420SP2RGB', 'COLOR_YUV420SP2RGBA', 'COLOR_YUV420p2BGR',
# 'COLOR_YUV420p2BGRA', 'COLOR_YUV420p2GRAY', 'COLOR_YUV420p2RGB', 'COLOR_YUV420p2RGBA', 'COLOR_YUV420sp2BGR', 'COLOR_YUV420sp2BGRA', 'COLOR_YUV420sp2GRAY', 'COLOR_YUV420sp2RGB', 'COLOR_YUV420sp2RGBA', 'COLOR_mRGBA2RGBA']


# Object Tracking
cap=cv.VideoCapture(0)



while(1):
    # Take each frame
    _,frame=cap.read()
    # Convert BGR to HSV
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask=cv.inRange(hsv,lower_blue,upper_blue)
    # Bitwise-AND mask and original image
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k=cv.waitKey(5) & 0xFF
    if k == 27:
        break
    cv.destroyAllWindows()
    

# Geometric transformation

# cv.warpAffine and cv.warpPerspective functions
# cv.warpAffine takes a 2x3 transformation matrix while cv.warpPerspective takes a 3x3 transformation matrix as input

# Scaling using cv.resize()

# There are different interpolation  methods such as:

# cv.INTER_AREA for shrinking and

# cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming

# By default,  the interpolation method cv.INTER_LINEAR is used for all resizing purposes.

# Resize image
img=cv.imread(r'F:\panag\Pictures\Saved Pictures\starry_night.jpg')
res=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
# OR
height,width=img.shape[:2]
res=cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)

img=cv.imread(r'F:\panag\Pictures\Saved Pictures\starry_night.jpg',0)
rows,cols=img.shape
M=np.float32([[1,0,100],[0,1,50]])
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

# width = number of columns
# height = number of rows

# Thresholding

# cv.threshold 

# Basic thresholding as described above is done by using the type cv.THRESH_BINARY

#types of thresholding :

# cv.THRESH_BINARY

# cv.THRESH_BINARY_INV

# cv.THRESH_TRUNC

# cv.THRESH_TOZERO

# cv.THRESH_TOZERO_INV

from matplotlib import pyplot as plt

img=cv.imread(r'F:\panag\Pictures\Saved Pictures\my_image.png')
ret,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
title=['ORIGINAL IMAGE','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
    plt.show()
    

# Harris Corner Detection in OpenCV
# cv.cornerHarris()
# cv.cornerSubPix()
# img - INPUT IMAGE. It should be grayscale and float32 type.
# blockSize - It is the size of neighbourhood considered for corner detection 
# ksize - Aperture parameter of Sobel derivative used.
# k - Harris detector free parameter in the equation.

filename=r'F:\panag\Pictures\Saved Pictures\image2.png'
img=cv.imread(filename)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=np.float32(gray)
dst=cv.cornerHarris(gray,2,3,0.04)
# Result is dilated for marking the corners, not important
dst=cv.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
    
# feature Detection using FAST ...
# FAST Feature Detector 
# cv.FastFeatureDetector_create()
# threshold - The threshold for the FAST feature detector. The higher the threshold, the fewer features will
# be detected.
# nonmaxSuppression - If true, then non-maximum suppression is applied to the detected corners
# fast=cv.FastFeatureDetector_create()


# Capture video

# Video=cv.VideoCapture(0)

# Video.release()

# import time

# video=cv.VideoCapture(0)

# time.sleep(5) # This will stop the script for 5 seconds 

# video.release()

# time.sleep(5)

# Motion detection

# Objects detection

# def nothing(x):
#     # any operation
#     pass
# cap=cv.VideoCapture(1)

# # eliminate as much noise as it is possible.
# area=cv.contourArea(cnt)
# approx=cv.approxPolyDP(cnt,0.02*cv.arcLength(cnt,True),True)
# x=approx.ravel()[0]
# y=approx.ravel()[1]

# if area > 400:
#     cv.drawContours(frame,[approx],0,(0,0,255),5)
    
#     if len(approx) == 3:
#         cv.putText(frame, "Triangle", (x, y), font,1,(0,0,0))
        
#     elif len(approx) == 4:
#         cv.putText(frame, "Rectangle", (x, y), font,1,(0,0,0))
    
#     elif 10 < len(approx) < 20 :
#         cv.putText(frame, "Circle", (x, y), font,1,(0,0,0))