import torch

# System check
if torch.cuda.is_available():
    print("System Check: GPU accessible.")
else:
    print("System Check: Fail on installing Pytorch GPU version")
