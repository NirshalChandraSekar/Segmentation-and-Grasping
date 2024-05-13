import numpy as np
import cv2
import matplotlib.pyplot as plt


data_demo = np.load('test_data/output_depth_image.npy', allow_pickle=True).item()

print(data_demo.keys())

K = data_demo['K']

# actual_data = np.load('test_data/7_image_array.npy', allow_pickle=True)

# print(actual_data.shape)

# ## Intial frame
# rgb_data_start = actual_data[10,:,:,0:3]
# depth_data_start = actual_data[10,:,:,3]

# rgb_data_end = actual_data[75,:,:,0:3]
# depth_data_end = actual_data[75,:,:,3]

cv2.imshow('RGB', data_demo['rgb'])
cv2.waitKey(0)
cv2.destroyAllWindows()