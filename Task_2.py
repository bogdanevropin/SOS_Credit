"""
Making RLE Encoder (27 min)
"""


def encode_message(message):
	"""
	encode function
    :param message:
    """
	encoded_string = ""
	i = 0
	while i <= len(message) - 1:
		count = 1
		ch = message[i]
		j = i
		while j < len(message) - 1:
			# if the character at the current index is the same as the character at the next index.
			# If the characters are the same, the count is incremented to 1
			if message[j] == message[j + 1]:
				count = count + 1
				j = j + 1
			else:
				break
		'''the count and the character is concatenated to the encoded string'''
		encoded_string = encoded_string + ch + str(count)
		i = j + 1
	if len(encoded_string) > len(message):
		return message
	else:
		return encoded_string


if __name__ == '__main__':
	m = input("Input string for RLE encoding: \n")
	print(f"Answer is :{encode_message(m)}")
