import cv2 as cv
import numpy as np
import cmake
import dlib

frontal_face_detector=dlib.get_frontal_face_detector()
frontal_shape_predictor=dlib.shape_predictor("./dataset/shape_predictor_68_face_landmarks.dat")
imu_bgr=cv.imread("./image/imu.jpg")
imu=cv.cvtColor(imu_bgr,cv.COLOR_BGR2GRAY)
#cv.imshow("Imran Khan",imu)
modi=cv.imread("./image/modi.jpg")
#cv.imshow("Narendra Modi",modi)
source_image_canvas=np.zeros_like(imu_bgr)
height,width,no_of_channels=modi.shape
destination_image_canvas=np.zeros((height,width,no_of_channels),np.uint8)
source_faces=frontal_face_detector(imu)
for source_face in source_faces:
    source_face_landmarks=frontal_shape_predictor(imu,source_face)
    source_face_landmark_points=[]
    for landmark_no in range(0,68):
        x_point=source_face_landmarks.part(landmark_no).x
        y_point=source_face_landmarks.part(landmark_no).y
        source_face_landmark_points.append((x_point,y_point))
        #cv.circle(imu_bgr,(x_point,y_point),2,(255,0,0),-1)
        #cv.imshow("landmarked",imu_bgr)
    source_face_landmark_points_array=np.array(source_face_landmark_points,np.int32)
    source_face_convexhull=cv.convexHull(source_face_landmark_points_array)
    #cv.polylines(imu_bgr, [source_face_convexhull], True, (255,0,0),3)
    #cv.imshow("Convex Hull",imu_bgr)
    cv.fillConvexPoly(source_image_canvas,source_face_convexhull, 255)
    cv.imshow("Canvass with convex hull",source_image_canvas)