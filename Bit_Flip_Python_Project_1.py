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
 

#Day 3: 21/08/26
#input and conditional:

bit_2 = int(input("Enter a bit, 0 or 1: "))

if bit_2 == 0 or bit_2 == 1:     # = assigns a value, == compares two values
    flipped_bit_2 = bit_2 ^ 1

    print("Original bit:", bit_2)
    print("Flipped bit:", flipped_bit_2)
else:
    print("That is not a valid bit.")


#Day 4: 22/08/26
#repeated bit flips

bit_3 = int(input("Enter a starting bit, 0 or 1: "))
number_of_flips = int(input("How many times should it flip? "))

if (bit_3 == 0 or bit_3 == 1) and number_of_flips >= 0:
    original_bit = bit_3

    for flip_number in range(1, number_of_flips + 1): #why "+1" here explained below.
        bit_3 = bit_3 ^ 1
        print("After flip", flip_number, ":" , bit_3)

    print("Original bit:", original_bit)
    print("Final bit:", bit_3)

    if bit_3 == original_bit:
        print("The bit returned to its original value.")
    else:
        print("The bit is different from its original value.")

else:
    print("Invalid input.")

#We do number_of_flips + 1, +1 due to python's range() stops before final number.
#i.e.
for number in range(1, 4):
    print(number)
#
#Outputs only: 1,2,3 (vertically no commas)
#Hence in our code we must do +1 to total number_of_flips to give the full range.


#Day 5: 23/08/26
#bit flip function

def flip_bit(bit_4):
    flipped_bit == bit_4 ^ 1
    return flipped_bit

starting_bit = int(input("Enter a starting bit, 0 or 1: "))
number_of_flips = int(input("How many times should it flip? "))

if (starting_bit == 0 or starting_bit == 1) and number_of_flips >= 0:
    current_bit = starting_bit

    for flip_number in range(1, number_of_flips + 1):
        current_bit = flip_bit(current_bit)
        print("After flip", flip_number, ":", current_bit)

    print("Original bit:", starting_bit)
    print("Final bit:", current_bit)

    if current_bit == starting_bit:
        print("The bit returned to its original value.")
    else:
        print("The bit is different from its original value.")

else:
    print("Invalid input.")

#Day 6: 24/08/26
#three bit repetition

def flip_bit(bit_5):
    return bit ^ 1


original_bit = int(input("Enter a bit to protect, 0 or 1: "))

if original_bit == 0 or original_bit == 1:
    codeword = [original_bit, original_bit, original_bit]

    print("Encoded codeword:", codeword)

    error_position = int(
        input("Which position should flip? Enter 1, 2, 3, or 0 for none: ")
    )

    if error_position >= 0 and error_position <= 3:

        if error_position != 0:
            index = error_position - 1
            codeword[index] = flip_bit(codeword[index])

        print("Received codeword:", codeword)

        number_of_ones = sum(codeword)

        if number_of_ones >= 2:
            decoded_bit = 1
        else:
            decoded_bit = 0

        print("Decoded bit:", decoded_bit)

        if decoded_bit == original_bit:
            print("The original information was recovered.")
        else:
            print("The correction failed.")

    else:
        print("Invalid error position.")

else:
    print("Invalid bit.")


#Debug Day5 and Day 6 tomorrow due to erros, we are getting errors due to 
#names of variables
    





