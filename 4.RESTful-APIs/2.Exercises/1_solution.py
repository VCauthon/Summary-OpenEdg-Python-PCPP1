import sys
from typing import Optional
import socket


def HTTP_message(http_type: str, direction: str):
    if http_type.lower() == "get":
        return b"GET / HTTP/1.1\r\nHost: " + bytes(direction, "utf8") + b"\r\nConnection: close\r\n\r\n"
    elif http_type.lower() == "head":
        return b"HEAD / HTTP/1.1\r\nHost: " + bytes(direction, "utf8") + b"\r\nConnection: close\r\n\r\n"


def fake_cli(*args):

    # Add each argument into the sys argv
    [sys.argv.append(str(a)) for a in args]

    # Raise an error if there are missing variables
    if len(sys.argv) not in [2, 3]:
        error_raiser(1)

    ip: str = sys.argv[1]
    port: int = parse_port(sys.argv[2] if len(sys.argv) > 2 else None)

    try:
        obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        obj_socket.connect((ip, port))

        obj_socket.send(HTTP_message("head", ip))
        print(obj_socket.recv(10000))

        obj_socket.shutdown(socket.SHUT_RDWR)
        obj_socket.close()

    except socket.timeout:
        error_raiser(3)
    except socket.gaierror:
        error_raiser(4)


def error_raiser(error_code: int):
    if error_code in [1, 2, 3, 4]:
        if error_code == 1:
            print("Improper number of arguments: at least one is required and not more than two are allowed:")
            print("- http server's address (required)")
            print("- port number (defaults to 80 if not specified)")
        elif error_code == 2:
            print("Port number is invalid - exiting.")
        elif error_code == 3:
            print("There has been detected a timeout on the request made")
        elif error_code == 4:
            print("There has been an unhandled error during the request")
        sys.exit(error_code)


def parse_port(port: str) -> Optional[int]:

    # Parsing the received value into an int
    if isinstance(port, str):
        try:
            port = int(port)

            # Check that the port number is valid
            if port < 1 or 65535 < port:
                error_raiser(2)

            return port

        except ValueError:
            error_raiser(2)

    # If there are no parsing return the default HTTP port
    else :
        return 80


# CLI simulator
if __name__ == "__main__":
    fake_cli("www.testingmcafeesites.com")
