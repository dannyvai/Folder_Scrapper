# -*- coding: utf-8 -*-

from pylab import *

def show_stats(n_dirs,n_files,file_ext_dict,private_data):
    file_ext_dict = eval(file_ext_dict)
    
    #ax = axes([0.1, 0.1, 0.8, 0.8])
    
#    total_objects = int(n_dirs) + int(n_files)
#    
#    dirs_frac = ( float(n_dirs) / float(total_objects) )* 100
#    files_frac = (float(n_files) / float(total_objects)) * 100
#
#    labels =    [ 'dirs','files' ]
#    fracs =     [ dirs_frac,files_frac ]
#    explode =   [ 0.05,0.05]
#    
#    pie(fracs, explode=explode, labels=labels,
#                autopct='%1.1f%%', shadow=True, startangle=90)
    
    total_size = 0
    labels = []
    n_files_frac = []
    size_frac = []
    
    for key in file_ext_dict.keys():
        ext = file_ext_dict.get(key)
        labels.append(key)
        total_size = total_size + ext['total_size']
        n_files_frac.append(float(ext['n_files'])/float(n_files))
    explode = [0]*len(labels)
    
    for key in file_ext_dict.keys():
        ext = file_ext_dict.get(key)
        size_frac.append(float(ext['total_size'])/float(total_size))    
    
    figure(1, figsize=(6,6))
    pie(n_files_frac, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
    figure(2, figsize=(6,6))            
    pie(size_frac, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
    show()
