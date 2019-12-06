import cv2
import numpy as np
cap = cv2.VideoCapture(0)
print(1%3)
while(True):

    x_list = []
    y_list = []
    ret,frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh, BWFrame = cv2.threshold(grayFrame, 250, 255, cv2.THRESH_BINARY)
    frameArray=np.asarray(BWFrame)
    """
    frameArray=np.reshape(frameArray,(1,640*480))
    counter = 1
    for i in range(frameArray.shape[1]):
        if frameArray[0][i] != 0:
            x_list.append((i+1)%680)

            if i%480 == 0 and i != 640*480-1:
                counter+=1
            y_list.append(counter)
            if i==640*480-1:
                counter = 1
    """
    #For Method
    for i in range(480):
        for j in range(640):
            if frameArray[i][j] != 0:
                x_list.append(i)
                y_list.append(j)
                break
    
    print(len(x_list))
    print(len(y_list))
    avg_y = np.sum(y_list)/len(y_list)
    avg_x = np.sum(x_list)/len(x_list)
    avg_xsq = np.sum(np.power(x_list,2))/len(x_list)
    avg_xy = (np.sum(np.multiply(x_list,y_list)))/len(y_list)
    slope = (avg_x*avg_y-avg_xy)/(avg_x**2-avg_xsq)
    bias = avg_y-slope*avg_x
    print("Average Y "+str(avg_y)+"\nAverage X "+str(avg_x)+"\nAverage X^2 "+str(avg_xsq)+"\n(Average X)^2 "+str(avg_x**2)+"\nAverage XY "+str(avg_xy)+"\nSlope "+str(slope)+"\nBias "+str(bias))
    #lined_frame = cv2.line(frame, (y_list[0],x_list[0]), (y_list[-1],x_list[-1]), (255, 0, 0), 9)
    lined_frame = cv2.line(frame, (int(slope*100+bias),100), (int(slope*380+bias),380), (255, 0, 0), 9)
    cv2.imshow('Contrast_Video', BWFrame)
    cv2.imshow('Lined_Video', lined_frame)
    # Image size is 480 by 640
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
