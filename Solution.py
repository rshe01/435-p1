import xml.etree.ElementTree as ET
import cv2
import re 
import sys
import os

#potential inputs:
#com.google.android.apps.transalte
#com.pandora.android
#com.yelp.android
#com.giphy.messenger-2
#com.giphy.messenger-1
#com.dropbox.android
#com.apalon.ringtones doesn't parse 

def main():
    args = sys.argv[1:]
    absolute_path = os.path.join(os.getcwd(), 'Programming-Assignment-Data',args[0])
    image = cv2.imread(absolute_path+'.png')
    tree = ET.parse(absolute_path+'.xml')
    root = tree.getroot()

    list = []

    for child in root.iter("*"):
        if(len(child) == 0):
            bounds = [int(s) for s in re.findall(r'\d+', child.get("bounds"))]
            list.append(bounds)

    height = int(image.shape[0])
    width = int(image.shape[1])
    dimension = (width, height)

    resized = cv2.resize(image, dimension)

    for bound in list:
        start_x = int (bound[0])
        start_y = int (bound[1])
        end_x = int (bound[2])
        end_y = int (bound[3])
        cv2.rectangle(resized, (start_x, start_y), (end_x,end_y), (13,218,253), 8)

    cv2.imshow(args[0], resized)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
