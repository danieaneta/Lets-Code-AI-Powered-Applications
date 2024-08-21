"""
1. Input Handling: Screenshot Handling
    -Take screenshot every 3 seconds (advanced functionality)
    OR
    -Manually take screenshots (User friendly - security wise)
    -Convert screenshot image to np.array using OpenCV
    -Resize image to appropiate dimensions.
        -This will enable us to optimize
        model usage and speed (could also
        optimize cost effectiveness.)
2. VLM Functionality: 
    -Screenshots will be automatically sent to VLM pipeline. 
    -VLM will process each screenshot.
    -VLM will output Contextual Data. 
    -VLM Functionality will delete screenshot once it has been processed,
    but will keep the contextual data.
        -optimize security measures and can keep data encrypted
        if needed.
    -VLM functionality will store contextual data within a temp
    database (pre-deployment, production database). 
        -Database will be a CSV file which will store 
        contextual data. 
3. LLM Functionality: 
    -LLM will have access to CSV file and enable 
    users to converse with their data.

    

Secondary Functionalities: 
    -Data Encryption for higher security.

"""

import cv2 
import os
from resize import Resize_Image
from detection import OpenAI_Detection
from datetime import datetime


Image_Directory = ''
Image_List = os.listdir(Image_Directory)


"""
Pseudo:

def Read_Images(images)
    images = cv2.imread(images)
    return images


class Recall_Function():
    def __init__(self, screenshot_directory)
    self. etc

    def Run_Recall():
        # Read Screenshot Directory + Read Images
        ND_Array_Image_List = []
        for Asset in self.screenshot_directoy
            Images = Read_Images
            ND_Array_Image_List.append(Images)

        #Process Images through Zero Shot Detection (call zero
        shot detection)

        #

"""


class Recall_Function():
    def __init__(self, Image_Directory, Response_Directory):
        self.Image_Directory = Image_Directory
        self.Response_Directory = Response_Directory

    def Read_Images(self, image):
        Image = cv2.imread(image)
        return Image
    
    def Save_Responses(self, text):
        current_datetime = datetime.now()
        formatted_time = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")

        with open(f'{self.Response_Directory}/{formatted_time}.txt', 'w') as file:
            file.write(str(text))
        return formatted_time 
    
    def Delete_Responses(self):
        #Security Purposes.
        """
        We will delete the reponses at beginning of session?
        """
        pass

    def Run_Recall(self):
        
        NDArray_Image_List = []
        for Asset in self.Image_Directory:
            if Asset.endswith('.jpg'):
                Image = self.Read_Images(Asset)
                NDArray_Image_List.append(Image)

        Image_Responses = []
        for converted_image in NDArray_Image_List:
            responses = OpenAI_Detection(converted_image).Run_Detection()
        
        Response_Timestamps = []
        for responses in Image_Responses:
            Timestamp = self.Save_Responses(responses)
            Response_Timestamps.append(Timestamp)

    def Initiate(self):
        self.Run_Recall()

    

        





