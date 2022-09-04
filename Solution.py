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
        f = os.fsdecode(filename)
        file_prefix.append(f)

    for i in range(0, len(file_prefix),2):
        try:
            draw(directory, file_prefix[i],file_prefix[i+1])
        except:
            print("ERROR: XML parsing issues with",file_prefix[i],"and",file_prefix[i+1])
        

def draw(directory, png_file, xml_file):
    png_path = os.path.join(os.getcwd(), directory, png_file)
    xml_path = os.path.join(os.getcwd(), directory, xml_file)

    tree = ET.parse(xml_path)
    image = cv2.imread(png_path)
    root = tree.getroot()

    list = []

    for child in root.iter("*"):
        if(len(child) == 0):
            bounds = [int(s) for s in re.findall(r'\d+', child.get("bounds"))]
            list.append(bounds)

    for bound in list:
        start_x = bound[0]
        start_y = bound[1]
        end_x = bound[2]
        end_y = bound[3]
        cv2.rectangle(image, (start_x, start_y), (end_x,end_y), (13,218,253), 8)

    output_folder = 'Output'
    cv2.imwrite(os.path.join(os.getcwd(), output_folder, png_file), image)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
