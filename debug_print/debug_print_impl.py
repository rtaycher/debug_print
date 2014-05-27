#!/usr/bin/env python
#printf style debugging

from __future__ import print_function
#import logging
import sys
#import datetime
#import os.path
import platform

_colorama = None
try:
    import colorama as _colorama
    _colorama.init()
except:
    pass
try:
    import inspect as _inspect
except:
    pass


##########################################
#copied/slightly changed from colorama by Jonathan Hartley
_CSI = '\033['

def _code_to_chars(code):
    return _CSI + str(code) + 'm'

class _AnsiEscapeSequences(object):
    FORE_BLACK   = _code_to_chars(30)
    FORE_RED     = _code_to_chars(31)
    FORE_GREEN   = _code_to_chars(32)
    FORE_YELLOW  = _code_to_chars(33)
    FORE_BLUE    = _code_to_chars(34)
    FORE_MAGENTA = _code_to_chars(35)
    FORE_CYAN    = _code_to_chars(36)
    FORE_WHITE   = _code_to_chars(37)
    FORE_RESET   = _code_to_chars(39)

    BACK_BLACK   = _code_to_chars(40)
    BACK_RED     = _code_to_chars(41)
    BACK_GREEN   = _code_to_chars(42)
    BACK_YELLOW  = _code_to_chars(43)
    BACK_BLUE    = _code_to_chars(44)
    BACK_MAGENTA = _code_to_chars(45)
    BACK_CYAN    = _code_to_chars(46)
    BACK_WHITE   = _code_to_chars(47)
    BACK_RESET   = _code_to_chars(49)

    STYLE_BRIGHT = _code_to_chars(1)

    STYLE_RESET_ALL = _code_to_chars(0)

class ColorSchemes(object):
    FORE_BLACK   = _AnsiEscapeSequences.FORE_BLACK
    FORE_RED     = _AnsiEscapeSequences.FORE_RED
    FORE_GREEN   = _AnsiEscapeSequences.FORE_GREEN
    FORE_YELLOW  = _AnsiEscapeSequences.FORE_YELLOW
    FORE_BLUE    = _AnsiEscapeSequences.FORE_BLUE
    FORE_PURPLE = _AnsiEscapeSequences.FORE_MAGENTA
    FORE_GREEN_BLUE    = _AnsiEscapeSequences.FORE_CYAN

def _c(string):
    if platform.system() == "Windows" and not _colorama:
        return ""
    else:
        return string

##########################################
default_settings = dict(
    with_filename=True,
    with_lineno=True,
    with_calling_func_name=True,
    with_expr=True,
    with_result_type=True,
    with_result=True,

    #logger=logging.getLogger(__name__),
    #log_level=logging.DEBUG,
    #print_level=logging.DEBUG
)
#_logger = logging.getLogger(__name__)

#_logger.setLevel(logging.NOTSET)
#default_settings["log_file"] = os.path.join("/tmp", "log_" + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
#if mode in [JUST_LOG, LOG_AND_PRINT]:
#    _logger.addHandler(logging.FileHandler(default_settings["log_file"]))
#if mode in [JUST_PRINT, LOG_AND_PRINT]:
#    _logger.addHandler(logging.StreamHandler())


def debug_eval_print(expression, filestream=sys.stderr, colorscheme=ColorSchemes.FORE_BLUE):
    filename = None
    lineno = None
    calling_func = None
    result = None

    s = ""
    try:
        stack = _inspect.stack()
        frame, filename, lineno, calling_func_name, _, _ = stack[1]
        first_line = []
        if default_settings["with_filename"]:
            first_line.append("File: " + filename)
        if default_settings["with_lineno"]:
            first_line.append("Line:" + repr(lineno))
        if default_settings["with_calling_func_name"]:
            first_line.append("Func:" + calling_func_name)
        if first_line:
            arr = zip(first_line, [_c(colorscheme + _AnsiEscapeSequences.STYLE_BRIGHT),
                   _c(colorscheme),
                   _c(colorscheme + _AnsiEscapeSequences.STYLE_BRIGHT)])
            s += " | ".join(sty + seg + _AnsiEscapeSequences.STYLE_RESET_ALL for (seg,sty) in arr)
            s += "\n"
        try:
            result = eval(expression,globals(), frame.f_locals)
        except Exception, e:
            result = e

    except Exception, e:
        print("Could not get frame info," + repr(e), end='', file=filestream)
    finally:
        del stack

    result_type = type(result)
    second_line = []
    if default_settings["with_expr"]:
        second_line.append("Expr: " + expression)
    if default_settings["with_result_type"]:
        second_line.append("type:" + repr(result_type))
    if default_settings["with_result"]:
        second_line.append(" result:" + repr(result))

    if second_line:
        arr = zip(second_line, [_c(colorscheme + _AnsiEscapeSequences.STYLE_BRIGHT),
                               _c(colorscheme),
                               _c(colorscheme + _AnsiEscapeSequences.STYLE_BRIGHT)])
        s += " | ".join(sty + seg + _AnsiEscapeSequences.STYLE_RESET_ALL for (seg,sty) in arr)

    #if default_settings["log_print_mode"] in [JUST_PRINT, LOG_AND_PRINT]:
    print(s, file=filestream)
    #if default_settings["log_print_mode"] in [JUST_LOG, LOG_AND_PRINT]:
    #    default_settings["logger"].log(default_settings["level"], s)
    return result


def debug_message(message, filestream=sys.stderr, colorscheme=ColorSchemes.FORE_BLUE):
    assert isinstance(message, basestring)
    filename = None
    lineno = None
    calling_func = None
    try:
        stack = _inspect.stack()
        _, filename, lineno, calling_func_name, _, _ = stack[1]
        s = ""
        first_line = []
        if default_settings["with_filename"]:
            first_line.append("File: " + filename)
        if default_settings["with_lineno"]:
            first_line.append("Line:" + repr(lineno))
        if default_settings["with_calling_func_name"]:
            first_line.append("Func:" + calling_func_name)
        if first_line:
            arr = zip(first_line, [_c(colorscheme + _AnsiEscapeSequences.STYLE_BRIGHT),
                                   _c(colorscheme),
                                   _c(colorscheme + _AnsiEscapeSequences.STYLE_BRIGHT)])
            s += " | ".join(sty + seg + _AnsiEscapeSequences.STYLE_RESET_ALL for (seg,sty) in arr)


        s += "\n" + _c(colorscheme) + message + _AnsiEscapeSequences.STYLE_RESET_ALL

        #if default_settings["log_print_mode"] in [JUST_PRINT, LOG_AND_PRINT]:
        print(s, file=filestream)
        #if default_settings["log_print_mode"] in [JUST_LOG, LOG_AND_PRINT]:
        #    default_settings["logger"].log(default_settings["level"], s)

    except Exception, e:
        print("Could not get frame info," + repr(e), end='', file=filestream)
    finally:
        del stack
