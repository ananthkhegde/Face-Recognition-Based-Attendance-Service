import face_recognition
import datetime
from time import gmtime, strftime

from django.db import connection


class FaceRecognition:


    """
    Method to recognize Face in an Image
    """
    def recognizeFaces(self,imgobj):

        unknown_image = face_recognition.load_image_file(imgobj)
        face_locations = face_recognition.face_locations(unknown_image)
        names = []

        cur = connection.cursor()
        cur.execute("SELECT face_encoding,face_name,face_id  from face_master")
        rows = cur.fetchall()
        faces = list()
        i = 0
        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_image = unknown_image[top:bottom, left:right]
            try:
                encoding = face_recognition.face_encodings(face_image)[0]
                for row in rows:
                    # a = numpy.array(row, dtype='double')
                    matchquery = face_recognition.compare_faces([row[0]], encoding, 0.53)
                    face_distances = face_recognition.face_distance([row[0]], encoding)
                    if matchquery[0] == True:
                        names.append(row[1])
                        face_dict = dict()
                        face_dict['faceId'] = row[2]
                        face_dict['faceName'] = row[1]
                        faces.append(face_dict)
                        i = i + 1
                        break
            except:
                pass



        connection.close()
        return faces

    """
    This method encodes Face
    """
    def encodeFace(self, input_dict):

        image = face_recognition.load_image_file(input_dict['file'])
        imgObjEncoding = face_recognition.face_encodings(image)[0]
        name = "'" +input_dict['name'] + "'"
        insertstmt = 'INSERT INTO face_master(face_name,face_encoding) VALUES ('
        insertstmt = insertstmt  + name + ",ARRAY["
        #print(len(imgObjEncoding))
        for index in range(len(imgObjEncoding)):
            insertstmt = insertstmt + str(imgObjEncoding[index]) + ','
        insertstmt = insertstmt[:-1]
        insertstmt = insertstmt + ']' + ');'
        cur = connection.cursor()
        cur.execute(insertstmt)
        connection.commit()
        connection.close()




