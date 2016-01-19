import ast, cmath, functools, itertools, jelly, math, sympy

inf = float('inf')
nan = float('nan')

def conv_dyadic_integer(link, larg, rarg):
	try:
		iconv_larg = int(larg)
		try:
			iconv_rarg = int(rarg)
			return link(iconv_larg, iconv_rarg)
		except:
			return iconv_larg
	except:
		try:
			return int(rarg)
		except:
			return 0

def conv_monadic_integer(link, arg):
	try:
		return link(int(arg))
	except:
		return 0

def from_base(digits, base):
	integer = 0
	for digit in digits:
		integer = base * integer + digit
	return integer

def from_exponents(exponents):
	integer = 1
	for index, exponent in enumerate(exponents):
		integer *= sympy.ntheory.generate.prime(index + 1) ** exponent
	return integer

def div(dividend, divisor, floor = False):
	if divisor == 0:
		return nan if dividend == 0 else inf
	if divisor == inf:
		return 0
	if floor or (type(dividend) == int and type(divisor) == int and not dividend % divisor):
		return int(dividend // divisor)
	return dividend / divisor

def eval(string):
	return listify(ast.literal_eval(string))

def identity(argument):
	return argument

def iterable(argument):
	return argument if type(argument) == list else [argument]

def index(haystack, needle):
	for index, item in enumerate(haystack):
		if item == needle:
			return 1 + index
	return 0

def isqrt(number):
	a = number
	b = (a + 1) // 2
	while b < a:
		a = b
		b = (a + number // a) // 2
	return int(a)

def listify(iterable):
	if type(iterable) in (int, float, complex) or (type(iterable) == str and len(iterable) == 1):
		return iterable
	return list(map(listify, iterable))

def ntimes(link, repetitions, args):
	ret, rarg = args
	for _ in range(jelly.variadic_link(repetitions, args)):
		larg = ret
		ret = jelly.variadic_link(link, (larg, rarg))
		rarg = larg
	return ret

def overload(operators, *args):
	for operator in operators:
		try:
			ret = operator(*args)
		except:
			pass
		else:
			return ret

def Pi(number):
	if type(number) == int:
		return inf if number < 0 else math.factorial(number)
	return math.gamma(number + 1)

def rld(runs):
	return list(itertools.chain(*[[u] * v for u, v in runs]))

def stringify(iterable, recurse = True):
	if type(iterable) != list:
		return iterable
	if str in map(type, iterable) and not list in map(type, iterable):
		return ''.join(map(str, iterable))
	iterable = [stringify(item) for item in iterable]
	return stringify(iterable, False) if recurse else iterable

def symmetric_mod(number, half_divisor):
	modulus = number % (2 * half_divisor)
	return modulus - 2 * half_divisor * (modulus > half_divisor)

def try_eval(string):
	try:
		return eval(string)
	except:
		return listify(string)

def to_base(integer, base):
	digits = []
	integer = abs(integer)
	base = abs(base)
	if base == 1:
		return [integer]
	if base == 1:
		return [1] * integer
	while integer:
		digits.append(integer % base)
		integer //= base
	return digits[::-1] or [0]

def to_exponents(integer):
	if integer == 1:
		return []
	pairs = sympy.ntheory.factor_.factorint(integer)
	exponents = []
	for prime in sympy.ntheory.generate.primerange(2, max(pairs.keys()) + 1):
		if prime in pairs.keys():
			exponents.append(pairs[prime])
		else:
			exponents.append(0)
	return exponents