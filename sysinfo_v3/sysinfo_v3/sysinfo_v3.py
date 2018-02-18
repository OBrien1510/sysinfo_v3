'''
Created on 18 Feb 2018

@author: hugh
'''

import platform
import shutil

def main():
    print("Platform: ", platform.platform())
    total, used, free = shutil.disk_usage(__file__)
    print("total, used, free: " , total, used, free)
    return
