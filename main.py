from Complete_SAM_Pipeline import SAM
from cgn.contact_graspnet_pytorch.inference import CGN
import numpy as np

test = np.load("output_1.npy", allow_pickle=True).item()
print("test", test)
rgb = test['rgb']
depth = test['depth']
k_matrix = test['K']

sam = SAM()
input_for_cgn = sam.main("direct", rgb, depth, k_matrix)

np.save("input_for_cgn.npy", input_for_cgn)

cgn = CGN(input_path="input_for_cgn.npy", K=k_matrix, z_range = [0.2,10], visualize=True, forward_passes=3)
pred_grasps, grasp_scores, contact_pts, gripper_openings = cgn.inference()

print("Pred Grasps length: ",len(pred_grasps))