import subprocess
import argparse

def strings_and_hex_decode(file_path):
    try:
        # Step 1: Run `strings` on the file and capture the output
        result = subprocess.run(['strings', file_path], stdout=subprocess.PIPE, text=True)
        output = result.stdout

        # Step 2: Process each line of the output
        for line in output.splitlines():
            # Remove whitespace and check if it's a valid hex string
            clean_line = line.strip()
            try:
                # Attempt to decode as hex
                decoded_line = bytes.fromhex(clean_line).decode('utf-8')
                print(f"Original: {clean_line} | Decoded: {decoded_line}")
            except ValueError:
                # Skip lines that are not valid hex
                print(f"Not hex: {clean_line}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Extract strings from a file and decode hex lines.")
    parser.add_argument("file", help="Path to the file to process")
    args = parser.parse_args()

    # Call the function with the provided file path
    strings_and_hex_decode(args.file)
