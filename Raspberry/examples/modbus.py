from PIL import Image
import pyautogui
import os
import time
def main():
    screenshot = pyautogui.screenshot()
    screenshot.save(r'/home/pi/Downloads/test.jpg')
    file_in = "test.jpg"
    img = Image.open(file_in)
    #img.thumbnail((1600, 1200), Image.LANCZOS)
    img = img.resize((1600,1200 ), Image.Resampling.LANCZOS)
    file_out=  "1600x1200_0.bmp"
    #file_out1= "1600x1200_0.bmp"
    file_out2= "1600x1200_1.bmp"
    file_out3= "1600x1200_2.bmp"
    file_out4= "1600x1200_3.bmp"
    file_out5= "1600x1200_4.bmp"
    file_out6= "1600x1200_5.bmp"
    file_out7= "1600x1200_6.bmp"
    print(len(img.split()))
    if len(img.split())==4:
          r,g,b,a = img.split()
          img=Image.merge("RGB",(r,g,b))
          img.save(file_out)
    else :
        img.save(file_out)
        #img.save(file_out1)
        img.save(file_out2)
        img.save(file_out3)
        img.save(file_out4)
        img.save(file_out5)
        img.save(file_out6)
        img.save(file_out7)
    #if os.path.exists("test.jpg"):
     # os.remove("test.jpg")
    #else:
     # print("The file does not exist")
    #os.system("cd")
    #os.system("sudo /home/pi/IT8951-ePaper/Raspberry/./epd -2.08 0")
    #os.system("sudo ./epd -2.08 0")


while True:
    main()
    time.sleep(2)
