'''
currency.py
__name__: wangchongbin
__pkuid__: 1800011716
__email__: 1800011716@pku.edu.cn
'''
from urllib.request import urlopen


def get_inf(currency_from, currency_to, amount_from):
	'''function for information getting
	
	get the origin information from the website 
	turn the string into a dictionary which is better for us to find what we want
	'''
	url = ('http://cs1110.cs.cornell.edu/2016fa/a1server.php?' + 'from=' 
			+ currency_from + '&to=' + currency_to + '&amt=' + amount_from)
	doc = urlopen(url)
	docstr = doc.read()
	doc.close()
	jstr = docstr.decode('ascii')
    # change docstr into a string: jstr
	true = True
	false = False 
	dict_jstr = eval(jstr)
	return dict_jstr
	
	
def exchange(currency_from, currency_to, amount_from, test = False):
	'''function for currency exchange

	This module provides several string parsing functions to implement a 
	simple currency exchange routine using an online currency service. 
	The primary function in this module is exchange.'''
	dict_jstr = get_inf(currency_from, currency_to, amount_from)
	list_number = ['.' ,'1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	str_to = dict_jstr['to']
	cnt = ''
	for i in str_to:
		if i in list_number:
			cnt += i
	if test == False:
		return float(cnt)
	else:
	#we only change 'test' in function test_exchange
	#we need it return other value that can tell us if exchange() is working well
		return dict_jstr['success']
	
	
def test_exchange():
	"""Unit test for exchange
	When run this test_exchange() function, this module invokes several procedures that 
	test the exchange() functions ."""
	assert exchange('USD', 'EUR', '2.5',True) == True
	assert exchange('USD', 'EUR', '2.5') == 2.1589225
	assert exchange('USD', 'CNY', '2.5',True) == True
	assert exchange('USD', 'CNY', '2.5') == 17.13025
	assert exchange('USD', 'JPY', '2.5',True) == True
	assert exchange('USD', 'JPY', '2.5') == 278.4975
	assert exchange('USD', 'GBP', '2.5',True) == True
	assert exchange('USD', 'GBP', '2.5') == 1.9449825
	print('function exchange() passed all tests!')

def main():
	test_exchange()
	# test you function before exchange
	currency_from = input('please input a currency from ')
	currency_to = input('please input a currency to ')
	amount_from = input('please input the amount you want to exchange ')
	dict_jstr = get_inf(currency_from, currency_to, amount_from)
	if dict_jstr['success'] == True:
		amount_to = exchange(currency_from, currency_to, amount_from)
		print ('the money you want is ' + str(amount_to))
	else:
	# if exchanging failed ,we can know the reason
		print(dict_jstr['error'])


if __name__ =="__main__":
	main()

