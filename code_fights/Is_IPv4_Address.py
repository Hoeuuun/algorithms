"""

CF.21

An IP address is a numerical label assigned to each device
(e.g., computer, printer) participating in a computer network that uses the
Internet Protocol for communication. There are two versions of the Internet
protocol, and thus two versions of addresses. One of them is the IPv4 address.

IPv4 addresses are represented in dot-decimal notation, which consists of four
decimal numbers, each ranging from 0 to 255, separated by dots,
e.g., 172.16.254.1.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.
"""

inputString = "1.1.1.1.1"

def isIPv4Address(inputString):
    try:
        separated = map(lambda x: int(x), inputString.split(".",len(inputString)))
    except ValueError:
        return False
    for i in xrange(0, len(separated)):
        if len(separated) != 4:
            return False
        else:
            if separated[i] < 0 or separated[i] > 255:
                #print separated[i]
                return False
    return True

print isIPv4Address(inputString)
