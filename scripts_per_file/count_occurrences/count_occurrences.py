# -*- coding: utf-8 -*-

def foreach_file_do(filepath, filename, file_ext, private_data):
    if 'file_count' not in private_data.keys():
        private_data['file_count'] = 1
    else:
        private_data['file_count'] = private_data['file_count'] + 1

    return private_data
