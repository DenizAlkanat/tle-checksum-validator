def verify_checksum(line: str) -> bool:
    """
    Validate checksum of a single TLE line (Line 1 or Line 2)
    according to the NORAD TLE specification.
    """

    line = line.rstrip()

    if len(line) < 2 or not line[-1].isdigit():
        return False

    checksum = 0

    for char in line[:-1]:
        if char.isdigit():
            checksum += int(char)
        elif char == "-":
            checksum += 1

    return (checksum % 10) == int(line[-1])


if __name__ == "__main__":
    l1 = "1 00900U 64063C   26018.58912361  .00000576  00000+0  57894-3 0  9993"
    l2 = "2 00900  90.2179  68.3105 0025762  30.5131 132.7264 13.76421819 50841"

    print("Line1:", verify_checksum(l1))
    print("Line2:", verify_checksum(l2))

    bad_l1 = l1[:-1] + ("0" if l1[-1] != "0" else "1")
    print("Bad1 :", verify_checksum(bad_l1))
