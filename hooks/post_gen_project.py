import os
import shutil


lisence = '{{cookiecutter.lisence}}'

def delete_resource(resource):
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)


if lisence == "None":
    delete_resource("LICENSE")

