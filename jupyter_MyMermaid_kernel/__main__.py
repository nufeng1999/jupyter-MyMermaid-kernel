from ipykernel.kernelapp import IPKernelApp
from .kernel import MermaidKernel
IPKernelApp.launch_instance(kernel_class=MermaidKernel)
