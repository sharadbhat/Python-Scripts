import cv2
import os

file_names = [fn for fn in os.listdir('./images')]

lsorted = sorted(file_names,key=lambda x: int(os.path.splitext(x)[0]))

vvw = cv2.VideoWriter('mymovie.gif',cv2.VideoWriter_fourcc('X','V','I','D'),24,(640,480))
frameslist = lsorted
howmanyframes = len(frameslist)
print('Frames count: '+str(howmanyframes)) #just for debugging

for i in range(0,howmanyframes):
    print(i)
    theframe = cv2.imread('./images/'+frameslist[i])
    vvw.write(theframe)
