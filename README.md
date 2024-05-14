<p align="center">
  <h2 align="center">SEGMENTATION AND GRASPING PIPELINE USING CONTACT GRASPNET AND SEGMENT ANYTHING MODEL</h2>
</p>

<img src="https://github.com/NirshalChandraSekar/Segmentation-and-Grasping/blob/cc3f69cdf154f75adbff375ed20350e29e39c3fd/image.png">

### About the project
The project focuses on creating a pipeline for object segmentation and grasp generation for real-world robots. Utilizing the Contact GraspNet model from Nvidia for grasp generation and the Segment Anything model from Facebook for object segmentation, the pipeline enables users to segment objects in an image and generate grasp poses. It provides various grasp options in the camera coordinate frame for each object along with corresponding grasp scores.

### Demo
Watch the full video here: https://drive.google.com/file/d/1uo-crcU8O-MHP1N5hgxUDoyyvciFkpbv/view?usp=sharing

### Usage
*The pipeline is tested in Python 3.9 version*
##### Required Libraries/Tools
1) Speech Recognition Module - To recognize the input audio from the user and convert it to text
   ```
   pip install SpeechRecognition
   ```
2) pyttsx3 Module - To convert the output text into speech to the user
   ```
   pip install pyttsx3
   ```
3) PyBullet - Physics simulation package
   ```
   pip install pybullet
   ```
4) Guidance - For controlling langiage models
   ```
   pip install guidance
   ```
--> Clone this repo on your local directory, and install all the above mentioned packages. 

--> Navigate to the "llm.py" file and set your OpenAI API key in line 8.

--> Run the main.py file on your terminal. Input '0' to start your conversation with the robot, and when you want to stop the conversation just say "STOP" out loud, and the simulation will rest and wait for you to input 0 again to continue your next conversation.

### Evaluation
For evaluations, we enabled the LLM to track and store the user's sentiment on a scale of 0 to 10 for each prompt, with 0 being extremely negative and 10 being extremely positive. When the user stops the conversation, we return this tracked sentiments ovre the conversation as a list and plot them to see how the user's sentiment is being changed over the period of the conversation. The goal is to try and flip the sentiment from a negative state to a positve state if the user is initially in a negative mood, and if the person is initially in a positive mood, then the llm should try and maintain this positivity of the user during the conversation.

Sample plots of sentiment over different conversations:
<img src="https://github.com/NirshalNiru/Human-Robot-Interaction-using-LLM/blob/b8673fd4ec24afbbebf980239f22380117c6f870/plots.png">

