# freeCodeCamp Advanced CV course
(Course: https://www.youtube.com/watch?v=01sAkU_NvOY)

## Installation
```bash
git clone https://github.com/balazsborsos/fCC-Advanced-CV.git
```

Create a virtual environment (or in your base environment) with Anaconda or any virtual environment manager (see Anaconda example below): 

```bash
conda create -n ffc-cv python=3.8
conda activate ffc-cv
pip install -r requirements.txt
```

## Project description
In this project I practiced state of the art computer vision techniques by building five projects with libraries such as OpenCV and Mediapipe. First, I've implemented core techniques like hand tracking, pose estimation, then I went on to create projects with real world applications using these tools.

### Gesture Volume Control
With this project one is able the control the system's volume setting using only their hands, where the distance between the thumb and index finger determines the volume.

### AI Virtual Painter
This tool let's the user paint virtually on their camera feed using their fingers and hands. There are multiple colors to choose from, and also there is the option to erase. It is made possible with a module that keeps track of which finger is used and a canvas that is merged to the camera feed in real time.

### AI Virtual Mouse
With the virtual mouse it is possible to control your computer using only your hands and a camera. It perfectly intregrates into Windows with the autopy package to have the full functionality of a real mouse.

### Pose estimation
This module can be used later in more advanced project, it is currently able to detect the position of a person's joints from a video clip/feed. It could be used to recommend better technique during workouts or have a companion app that couns the repetitions for you and keeps track of your form.
