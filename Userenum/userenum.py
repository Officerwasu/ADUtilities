#!/usr/bin/env python3

# Author : PaiN05 , Uday, Officerwasu
import argparse

def generate_variations(first, last, minimal=False):
    first = first.lower()
    last = last.lower()
    
    if minimal:
        return list(set([
            f"{first}.{last}",
            f"{first[0]}.{last}"
        ]))

    return list(set([
        f"{first}.{last}",
        f"{first}{last}",
        f"{first[0]}{last}",
        f"{first}{last[0]}",
        f"{first}_{last}",
        f"{first}",
        f"{last}",
        f"{first[0]}.{last}",
        f"{first}.{last[0]}",
        f"{first[0]}{last[0]}",
        f"{last}{first[0]}"
    ]))

def parse_name(line):
    line = line.strip()
    if not line:
        return None

    
    if "." in line and " " not in line:
        parts = line.split(".")
    else:
        parts = line.split()

    if len(parts) == 2:
        return parts[0], parts[1]

    return None

def main():
    parser = argparse.ArgumentParser(description="Generate username variations.")
    parser.add_argument("-i", "--input", required=True, help="Input file with names")
    parser.add_argument("-o", "--output", default="users.txt", help="Output file for username variations")
    parser.add_argument("-m", "--minimal", action="store_true", help="Generate minimal variations (first.last and f.last only)")

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    usernames = set()

    try:
        with open(input_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[!] File '{input_file}' not found.")
        return

    for line in lines:
        parsed = parse_name(line)
        if parsed:
            first, last = parsed
            variations = generate_variations(first, last, minimal=args.minimal)
            usernames.update(variations)
        else:
            print(f"[!] Skipping invalid entry: {line.strip()}")

    with open(output_file, "w") as f:
        for name in sorted(usernames):
            f.write(name + "\n")

    print(f"[+] Wrote {len(usernames)} username variations to {output_file}")

if __name__ == "__main__":
    main()
