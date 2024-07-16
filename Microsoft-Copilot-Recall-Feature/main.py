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


Image_Directory = ''
Image_List = os.listdir(Image_Directory)








