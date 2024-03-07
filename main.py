from deepface import DeepFace
import cv2
import time
import keyboard


def main():
     imageDict = {}
     livefeed
     while(True):
          case = input("Press 1 to enter face\nPress 2 to start recognition\nPress 3 to stop completely\n")
          if(case=="1"):
               imageDict = newFace(imageDict)
          elif(case=="2"):
               #livefeed()
               recognition(imageDict)
               
               #Capturing(0)
               print("Executed 2")
          elif(case=="3"):
               break
          else:
               print("Invalid value entered")
          
def livefeed():
     cap = cv2.VideoCapture(0)

     if not cap.isOpened():
          print("Error opening video stream or file")
          exit()
     while(True):
          if(keyboard.is_pressed('q')):
               break
          else:
               while True:
                    ret, frame = cap.read()
                    if ret:
                         cv2.imshow('Camera Feed', frame)
                         if cv2.waitKey(1) & 0xFF == ord('q'):
                              break
                    else:
                         break
               cap.release()
               cv2.destroyAllWindows()


def Capturing(vidcap):
    while(True):
        if vidcap.isOpened():

            returnVal, img = vidcap.read()

            if(returnVal):
                    return img
               
        else:
            print("Couldn't Capture Camera!!")
            vidcap.release()
            break
        
def newFace(imageDict):

     name = input("Enter name: ")
     source = input("Enter url: ")
     source = source.replace("\\", "/")
     source = source.replace('"', "")


     imageDict[name] = source

     sourimg = cv2.imread(imageDict[name])
     #cv2.imshow("test", sourimg)
     #cv2.waitKey(0)

     return imageDict

    
def recognition(imageDict):
     
     vidcap = cv2.VideoCapture(0)
     while(True):
          returnVal, liveImage = vidcap.read()            
          for name in imageDict:
               try:
                    result = DeepFace.verify(imageDict[name], liveImage.copy())
                    if(result['verified'] == True and result['distance'] < 0.3):
                         print(f"Welcome {name}: {result['distance']}") 
                    else:
                         print(f"not recognized {result['distance']}")
               except:
                    continue
          key = cv2.waitKey(1) & 0xFF
          if key == ord('q'):
               break


if __name__== "__main__":
   main()




