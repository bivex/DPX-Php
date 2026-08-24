# Generated from /Volumes/External/Code/DPX-Php/grammars/PHPParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,67,732,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,3,0,92,8,0,
        1,0,5,0,95,8,0,10,0,12,0,98,9,0,1,0,3,0,101,8,0,1,0,5,0,104,8,0,
        10,0,12,0,107,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,1,2,5,2,124,8,2,10,2,12,2,127,9,2,1,2,3,2,130,8,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,143,8,3,10,3,12,3,146,
        9,3,1,3,1,3,1,3,3,3,151,8,3,1,4,1,4,1,4,5,4,156,8,4,10,4,12,4,159,
        9,4,1,5,1,5,1,5,3,5,164,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,173,
        8,6,1,7,5,7,176,8,7,10,7,12,7,179,9,7,1,7,1,7,1,7,1,7,3,7,185,8,
        7,1,7,1,7,3,7,189,8,7,1,7,1,7,5,7,193,8,7,10,7,12,7,196,9,7,1,7,
        1,7,1,8,1,8,1,8,1,8,3,8,204,8,8,1,8,1,8,5,8,208,8,8,10,8,12,8,211,
        9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,219,8,9,10,9,12,9,222,9,9,1,9,1,
        9,1,10,1,10,1,10,1,10,3,10,230,8,10,1,10,1,10,3,10,234,8,10,1,10,
        1,10,5,10,238,8,10,10,10,12,10,241,9,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,3,11,250,8,11,1,12,1,12,1,12,1,12,1,13,5,13,257,8,13,10,
        13,12,13,260,9,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,4,14,269,8,
        14,11,14,12,14,270,1,14,3,14,274,8,14,1,14,1,14,1,14,3,14,279,8,
        14,1,14,1,14,1,14,1,14,3,14,285,8,14,5,14,287,8,14,10,14,12,14,290,
        9,14,1,14,1,14,1,15,5,15,295,8,15,10,15,12,15,298,9,15,1,15,1,15,
        1,15,1,15,3,15,304,8,15,1,15,1,15,1,15,3,15,309,8,15,1,15,1,15,3,
        15,313,8,15,1,16,1,16,1,16,1,16,3,16,319,8,16,1,16,1,16,1,16,3,16,
        324,8,16,1,16,1,16,1,17,1,17,3,17,330,8,17,1,18,1,18,1,19,1,19,1,
        19,5,19,337,8,19,10,19,12,19,340,9,19,1,19,3,19,343,8,19,1,20,5,
        20,346,8,20,10,20,12,20,349,9,20,1,20,3,20,352,8,20,1,20,3,20,355,
        8,20,1,20,3,20,358,8,20,1,20,1,20,1,20,3,20,363,8,20,1,21,1,21,1,
        22,1,22,1,23,1,23,1,23,5,23,372,8,23,10,23,12,23,375,9,23,1,24,3,
        24,378,8,24,1,24,1,24,3,24,382,8,24,1,24,1,24,1,24,3,24,387,8,24,
        5,24,389,8,24,10,24,12,24,392,9,24,1,25,1,25,1,26,3,26,397,8,26,
        1,26,1,26,1,26,5,26,402,8,26,10,26,12,26,405,9,26,1,27,1,27,5,27,
        409,8,27,10,27,12,27,412,9,27,1,27,1,27,1,28,1,28,1,28,3,28,419,
        8,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,5,28,437,8,28,10,28,12,28,440,9,28,1,28,1,28,
        3,28,444,8,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,452,8,28,10,28,
        12,28,455,9,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,3,28,468,8,28,1,28,1,28,3,28,472,8,28,1,28,1,28,3,28,476,8,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,487,8,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,5,
        28,502,8,28,10,28,12,28,505,9,28,1,28,1,28,3,28,509,8,28,1,28,1,
        28,1,28,1,28,3,28,515,8,28,1,29,1,29,1,29,3,29,520,8,29,1,29,1,29,
        5,29,524,8,29,10,29,12,29,527,9,29,1,30,1,30,1,30,1,30,5,30,533,
        8,30,10,30,12,30,536,9,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,3,31,552,8,31,1,32,1,32,1,32,1,32,
        3,32,558,8,32,1,32,3,32,561,8,32,1,32,1,32,1,32,1,32,3,32,567,8,
        32,1,32,1,32,3,32,571,8,32,1,32,1,32,3,32,575,8,32,1,32,1,32,1,32,
        5,32,580,8,32,10,32,12,32,583,9,32,1,32,3,32,586,8,32,1,33,1,33,
        1,33,1,34,3,34,592,8,34,1,34,1,34,1,34,3,34,597,8,34,1,34,1,34,1,
        34,1,34,3,34,603,8,34,1,34,3,34,606,8,34,1,34,1,34,3,34,610,8,34,
        1,34,1,34,3,34,614,8,34,1,34,1,34,1,34,3,34,619,8,34,1,34,1,34,1,
        34,3,34,624,8,34,1,34,1,34,3,34,628,8,34,1,35,1,35,1,35,1,35,5,35,
        634,8,35,10,35,12,35,637,9,35,1,35,3,35,640,8,35,3,35,642,8,35,1,
        35,1,35,1,36,1,36,1,36,3,36,649,8,36,1,36,1,36,1,37,1,37,1,37,1,
        37,1,37,1,37,1,37,1,37,5,37,661,8,37,10,37,12,37,664,9,37,1,37,3,
        37,667,8,37,3,37,669,8,37,1,37,1,37,1,38,1,38,1,38,5,38,676,8,38,
        10,38,12,38,679,9,38,1,38,3,38,682,8,38,1,38,1,38,1,38,1,39,1,39,
        1,39,3,39,690,8,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,3,40,
        700,8,40,1,40,1,40,1,40,1,40,3,40,706,8,40,1,41,1,41,1,41,5,41,711,
        8,41,10,41,12,41,714,9,41,1,41,3,41,717,8,41,1,42,1,42,3,42,721,
        8,42,1,42,3,42,724,8,42,1,42,1,42,1,43,1,43,1,44,1,44,1,44,0,0,45,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,
        0,7,2,0,3,11,13,38,1,0,17,19,1,0,13,19,2,0,46,47,67,67,1,0,44,46,
        1,0,62,63,6,0,38,38,43,46,48,48,56,57,59,59,67,67,811,0,91,1,0,0,
        0,2,110,1,0,0,0,4,118,1,0,0,0,6,150,1,0,0,0,8,152,1,0,0,0,10,160,
        1,0,0,0,12,172,1,0,0,0,14,177,1,0,0,0,16,199,1,0,0,0,18,214,1,0,
        0,0,20,225,1,0,0,0,22,249,1,0,0,0,24,251,1,0,0,0,26,258,1,0,0,0,
        28,268,1,0,0,0,30,296,1,0,0,0,32,314,1,0,0,0,34,329,1,0,0,0,36,331,
        1,0,0,0,38,333,1,0,0,0,40,347,1,0,0,0,42,364,1,0,0,0,44,366,1,0,
        0,0,46,368,1,0,0,0,48,377,1,0,0,0,50,393,1,0,0,0,52,396,1,0,0,0,
        54,406,1,0,0,0,56,514,1,0,0,0,58,519,1,0,0,0,60,528,1,0,0,0,62,551,
        1,0,0,0,64,585,1,0,0,0,66,587,1,0,0,0,68,627,1,0,0,0,70,629,1,0,
        0,0,72,648,1,0,0,0,74,652,1,0,0,0,76,681,1,0,0,0,78,686,1,0,0,0,
        80,699,1,0,0,0,82,707,1,0,0,0,84,720,1,0,0,0,86,727,1,0,0,0,88,729,
        1,0,0,0,90,92,5,1,0,0,91,90,1,0,0,0,91,92,1,0,0,0,92,96,1,0,0,0,
        93,95,3,2,1,0,94,93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,
        0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,99,101,3,4,2,0,100,99,1,0,0,0,
        100,101,1,0,0,0,101,105,1,0,0,0,102,104,3,12,6,0,103,102,1,0,0,0,
        104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,
        107,105,1,0,0,0,108,109,5,0,0,1,109,1,1,0,0,0,110,111,5,39,0,0,111,
        112,5,49,0,0,112,113,3,48,24,0,113,114,5,59,0,0,114,115,3,86,43,
        0,115,116,5,50,0,0,116,117,5,40,0,0,117,3,1,0,0,0,118,119,5,2,0,
        0,119,129,3,48,24,0,120,130,5,40,0,0,121,125,5,51,0,0,122,124,3,
        12,6,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,1,
        0,0,0,126,128,1,0,0,0,127,125,1,0,0,0,128,130,5,52,0,0,129,120,1,
        0,0,0,129,121,1,0,0,0,130,5,1,0,0,0,131,132,5,3,0,0,132,133,3,8,
        4,0,133,134,5,40,0,0,134,151,1,0,0,0,135,136,5,3,0,0,136,137,3,48,
        24,0,137,138,5,46,0,0,138,139,5,51,0,0,139,144,3,10,5,0,140,141,
        5,42,0,0,141,143,3,10,5,0,142,140,1,0,0,0,143,146,1,0,0,0,144,142,
        1,0,0,0,144,145,1,0,0,0,145,147,1,0,0,0,146,144,1,0,0,0,147,148,
        5,52,0,0,148,149,5,40,0,0,149,151,1,0,0,0,150,131,1,0,0,0,150,135,
        1,0,0,0,151,7,1,0,0,0,152,157,3,10,5,0,153,154,5,42,0,0,154,156,
        3,10,5,0,155,153,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,
        1,0,0,0,158,9,1,0,0,0,159,157,1,0,0,0,160,163,3,48,24,0,161,162,
        5,4,0,0,162,164,5,61,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,11,
        1,0,0,0,165,173,3,6,3,0,166,173,3,14,7,0,167,173,3,16,8,0,168,173,
        3,18,9,0,169,173,3,20,10,0,170,173,3,32,16,0,171,173,3,56,28,0,172,
        165,1,0,0,0,172,166,1,0,0,0,172,167,1,0,0,0,172,168,1,0,0,0,172,
        169,1,0,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,13,1,0,0,0,174,176,
        3,42,21,0,175,174,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,0,180,181,5,5,0,0,181,184,
        5,61,0,0,182,183,5,9,0,0,183,185,3,48,24,0,184,182,1,0,0,0,184,185,
        1,0,0,0,185,188,1,0,0,0,186,187,5,10,0,0,187,189,3,46,23,0,188,186,
        1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,194,5,51,0,0,191,193,
        3,22,11,0,192,191,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,
        1,0,0,0,195,197,1,0,0,0,196,194,1,0,0,0,197,198,5,52,0,0,198,15,
        1,0,0,0,199,200,5,6,0,0,200,203,5,61,0,0,201,202,5,9,0,0,202,204,
        3,46,23,0,203,201,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,209,
        5,51,0,0,206,208,3,22,11,0,207,206,1,0,0,0,208,211,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,209,1,0,0,0,212,213,
        5,52,0,0,213,17,1,0,0,0,214,215,5,7,0,0,215,216,5,61,0,0,216,220,
        5,51,0,0,217,219,3,22,11,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,
        1,0,0,0,220,221,1,0,0,0,221,223,1,0,0,0,222,220,1,0,0,0,223,224,
        5,52,0,0,224,19,1,0,0,0,225,226,5,8,0,0,226,229,5,61,0,0,227,228,
        5,41,0,0,228,230,3,52,26,0,229,227,1,0,0,0,229,230,1,0,0,0,230,233,
        1,0,0,0,231,232,5,10,0,0,232,234,3,46,23,0,233,231,1,0,0,0,233,234,
        1,0,0,0,234,235,1,0,0,0,235,239,5,51,0,0,236,238,3,22,11,0,237,236,
        1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,242,
        1,0,0,0,241,239,1,0,0,0,242,243,5,52,0,0,243,21,1,0,0,0,244,250,
        3,30,15,0,245,250,3,28,14,0,246,250,3,26,13,0,247,250,3,24,12,0,
        248,250,3,56,28,0,249,244,1,0,0,0,249,245,1,0,0,0,249,246,1,0,0,
        0,249,247,1,0,0,0,249,248,1,0,0,0,250,23,1,0,0,0,251,252,5,3,0,0,
        252,253,3,46,23,0,253,254,5,40,0,0,254,25,1,0,0,0,255,257,3,44,22,
        0,256,255,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,
        0,259,261,1,0,0,0,260,258,1,0,0,0,261,262,5,20,0,0,262,263,5,61,
        0,0,263,264,5,59,0,0,264,265,3,60,30,0,265,266,5,40,0,0,266,27,1,
        0,0,0,267,269,3,44,22,0,268,267,1,0,0,0,269,270,1,0,0,0,270,268,
        1,0,0,0,270,271,1,0,0,0,271,273,1,0,0,0,272,274,3,52,26,0,273,272,
        1,0,0,0,273,274,1,0,0,0,274,275,1,0,0,0,275,278,5,60,0,0,276,277,
        5,59,0,0,277,279,3,60,30,0,278,276,1,0,0,0,278,279,1,0,0,0,279,288,
        1,0,0,0,280,281,5,42,0,0,281,284,5,60,0,0,282,283,5,59,0,0,283,285,
        3,60,30,0,284,282,1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,280,
        1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,291,
        1,0,0,0,290,288,1,0,0,0,291,292,5,40,0,0,292,29,1,0,0,0,293,295,
        3,44,22,0,294,293,1,0,0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,
        1,0,0,0,297,299,1,0,0,0,298,296,1,0,0,0,299,300,5,11,0,0,300,301,
        3,34,17,0,301,303,5,49,0,0,302,304,3,38,19,0,303,302,1,0,0,0,303,
        304,1,0,0,0,304,305,1,0,0,0,305,308,5,50,0,0,306,307,5,41,0,0,307,
        309,3,52,26,0,308,306,1,0,0,0,308,309,1,0,0,0,309,312,1,0,0,0,310,
        313,3,54,27,0,311,313,5,40,0,0,312,310,1,0,0,0,312,311,1,0,0,0,313,
        31,1,0,0,0,314,315,5,11,0,0,315,316,5,61,0,0,316,318,5,49,0,0,317,
        319,3,38,19,0,318,317,1,0,0,0,318,319,1,0,0,0,319,320,1,0,0,0,320,
        323,5,50,0,0,321,322,5,41,0,0,322,324,3,52,26,0,323,321,1,0,0,0,
        323,324,1,0,0,0,324,325,1,0,0,0,325,326,3,54,27,0,326,33,1,0,0,0,
        327,330,5,61,0,0,328,330,3,36,18,0,329,327,1,0,0,0,329,328,1,0,0,
        0,330,35,1,0,0,0,331,332,7,0,0,0,332,37,1,0,0,0,333,338,3,40,20,
        0,334,335,5,42,0,0,335,337,3,40,20,0,336,334,1,0,0,0,337,340,1,0,
        0,0,338,336,1,0,0,0,338,339,1,0,0,0,339,342,1,0,0,0,340,338,1,0,
        0,0,341,343,5,42,0,0,342,341,1,0,0,0,342,343,1,0,0,0,343,39,1,0,
        0,0,344,346,3,44,22,0,345,344,1,0,0,0,346,349,1,0,0,0,347,345,1,
        0,0,0,347,348,1,0,0,0,348,351,1,0,0,0,349,347,1,0,0,0,350,352,3,
        52,26,0,351,350,1,0,0,0,351,352,1,0,0,0,352,354,1,0,0,0,353,355,
        5,57,0,0,354,353,1,0,0,0,354,355,1,0,0,0,355,357,1,0,0,0,356,358,
        5,58,0,0,357,356,1,0,0,0,357,358,1,0,0,0,358,359,1,0,0,0,359,362,
        5,60,0,0,360,361,5,59,0,0,361,363,3,60,30,0,362,360,1,0,0,0,362,
        363,1,0,0,0,363,41,1,0,0,0,364,365,7,1,0,0,365,43,1,0,0,0,366,367,
        7,2,0,0,367,45,1,0,0,0,368,373,3,48,24,0,369,370,5,42,0,0,370,372,
        3,48,24,0,371,369,1,0,0,0,372,375,1,0,0,0,373,371,1,0,0,0,373,374,
        1,0,0,0,374,47,1,0,0,0,375,373,1,0,0,0,376,378,5,47,0,0,377,376,
        1,0,0,0,377,378,1,0,0,0,378,381,1,0,0,0,379,382,5,61,0,0,380,382,
        3,36,18,0,381,379,1,0,0,0,381,380,1,0,0,0,382,390,1,0,0,0,383,386,
        3,50,25,0,384,387,5,61,0,0,385,387,3,36,18,0,386,384,1,0,0,0,386,
        385,1,0,0,0,387,389,1,0,0,0,388,383,1,0,0,0,389,392,1,0,0,0,390,
        388,1,0,0,0,390,391,1,0,0,0,391,49,1,0,0,0,392,390,1,0,0,0,393,394,
        7,3,0,0,394,51,1,0,0,0,395,397,5,55,0,0,396,395,1,0,0,0,396,397,
        1,0,0,0,397,398,1,0,0,0,398,403,3,48,24,0,399,400,5,56,0,0,400,402,
        3,48,24,0,401,399,1,0,0,0,402,405,1,0,0,0,403,401,1,0,0,0,403,404,
        1,0,0,0,404,53,1,0,0,0,405,403,1,0,0,0,406,410,5,51,0,0,407,409,
        3,56,28,0,408,407,1,0,0,0,409,412,1,0,0,0,410,408,1,0,0,0,410,411,
        1,0,0,0,411,413,1,0,0,0,412,410,1,0,0,0,413,414,5,52,0,0,414,55,
        1,0,0,0,415,515,3,54,27,0,416,418,5,21,0,0,417,419,3,60,30,0,418,
        417,1,0,0,0,418,419,1,0,0,0,419,420,1,0,0,0,420,515,5,40,0,0,421,
        422,5,34,0,0,422,423,3,60,30,0,423,424,5,40,0,0,424,515,1,0,0,0,
        425,426,5,26,0,0,426,427,5,49,0,0,427,428,3,60,30,0,428,429,5,50,
        0,0,429,438,3,56,28,0,430,431,5,27,0,0,431,432,5,49,0,0,432,433,
        3,60,30,0,433,434,5,50,0,0,434,435,3,56,28,0,435,437,1,0,0,0,436,
        430,1,0,0,0,437,440,1,0,0,0,438,436,1,0,0,0,438,439,1,0,0,0,439,
        443,1,0,0,0,440,438,1,0,0,0,441,442,5,28,0,0,442,444,3,56,28,0,443,
        441,1,0,0,0,443,444,1,0,0,0,444,515,1,0,0,0,445,446,5,23,0,0,446,
        447,5,49,0,0,447,448,3,60,30,0,448,449,5,50,0,0,449,453,5,51,0,0,
        450,452,3,58,29,0,451,450,1,0,0,0,452,455,1,0,0,0,453,451,1,0,0,
        0,453,454,1,0,0,0,454,456,1,0,0,0,455,453,1,0,0,0,456,457,5,52,0,
        0,457,515,1,0,0,0,458,459,5,29,0,0,459,460,5,49,0,0,460,461,3,60,
        30,0,461,462,5,50,0,0,462,463,3,56,28,0,463,515,1,0,0,0,464,465,
        5,30,0,0,465,467,5,49,0,0,466,468,3,60,30,0,467,466,1,0,0,0,467,
        468,1,0,0,0,468,469,1,0,0,0,469,471,5,40,0,0,470,472,3,60,30,0,471,
        470,1,0,0,0,471,472,1,0,0,0,472,473,1,0,0,0,473,475,5,40,0,0,474,
        476,3,60,30,0,475,474,1,0,0,0,475,476,1,0,0,0,476,477,1,0,0,0,477,
        478,5,50,0,0,478,515,3,56,28,0,479,480,5,31,0,0,480,481,5,49,0,0,
        481,482,3,60,30,0,482,486,5,4,0,0,483,484,3,60,30,0,484,485,5,48,
        0,0,485,487,1,0,0,0,486,483,1,0,0,0,486,487,1,0,0,0,487,488,1,0,
        0,0,488,489,3,60,30,0,489,490,5,50,0,0,490,491,3,56,28,0,491,515,
        1,0,0,0,492,493,5,35,0,0,493,503,3,54,27,0,494,495,5,36,0,0,495,
        496,5,49,0,0,496,497,3,52,26,0,497,498,5,60,0,0,498,499,5,50,0,0,
        499,500,3,54,27,0,500,502,1,0,0,0,501,494,1,0,0,0,502,505,1,0,0,
        0,503,501,1,0,0,0,503,504,1,0,0,0,504,508,1,0,0,0,505,503,1,0,0,
        0,506,507,5,37,0,0,507,509,3,54,27,0,508,506,1,0,0,0,508,509,1,0,
        0,0,509,515,1,0,0,0,510,511,3,60,30,0,511,512,5,40,0,0,512,515,1,
        0,0,0,513,515,5,40,0,0,514,415,1,0,0,0,514,416,1,0,0,0,514,421,1,
        0,0,0,514,425,1,0,0,0,514,445,1,0,0,0,514,458,1,0,0,0,514,464,1,
        0,0,0,514,479,1,0,0,0,514,492,1,0,0,0,514,510,1,0,0,0,514,513,1,
        0,0,0,515,57,1,0,0,0,516,517,5,24,0,0,517,520,3,60,30,0,518,520,
        5,25,0,0,519,516,1,0,0,0,519,518,1,0,0,0,520,521,1,0,0,0,521,525,
        5,41,0,0,522,524,3,56,28,0,523,522,1,0,0,0,524,527,1,0,0,0,525,523,
        1,0,0,0,525,526,1,0,0,0,526,59,1,0,0,0,527,525,1,0,0,0,528,534,3,
        62,31,0,529,530,3,88,44,0,530,531,3,62,31,0,531,533,1,0,0,0,532,
        529,1,0,0,0,533,536,1,0,0,0,534,532,1,0,0,0,534,535,1,0,0,0,535,
        61,1,0,0,0,536,534,1,0,0,0,537,552,5,60,0,0,538,552,3,86,43,0,539,
        552,3,48,24,0,540,552,3,74,37,0,541,552,3,64,32,0,542,552,3,66,33,
        0,543,552,3,68,34,0,544,552,3,70,35,0,545,552,3,78,39,0,546,552,
        3,80,40,0,547,548,5,49,0,0,548,549,3,60,30,0,549,550,5,50,0,0,550,
        552,1,0,0,0,551,537,1,0,0,0,551,538,1,0,0,0,551,539,1,0,0,0,551,
        540,1,0,0,0,551,541,1,0,0,0,551,542,1,0,0,0,551,543,1,0,0,0,551,
        544,1,0,0,0,551,545,1,0,0,0,551,546,1,0,0,0,551,547,1,0,0,0,552,
        63,1,0,0,0,553,554,5,32,0,0,554,560,3,48,24,0,555,557,5,49,0,0,556,
        558,3,82,41,0,557,556,1,0,0,0,557,558,1,0,0,0,558,559,1,0,0,0,559,
        561,5,50,0,0,560,555,1,0,0,0,560,561,1,0,0,0,561,586,1,0,0,0,562,
        563,5,32,0,0,563,566,5,5,0,0,564,565,5,9,0,0,565,567,3,48,24,0,566,
        564,1,0,0,0,566,567,1,0,0,0,567,570,1,0,0,0,568,569,5,10,0,0,569,
        571,3,46,23,0,570,568,1,0,0,0,570,571,1,0,0,0,571,572,1,0,0,0,572,
        574,5,49,0,0,573,575,3,82,41,0,574,573,1,0,0,0,574,575,1,0,0,0,575,
        576,1,0,0,0,576,577,5,50,0,0,577,581,5,51,0,0,578,580,3,22,11,0,
        579,578,1,0,0,0,580,583,1,0,0,0,581,579,1,0,0,0,581,582,1,0,0,0,
        582,584,1,0,0,0,583,581,1,0,0,0,584,586,5,52,0,0,585,553,1,0,0,0,
        585,562,1,0,0,0,586,65,1,0,0,0,587,588,5,33,0,0,588,589,3,60,30,
        0,589,67,1,0,0,0,590,592,5,16,0,0,591,590,1,0,0,0,591,592,1,0,0,
        0,592,593,1,0,0,0,593,594,5,11,0,0,594,596,5,49,0,0,595,597,3,38,
        19,0,596,595,1,0,0,0,596,597,1,0,0,0,597,598,1,0,0,0,598,605,5,50,
        0,0,599,600,5,3,0,0,600,602,5,49,0,0,601,603,3,38,19,0,602,601,1,
        0,0,0,602,603,1,0,0,0,603,604,1,0,0,0,604,606,5,50,0,0,605,599,1,
        0,0,0,605,606,1,0,0,0,606,609,1,0,0,0,607,608,5,41,0,0,608,610,3,
        52,26,0,609,607,1,0,0,0,609,610,1,0,0,0,610,611,1,0,0,0,611,628,
        3,54,27,0,612,614,5,16,0,0,613,612,1,0,0,0,613,614,1,0,0,0,614,615,
        1,0,0,0,615,616,5,12,0,0,616,618,5,49,0,0,617,619,3,38,19,0,618,
        617,1,0,0,0,618,619,1,0,0,0,619,620,1,0,0,0,620,623,5,50,0,0,621,
        622,5,41,0,0,622,624,3,52,26,0,623,621,1,0,0,0,623,624,1,0,0,0,624,
        625,1,0,0,0,625,626,5,48,0,0,626,628,3,60,30,0,627,591,1,0,0,0,627,
        613,1,0,0,0,628,69,1,0,0,0,629,641,5,53,0,0,630,635,3,72,36,0,631,
        632,5,42,0,0,632,634,3,72,36,0,633,631,1,0,0,0,634,637,1,0,0,0,635,
        633,1,0,0,0,635,636,1,0,0,0,636,639,1,0,0,0,637,635,1,0,0,0,638,
        640,5,42,0,0,639,638,1,0,0,0,639,640,1,0,0,0,640,642,1,0,0,0,641,
        630,1,0,0,0,641,642,1,0,0,0,642,643,1,0,0,0,643,644,5,54,0,0,644,
        71,1,0,0,0,645,646,3,60,30,0,646,647,5,48,0,0,647,649,1,0,0,0,648,
        645,1,0,0,0,648,649,1,0,0,0,649,650,1,0,0,0,650,651,3,60,30,0,651,
        73,1,0,0,0,652,653,5,22,0,0,653,654,5,49,0,0,654,655,3,60,30,0,655,
        656,5,50,0,0,656,668,5,51,0,0,657,662,3,76,38,0,658,659,5,42,0,0,
        659,661,3,76,38,0,660,658,1,0,0,0,661,664,1,0,0,0,662,660,1,0,0,
        0,662,663,1,0,0,0,663,666,1,0,0,0,664,662,1,0,0,0,665,667,5,42,0,
        0,666,665,1,0,0,0,666,667,1,0,0,0,667,669,1,0,0,0,668,657,1,0,0,
        0,668,669,1,0,0,0,669,670,1,0,0,0,670,671,5,52,0,0,671,75,1,0,0,
        0,672,677,3,60,30,0,673,674,5,42,0,0,674,676,3,60,30,0,675,673,1,
        0,0,0,676,679,1,0,0,0,677,675,1,0,0,0,677,678,1,0,0,0,678,682,1,
        0,0,0,679,677,1,0,0,0,680,682,5,25,0,0,681,672,1,0,0,0,681,680,1,
        0,0,0,682,683,1,0,0,0,683,684,5,48,0,0,684,685,3,60,30,0,685,77,
        1,0,0,0,686,687,3,48,24,0,687,689,5,49,0,0,688,690,3,82,41,0,689,
        688,1,0,0,0,689,690,1,0,0,0,690,691,1,0,0,0,691,692,5,50,0,0,692,
        79,1,0,0,0,693,700,5,60,0,0,694,700,3,48,24,0,695,696,5,49,0,0,696,
        697,3,60,30,0,697,698,5,50,0,0,698,700,1,0,0,0,699,693,1,0,0,0,699,
        694,1,0,0,0,699,695,1,0,0,0,700,701,1,0,0,0,701,705,7,4,0,0,702,
        706,5,61,0,0,703,706,5,60,0,0,704,706,3,78,39,0,705,702,1,0,0,0,
        705,703,1,0,0,0,705,704,1,0,0,0,706,81,1,0,0,0,707,712,3,84,42,0,
        708,709,5,42,0,0,709,711,3,84,42,0,710,708,1,0,0,0,711,714,1,0,0,
        0,712,710,1,0,0,0,712,713,1,0,0,0,713,716,1,0,0,0,714,712,1,0,0,
        0,715,717,5,42,0,0,716,715,1,0,0,0,716,717,1,0,0,0,717,83,1,0,0,
        0,718,719,5,61,0,0,719,721,5,41,0,0,720,718,1,0,0,0,720,721,1,0,
        0,0,721,723,1,0,0,0,722,724,5,58,0,0,723,722,1,0,0,0,723,724,1,0,
        0,0,724,725,1,0,0,0,725,726,3,60,30,0,726,85,1,0,0,0,727,728,7,5,
        0,0,728,87,1,0,0,0,729,730,7,6,0,0,730,89,1,0,0,0,97,91,96,100,105,
        125,129,144,150,157,163,172,177,184,188,194,203,209,220,229,233,
        239,249,258,270,273,278,284,288,296,303,308,312,318,323,329,338,
        342,347,351,354,357,362,373,377,381,386,390,396,403,410,418,438,
        443,453,467,471,475,486,503,508,514,519,525,534,551,557,560,566,
        570,574,581,585,591,596,602,605,609,613,618,623,627,635,639,641,
        648,662,666,668,677,681,689,699,705,712,716,720,723
    ]

