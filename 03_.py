def reverse_number(n: int) -> int:
	"""Return the integer obtained by reversing the digits of n, preserving sign."""
	sign = -1 if n < 0 else 1
	rev = int(str(abs(n))[::-1])
	return sign * rev

if __name__ == "__main__":
	# Example usage
	examples = [234, -1200, 0]
	for ex in examples:
		print(ex, "->", reverse_number(ex))