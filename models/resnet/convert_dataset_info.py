
import json
import struct
import sys


def convert(input_path, output_path):
    with open(input_path) as f:
        dataset_info = json.load(f)

    num_classes = dataset_info['default']['features']['label']['num_classes']
    
    names =  dataset_info['default']['features']['label']['names']

    with open(output_path, 'wb') as f:
        f.write(struct.pack("I", num_classes))
        for i in range(num_classes):
            bytes = names[i].encode('utf-8')
            f.write(struct.pack("I", len(bytes)))
            f.write(bytes)

# def test(input_path):
#     with open(input_path, 'rb'):
#         struct.unpack('I')

if __name__ == '__main__':
    # python convert_dataset_info.py dataset_info.json dataset_info.bin
    if len(sys.argv) == 1:
        print(f'[dataset_info json] [data_info bin]')
        exit()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    convert(input_path, output_path)

