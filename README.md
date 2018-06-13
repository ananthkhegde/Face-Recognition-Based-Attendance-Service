# Face Recognition

Recognize faces from Python with
the world's simplest face recognition library [python face_recognition](https://github.com/ageitgey/face_recognition/).

This service exposes functionality to train the face of a particular person
and also to predict the face of the person or set of faces in a group photo.

Built using [dlib](http://dlib.net/)'s state-of-the-art face recognition
built with deep learning. The model has an accuracy of 99.38% on the
[Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) benchmark.

## Installation

Requirements:
* Python 3+
* numpy
* scipy
* dlib (prerequisites: install cmake(min version required 3.4)
* face_recognition
* django
* django rest framework
* coreapi (for api documentation)
* postgre sql

## Guide to setting up database
* restore database backup file from [here](https://github.com/CSTEPBLR/Face-Recognition-Service/blob/master/assets/anganwadi_db)
* edit the database connection in setting.py in project file to connect locally

## Instruction to run project

* save project to local directory
* go to project folder i.e cd facecognition and execute below command
* python manage.py runserver 8000


## Guide to installing and running Rest service through API Client

* Install rest api client
https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwiDzOrtmM_VAhWMo48KHYfyC9UQFgglMAA&url=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fpostman%2Ffhbjgbiflinjbdggehcddcbncdddomop%3Fhl%3Den&usg=AFQjCNE_Yq59TT1ZExzJ68FTldg4ho_lGw

### Rest API
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
         
  * POST /identifyface/
    * Recognizes Face(s) in an Image and returns matching face id/name.
    * Request:
        *    Request Type -- multipart/form-data
        * parameters (key value pair)
         *  key = file , value = link to your file,type = file
    * Response:
         ```python
           [
              {
                  "id": 1,
                  "name": "user1"
              },
              {
                  "id": 2,
                  "name": "user2"
              }
           ]   
         ```
