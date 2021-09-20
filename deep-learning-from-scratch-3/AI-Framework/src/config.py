# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:53:21 2020

@author: sample
"""

import os
import configparser


INI_FILE = '../parameter/config.ini'

inifile = configparser.ConfigParser()
inifile.read(INI_FILE, 'UTF-8')


def get_parameter(kind, section, item):
    import common.logger

    if kind == "int":
        parameter = inifile.getint(section, item)
    elif kind == "float":
        parameter = inifile.getfloat(section, item)
    elif kind == "boolean":
        parameter = inifile.getboolean(section, item)
    elif kind == "string":
        parameter = inifile.get(section, item)
    else:
        parameter = "parameter not found"

    log_mesg = "[" + section + "]" + item + " : " + str(parameter)
    common.logger.app_logger.debug(log_mesg)

    return parameter


# パラメータ取得
config_log = inifile.get('config', 'log')
syslog_facility = inifile.get('syslog', 'facility')
syslog_option = inifile.get('syslog', 'option')
database = get_parameter('string', 'database', 'database')
line_notify_api = get_parameter('string', 'line', 'notify_api')
line_notify_token = get_parameter('string', 'line', 'notify_token')
translation_language = get_parameter('string', 'translation', 'language')
translation_dictionary_dir = get_parameter('string', 'translation', 'dictionary_dir')
translation_dictionary_file = get_parameter('string', 'translation', 'dictionary_file')
function_param_int = get_parameter('int', 'function', 'param_int')
function_param_float = get_parameter('float', 'function', 'param_float')
function_param_boolean = get_parameter('boolean', 'function', 'param_boolean')


def init():
    print()


def logging_paramter():
    import common.logger
    common.logger.app_logger.debug("[config]log:%s", config_log)
    common.logger.app_logger.debug("[config]facility:%s", syslog_facility)
    common.logger.app_logger.debug("[config]option:%s", syslog_option)
