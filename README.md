<p align="center">
  <h2 align="center">SEGMENTATION AND GRASPING PIPELINE USING SEGMENT ANYTHING MODEL AND CONTACT GRASPNET</h2>
</p>

<img src="https://github.com/NirshalChandraSekar/Segmentation-and-Grasping/blob/cc3f69cdf154f75adbff375ed20350e29e39c3fd/image.png">

### About the project
The project focuses on creating a pipeline for object segmentation and grasp generation for real-world robots. Utilizing the Contact GraspNet model from Nvidia for grasp generation and the Segment Anything model from Facebook for object segmentation, the pipeline enables users to segment objects in an image and generate grasp poses. It provides various grasp options in the camera coordinate frame for each object along with corresponding grasp scores.

### Demo
Watch the full video here: https://drive.google.com/file/d/1ks-L4mX4VIew_cKRrXlJG7AtwPemp42E/view?usp=sharing

### Usage
*The pipeline is tested in Python 3.9 version*
##### Required Libraries/Tools
1) Contact GraspNet - Follow the steps in the official repo install all the required packages (https://github.com/elchun/contact_graspnet_pytorch)
2) Segment Anything Model 
   ```
   pip install git+https://github.com/facebookresearch/segment-anything.git
   ```
3) Realsense SDK
   ```
   pip install pyrealsense2
   ```

--> Clone this repo on your local directory, and install all the above mentioned packages. 

--> Before running the main.py file, make sure you have specified the images and the camera matrix in the main.py file if you are directly passing the images. If you are streaming from an intel realsense camera make sure the camera is connected, and change the depth scale value in the Complete_SAM_Pipeline.py file based on the model of your realsense camera.




