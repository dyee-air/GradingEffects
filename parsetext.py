from functools import partial
import os
# %%
MPLUS_FILE = 'U:/ESSIN Task 14/RAPS/03_Studies/2019/3_Grading effects study/2_Working/data/2013_NAEP_G12_Math_wo3PL-irt.txt'

outlines = list()

param_map = {
    '2PL': (
        'Item',
        'Label',
        'P#',
        'a',
        'se_a',
        'P#',
        'c',
        'se_c',
        'b',
        'se_b'
    ),
    'Graded': (
        'Item',
        'Label',
        'P#',
        'a',
        'se_a',
        'b1',
        'se_b1',
        'b2',
        'se_b2',
        'b3',
        'se_b3',
        'b4',
        'se_b4'
    )
}

IRT_2PL = dict((col, list())
               for col in ('Item', 'Label', 'a', 'b'))
IRT_GRM = dict((col, list())
               for col in ('Item', 'Label', 'a', 'b1', 'b2', 'b3', 'b4'))


def addIrtParams(irt_dict, params):
    if params:
        for col in irt_dict:
            irt_dict[col].append(params.get(col, None))


with open(MPLUS_FILE, 'r') as in_file:
    for line in in_file:
        if line.startswith(tuple(param_map)) and not 'c 1' in next(in_file):
            header = param_map[line.split()[0]]
            while not line.startswith('\n'):
                line = next(in_file)
                item_params = dict(zip(header, line.split()))
                if 'c' in header:
                    addIrtParams(IRT_2PL, item_params)
                else:
                    addIrtParams(IRT_GRM, item_params)
# %%
