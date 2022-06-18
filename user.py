import cv2
import os

while True:
    print("\n PICK BETWEEN \n[yelan]\n[bonsai]")
    pic = input(" \nPicture name: ")
    pic_name = str(pic+'.jpg')
    print(pic_name)
    flag = int(input("[1] COLORED \n[2] GRAYSCALE \nENTER CHOICE: "))

    if flag == 1:
        if os.path.exists(pic_name):
      
            image = cv2.imread(pic_name,1)
            if pic == 'yelan':
                title = 'At your Service my Queen'
                cv2.imshow(title, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            
            if pic == 'bonsai':
                title = 'My true Queen'
                cv2.imshow(title, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break

        else:
            print("Invalid Picture...")

    elif flag == 2:
        if os.path.exists(pic_name):
            image = cv2.imread(pic_name,0)
            if pic == 'yelan':
                title = 'At your Service my Queen'
                cv2.imshow(title, image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break

            if pic == 'bonsai':
                title = 'My true Queen'
                cv2.imshow(title, image)
                cv2.waitKey(0)  
                cv2.destroyAllWindows()
                break

        else:
            print("Invalid Picture...")

    else:
        print("Invalid Flag...")