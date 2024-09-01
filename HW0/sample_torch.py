import torch
print("\n\n")
print(torch.__version__) 
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))
print("\n\n")