# coding=utf-8

# Copyright (c) 2018 - <tao.zhang@moji.com>

"""
Author: tao.zhang
Create Date: 2019/5/24
@Software: PyCharm
descirption:
"""
import random


class RandomStr(object):
    def __init__(self, str_len=4):
        self.randon_chr_list = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.str_len = str_len

    @classmethod
    def gen_str(cls, str_len=4):
        obj = cls(str_len)
        # return "".join([random.choice(obj.randon_chr_list) for _ in range(obj.str_len)])
        return "".join(random.sample(obj.randon_chr_list, str_len))


if __name__ == "__main__":
    for _ in range(10):
        print(RandomStr.gen_str())
