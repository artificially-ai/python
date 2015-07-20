'''
Created on Sep 2, 2010

@author: Wilder Rodrigues (wilder.rodrigues@ekholabs.nl)
'''

'''
Imports functions1st module from com.irdeto.python.module package.
'''
from com.irdeto.sample.python.module import functions1st

'''
Testing ask_gender function, which will read the user input via the console. THis call uses the
required parameters for that function. Below there is another call that informs an optional parameter.
'''
result = functions1st.ask_gender('What is your gender? ', 'Robert Poulsen')
print result

'''
Now testing the same functions, but informing one of the optional fields: number of retries.
'''
result = functions1st.ask_gender('And you gender is...? ', 'Helen', retries = 3)
print result

'''
Testing print_address function, which has as parameters arguments and keywords. Refer to functions1st.py
module imported above.
'''
functions1st.print_address('Sir', 'Robert', 'Poulsen', street = 'Planetenweg', number = 49, postcode = '2132HM', city = 'Hoofddorp', country = 'Netherlands')
