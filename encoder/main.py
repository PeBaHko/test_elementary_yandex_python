from decoder import Decoder
dec = Decoder()
print('one symbol from A to I - ' + dec.decoding('4'))
print('two symbols from A to I - ' + dec.decoding('36'))
print('three symbols from A to I - ' + dec.decoding('258'))
print('one symbol from J to Z - ' + dec.decoding('23#'))
print('two symbols from J to Z and from A to I - ' + dec.decoding('25#7'))
print('four symbols from A to I - ' + dec.decoding('2468'))
try:
    dec.decoding('0')
except Exception as e:
    print('wrong code of one symbol - ' + e.__str__())
try:
    dec.decoding('20')
except Exception as e:
    print('wrong code of two symbol - ' + e.__str__())
try:
    dec.decoding('2#')
except Exception as e:
    print('wrong code of two symbol - ' + e.__str__())
print('text: "helloworld" - ' + dec.decoding('8512#12#15#23#15#18#12#4'))
