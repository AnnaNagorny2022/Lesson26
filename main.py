from bus import Bus
from manager import find_bus


def main():
    bus1 = Bus("Scania", 23000, 42)
    bus2 = Bus("MAZ", 1200, 34)
    bus3 = Bus("Volvo", 31000, 48)
    bus4 = Bus("PAZ", 11000, 15)
    bus5 = Bus("Mercedes Benz", 123000, 67)

    buses = (bus1, bus2, bus3, bus4, bus5)

    result = find_bus(buses)

    print(result)


if __name__ == "__main__":
    main()
