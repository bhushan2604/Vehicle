import cv2
import math
import time
import numpy as np
import mysql.connector
from datetime import datetime
now = datetime.now()

#database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "vehicle"
)
cursor = mydb.cursor()
if mydb.is_connected():
    print("connected")

def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binarydata = file.read()
    return binarydata

limit = 40 #km/hr

file = open("C://Users//dell//Desktop//Vehicle detection//speed2//TrafficRecord//SpeedRecord.txt","w")
file.write("ID \t SPEED\n------\t-------\n")
file.close()


class EuclideanDistTracker:
    def __init__(self):
        # Store the center positions of the objects
        self.center_points = {}

        self.id_count = 0
        #self.start = 0
        #self.stop = 0
        self.et=0
        self.s1 = np.zeros((1,1000))
        self.s2 = np.zeros((1,1000))
        self.s = np.zeros((1,1000))
        self.f = np.zeros(1000)
        self.capf = np.zeros(1000)
        self.count = 0
        self.exceeded = 0


    def update(self, objects_rect):
        objects_bbs_ids = []

        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            #CHECK IF OBJECT IS DETECTED ALREADY
            same_object_detected = False

            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 70:
                    self.center_points[id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True

                    #START TIMER
                    if (y >= 410 and y <= 430):
                        self.s1[0,id] = time.time()

                    #STOP TIMER and FIND DIFFERENCE
                    if (y >= 235 and y <= 255):
                        self.s2[0,id] = time.time()
                        self.s[0,id] = self.s2[0,id] - self.s1[0,id]

                    #CAPTURE FLAG
                    if (y<235):
                        self.f[id]=1


            #NEW OBJECT DETECTION
            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1
                self.s[0,self.id_count]=0
                self.s1[0,self.id_count]=0
                self.s2[0,self.id_count]=0

        # ASSIGN NEW ID to OBJECT
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        self.center_points = new_center_points.copy()
        return objects_bbs_ids

    #SPEEED FUNCTION
    def getsp(self,id):
        if (self.s[0,id]!=0):
            # s = 214.15 / self.s[0, id]
            s = 175 / self.s[0, id]
        else:
            s = 0

        return int(s)

    #SAVE VEHICLE DATA
    def capture(self,img,x,y,h,w,sp,id,d,t):
        if(self.capf[id]==0):
            self.capf[id] = 1
            self.f[id]=0
            crop_img = img[y-5:y + h+5, x-5:x + w+5]

            



            spee = str(sp)
            n = str(id)+"_speed_"+str(sp)
            file = 'C://Users//dell//Desktop//Vehicle detection//speed2//TrafficRecord//' + n + '.jpg'
            cv2.imwrite(file, crop_img)
            self.count += 1
            filet = open("C://Users//dell//Desktop//Vehicle detection//speed2//TrafficRecord//SpeedRecord.txt", "a")
            if(sp>limit):
                file2 = 'C://Users//dell//Desktop//Vehicle detection//speed2//TrafficRecord//exceeded//' + '0' + '.jpg'
                cv2.imwrite(file2, crop_img)
                convertPic = convertToBinary('C://Users//dell//Desktop//Vehicle detection//speed2//TrafficRecord//exceeded//0.jpg')
                insert1 = ("INSERT INTO veh(date,time,images,count,status) VALUES(%s, %s, %s, %s ,%s)")
                val = (d,t,convertPic,n,spee)
                cursor.execute(insert1,val)
                mydb.commit()



                filet.write(str(id)+" \t "+str(sp)+"<---exceeded\n")
                self.exceeded+=1
            else:
                filet.write(str(id) + " \t " + str(sp) + "\n")
            filet.close()


    #SPEED_LIMIT
    def limit(self):
        return limit

    #TEXT FILE SUMMARY
    def end(self):
        file = open("C://Users//dell//Desktop//Vehicle detection//speed2//TrafficRecord//SpeedRecord.txt", "a")
        file.write("\n-------------\n")
        file.write("-------------\n")
        file.write("SUMMARY\n")
        file.write("-------------\n")
        file.write("Total Vehicles :\t"+str(self.count)+"\n")
        file.write("Exceeded speed limit :\t"+str(self.exceeded))
        file.close()