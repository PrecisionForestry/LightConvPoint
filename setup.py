from setuptools import setup, find_packages
from torch.utils import cpp_extension
import sys

print(sys.argv)

if "--nocompile" in sys.argv:
    print("LIGHTCONVPOINT -- PYTHON MODULES")
    ext_modules=[]
    cmdclass={}
else:
    print("LIGHTCONVPOINT -- COMPILING CPP MODULES")
    ext_modules=[
       cpp_extension.CppExtension(
           "lightconvpoint.knn_c_func",
           [
               "lightconvpoint/src/knn.cxx",
               "lightconvpoint/src/knn_bind.cxx",
               "lightconvpoint/src/knn_random.cxx",
               "lightconvpoint/src/knn_farthest.cxx",
               "lightconvpoint/src/knn_convpoint.cxx",
               "lightconvpoint/src/knn_quantized.cxx",
           ],
           extra_compile_args=["-fopenmp"],
           extra_link_args=["-fopenmp"],
       )
    ]
    cmdclass={"build_ext": cpp_extension.BuildExtension}
    #sys.argv.remove("--compile")

setup(
    version="0.1.0",
    packages=find_packages(),  # ✅ This line adds all Python modules
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    include_package_data=True,  # Optional: add this if you want to include config/data files
)
