# -*- coding: utf-8 -*-

import os


def concat_directory(path_to_dir, path_to_outfile):
    """Function concatening part-* file in given directory

    Keyword arguments:
    path_to_dir     (string) -- path to directory
                                containing files to be concatenated
    path_to_outfile (string) -- path to output file
    """

    with open(path_to_outfile, 'w') as outfile:
        for part_file in [
            _ for _ in os.listdir(path_to_dir)
            if 'part' in _ and not _.endswith('.crc')
        ]:

            for line in part_file:
                outfile.write(line)
