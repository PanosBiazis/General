# import cx_Freeze as cx

import importlib
import pkg_resources
import importlib.metadata

# cxvol=cx.__version__

# print("The version of cxfreeze is ",cxvol)

# import importlib

# def get_module_version(module_name):
#     module = importlib.import_module(module_name)
#     if hasattr(module, '__version__'):
#         return module.__version__
#     else:
#         return "Version not found"

# # Check version of cx_Freeze
# print("The version of cx_Freeze is", get_module_version('cx_Freeze'))

# # Check version of other modules
# print("The version of requests is", get_module_version('requests'))
# print("The version of numpy is", get_module_version('numpy'))

# import pkg_resources

# def get_module_version(module_name):
#     try:
#         return pkg_resources.get_distribution(module_name).version
#     except pkg_resources.DistributionNotFound:
#         return "Version not found"

# # Check version of cx_Freeze
# print("The version of cx_Freeze is", get_module_version('cx_Freeze'))

# # Check version of other modules
# print("The version of requests is", get_module_version('requests'))
# print("The version of numpy is", get_module_version('numpy'))


# import importlib.metadata

# def get_module_version(module_name):
#     try:
#         return importlib.metadata.version(module_name)
#     except importlib.metadata.PackageNotFoundError:
#         return "Version not found"

# # Check version of cx_Freeze
# print("The version of cx_Freeze is", get_module_version('cx_Freeze'))

# # Check version of other modules
# print("The version of requests is", get_module_version('requests'))
# print("The version of numpy is", get_module_version('numpy'))


def get_module_version(module_name):
    
    module = importlib.import_module(module_name)
    
    if hasattr(module, '__version__'):
    
        return module.__version__
    
    else:
    
         return "Version not found"


module_name=str(input("Give a module you want to check >>"))

# Check version of every module

print("The version of "+module_name+" is ", get_module_version(module_name))

choice=str(input("Do you want to check another module? (y/n) >>"))


if choice == 'y':
    
    times=int(input("How many times do you want to check the modules? >>"))
    
    for times in range (0,times,1) :
        
        module_name=str(input("Give a module you want to check >>"))
        
        print("The version of "+module_name+" is ", get_module_version(module_name))
        
elif choice == 'n':
    
    print("Goodbye")

else:
    print("Invalid choice!!!\a\nTRY AGAIN!!!")