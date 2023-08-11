
import json
import struct
import sys
import torch
import torchvision

from pathlib import Path


def convert(input_path, params_path, output_path):
    with open(params_path) as f:
        params = json.load(f)
    input_shape = params['input_shape']
    img_shape = input_shape[2:]
    filtered = list(Path(input_path).glob('[0-9]*.jpg'))

    fi = open(output_path, 'wb')
    header = struct.pack(
        'iiii',
        input_shape[0], input_shape[1], input_shape[2], input_shape[3], 
    )
    fi.write(header)

    for file in filtered:
        file = f'{file}'
        img = torchvision.io.read_image(file)
        print(f'{file} shape is {img.shape}')
        resize = torchvision.transforms.Resize(size=img_shape,)
        img_r = resize(img)
        t = img_r.contiguous().view(-1).type(torch.float32).detach().numpy()
        fi.write(memoryview(t))
        print(f'{file} shape is {img_r.shape}')
        torchvision.io.write_jpeg(img_r, f'resize_{file}')


if __name__ == '__main__':
    # python ../convert_image.py ./ ../resnet34/params.json ./resnet34_input.bin 
    if len(sys.argv) == 1:
        print('[src forder] [params json] [dst bin] ')
        exit()
    
    input_path = sys.argv[1]
    params_path = sys.argv[2]
    output_path = sys.argv[3]

    convert(input_path, params_path, output_path)