class PHPParser ( Parser ):

    grammarFileName = "PHPParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'namespace'", "'use'", "'as'", 
                     "'class'", "'interface'", "'trait'", "'enum'", "'extends'", 
                     "'implements'", "'function'", "'fn'", "'public'", "'protected'", 
                     "'private'", "'static'", "'final'", "'abstract'", "'readonly'", 
                     "'const'", "'return'", "'match'", "'switch'", "'case'", 
                     "'default'", "'if'", "'elseif'", "'else'", "'while'", 
                     "'for'", "'foreach'", "'new'", "'clone'", "'throw'", 
                     "'try'", "'catch'", "'finally'", "'instanceof'", "'declare'", 
                     "';'", "':'", "','", "'.'", "'->'", "'?->'", "'::'", 
                     "'\\'", "'=>'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "'?'", "'|'", "'&'", "'...'", "'='" ]

    symbolicNames = [ "<INVALID>", "PHP_OPEN", "NAMESPACE", "USE", "AS", 
                      "CLASS", "INTERFACE", "TRAIT", "ENUM", "EXTENDS", 
                      "IMPLEMENTS", "FUNCTION", "FN", "PUBLIC", "PROTECTED", 
                      "PRIVATE", "STATIC", "FINAL", "ABSTRACT", "READONLY", 
                      "CONST", "RETURN", "MATCH", "SWITCH", "CASE", "DEFAULT", 
                      "IF", "ELSEIF", "ELSE", "WHILE", "FOR", "FOREACH", 
                      "NEW", "CLONE", "THROW", "TRY", "CATCH", "FINALLY", 
                      "INSTANCEOF", "DECLARE", "SEMI", "COLON", "COMMA", 
                      "DOT", "ARROW", "NULLSAFE_ARROW", "DOUBLE_COLON", 
                      "BACKSLASH", "DOUBLE_ARROW", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "QUESTION", "PIPE", 
                      "AMP", "ELLIPSIS", "EQUAL", "VARIABLE", "IDENTIFIER", 
                      "NUMBER", "STRING_LITERAL", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS", "OTHER_OP" ]

    RULE_phpFile = 0
    RULE_declareStatement = 1
    RULE_namespaceStatement = 2
    RULE_useStatement = 3
    RULE_useDeclarationList = 4
    RULE_useItem = 5
    RULE_topLevelStatement = 6
    RULE_classDeclaration = 7
    RULE_interfaceDeclaration = 8
    RULE_traitDeclaration = 9
    RULE_enumDeclaration = 10
    RULE_classMember = 11
    RULE_useTraitStatement = 12
    RULE_constDeclaration = 13
    RULE_propertyDeclaration = 14
    RULE_methodDeclaration = 15
    RULE_functionDeclaration = 16
    RULE_methodName = 17
    RULE_keywordAsIdentifier = 18
    RULE_parameterList = 19
    RULE_parameter = 20
    RULE_classModifier = 21
    RULE_memberModifier = 22
    RULE_qualifiedNameList = 23
    RULE_qualifiedName = 24
    RULE_qualifiedSeparator = 25
    RULE_type = 26
    RULE_block = 27
    RULE_statement = 28
    RULE_switchBlock = 29
    RULE_expression = 30
    RULE_primaryExpression = 31
    RULE_newExpression = 32
    RULE_cloneExpression = 33
    RULE_closureExpression = 34
    RULE_arrayExpression = 35
    RULE_arrayElement = 36
    RULE_matchExpression = 37
    RULE_matchArm = 38
    RULE_functionCall = 39
    RULE_memberAccess = 40
    RULE_argumentList = 41
    RULE_argument = 42
    RULE_literal = 43
    RULE_operator = 44

    ruleNames =  [ "phpFile", "declareStatement", "namespaceStatement", 
                   "useStatement", "useDeclarationList", "useItem", "topLevelStatement", 
                   "classDeclaration", "interfaceDeclaration", "traitDeclaration", 
                   "enumDeclaration", "classMember", "useTraitStatement", 
                   "constDeclaration", "propertyDeclaration", "methodDeclaration", 
                   "functionDeclaration", "methodName", "keywordAsIdentifier", 
                   "parameterList", "parameter", "classModifier", "memberModifier", 
                   "qualifiedNameList", "qualifiedName", "qualifiedSeparator", 
                   "type", "block", "statement", "switchBlock", "expression", 
                   "primaryExpression", "newExpression", "cloneExpression", 
                   "closureExpression", "arrayExpression", "arrayElement", 
                   "matchExpression", "matchArm", "functionCall", "memberAccess", 
                   "argumentList", "argument", "literal", "operator" ]

    EOF = Token.EOF
    PHP_OPEN=1
    NAMESPACE=2
    USE=3
    AS=4
    CLASS=5
    INTERFACE=6
    TRAIT=7
    ENUM=8
    EXTENDS=9
    IMPLEMENTS=10
    FUNCTION=11
    FN=12
    PUBLIC=13
    PROTECTED=14
    PRIVATE=15
    STATIC=16
    FINAL=17
    ABSTRACT=18
    READONLY=19
    CONST=20
    RETURN=21
    MATCH=22
    SWITCH=23
    CASE=24
    DEFAULT=25
    IF=26
    ELSEIF=27
    ELSE=28
    WHILE=29
    FOR=30
    FOREACH=31
    NEW=32
    CLONE=33
    THROW=34
    TRY=35
    CATCH=36
    FINALLY=37
    INSTANCEOF=38
    DECLARE=39
    SEMI=40
    COLON=41
    COMMA=42
    DOT=43
    ARROW=44
    NULLSAFE_ARROW=45
    DOUBLE_COLON=46
    BACKSLASH=47
    DOUBLE_ARROW=48
    LPAREN=49
    RPAREN=50
    LBRACE=51
    RBRACE=52
    LBRACK=53
    RBRACK=54
    QUESTION=55
    PIPE=56
    AMP=57
    ELLIPSIS=58
    EQUAL=59
    VARIABLE=60
    IDENTIFIER=61
    NUMBER=62
    STRING_LITERAL=63
    LINE_COMMENT=64
    BLOCK_COMMENT=65
    WS=66
    OTHER_OP=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PhpFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PHPParser.EOF, 0)

        def PHP_OPEN(self):
            return self.getToken(PHPParser.PHP_OPEN, 0)

        def declareStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.DeclareStatementContext)
            else:
                return self.getTypedRuleContext(PHPParser.DeclareStatementContext,i)


        def namespaceStatement(self):
            return self.getTypedRuleContext(PHPParser.NamespaceStatementContext,0)


        def topLevelStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.TopLevelStatementContext)
            else:
                return self.getTypedRuleContext(PHPParser.TopLevelStatementContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_phpFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhpFile" ):
                listener.enterPhpFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhpFile" ):
                listener.exitPhpFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhpFile" ):
                return visitor.visitPhpFile(self)
            else:
                return visitor.visitChildren(self)




    def phpFile(self):

        localctx = PHPParser.PhpFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_phpFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 90
                self.match(PHPParser.PHP_OPEN)


            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 93
                self.declareStatement()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 99
                self.namespaceStatement()


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1140957168829202440) != 0):
                self.state = 102
                self.topLevelStatement()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(PHPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(PHPParser.DECLARE, 0)

        def LPAREN(self):
            return self.getToken(PHPParser.LPAREN, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def EQUAL(self):
            return self.getToken(PHPParser.EQUAL, 0)

        def literal(self):
            return self.getTypedRuleContext(PHPParser.LiteralContext,0)


        def RPAREN(self):
            return self.getToken(PHPParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(PHPParser.SEMI, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_declareStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareStatement" ):
                listener.enterDeclareStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareStatement" ):
                listener.exitDeclareStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareStatement" ):
                return visitor.visitDeclareStatement(self)
            else:
                return visitor.visitChildren(self)




    def declareStatement(self):

        localctx = PHPParser.DeclareStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declareStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(PHPParser.DECLARE)
            self.state = 111
            self.match(PHPParser.LPAREN)
            self.state = 112
            self.qualifiedName()
            self.state = 113
            self.match(PHPParser.EQUAL)
            self.state = 114
            self.literal()
            self.state = 115
            self.match(PHPParser.RPAREN)
            self.state = 116
            self.match(PHPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMESPACE(self):
            return self.getToken(PHPParser.NAMESPACE, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def SEMI(self):
            return self.getToken(PHPParser.SEMI, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def topLevelStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.TopLevelStatementContext)
            else:
                return self.getTypedRuleContext(PHPParser.TopLevelStatementContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_namespaceStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespaceStatement" ):
                listener.enterNamespaceStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespaceStatement" ):
                listener.exitNamespaceStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespaceStatement" ):
                return visitor.visitNamespaceStatement(self)
            else:
                return visitor.visitChildren(self)




    def namespaceStatement(self):

        localctx = PHPParser.NamespaceStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namespaceStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(PHPParser.NAMESPACE)
            self.state = 119
            self.qualifiedName()
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.state = 120
                self.match(PHPParser.SEMI)
                pass
            elif token in [51]:
                self.state = 121
                self.match(PHPParser.LBRACE)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1140957168829202440) != 0):
                    self.state = 122
                    self.topLevelStatement()
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 128
                self.match(PHPParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(PHPParser.USE, 0)

        def useDeclarationList(self):
            return self.getTypedRuleContext(PHPParser.UseDeclarationListContext,0)


        def SEMI(self):
            return self.getToken(PHPParser.SEMI, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(PHPParser.DOUBLE_COLON, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def useItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.UseItemContext)
            else:
                return self.getTypedRuleContext(PHPParser.UseItemContext,i)


        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_useStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseStatement" ):
                listener.enterUseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseStatement" ):
                listener.exitUseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseStatement" ):
                return visitor.visitUseStatement(self)
            else:
                return visitor.visitChildren(self)




    def useStatement(self):

        localctx = PHPParser.UseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_useStatement)
        self._la = 0 # Token type
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(PHPParser.USE)
                self.state = 132
                self.useDeclarationList()
                self.state = 133
                self.match(PHPParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(PHPParser.USE)
                self.state = 136
                self.qualifiedName()
                self.state = 137
                self.match(PHPParser.DOUBLE_COLON)
                self.state = 138
                self.match(PHPParser.LBRACE)
                self.state = 139
                self.useItem()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 140
                    self.match(PHPParser.COMMA)
                    self.state = 141
                    self.useItem()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 147
                self.match(PHPParser.RBRACE)
                self.state = 148
                self.match(PHPParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseDeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def useItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.UseItemContext)
            else:
                return self.getTypedRuleContext(PHPParser.UseItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_useDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseDeclarationList" ):
                listener.enterUseDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseDeclarationList" ):
                listener.exitUseDeclarationList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseDeclarationList" ):
                return visitor.visitUseDeclarationList(self)
            else:
                return visitor.visitChildren(self)




    def useDeclarationList(self):

        localctx = PHPParser.UseDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_useDeclarationList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.useItem()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 153
                self.match(PHPParser.COMMA)
                self.state = 154
                self.useItem()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def AS(self):
            return self.getToken(PHPParser.AS, 0)

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_useItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseItem" ):
                listener.enterUseItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseItem" ):
                listener.exitUseItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseItem" ):
                return visitor.visitUseItem(self)
            else:
                return visitor.visitChildren(self)




    def useItem(self):

        localctx = PHPParser.UseItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_useItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.qualifiedName()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 161
                self.match(PHPParser.AS)
                self.state = 162
                self.match(PHPParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopLevelStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def useStatement(self):
            return self.getTypedRuleContext(PHPParser.UseStatementContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(PHPParser.ClassDeclarationContext,0)


        def interfaceDeclaration(self):
            return self.getTypedRuleContext(PHPParser.InterfaceDeclarationContext,0)


        def traitDeclaration(self):
            return self.getTypedRuleContext(PHPParser.TraitDeclarationContext,0)


        def enumDeclaration(self):
            return self.getTypedRuleContext(PHPParser.EnumDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(PHPParser.FunctionDeclarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(PHPParser.StatementContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_topLevelStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopLevelStatement" ):
                listener.enterTopLevelStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopLevelStatement" ):
                listener.exitTopLevelStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTopLevelStatement" ):
                return visitor.visitTopLevelStatement(self)
            else:
                return visitor.visitChildren(self)




    def topLevelStatement(self):

        localctx = PHPParser.TopLevelStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_topLevelStatement)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.useStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.classDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.interfaceDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.traitDeclaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                self.enumDeclaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 170
                self.functionDeclaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 171
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(PHPParser.CLASS, 0)

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def classModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ClassModifierContext)
            else:
                return self.getTypedRuleContext(PHPParser.ClassModifierContext,i)


        def EXTENDS(self):
            return self.getToken(PHPParser.EXTENDS, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def IMPLEMENTS(self):
            return self.getToken(PHPParser.IMPLEMENTS, 0)

        def qualifiedNameList(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameListContext,0)


        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(PHPParser.ClassMemberContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = PHPParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0):
                self.state = 174
                self.classModifier()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(PHPParser.CLASS)
            self.state = 181
            self.match(PHPParser.IDENTIFIER)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 182
                self.match(PHPParser.EXTENDS)
                self.state = 183
                self.qualifiedName()


            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 186
                self.match(PHPParser.IMPLEMENTS)
                self.state = 187
                self.qualifiedNameList()


            self.state = 190
            self.match(PHPParser.LBRACE)
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1140957168829202440) != 0):
                self.state = 191
                self.classMember()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self.match(PHPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERFACE(self):
            return self.getToken(PHPParser.INTERFACE, 0)

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def EXTENDS(self):
            return self.getToken(PHPParser.EXTENDS, 0)

        def qualifiedNameList(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameListContext,0)


        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(PHPParser.ClassMemberContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_interfaceDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterfaceDeclaration" ):
                listener.enterInterfaceDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterfaceDeclaration" ):
                listener.exitInterfaceDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDeclaration" ):
                return visitor.visitInterfaceDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDeclaration(self):

        localctx = PHPParser.InterfaceDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_interfaceDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(PHPParser.INTERFACE)
            self.state = 200
            self.match(PHPParser.IDENTIFIER)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 201
                self.match(PHPParser.EXTENDS)
                self.state = 202
                self.qualifiedNameList()


            self.state = 205
            self.match(PHPParser.LBRACE)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1140957168829202440) != 0):
                self.state = 206
                self.classMember()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 212
            self.match(PHPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TraitDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRAIT(self):
            return self.getToken(PHPParser.TRAIT, 0)

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(PHPParser.ClassMemberContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_traitDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTraitDeclaration" ):
                listener.enterTraitDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTraitDeclaration" ):
                listener.exitTraitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTraitDeclaration" ):
                return visitor.visitTraitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def traitDeclaration(self):

        localctx = PHPParser.TraitDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_traitDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(PHPParser.TRAIT)
            self.state = 215
            self.match(PHPParser.IDENTIFIER)
            self.state = 216
            self.match(PHPParser.LBRACE)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1140957168829202440) != 0):
                self.state = 217
                self.classMember()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
            self.match(PHPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnumDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM(self):
            return self.getToken(PHPParser.ENUM, 0)

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def COLON(self):
            return self.getToken(PHPParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(PHPParser.TypeContext,0)


        def IMPLEMENTS(self):
            return self.getToken(PHPParser.IMPLEMENTS, 0)

        def qualifiedNameList(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameListContext,0)


        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(PHPParser.ClassMemberContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_enumDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnumDeclaration" ):
                listener.enterEnumDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnumDeclaration" ):
                listener.exitEnumDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnumDeclaration" ):
                return visitor.visitEnumDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def enumDeclaration(self):

        localctx = PHPParser.EnumDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_enumDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(PHPParser.ENUM)
            self.state = 226
            self.match(PHPParser.IDENTIFIER)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 227
                self.match(PHPParser.COLON)
                self.state = 228
                self.type_()


            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 231
                self.match(PHPParser.IMPLEMENTS)
                self.state = 232
                self.qualifiedNameList()


            self.state = 235
            self.match(PHPParser.LBRACE)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1140957168829202440) != 0):
                self.state = 236
                self.classMember()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self.match(PHPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDeclaration(self):
            return self.getTypedRuleContext(PHPParser.MethodDeclarationContext,0)


        def propertyDeclaration(self):
            return self.getTypedRuleContext(PHPParser.PropertyDeclarationContext,0)


        def constDeclaration(self):
            return self.getTypedRuleContext(PHPParser.ConstDeclarationContext,0)


        def useTraitStatement(self):
            return self.getTypedRuleContext(PHPParser.UseTraitStatementContext,0)


        def statement(self):
            return self.getTypedRuleContext(PHPParser.StatementContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_classMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMember" ):
                listener.enterClassMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMember" ):
                listener.exitClassMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMember" ):
                return visitor.visitClassMember(self)
            else:
                return visitor.visitChildren(self)




    def classMember(self):

        localctx = PHPParser.ClassMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_classMember)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.methodDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.propertyDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 246
                self.constDeclaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.useTraitStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseTraitStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USE(self):
            return self.getToken(PHPParser.USE, 0)

        def qualifiedNameList(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameListContext,0)


        def SEMI(self):
            return self.getToken(PHPParser.SEMI, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_useTraitStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseTraitStatement" ):
                listener.enterUseTraitStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseTraitStatement" ):
                listener.exitUseTraitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseTraitStatement" ):
                return visitor.visitUseTraitStatement(self)
            else:
                return visitor.visitChildren(self)




    def useTraitStatement(self):

        localctx = PHPParser.UseTraitStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_useTraitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(PHPParser.USE)
            self.state = 252
            self.qualifiedNameList()
            self.state = 253
            self.match(PHPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(PHPParser.CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(PHPParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(PHPParser.SEMI, 0)

        def memberModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.MemberModifierContext)
            else:
                return self.getTypedRuleContext(PHPParser.MemberModifierContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_constDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstDeclaration" ):
                listener.enterConstDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstDeclaration" ):
                listener.exitConstDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDeclaration" ):
                return visitor.visitConstDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def constDeclaration(self):

        localctx = PHPParser.ConstDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_constDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1040384) != 0):
                self.state = 255
                self.memberModifier()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 261
            self.match(PHPParser.CONST)
            self.state = 262
            self.match(PHPParser.IDENTIFIER)
            self.state = 263
            self.match(PHPParser.EQUAL)
            self.state = 264
            self.expression()
            self.state = 265
            self.match(PHPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.VARIABLE)
            else:
                return self.getToken(PHPParser.VARIABLE, i)

        def SEMI(self):
            return self.getToken(PHPParser.SEMI, 0)

        def memberModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.MemberModifierContext)
            else:
                return self.getTypedRuleContext(PHPParser.MemberModifierContext,i)


        def type_(self):
            return self.getTypedRuleContext(PHPParser.TypeContext,0)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.EQUAL)
            else:
                return self.getToken(PHPParser.EQUAL, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PHPParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_propertyDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyDeclaration" ):
                listener.enterPropertyDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyDeclaration" ):
                listener.exitPropertyDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPropertyDeclaration" ):
                return visitor.visitPropertyDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def propertyDeclaration(self):

        localctx = PHPParser.PropertyDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_propertyDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 267
                    self.memberModifier()

                else:
                    raise NoViableAltException(self)
                self.state = 270 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2342013093476823032) != 0):
                self.state = 272
                self.type_()


            self.state = 275
            self.match(PHPParser.VARIABLE)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 276
                self.match(PHPParser.EQUAL)
                self.state = 277
                self.expression()


            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 280
                self.match(PHPParser.COMMA)
                self.state = 281
                self.match(PHPParser.VARIABLE)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==59:
                    self.state = 282
                    self.match(PHPParser.EQUAL)
                    self.state = 283
                    self.expression()


                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
            self.match(PHPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(PHPParser.FUNCTION, 0)

        def methodName(self):
            return self.getTypedRuleContext(PHPParser.MethodNameContext,0)


        def LPAREN(self):
            return self.getToken(PHPParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PHPParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(PHPParser.BlockContext,0)


        def SEMI(self):
            return self.getToken(PHPParser.SEMI, 0)

        def memberModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.MemberModifierContext)
            else:
                return self.getTypedRuleContext(PHPParser.MemberModifierContext,i)


        def parameterList(self):
            return self.getTypedRuleContext(PHPParser.ParameterListContext,0)


        def COLON(self):
            return self.getToken(PHPParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(PHPParser.TypeContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = PHPParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1040384) != 0):
                self.state = 293
                self.memberModifier()
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 299
            self.match(PHPParser.FUNCTION)
            self.state = 300
            self.methodName()
            self.state = 301
            self.match(PHPParser.LPAREN)
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3927280162311237624) != 0):
                self.state = 302
                self.parameterList()


            self.state = 305
            self.match(PHPParser.RPAREN)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 306
                self.match(PHPParser.COLON)
                self.state = 307
                self.type_()


            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [51]:
                self.state = 310
                self.block()
                pass
            elif token in [40]:
                self.state = 311
                self.match(PHPParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(PHPParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(PHPParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PHPParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(PHPParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(PHPParser.ParameterListContext,0)


        def COLON(self):
            return self.getToken(PHPParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(PHPParser.TypeContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = PHPParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(PHPParser.FUNCTION)
            self.state = 315
            self.match(PHPParser.IDENTIFIER)
            self.state = 316
            self.match(PHPParser.LPAREN)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3927280162311237624) != 0):
                self.state = 317
                self.parameterList()


            self.state = 320
            self.match(PHPParser.RPAREN)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 321
                self.match(PHPParser.COLON)
                self.state = 322
                self.type_()


            self.state = 325
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def keywordAsIdentifier(self):
            return self.getTypedRuleContext(PHPParser.KeywordAsIdentifierContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_methodName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodName" ):
                listener.enterMethodName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodName" ):
                listener.exitMethodName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodName" ):
                return visitor.visitMethodName(self)
            else:
                return visitor.visitChildren(self)




    def methodName(self):

        localctx = PHPParser.MethodNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_methodName)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [61]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(PHPParser.IDENTIFIER)
                pass
            elif token in [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.keywordAsIdentifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordAsIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATCH(self):
            return self.getToken(PHPParser.MATCH, 0)

        def SWITCH(self):
            return self.getToken(PHPParser.SWITCH, 0)

        def CASE(self):
            return self.getToken(PHPParser.CASE, 0)

        def DEFAULT(self):
            return self.getToken(PHPParser.DEFAULT, 0)

        def IF(self):
            return self.getToken(PHPParser.IF, 0)

        def ELSEIF(self):
            return self.getToken(PHPParser.ELSEIF, 0)

        def ELSE(self):
            return self.getToken(PHPParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(PHPParser.WHILE, 0)

        def FOR(self):
            return self.getToken(PHPParser.FOR, 0)

        def FOREACH(self):
            return self.getToken(PHPParser.FOREACH, 0)

        def NEW(self):
            return self.getToken(PHPParser.NEW, 0)

        def CLONE(self):
            return self.getToken(PHPParser.CLONE, 0)

        def THROW(self):
            return self.getToken(PHPParser.THROW, 0)

        def TRY(self):
            return self.getToken(PHPParser.TRY, 0)

        def CATCH(self):
            return self.getToken(PHPParser.CATCH, 0)

        def FINALLY(self):
            return self.getToken(PHPParser.FINALLY, 0)

        def CLASS(self):
            return self.getToken(PHPParser.CLASS, 0)

        def INTERFACE(self):
            return self.getToken(PHPParser.INTERFACE, 0)

        def TRAIT(self):
            return self.getToken(PHPParser.TRAIT, 0)

        def ENUM(self):
            return self.getToken(PHPParser.ENUM, 0)

        def EXTENDS(self):
            return self.getToken(PHPParser.EXTENDS, 0)

        def IMPLEMENTS(self):
            return self.getToken(PHPParser.IMPLEMENTS, 0)

        def FUNCTION(self):
            return self.getToken(PHPParser.FUNCTION, 0)

        def PUBLIC(self):
            return self.getToken(PHPParser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(PHPParser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(PHPParser.PRIVATE, 0)

        def STATIC(self):
            return self.getToken(PHPParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(PHPParser.FINAL, 0)

        def ABSTRACT(self):
            return self.getToken(PHPParser.ABSTRACT, 0)

        def READONLY(self):
            return self.getToken(PHPParser.READONLY, 0)

        def CONST(self):
            return self.getToken(PHPParser.CONST, 0)

        def RETURN(self):
            return self.getToken(PHPParser.RETURN, 0)

        def USE(self):
            return self.getToken(PHPParser.USE, 0)

        def AS(self):
            return self.getToken(PHPParser.AS, 0)

        def INSTANCEOF(self):
            return self.getToken(PHPParser.INSTANCEOF, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_keywordAsIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordAsIdentifier" ):
                listener.enterKeywordAsIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordAsIdentifier" ):
                listener.exitKeywordAsIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywordAsIdentifier" ):
                return visitor.visitKeywordAsIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def keywordAsIdentifier(self):

        localctx = PHPParser.KeywordAsIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_keywordAsIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 549755809784) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PHPParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = PHPParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.parameter()
            self.state = 338
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 334
                    self.match(PHPParser.COMMA)
                    self.state = 335
                    self.parameter() 
                self.state = 340
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 341
                self.match(PHPParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(PHPParser.VARIABLE, 0)

        def memberModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.MemberModifierContext)
            else:
                return self.getTypedRuleContext(PHPParser.MemberModifierContext,i)


        def type_(self):
            return self.getTypedRuleContext(PHPParser.TypeContext,0)


        def AMP(self):
            return self.getToken(PHPParser.AMP, 0)

        def ELLIPSIS(self):
            return self.getToken(PHPParser.ELLIPSIS, 0)

        def EQUAL(self):
            return self.getToken(PHPParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = PHPParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 344
                    self.memberModifier() 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2342013093476823032) != 0):
                self.state = 350
                self.type_()


            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 353
                self.match(PHPParser.AMP)


            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 356
                self.match(PHPParser.ELLIPSIS)


            self.state = 359
            self.match(PHPParser.VARIABLE)
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==59:
                self.state = 360
                self.match(PHPParser.EQUAL)
                self.state = 361
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABSTRACT(self):
            return self.getToken(PHPParser.ABSTRACT, 0)

        def FINAL(self):
            return self.getToken(PHPParser.FINAL, 0)

        def READONLY(self):
            return self.getToken(PHPParser.READONLY, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_classModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassModifier" ):
                listener.enterClassModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassModifier" ):
                listener.exitClassModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassModifier" ):
                return visitor.visitClassModifier(self)
            else:
                return visitor.visitChildren(self)




    def classModifier(self):

        localctx = PHPParser.ClassModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_classModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(PHPParser.PUBLIC, 0)

        def PROTECTED(self):
            return self.getToken(PHPParser.PROTECTED, 0)

        def PRIVATE(self):
            return self.getToken(PHPParser.PRIVATE, 0)

        def STATIC(self):
            return self.getToken(PHPParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(PHPParser.FINAL, 0)

        def ABSTRACT(self):
            return self.getToken(PHPParser.ABSTRACT, 0)

        def READONLY(self):
            return self.getToken(PHPParser.READONLY, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_memberModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberModifier" ):
                listener.enterMemberModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberModifier" ):
                listener.exitMemberModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberModifier" ):
                return visitor.visitMemberModifier(self)
            else:
                return visitor.visitChildren(self)




    def memberModifier(self):

        localctx = PHPParser.MemberModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_memberModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1040384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedNameListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.QualifiedNameContext)
            else:
                return self.getTypedRuleContext(PHPParser.QualifiedNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_qualifiedNameList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedNameList" ):
                listener.enterQualifiedNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedNameList" ):
                listener.exitQualifiedNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedNameList" ):
                return visitor.visitQualifiedNameList(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedNameList(self):

        localctx = PHPParser.QualifiedNameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_qualifiedNameList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.qualifiedName()
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 369
                self.match(PHPParser.COMMA)
                self.state = 370
                self.qualifiedName()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.IDENTIFIER)
            else:
                return self.getToken(PHPParser.IDENTIFIER, i)

        def keywordAsIdentifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.KeywordAsIdentifierContext)
            else:
                return self.getTypedRuleContext(PHPParser.KeywordAsIdentifierContext,i)


        def BACKSLASH(self):
            return self.getToken(PHPParser.BACKSLASH, 0)

        def qualifiedSeparator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.QualifiedSeparatorContext)
            else:
                return self.getTypedRuleContext(PHPParser.QualifiedSeparatorContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_qualifiedName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedName" ):
                listener.enterQualifiedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedName" ):
                listener.exitQualifiedName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedName" ):
                return visitor.visitQualifiedName(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedName(self):

        localctx = PHPParser.QualifiedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_qualifiedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 376
                self.match(PHPParser.BACKSLASH)


            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [61]:
                self.state = 379
                self.match(PHPParser.IDENTIFIER)
                pass
            elif token in [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]:
                self.state = 380
                self.keywordAsIdentifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 383
                    self.qualifiedSeparator()
                    self.state = 386
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [61]:
                        self.state = 384
                        self.match(PHPParser.IDENTIFIER)
                        pass
                    elif token in [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]:
                        self.state = 385
                        self.keywordAsIdentifier()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedSeparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKSLASH(self):
            return self.getToken(PHPParser.BACKSLASH, 0)

        def DOUBLE_COLON(self):
            return self.getToken(PHPParser.DOUBLE_COLON, 0)

        def OTHER_OP(self):
            return self.getToken(PHPParser.OTHER_OP, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_qualifiedSeparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedSeparator" ):
                listener.enterQualifiedSeparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedSeparator" ):
                listener.exitQualifiedSeparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQualifiedSeparator" ):
                return visitor.visitQualifiedSeparator(self)
            else:
                return visitor.visitChildren(self)




    def qualifiedSeparator(self):

        localctx = PHPParser.QualifiedSeparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_qualifiedSeparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            _la = self._input.LA(1)
            if not(((((_la - 46)) & ~0x3f) == 0 and ((1 << (_la - 46)) & 2097155) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.QualifiedNameContext)
            else:
                return self.getTypedRuleContext(PHPParser.QualifiedNameContext,i)


        def QUESTION(self):
            return self.getToken(PHPParser.QUESTION, 0)

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.PIPE)
            else:
                return self.getToken(PHPParser.PIPE, i)

        def getRuleIndex(self):
            return PHPParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PHPParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 395
                self.match(PHPParser.QUESTION)


            self.state = 398
            self.qualifiedName()
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==56:
                self.state = 399
                self.match(PHPParser.PIPE)
                self.state = 400
                self.qualifiedName()
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.StatementContext)
            else:
                return self.getTypedRuleContext(PHPParser.StatementContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = PHPParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(PHPParser.LBRACE)
            self.state = 410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1140957168829202440) != 0):
                self.state = 407
                self.statement()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 413
            self.match(PHPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.BlockContext)
            else:
                return self.getTypedRuleContext(PHPParser.BlockContext,i)


        def RETURN(self):
            return self.getToken(PHPParser.RETURN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.SEMI)
            else:
                return self.getToken(PHPParser.SEMI, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PHPParser.ExpressionContext,i)


        def THROW(self):
            return self.getToken(PHPParser.THROW, 0)

        def IF(self):
            return self.getToken(PHPParser.IF, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.LPAREN)
            else:
                return self.getToken(PHPParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.RPAREN)
            else:
                return self.getToken(PHPParser.RPAREN, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.StatementContext)
            else:
                return self.getTypedRuleContext(PHPParser.StatementContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.ELSEIF)
            else:
                return self.getToken(PHPParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(PHPParser.ELSE, 0)

        def SWITCH(self):
            return self.getToken(PHPParser.SWITCH, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def switchBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.SwitchBlockContext)
            else:
                return self.getTypedRuleContext(PHPParser.SwitchBlockContext,i)


        def WHILE(self):
            return self.getToken(PHPParser.WHILE, 0)

        def FOR(self):
            return self.getToken(PHPParser.FOR, 0)

        def FOREACH(self):
            return self.getToken(PHPParser.FOREACH, 0)

        def AS(self):
            return self.getToken(PHPParser.AS, 0)

        def DOUBLE_ARROW(self):
            return self.getToken(PHPParser.DOUBLE_ARROW, 0)

        def TRY(self):
            return self.getToken(PHPParser.TRY, 0)

        def CATCH(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.CATCH)
            else:
                return self.getToken(PHPParser.CATCH, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.TypeContext)
            else:
                return self.getTypedRuleContext(PHPParser.TypeContext,i)


        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.VARIABLE)
            else:
                return self.getToken(PHPParser.VARIABLE, i)

        def FINALLY(self):
            return self.getToken(PHPParser.FINALLY, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PHPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.match(PHPParser.RETURN)
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -1143210068154515464) != 0):
                    self.state = 417
                    self.expression()


                self.state = 420
                self.match(PHPParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 421
                self.match(PHPParser.THROW)
                self.state = 422
                self.expression()
                self.state = 423
                self.match(PHPParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 425
                self.match(PHPParser.IF)
                self.state = 426
                self.match(PHPParser.LPAREN)
                self.state = 427
                self.expression()
                self.state = 428
                self.match(PHPParser.RPAREN)
                self.state = 429
                self.statement()
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 430
                        self.match(PHPParser.ELSEIF)
                        self.state = 431
                        self.match(PHPParser.LPAREN)
                        self.state = 432
                        self.expression()
                        self.state = 433
                        self.match(PHPParser.RPAREN)
                        self.state = 434
                        self.statement() 
                    self.state = 440
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                self.state = 443
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 441
                    self.match(PHPParser.ELSE)
                    self.state = 442
                    self.statement()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 445
                self.match(PHPParser.SWITCH)
                self.state = 446
                self.match(PHPParser.LPAREN)
                self.state = 447
                self.expression()
                self.state = 448
                self.match(PHPParser.RPAREN)
                self.state = 449
                self.match(PHPParser.LBRACE)
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24 or _la==25:
                    self.state = 450
                    self.switchBlock()
                    self.state = 455
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 456
                self.match(PHPParser.RBRACE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 458
                self.match(PHPParser.WHILE)
                self.state = 459
                self.match(PHPParser.LPAREN)
                self.state = 460
                self.expression()
                self.state = 461
                self.match(PHPParser.RPAREN)
                self.state = 462
                self.statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 464
                self.match(PHPParser.FOR)
                self.state = 465
                self.match(PHPParser.LPAREN)
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -1143210068154515464) != 0):
                    self.state = 466
                    self.expression()


                self.state = 469
                self.match(PHPParser.SEMI)
                self.state = 471
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -1143210068154515464) != 0):
                    self.state = 470
                    self.expression()


                self.state = 473
                self.match(PHPParser.SEMI)
                self.state = 475
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -1143210068154515464) != 0):
                    self.state = 474
                    self.expression()


                self.state = 477
                self.match(PHPParser.RPAREN)
                self.state = 478
                self.statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 479
                self.match(PHPParser.FOREACH)
                self.state = 480
                self.match(PHPParser.LPAREN)
                self.state = 481
                self.expression()
                self.state = 482
                self.match(PHPParser.AS)
                self.state = 486
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                if la_ == 1:
                    self.state = 483
                    self.expression()
                    self.state = 484
                    self.match(PHPParser.DOUBLE_ARROW)


                self.state = 488
                self.expression()
                self.state = 489
                self.match(PHPParser.RPAREN)
                self.state = 490
                self.statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 492
                self.match(PHPParser.TRY)
                self.state = 493
                self.block()
                self.state = 503
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,58,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 494
                        self.match(PHPParser.CATCH)
                        self.state = 495
                        self.match(PHPParser.LPAREN)
                        self.state = 496
                        self.type_()
                        self.state = 497
                        self.match(PHPParser.VARIABLE)
                        self.state = 498
                        self.match(PHPParser.RPAREN)
                        self.state = 499
                        self.block() 
                    self.state = 505
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,58,self._ctx)

                self.state = 508
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                if la_ == 1:
                    self.state = 506
                    self.match(PHPParser.FINALLY)
                    self.state = 507
                    self.block()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 510
                self.expression()
                self.state = 511
                self.match(PHPParser.SEMI)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 513
                self.match(PHPParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(PHPParser.COLON, 0)

        def CASE(self):
            return self.getToken(PHPParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def DEFAULT(self):
            return self.getToken(PHPParser.DEFAULT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.StatementContext)
            else:
                return self.getTypedRuleContext(PHPParser.StatementContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_switchBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchBlock" ):
                listener.enterSwitchBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchBlock" ):
                listener.exitSwitchBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchBlock" ):
                return visitor.visitSwitchBlock(self)
            else:
                return visitor.visitChildren(self)




    def switchBlock(self):

        localctx = PHPParser.SwitchBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_switchBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.state = 516
                self.match(PHPParser.CASE)
                self.state = 517
                self.expression()
                pass
            elif token in [25]:
                self.state = 518
                self.match(PHPParser.DEFAULT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 521
            self.match(PHPParser.COLON)
            self.state = 525
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 522
                    self.statement() 
                self.state = 527
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.PrimaryExpressionContext)
            else:
                return self.getTypedRuleContext(PHPParser.PrimaryExpressionContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.OperatorContext)
            else:
                return self.getTypedRuleContext(PHPParser.OperatorContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PHPParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.primaryExpression()
            self.state = 534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,63,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 529
                    self.operator()
                    self.state = 530
                    self.primaryExpression() 
                self.state = 536
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,63,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(PHPParser.VARIABLE, 0)

        def literal(self):
            return self.getTypedRuleContext(PHPParser.LiteralContext,0)


        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def matchExpression(self):
            return self.getTypedRuleContext(PHPParser.MatchExpressionContext,0)


        def newExpression(self):
            return self.getTypedRuleContext(PHPParser.NewExpressionContext,0)


        def cloneExpression(self):
            return self.getTypedRuleContext(PHPParser.CloneExpressionContext,0)


        def closureExpression(self):
            return self.getTypedRuleContext(PHPParser.ClosureExpressionContext,0)


        def arrayExpression(self):
            return self.getTypedRuleContext(PHPParser.ArrayExpressionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(PHPParser.FunctionCallContext,0)


        def memberAccess(self):
            return self.getTypedRuleContext(PHPParser.MemberAccessContext,0)


        def LPAREN(self):
            return self.getToken(PHPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PHPParser.RPAREN, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = PHPParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_primaryExpression)
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.match(PHPParser.VARIABLE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 539
                self.qualifiedName()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 540
                self.matchExpression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 541
                self.newExpression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 542
                self.cloneExpression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 543
                self.closureExpression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 544
                self.arrayExpression()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 545
                self.functionCall()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 546
                self.memberAccess()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 547
                self.match(PHPParser.LPAREN)
                self.state = 548
                self.expression()
                self.state = 549
                self.match(PHPParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(PHPParser.NEW, 0)

        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def LPAREN(self):
            return self.getToken(PHPParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PHPParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(PHPParser.ArgumentListContext,0)


        def CLASS(self):
            return self.getToken(PHPParser.CLASS, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def EXTENDS(self):
            return self.getToken(PHPParser.EXTENDS, 0)

        def IMPLEMENTS(self):
            return self.getToken(PHPParser.IMPLEMENTS, 0)

        def qualifiedNameList(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameListContext,0)


        def classMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ClassMemberContext)
            else:
                return self.getTypedRuleContext(PHPParser.ClassMemberContext,i)


        def getRuleIndex(self):
            return PHPParser.RULE_newExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewExpression" ):
                listener.enterNewExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewExpression" ):
                listener.exitNewExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewExpression" ):
                return visitor.visitNewExpression(self)
            else:
                return visitor.visitChildren(self)




    def newExpression(self):

        localctx = PHPParser.NewExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_newExpression)
        self._la = 0 # Token type
        try:
            self.state = 585
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.match(PHPParser.NEW)
                self.state = 554
                self.qualifiedName()
                self.state = 560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==49:
                    self.state = 555
                    self.match(PHPParser.LPAREN)
                    self.state = 557
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & -854979692002803720) != 0):
                        self.state = 556
                        self.argumentList()


                    self.state = 559
                    self.match(PHPParser.RPAREN)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 562
                self.match(PHPParser.NEW)
                self.state = 563
                self.match(PHPParser.CLASS)
                self.state = 566
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 564
                    self.match(PHPParser.EXTENDS)
                    self.state = 565
                    self.qualifiedName()


                self.state = 570
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 568
                    self.match(PHPParser.IMPLEMENTS)
                    self.state = 569
                    self.qualifiedNameList()


                self.state = 572
                self.match(PHPParser.LPAREN)
                self.state = 574
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -854979692002803720) != 0):
                    self.state = 573
                    self.argumentList()


                self.state = 576
                self.match(PHPParser.RPAREN)
                self.state = 577
                self.match(PHPParser.LBRACE)
                self.state = 581
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1140957168829202440) != 0):
                    self.state = 578
                    self.classMember()
                    self.state = 583
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 584
                self.match(PHPParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloneExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLONE(self):
            return self.getToken(PHPParser.CLONE, 0)

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_cloneExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCloneExpression" ):
                listener.enterCloneExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCloneExpression" ):
                listener.exitCloneExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCloneExpression" ):
                return visitor.visitCloneExpression(self)
            else:
                return visitor.visitChildren(self)




    def cloneExpression(self):

        localctx = PHPParser.CloneExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_cloneExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 587
            self.match(PHPParser.CLONE)
            self.state = 588
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClosureExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(PHPParser.FUNCTION, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.LPAREN)
            else:
                return self.getToken(PHPParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.RPAREN)
            else:
                return self.getToken(PHPParser.RPAREN, i)

        def block(self):
            return self.getTypedRuleContext(PHPParser.BlockContext,0)


        def STATIC(self):
            return self.getToken(PHPParser.STATIC, 0)

        def parameterList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ParameterListContext)
            else:
                return self.getTypedRuleContext(PHPParser.ParameterListContext,i)


        def USE(self):
            return self.getToken(PHPParser.USE, 0)

        def COLON(self):
            return self.getToken(PHPParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(PHPParser.TypeContext,0)


        def FN(self):
            return self.getToken(PHPParser.FN, 0)

        def DOUBLE_ARROW(self):
            return self.getToken(PHPParser.DOUBLE_ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_closureExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosureExpression" ):
                listener.enterClosureExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosureExpression" ):
                listener.exitClosureExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosureExpression" ):
                return visitor.visitClosureExpression(self)
            else:
                return visitor.visitChildren(self)




    def closureExpression(self):

        localctx = PHPParser.ClosureExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_closureExpression)
        self._la = 0 # Token type
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 590
                    self.match(PHPParser.STATIC)


                self.state = 593
                self.match(PHPParser.FUNCTION)
                self.state = 594
                self.match(PHPParser.LPAREN)
                self.state = 596
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3927280162311237624) != 0):
                    self.state = 595
                    self.parameterList()


                self.state = 598
                self.match(PHPParser.RPAREN)
                self.state = 605
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 599
                    self.match(PHPParser.USE)
                    self.state = 600
                    self.match(PHPParser.LPAREN)
                    self.state = 602
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3927280162311237624) != 0):
                        self.state = 601
                        self.parameterList()


                    self.state = 604
                    self.match(PHPParser.RPAREN)


                self.state = 609
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==41:
                    self.state = 607
                    self.match(PHPParser.COLON)
                    self.state = 608
                    self.type_()


                self.state = 611
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 613
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 612
                    self.match(PHPParser.STATIC)


                self.state = 615
                self.match(PHPParser.FN)
                self.state = 616
                self.match(PHPParser.LPAREN)
                self.state = 618
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3927280162311237624) != 0):
                    self.state = 617
                    self.parameterList()


                self.state = 620
                self.match(PHPParser.RPAREN)
                self.state = 623
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==41:
                    self.state = 621
                    self.match(PHPParser.COLON)
                    self.state = 622
                    self.type_()


                self.state = 625
                self.match(PHPParser.DOUBLE_ARROW)
                self.state = 626
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(PHPParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(PHPParser.RBRACK, 0)

        def arrayElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ArrayElementContext)
            else:
                return self.getTypedRuleContext(PHPParser.ArrayElementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_arrayExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpression" ):
                listener.enterArrayExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpression" ):
                listener.exitArrayExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpression" ):
                return visitor.visitArrayExpression(self)
            else:
                return visitor.visitChildren(self)




    def arrayExpression(self):

        localctx = PHPParser.ArrayExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arrayExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(PHPParser.LBRACK)
            self.state = 641
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -1143210068154515464) != 0):
                self.state = 630
                self.arrayElement()
                self.state = 635
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 631
                        self.match(PHPParser.COMMA)
                        self.state = 632
                        self.arrayElement() 
                    self.state = 637
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

                self.state = 639
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 638
                    self.match(PHPParser.COMMA)




            self.state = 643
            self.match(PHPParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PHPParser.ExpressionContext,i)


        def DOUBLE_ARROW(self):
            return self.getToken(PHPParser.DOUBLE_ARROW, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_arrayElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayElement" ):
                listener.enterArrayElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayElement" ):
                listener.exitArrayElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayElement" ):
                return visitor.visitArrayElement(self)
            else:
                return visitor.visitChildren(self)




    def arrayElement(self):

        localctx = PHPParser.ArrayElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrayElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 645
                self.expression()
                self.state = 646
                self.match(PHPParser.DOUBLE_ARROW)


            self.state = 650
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATCH(self):
            return self.getToken(PHPParser.MATCH, 0)

        def LPAREN(self):
            return self.getToken(PHPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PHPParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(PHPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(PHPParser.RBRACE, 0)

        def matchArm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.MatchArmContext)
            else:
                return self.getTypedRuleContext(PHPParser.MatchArmContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_matchExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchExpression" ):
                listener.enterMatchExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchExpression" ):
                listener.exitMatchExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchExpression" ):
                return visitor.visitMatchExpression(self)
            else:
                return visitor.visitChildren(self)




    def matchExpression(self):

        localctx = PHPParser.MatchExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_matchExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.match(PHPParser.MATCH)
            self.state = 653
            self.match(PHPParser.LPAREN)
            self.state = 654
            self.expression()
            self.state = 655
            self.match(PHPParser.RPAREN)
            self.state = 656
            self.match(PHPParser.LBRACE)
            self.state = 668
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -1143210068154515464) != 0):
                self.state = 657
                self.matchArm()
                self.state = 662
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,85,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 658
                        self.match(PHPParser.COMMA)
                        self.state = 659
                        self.matchArm() 
                    self.state = 664
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,85,self._ctx)

                self.state = 666
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 665
                    self.match(PHPParser.COMMA)




            self.state = 670
            self.match(PHPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchArmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_ARROW(self):
            return self.getToken(PHPParser.DOUBLE_ARROW, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PHPParser.ExpressionContext,i)


        def DEFAULT(self):
            return self.getToken(PHPParser.DEFAULT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_matchArm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatchArm" ):
                listener.enterMatchArm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatchArm" ):
                listener.exitMatchArm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchArm" ):
                return visitor.visitMatchArm(self)
            else:
                return visitor.visitChildren(self)




    def matchArm(self):

        localctx = PHPParser.MatchArmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_matchArm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.state = 672
                self.expression()
                self.state = 677
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 673
                    self.match(PHPParser.COMMA)
                    self.state = 674
                    self.expression()
                    self.state = 679
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 680
                self.match(PHPParser.DEFAULT)
                pass


            self.state = 683
            self.match(PHPParser.DOUBLE_ARROW)
            self.state = 684
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def LPAREN(self):
            return self.getToken(PHPParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(PHPParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(PHPParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = PHPParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            self.qualifiedName()
            self.state = 687
            self.match(PHPParser.LPAREN)
            self.state = 689
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -854979692002803720) != 0):
                self.state = 688
                self.argumentList()


            self.state = 691
            self.match(PHPParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARROW(self):
            return self.getToken(PHPParser.ARROW, 0)

        def NULLSAFE_ARROW(self):
            return self.getToken(PHPParser.NULLSAFE_ARROW, 0)

        def DOUBLE_COLON(self):
            return self.getToken(PHPParser.DOUBLE_COLON, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.VARIABLE)
            else:
                return self.getToken(PHPParser.VARIABLE, i)

        def qualifiedName(self):
            return self.getTypedRuleContext(PHPParser.QualifiedNameContext,0)


        def LPAREN(self):
            return self.getToken(PHPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(PHPParser.RPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(PHPParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return PHPParser.RULE_memberAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberAccess" ):
                listener.enterMemberAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberAccess" ):
                listener.exitMemberAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccess" ):
                return visitor.visitMemberAccess(self)
            else:
                return visitor.visitChildren(self)




    def memberAccess(self):

        localctx = PHPParser.MemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_memberAccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [60]:
                self.state = 693
                self.match(PHPParser.VARIABLE)
                pass
            elif token in [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 47, 61]:
                self.state = 694
                self.qualifiedName()
                pass
            elif token in [49]:
                self.state = 695
                self.match(PHPParser.LPAREN)
                self.state = 696
                self.expression()
                self.state = 697
                self.match(PHPParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 701
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 123145302310912) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 705
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.state = 702
                self.match(PHPParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 703
                self.match(PHPParser.VARIABLE)
                pass

            elif la_ == 3:
                self.state = 704
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PHPParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(PHPParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PHPParser.COMMA)
            else:
                return self.getToken(PHPParser.COMMA, i)

        def getRuleIndex(self):
            return PHPParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = PHPParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            self.argument()
            self.state = 712
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,93,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 708
                    self.match(PHPParser.COMMA)
                    self.state = 709
                    self.argument() 
                self.state = 714
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,93,self._ctx)

            self.state = 716
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 715
                self.match(PHPParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PHPParser.ExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(PHPParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(PHPParser.COLON, 0)

        def ELLIPSIS(self):
            return self.getToken(PHPParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = PHPParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.state = 718
                self.match(PHPParser.IDENTIFIER)
                self.state = 719
                self.match(PHPParser.COLON)


            self.state = 723
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 722
                self.match(PHPParser.ELLIPSIS)


            self.state = 725
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PHPParser.NUMBER, 0)

        def STRING_LITERAL(self):
            return self.getToken(PHPParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = PHPParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
            _la = self._input.LA(1)
            if not(_la==62 or _la==63):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(PHPParser.EQUAL, 0)

        def DOUBLE_ARROW(self):
            return self.getToken(PHPParser.DOUBLE_ARROW, 0)

        def ARROW(self):
            return self.getToken(PHPParser.ARROW, 0)

        def NULLSAFE_ARROW(self):
            return self.getToken(PHPParser.NULLSAFE_ARROW, 0)

        def DOUBLE_COLON(self):
            return self.getToken(PHPParser.DOUBLE_COLON, 0)

        def DOT(self):
            return self.getToken(PHPParser.DOT, 0)

        def PIPE(self):
            return self.getToken(PHPParser.PIPE, 0)

        def AMP(self):
            return self.getToken(PHPParser.AMP, 0)

        def INSTANCEOF(self):
            return self.getToken(PHPParser.INSTANCEOF, 0)

        def OTHER_OP(self):
            return self.getToken(PHPParser.OTHER_OP, 0)

        def getRuleIndex(self):
            return PHPParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = PHPParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            _la = self._input.LA(1)
            if not(((((_la - 38)) & ~0x3f) == 0 and ((1 << (_la - 38)) & 539756001) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





