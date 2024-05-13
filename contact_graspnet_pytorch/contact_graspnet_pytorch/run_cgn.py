import inference as cgn_inference
from contact_graspnet_pytorch import config_utils


global_config = config_utils.load_config('checkpoints/contact_graspnet', batch_size=forward_passes, arg_configs=[])

print(str(global_config))
# print('pid: %s'%(str(os.getpid())))

cgn_inference.inference(global_config, 
              ckpt_dir,
              input_paths, 
              local_regions=True, 
              filter_grasps=True, 
              skip_border_objects=False,
              z_range = [0.2,1.8],
              forward_passes=1,
              K=None,)
