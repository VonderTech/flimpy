import torch

# Check if CUDA is available
print("CUDA Available:", torch.cuda.is_available())
# Print CUDA version
print("CUDA Version:", torch.version.cuda)
