#!/usr/bin/env python
# coding=utf-8

import json
import time
import os
import sys, traceback 
from logger import logger

#######函数列表######
# print_traceback -- 打印堆栈信息
# get_val -- 默认取值
# time_to_str -- 时间戳转字符串
# str_to_time -- 字符串转为时间戳
# check_has_keys -- 检查字段有无相关key
# split_list -- 数组分块，每块n个元素
# list_to_str -- 数组转为字符串
# encode_json -- json encode
# decode_json -- json decode
# is_exist_path -- 判断文件是否存在
# count_str -- 计算字符串长度(支持中文)
# cut_str -- 截取前N个字符(支持中文)
# is_chinese_char -- 字符是否是中文
# log2file 打印到文件


#打印堆栈信息
def print_traceback():
	err_msg = traceback.format_exc()
	logger.error("traceback begin------------>")
	logger.error("%s" %(str(err_msg)))
	logger.error("traceback   end<------------")
	

#取dict的值
def get_val(_dict, _key, _def=None):
	if _key not in _dict or _dict[_key] == None:
		return _def
	return _dict[_key]
	
	
#时间戳转字符串
def time_to_str(i_date, _format):
	return str(time.strftime(_format, time.localtime(i_date)))


#字符串转为时间戳
def str_to_time(str_time, _format):
	return int(time.mktime(time.strptime(str_time, _format)))
	

#检查dict 
def check_has_keys(_dict, keys):
	for key in keys:
		if key not in _dict:
			return False
	return True


# list分块
def split_list(_list, n):
	if not isinstance(_list, list) or n <= 0:
		return []
	
	_list_len = len(_list)
	if _list_len < n: # 分1块的情况
		return [_list]
	
	retlist = [_list[i:i+n] for i in range(0, _list_len, n)]
	
	return retlist


# list按指定分隔符拼接字符串
def list_to_str(_list, sep=","):
	return sep.join(_list)


#json encode
def encode_json(_dict, show_chinese=False):
	if show_chinese:
		return json.dumps(_dict, separators=(',',':'), ensure_ascii=False)
	return json.dumps(_dict, separators=(',',':'))


#json decode
def decode_json(_str):
	try:
		return json.loads(_str)
	except Exception, e:
		return None

	
# 文件是否存在
def is_exist_path(_path):
	return os.path.exists(_path)


# 计算字符个数
def count_str(_str, use_utf8=False):
	_local_str = _str
	if use_utf8:
		_local_str = _str.decode("utf-8")
	return len(_local_str)


# 按偏移截取字符串
def cut_str(_str, _begin, _end, use_utf8=False):
	_local_str = _str
	if use_utf8:
		_local_str = _str.decode("utf-8")
	
	return _local_str[_begin:_end]


# 判断是否是中文字符(使用前请decode成utf-8)
def is_chinese_char(_char):
	return _char >= u'\u4e00' and _char <= u'\u9fff'


#记录文件
def log2file(msg, second_dir="processed"):
	#创建目录
	log_dir = "./logs/%s/" %(second_dir)
	if not is_exist_path(log_dir):
		os.makedirs(log_dir)
	
	filename = log_dir + str(time.strftime('%Y%m%d',time.localtime(time.time())))+".log"
	
	msg = msg + "\r\n"
	
	#写文件
	f = open(filename,'a')
	f.write(msg)
	f.close()


#记录文件
def log2transfilebymin(msg, second_dir="transdata", fileidx=None):
	#按日期分目录
	localtime = time.localtime(time.time())

	#创建按天的目录
	day = str(time.strftime('%Y%m%d', localtime))
	log_dir = "./%s/%s/" %(second_dir, day)
	if not is_exist_path(log_dir):
		os.makedirs(log_dir)
	
	#写按分钟的文件
	if fileidx == None:
		fileidx = ""
	filename = log_dir + str(fileidx) + "_" + str(time.strftime('%H%M', localtime))+".log"
	
	msg = msg + "\r\n"
	
	#写文件
	f = open(filename,'a')
	f.write(msg)
	f.close()
