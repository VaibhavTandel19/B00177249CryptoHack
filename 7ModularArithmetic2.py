# #This is cryptohack Modular arithmetic 2 lab
# We used Fermat's Little Theorem which is A^P-1 mod P is always 1 if P is prime number and A is not divisible by P


A = 273246787654
P = 65537


def main() -> None:
    result = pow(A, P - 1, P)
    print(result)


if __name__ == "__main__":
    main()