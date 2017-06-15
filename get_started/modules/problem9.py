#Write a regular expression to validate a phone number.
import sys
def phonRegx():
	print re.compile(r'^(\d{3})-(\d{3})-(\d{4})$',sys.argv[1])

phonRegx()  

