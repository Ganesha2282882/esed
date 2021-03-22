import sys

try:
	if sys.argv[1] == "--help":
		print("esed 1.0, Easy Stream EDitor")
		print("Usage:")
		print("esed Never Always < RickRoll.txt                 \t- replace \"Never\" with \"Always\"")
		print("esed Never Always < RickRoll.txt > RickRoll.txt.1\t- same thing but output to another file")
		print("Flags:")
		print("-v    \t- Version")
		print("--help\t- Help")

	elif sys.argv[1] == "-v":
		print("esed 1.0, Easy Stream EDitor")

	else:
		stream0 = sys.stdin.read()
		stream0 = stream0.replace(sys.argv[1], sys.argv[2])
		print(stream0)

except:
	print(sys.argv[0] + ": error. try \"--help\" and see if you are correct.")

