# Drowsiness_Detection_System
The repo consists the code for computer vision project(detection of eye)

Created an end to end computer vision project

Built a Drowsiness Detector using open cv python and Machine Learning. Delve deep into Deep Learning, used MobileNet transformer model to accomplish the objective.

### Dataset: 

The dataset consists of 2 folders. One with images which holds open eye and the other folder with closed eye

### Objective:

• We can use this model for predicting if the eye is closed or open and also it can be used for mainly Driver Drowsiness Detection

• This system can be helpful to cab drivers which may prevent both customers and the drivers from accident as one can use this system with an alert in their vehicles/cabs

### Project is divided into 2 segments-

•	Machine Learning/Deep Learning Segment
•	Deployment Segment

👉 Deep Learning Segment: Used MobileNet, a light weight transformer model; as my base model and then built my final model on top of it with a Dense layer. Achieved about 99% accuracy on training data and 100% on test data.

👉 Deployment Segment: The trained model is saved and loaded. Created the webapp using streamlit and using ngrok to host the model. ngrok will take the model from the local server and host it on to the web(public server). 

### This is how the webapp looks like => 

![image](https://user-images.githubusercontent.com/111883941/200590151-f33ba447-6828-444a-b971-7fe3f4706037.png)

![image](https://user-images.githubusercontent.com/111883941/200590601-f53c7d94-f32b-4281-9503-08dbc35aa5db.png)

![image](https://user-images.githubusercontent.com/111883941/200591165-dbc8886d-3552-4615-91b5-8fccbdefddfb.png)

