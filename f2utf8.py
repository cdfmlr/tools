#!python3

# f2utf8
# Yet another util converts files to UTF-8.
# CDFMLR 2021

import os
import chardet
import argparse

def detect_decode(file_content: bytes) -> str:
    """detect_decode detect the encoding of file_content,
     then decode file_content on the detected encoding.

    # Copy from github.com/cdfmlr/pyflowchart #
    # Copyright (c) 2020 CDFMLR   MIT License #

    If the confidence of detect result is less then 0.9,
    the UTF-8 will be used to decode. PyFlowchart is
    designed to convert Python 3 codes into flowcharts.
    And Python 3 is coding in UTF-8 in default. So only
    if we can make sure the file is not UTF-8 encoded (
    i.e. confidence > 0.9) than we will use that no
    default encoding to decoded it.

    Args:
        file_content: bytes: binary file content to decode

    Returns:
        str: decoded content
    """
    # detect encoding
    detect_result = chardet.detect(file_content)
    # print("DEBUG detect_result =", detect_result)

    encoding = detect_result.get("encoding")
    confidence = detect_result.get("confidence")

    if confidence < 0.9:
        encoding = "UTF-8"

    # decode file content by detected encoding
    try:
        content = file_content.decode(encoding=encoding, errors='ignore')
    except TypeError:  # TypeError: decode() argument 1 must be str, not None
        content = file_content.decode()

    return content


def convert(file, outfile):
    # read file content: binary
    file_content: bytes = file.read()
    # detect encoding and decode file content by detected encoding
    content = detect_decode(file_content)
    # write
    outfile.write(content.encode("utf-8"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='convert file to utf-8 encoded')

    # file: open as binary, detect encoding and decode in main later
    parser.add_argument('file', type=str)
    # outfile: write utf-8 in binary
    parser.add_argument('-o', '--outfile', type=str, default="")
    
    args = parser.parse_args()
    

    of = args.outfile
    if not of:
        l = args.file.split('.')
        l.insert(-1, 'utf8')
        of = '.'.join(l)
    
    with open(args.file, "rb") as file:
        with open(of, "wb") as outfile:
            convert(file, outfile)

