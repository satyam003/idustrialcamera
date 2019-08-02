import os
from PIL import Image

def fail_image(i):
    filename1: str = "Receive_Image_" + str(i) + ".bmp"
    filename2: str = "C:\\Users\satyam\Desktop\\NOK\\"
    filename = filename2+filename1
    print(i)
    with open('receive_image.bmp', 'rb') as rf:
        with open(filename, 'wb') as wf:
            chunck_size = 10240
            rf.seek(14)
            rf_chunk = rf.read(chunck_size)
            while len(rf_chunk) > 0:
                wf.write(rf_chunk)
                rf_chunk = rf.read(chunck_size)
        wf.close()
    rf.close()
    os.remove("receive_image.bmp")
    img = Image.open(filename)
    img.show()
    print("Thread is close")