import time
import torch

size = 6000

a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start

print(f"CPU time: {cpu_time:.3f} seconds")

a_gpu = a_cpu.to("cuda")
b_gpu = b_cpu.to("cuda")

_ = a_gpu @ b_gpu
torch.cuda.synchronize()

start = time.time()
c_gpu = a_gpu @ b_gpu
torch.cuda.synchronize()
gpu_time = time.time() - start

print(f"GPU time: {gpu_time:.3f} seconds")
print(f"Speedup: {cpu_time / gpu_time:.1f}x")
print("GPU:", torch.cuda.get_device_name(0))
