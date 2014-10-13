import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/home/ubuser/scrapper/face_detect/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/ubuser/scrapper/face_detect/haarcascade_eye.xml')


def find_faces(imagePath):

	global face_cascade,eye_cascade

	has_faces = False

	# Read the image
	img = cv2.imread(imagePath)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	if len(faces) > 0:
		for (x,y,w,h) in faces:
		    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		    roi_gray = gray[y:y+h, x:x+w]
		    roi_color = img[y:y+h, x:x+w]
		    eyes = eye_cascade.detectMultiScale(roi_gray)
		    if len(eyes) > 0:
			    has_faces = True
			    for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

		if has_faces:
			cv2.imshow('img',img)
			cv2.waitKey(100)

		cv2.destroyAllWindows()

	if has_faces:
		return len(faces)
	else:
		return 0