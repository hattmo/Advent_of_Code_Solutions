import os
from typing import List
import math

def to_bin_str(data:int,print_len=8):
    out = ""
    while data > 0:
        if data % 2 == 0:
            out = "0" + out
        else:
            out = "1" + out
        data = data // 2
    while len(out) < print_len:
        out = "0" + out
    return out

class Bit_Reader:
    def __init__(self,data:bytes):
        self.data = data
        self.index:int = 0
        self.offset:int = 0

    def read_bits(self,num_bits:int)->int:
        target_offset = self.offset + num_bits
        target_index = self.index + target_offset // 8
        target_offset %= 8
        if target_index == self.index:
            out_data = ((self.data[self.index] << self.offset) % 256) >> self.offset + (8 - target_offset)
            self.index = target_index
            self.offset = target_offset
            return out_data

        out_data = (((self.data[self.index] << self.offset) % 256) >> self.offset)
        for i in range(self.index + 1, target_index):
            out_data *= 256
            out_data += self.data[i]
        out_data *= pow(2,target_offset)
        if target_offset != 0:
            out_data += self.data[target_index] >> (8 - target_offset)
        self.index = target_index
        self.offset = target_offset
        return out_data


class Result:
    def __init__(self,bits_read:int,data:List[int]):
        self.bits_read = bits_read
        self.data = data

def done_processing(packets_read,bytes_read,packet_limit,byte_limit):
    if packet_limit != 0:
        return packets_read >= packet_limit
    else:
        return bytes_read >= byte_limit

def parse_packets(reader:Bit_Reader,packet_limit=0,bit_limit=0):
    values:List[int] = list()
    packets_read:int = 0
    bits_read:int = 0
    while not done_processing(packets_read,bits_read,packet_limit,bit_limit):
        version = reader.read_bits(3)
        packet_type_id = reader.read_bits(3)
        bits_read += 6

        if packet_type_id == 4:
            data = 0
            more_bits = True
            while more_bits:
                if reader.read_bits(1) == 0:
                    more_bits = False
                data *= 16
                data += reader.read_bits(4)
                bits_read += 5
            values.append(data)
        else:
            length_type = reader.read_bits(1)
            result: Result
            if length_type == 0:
                total_length = reader.read_bits(15)
                bits_read += 16
                result = parse_packets(reader,bit_limit=total_length)
                bits_read += result.bits_read
            else:
                number_sub_packets = reader.read_bits(11)
                bits_read += 12
                result = parse_packets(reader,packet_limit=number_sub_packets)
                bits_read += result.bits_read
            if packet_type_id == 0:
                values.append(sum(result.data))
            if packet_type_id == 1:
                values.append(math.prod(result.data))
            if packet_type_id == 2:
                values.append(min(result.data))
            if packet_type_id == 3:
                values.append(max(result.data))
            if packet_type_id == 5:
                values.append(1 if result.data[0] > result.data[1] else 0)
            if packet_type_id == 6:
                values.append(1 if result.data[0] < result.data[1] else 0)
            if packet_type_id == 7:
                values.append(1 if result.data[0] == result.data[1] else 0)

        packets_read += 1
    return Result(bits_read, values)

def main():
    with open(f"{os.path.dirname(__file__)}/input.txt","r") as in_file:
        data = bytes.fromhex(in_file.read())
        reader = Bit_Reader(data)
        print(f"solution: {parse_packets(reader,packet_limit=1).data[0]}")


if __name__ == "__main__":
    main()


