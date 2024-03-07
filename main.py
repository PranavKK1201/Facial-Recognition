from deepface import DeepFace
import cv2
import time
import keyboard
import threading


def main():
     imageDict = {}
     livefeed
     while(True):
          case = input("Press 1 to enter face\nPress 2 to start recognition\nPress 3 to stop completely\n")
          if(case=="1"):
               imageDict = newFace(imageDict)
          elif(case=="2"):
               livefeed(imageDict)
          elif(case=="3"):
               break
          else:
               print("Invalid value entered")
          
def livefeed(imageDict):
     cap = cv2.VideoCapture(0)
     count = 0

     while True:
          while True:
               ret, frame = cap.read()
               if ret:
                    if (count%40 ==0):
                         try:
                              threading.Thread(target=recognition, args=(imageDict, frame, )).start()
                         except Exception:
                              pass
                    count+=1
                    cv2.imshow('Camera Feed', frame)
                         
               key = cv2.waitKey(1)
               if key == ord('q'):
                    break
               
               
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
     cv2.imshow("test", sourimg)
     cv2.waitKey(0)

     return imageDict


def recognition(imageDict, frame):
     for name in imageDict:
          try:
               if DeepFace.verify(frame, imageDict[name])['verified']:
                    cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
          except Exception:
               pass
"""def recognition(imageDict, feed):
     vidcap = cv2.VideoCapture(0)
     while(True):
          if(keyboard.is_pressed('q')):
               break
          else:
            
               liveImage = Capturing(vidcap)
               for name in imageDict:
                    try:
                         result = DeepFace.verify(imageDict[name], liveImage)
                         if(result['verified'] == True):
                              print(f"Welcome {name}")
                              continue
                    except:
                         print("face no found")
                         continue
               """

if __name__ == "__main__":
     main()
     