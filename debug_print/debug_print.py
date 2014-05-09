# !/usr/bin/env python
# printf style debugging

from __future__ import print_function
import logging
import sys
import datetime
import os.path

_inspect = None
try:
    import inspect as _inspect
except:
    pass

JUST_PRINT, JUST_LOG, LOG_AND_PRINT = "JUST_PRINT", "JUST_LOG", "LOG_AND_PRINT"
_log_print_mode = JUST_PRINT
_logger = None
default_settings = dict(
    with_filename=True,
    with_lineno=True,
    with_calling_func_name=True,
    with_expr=True,
    with_result_type=True,
    with_result=True,
    log_print_mode=JUST_PRINT,
    logger=logging.getLogger(__name__),
    log_level=logging.DEBUG,
    print_level=logging.DEBUG
)
_logger = logging.getLogger(__name__)

_logger.setLevel(logging.NOTSET)
default_settings["log_file"] = os.path.join("/tmp", "log_" + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
#if mode in [JUST_LOG, LOG_AND_PRINT]:
#    _logger.addHandler(logging.FileHandler(default_settings["log_file"]))
#if mode in [JUST_PRINT, LOG_AND_PRINT]:
#    _logger.addHandler(logging.StreamHandler())

def set_debug_print_mode(mode, logger=None):
    default_settings["log_print_mode"] = mode
    if mode in [JUST_LOG, LOG_AND_PRINT]:
        if logger:
            default_settings["logger"] = logger
        elif default_settings["logger"]:
            pass
        else:
            default_settings["logger"] = logging.getLogger()  #use root logger

info_sep = "\n"
def debug_print(expression, filestream=sys.stderr):
    filename = None
    lineno = None
    calling_func = None
    result = None

    s = ""
    try:
        stack = _inspect.stack()
        frame, filename, lineno, calling_func_name, _, _ = stack[1]
        if default_settings["with_filename"]:
            s += info_sep + "File: " + filename
        if default_settings["with_lineno"]:
            s += info_sep + " lineno:" + repr(lineno)
        if default_settings["with_calling_func_name"]:
            s += info_sep + "calling_func_name:" + calling_func_name
        try:
            result = eval(expression,globals(), frame.f_locals)
        except Exception, e:
            result = e

    except Exception, e:
        print("Could not get frame info," + repr(e), end='', file=filestream)
    finally:
        del stack

    result_type = type(result)

    if default_settings["with_expr"]:
        s += info_sep + "The result of expr " + expression +" is:"
    if default_settings["with_result_type"]:
        s += "(of type:" + repr(result_type) + ")"

    s += " result:" + repr(result)
    if default_settings["log_print_mode"] in [JUST_PRINT, LOG_AND_PRINT]:
        print(s, file=filestream)
    if default_settings["log_print_mode"] in [JUST_LOG, LOG_AND_PRINT]:
        default_settings["logger"].log(default_settings["level"], s)
    return result


def debug_message(message, filestream=sys.stderr):
    assert isinstance(message, basestring)
    filename = None
    lineno = None
    calling_func = None
    try:
        stack = _inspect.stack()
        _, filename, lineno, calling_func_name, _, _ = stack[1]
        s = ""
        if default_settings["with_filename"]:
            s += info_sep + "File: " + filename
        if default_settings["with_lineno"]:
            s += info_sep + "lineno:" + repr(lineno)
        if default_settings["with_calling_func_name"]:
            s += info_sep + "calling_func_name:" + calling_func_name
        s = message + s

        if default_settings["log_print_mode"] in [JUST_PRINT, LOG_AND_PRINT]:
            print(s, file=filestream)
        if default_settings["log_print_mode"] in [JUST_LOG, LOG_AND_PRINT]:
            default_settings["logger"].log(default_settings["level"], s)

    except Exception, e:
        print("Could not get frame info," + repr(e), end='', file=filestream)
    finally:
        del stack


def debug_trace():
    """"based on showme.trace"""
    pass
