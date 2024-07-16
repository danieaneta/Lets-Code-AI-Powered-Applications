import cv2


def Resize_Image(image):
    original_dimensions = image.shape
    original_width = original_dimensions[0]
    original_height = original_dimensions[1]
    scale = float(original_width / 1000)
    new_width = int(original_width * scale)
    new_height = int(original_height * scale)
    new_dim = (new_width, new_height)

    Resized_Image = cv2.resize(image, (new_dim), interpolation=cv2.INTER_LINEAR) 
    return Resized_Image
    
