'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports textFormat module from com.irdeto.python.format package.
'''
from com.irdeto.sample.python.format import textFormat

'''
Tests the variations of format_columns* functions.
'''
textFormat.format_columns(range(1, 11))
textFormat.format_columns_2(range(1, 11))
textFormat.format_columns_3(range(1, 11))

'''
Tests the variations of format_pi* functions.
'''
textFormat.format_pi();
textFormat.format_pi_2();
textFormat.format_pi_3();
textFormat.format_pi_4();
