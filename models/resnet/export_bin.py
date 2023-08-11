'''
This script exports the resnet weights in resnet.bin format
'''
import json
import os
import struct
import sys
from pathlib import Path
import torch


def export(p, state_dict, filepath='model.bin'):
    '''export the model weights in fp32 into .bin file to be read from c'''
    f = open(filepath, 'wb')

    def serialize(key):
        print(f'writing {key}, shape {state_dict[key].shape}...')
        t = state_dict[key].contiguous().view(-1).type(torch.float32).detach().numpy()
        f.write(memoryview(t))
        # del state_dict[key]

    layers = p['layers']
    header = struct.pack(
        'iiii',
        layers[0], layers[1], layers[2], layers[3]
    )
    f.write(header)

    serialize('conv1.weight')
    serialize('bn1.running_mean')
    serialize('bn1.running_var')
    serialize('bn1.weight')
    serialize('bn1.bias')

    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.conv1.weight')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.bn1.running_mean')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.bn1.running_var')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.bn1.weight')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.bn1.bias')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.conv2.weight')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.bn2.running_mean')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.bn2.running_var')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.bn2.weight')
    for i in range(len(layers)): 
        for j in range(layers[i]):
            serialize(f'layer{i + 1}.{j}.bn2.bias')

    for i in range(1, len(layers)):
        serialize(f'layer{i + 1}.0.downsample.0.weight')
        serialize(f'layer{i + 1}.0.downsample.1.running_mean')
        serialize(f'layer{i + 1}.0.downsample.1.running_var')
        serialize(f'layer{i + 1}.0.downsample.1.weight')
        serialize(f'layer{i + 1}.0.downsample.1.bias')

    serialize('fc.weight')
    serialize('fc.bias')


def load_and_export(model_path: str, output_path: str):
    params_path = os.path.join(model_path, 'params.json')
    with open(params_path) as f:
        params = json.load(f)
        print(params)
    
    model_paths = sorted(list(Path(model_path).glob('resnet*.pth')))
    model = torch.load(model_paths[0], map_location='cpu')
    
    state_dict = {}
    for name in list(model):
        tensors = model[name]
        print(f'model name: {name}, shape: {model[name].shape}, type: {model[name].dtype}')
        state_dict[name] = tensors
    del model
    export(params, state_dict, output_path)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('[resnet model folder path] [output path]')
        exit()

    model_path = sys.argv[1]
    output_path = sys.argv[2]
    load_and_export(model_path, output_path)

