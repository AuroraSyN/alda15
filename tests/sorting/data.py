#!/usr/bin/env python
#-*- coding:utf-8 -*-

array = [714805, 849868, 200803, 555883, -60455, 842763, 320908, 436470,
        127774, 791405, 97527, 120441, 793083, 706593, 526308, 304052, 210701,
        778987, 563337, 368063, -21517, 808998, 373323, 714939, 783387, 519404,
        700138, 424782, 621760, 452614, -86487, -65166, 236555, 837463, 242674,
        381597, 170495, 400580, 675162, -45492, 679939, 593171, 173405, -58419,
        553325, -6198, 249568, 805814, 814618, 475751, 323651, 52278, 219421,
        129670, 289166, 341995, 921422, 65455, 783130, 420950, 481901, 203674,
        787375, 795938, 729533, -85649, 820006, 637852, 351431, 564496, 209767,
        746956, 863462, -93278, 942467, 321524, 698579, 913817, 240651, 156495,
        511792, 165845, 45169, 896737, 928144, 706516, 937842, -64749, 647812,
        -60684, 869692, 35452, 636570, 370491, 196961, 356166, 760858, -88442,
        877647, 439942, 331440, 914029, 554935, 290210, 302467, 320959, 279261,
        485666, 836392, 481600, 771263, 484739, 167939, 311287, 2510, 244616,
        856747, 651541, 307140, 340050, -13471, 666442, 386638, 573566, -44902,
        577854, 194195, -16718, 17273, 854570, 647627, 902942, 868678, -69048,
        890360, 993326, 414448, 807725, 274579, 925055, 474551, 168700, 401519,
        167933, 708045, 587092, -9494, 982293, 649661, 793758, 461368, 503468,
        883750, 196935, 532620, 948938, 836568, 202818, 462970, 393414, 879437,
        347287, 416534, 516775, -57993, 251969, 470863, -14956, 143594, 776972,
        -62996, 545177, 820011, 734405, 414938, 158851, 112431, 838844, 313019,
        434877, 847638, 364101, 233694, 512234, 874307, 996514, 230269, 979561,
        444354, 814439, 115512, -42078, 163646, 143245, 364867, 844573, 504931,
        383114, 198544, -56898, 206359]

sorted_array = [-93278, -88442, -86487, -85649, -69048, -65166, -64749, -62996,
        -60684, -60455, -58419, -57993, -56898, -45492, -44902, -42078, -21517,
        -16718, -14956, -13471, -9494, -6198, 2510, 17273, 35452, 45169, 52278,
        65455, 97527, 112431, 115512, 120441, 127774, 129670, 143245, 143594,
        156495, 158851, 163646, 165845, 167933, 167939, 168700, 170495, 173405,
        194195, 196935, 196961, 198544, 200803, 202818, 203674, 206359, 209767,
        210701, 219421, 230269, 233694, 236555, 240651, 242674, 244616, 249568,
        251969, 274579, 279261, 289166, 290210, 302467, 304052, 307140, 311287,
        313019, 320908, 320959, 321524, 323651, 331440, 340050, 341995, 347287,
        351431, 356166, 364101, 364867, 368063, 370491, 373323, 381597, 383114,
        386638, 393414, 400580, 401519, 414448, 414938, 416534, 420950, 424782,
        434877, 436470, 439942, 444354, 452614, 461368, 462970, 470863, 474551,
        475751, 481600, 481901, 484739, 485666, 503468, 504931, 511792, 512234,
        516775, 519404, 526308, 532620, 545177, 553325, 554935, 555883, 563337,
        564496, 573566, 577854, 587092, 593171, 621760, 636570, 637852, 647627,
        647812, 649661, 651541, 666442, 675162, 679939, 698579, 700138, 706516,
        706593, 708045, 714805, 714939, 729533, 734405, 746956, 760858, 771263,
        776972, 778987, 783130, 783387, 787375, 791405, 793083, 793758, 795938,
        805814, 807725, 808998, 814439, 814618, 820006, 820011, 836392, 836568,
        837463, 838844, 842763, 844573, 847638, 849868, 854570, 856747, 863462,
        868678, 869692, 874307, 877647, 879437, 883750, 890360, 896737, 902942,
        913817, 914029, 921422, 925055, 928144, 937842, 942467, 948938, 979561,
        982293, 993326, 996514]

