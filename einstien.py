def main():
    c = 300_000_000  # 3 * 10^8 m/s
    mass = int(input("Enter mass in kilograms: "))
    energy = mass * c ** 2
    print(energy)

if __name__ == "__main__":
    main()
