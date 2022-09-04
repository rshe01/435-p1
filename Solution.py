import xml.etree.ElementTree as ET
import cv2
import re 
import sys
import os

def main():
    args = sys.argv[1:]
    
    #input is our folder path: Programming-Assignment-Data
    directory = args[0]

    file_prefix = []
    
    for filename in os.listdir(directory):
        f = os.path.join(os.getcwd(), directory, filename)
        if os.path.isfile(f):
            file_prefix.append(f)

    for i in range(0, len(file_prefix),2):
        try:
            draw(file_prefix[i],file_prefix[i+1])
        except:
            print("ERROR: XML parsing issues with",file_prefix[i],"and",file_prefix[i+1])
        

def draw(png_file, xml_file):
    tree = ET.parse(xml_file)
    image = cv2.imread(png_file)
    root = tree.getroot()

    list = []

    for child in root.iter("*"):
        if(len(child) == 0):
            bounds = [int(s) for s in re.findall(r'\d+', child.get("bounds"))]
            list.append(bounds)

    for bound in list:
        start_x = int (bound[0])
        start_y = int (bound[1])
        end_x = int (bound[2])
        end_y = int (bound[3])
        cv2.rectangle(image, (start_x, start_y), (end_x,end_y), (13,218,253), 8)

    cv2.imshow(png_file, image)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
