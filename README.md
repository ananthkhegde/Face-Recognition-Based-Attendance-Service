# Face Recognition - Attendance Service

Recognize faces from Python with
the world's simplest face recognition library [python face_recognition](https://github.com/ageitgey/face_recognition/).

This service exposes functionality to train the face of a particular person
and also to predict the face of the person or set of faces in a group photo.

Built using [dlib](http://dlib.net/)'s state-of-the-art face recognition
built with deep learning. The model has an accuracy of 99.38% on the
[Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) benchmark.

## About project
 * There are 2 API's developed as a part of this project
 * API (/encodeface/) - to train person face. Input to this API is individual facial photo of a person.It extract facial feature and        computes the face encoding and stores it in database for matching purpose
 * API (/identifyface/) - to get all the matching faces from the database. Input can be photo containing indidual face or group of          faces. It works by counting the no of faces and computes face encoding and matches all the face encoding in the database and            returns list of identified faces present in input image

## Installation

Requirements:
* Python 3+
* numpy
* scipy
* dlib (prerequisite cmake)
* face_recognition
* django
* django rest framework
* coreapi (for api documentation)
* postgre sql

## Guide to setting up database
* restore database backup file from [here](https://github.com/ananthkhegde/Face-Recognition-Based-Attendance-Service/tree/master/database)
* edit the database connection in setting.py in project file to connect locally

## Instruction to run project

* save project to local directory
* go to project folder i.e cd facecognition and execute below command
* python manage.py runserver 0.0.0.0:8001


## Guide to installing and running Rest service through API Client

* Install rest api client
https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwiDzOrtmM_VAhWMo48KHYfyC9UQFgglMAA&url=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fpostman%2Ffhbjgbiflinjbdggehcddcbncdddomop%3Fhl%3Den&usg=AFQjCNE_Yq59TT1ZExzJ68FTldg4ho_lGw

### Rest API
#### Training the faces(image encoding)
![alt text](https://github.com/ananthkhegde/Face-Recognition-Based-Attendance-Service/blob/master/assets/train.png)
* POST /encodeface/
 * Encodes Face in an Image and saves it in database and returns response message
   * Request:
      * Request Type -- multipart/form-data
      * parameters (key value pair)
         *  key = file , value = link to your file,type = file
         *  key = name, value = name of the person, type = text
    * Response:
         ```python
            {
                "message": "Success",
                "code": "0"
            }
         ```
        
#### Identifying the faces(image encoding)
 ![alt text](https://github.com/ananthkhegde/Face-Recognition-Based-Attendance-Service/blob/master/assets/response.png)      
  * POST /identifyface/
    * Recognizes Face(s) in an Image and returns matching face id/name.
    * Request:
        *    Request Type -- multipart/form-data
        * parameters (key value pair)
         *  key = file , value = link to your file,type = file
    * Response:
         ```
           [
              {
                  "faceId": 1,
                  "faceName": "Venkat"
              },
              {
                  "faceId": 2,
                  "faceName": "Ananth"
              }
           ]   
         ```
