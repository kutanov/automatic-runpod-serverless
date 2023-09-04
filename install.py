import launch

# TODO: add pip dependency if need extra module only on extension

if not launch.is_installed("runpod"):
     launch.run_pip("install runpod", "requirements for RunPodServerless")
