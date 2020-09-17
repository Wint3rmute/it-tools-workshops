#!/usr/bin/env python 
import argparse
from builder import Builder
from os import path
import os
import traceback

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prometheus - a Markdown-based HTML presentation generator')
    parser.add_argument('-i', '--input', type=str, required=True)
    # parser.add_argument('-o', '--out', type=str, required=True)

    args = parser.parse_args()
    input_file_path = path.abspath(args.input)
    input_file_name = path.basename(input_file_path)
    output_file_path = path.join(
        os.path.dirname(__file__),
        'build',
        input_file_name.replace('.md', '.html')
    )
    # print(input_file_name)
    # exit()
    

    print(f'Building {output_file_path}...')
    try:
        b = Builder(input_file_path, output_file_path)

        b.build()


        os.system('notify-send "Build successful"')
        print(f'Build successful')
    except Exception as e:
        os.system(f'notify-send -u critical "{e}"')
        
        traceback.print_exc()