brray = [714805, 849868, 200803, 555883, -60455, 842763, 320908, 436470,
        127774, 791405, 97527, 120441, 793083, 706593, 526308, 304052, 210701,
        778987, 563337, 368063, -21517, 808998, 373323, 714939, 783387, 519404,
        700138, 424782, 621760, 452614, -86487, -65166, 236555, 837463, 242674,
        381597, 170495, 400580, 675162, -45492, 679939, 593171, 173405, -58419,
        553325, -6198, 249568, 805814, 814618, 475751, 323651, 52278, 219421,
        129670, 289166, 341995, 921422, 65455, 783130, 420950, 481901, 203674,
        787375, 795938, 729533, -85649, 820006, 637852, 351431, 564496, 209767,
        746956, 863462, -93278, 942467, 321524, 698579, 913817, 240651, 156495,
        511792, 165845, 45169, 896737, 928144, 706516, 937842, -64749, 647812,
        -60684, 869692, 35452, 636570, 370491, 196961, 356166, 760858, -88442,
        877647, 439942, 331440, 914029, 554935, 290210, 302467, 320959, 279261,
        485666, 836392, 481600, 771263, 484739, 167939, 311287, 2510, 244616,
        856747, 651541, 307140, 340050, -13471, 666442, 386638, 573566, -44902,
        577854, 194195, -16718, 17273, 854570, 647627, 902942, 868678, -69048,
        890360, 993326, 414448, 807725, 274579, 925055, 474551, 168700, 401519,
        167933, 708045, 587092, -9494, 982293, 649661, 793758, 461368, 503468,
        883750, 196935, 532620, 948938, 836568, 202818, 462970, 393414, 879437,
        347287, 416534, 516775, -57993, 251969, 470863, -14956, 143594, 776972,
        -62996, 545177, 820011, 734405, 414938, 158851, 112431, 838844, 313019,
        434877, 847638, 364101, 233694, 512234, 874307, 230269, 979561, 444354,
        814439, 115512, -42078, 163646, 143245, 364867, 844573, 504931, 383114,
        198544, -56898, 206359]

sorted_brray = [-93278, -88442, -86487, -85649, -69048, -65166, -64749, -62996,
        -60684, -60455, -58419, -57993, -56898, -45492, -44902, -42078, -21517,
        -16718, -14956, -13471, -9494, -6198, 2510, 17273, 35452, 45169, 52278,
        65455, 97527, 112431, 115512, 120441, 127774, 129670, 143245, 143594,
        156495, 158851, 163646, 165845, 167933, 167939, 168700, 170495, 173405,
        194195, 196935, 196961, 198544, 200803, 202818, 203674, 206359, 209767,
        210701, 219421, 230269, 233694, 236555, 240651, 242674, 244616, 249568,
        251969, 274579, 279261, 289166, 290210, 302467, 304052, 307140, 311287,
        313019, 320908, 320959, 321524, 323651, 331440, 340050, 341995, 347287,
        351431, 356166, 364101, 364867, 368063, 370491, 373323, 381597, 383114,
        386638, 393414, 400580, 401519, 414448, 414938, 416534, 420950, 424782,
        434877, 436470, 439942, 444354, 452614, 461368, 462970, 470863, 474551,
        475751, 481600, 481901, 484739, 485666, 503468, 504931, 511792, 512234,
        516775, 519404, 526308, 532620, 545177, 553325, 554935, 555883, 563337,
        564496, 573566, 577854, 587092, 593171, 621760, 636570, 637852, 647627,
        647812, 649661, 651541, 666442, 675162, 679939, 698579, 700138, 706516,
        706593, 708045, 714805, 714939, 729533, 734405, 746956, 760858, 771263,
        776972, 778987, 783130, 783387, 787375, 791405, 793083, 793758, 795938,
        805814, 807725, 808998, 814439, 814618, 820006, 820011, 836392, 836568,
        837463, 838844, 842763, 844573, 847638, 849868, 854570, 856747, 863462,
        868678, 869692, 874307, 877647, 879437, 883750, 890360, 896737, 902942,
        913817, 914029, 921422, 925055, 928144, 937842, 942467, 948938, 979561,
        982293, 993326]
