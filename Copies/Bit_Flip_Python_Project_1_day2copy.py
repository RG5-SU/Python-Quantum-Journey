#Day 1: 19/08/26

print("Hello world!")

bit = 0

print("Original bit:", bit)

bit = bit ^ 1  #XOR operator

print("Bit after error:", bit) #Will add inputs/more variety.


#Day 2: 20/08/26

#Thoughts on bitflip project code from day 1:
# Okay so the code from before was a classical simulation of a bit-flip error
# Classically we use the XOR gate, the quantum version is a Pauli-X gate
# I'll learn bits, binary and XOR for at least the coming week.


#binary
number = 0b1101 #binary in python
print(number)

number_2 = 13
print(bin(number_2)) #converts decimal to binary


#XOR
#XOR means exclusive OR
#The rule is the output is 1 when the 2 input bits are different

print(0 ^ 0)
print(0 ^ 1)
print(1 ^ 0)
print(1 ^ 1)

#XOR with multiple bits:
#Compares each position seperately.

#  1011
#^ 0110
#------
#  1101

first_number = 0b1011
second_number = 0b0110

result = first_number ^ second_number

print(bin(result))

#XOR part 2

decimal_number = 13
binary_number = 0b1101   #0b tells python this number is written in binary

print("13 in binary:", bin(decimal_number))
print("1101 in decimal:", binary_number)

bit_1 = 0
print("Original bit:", bit_1)

bit_1 = bit_1 ^ 1
print("After first flip:", bit_1) #bit_1 used as variable name avoid ambiguity to previous.

bit_1 = bit_1 ^ 1
print("After second flip:", bit_1)

print(bin(0b1010 ^ 0b1100))   #The check it should be this number.

#Ran the code it worked.
#Python's bin() remove unescessary leading zeros.
#However I still want to understand the bitflips properly
#so will look at in on day 3 aswell.
 

























