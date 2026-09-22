from pathlib import Path
import hashlib


def sha256_file(file_path: str) -> str:
    """Return a file's SHA-256 hash, reading it in chunks."""
    digest = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(1024 * 1024):  # 1 MB chunks
            digest.update(chunk)

    return digest.hexdigest()


def main():
    input_name = input("Enter the plaintext list filename: ").strip().strip('"')

    input_path = Path(input_name)

    if not input_path.is_file():
        print(f"Error: input file not found: {input_path}")
        return

    # Example:
    # files.txt -> files.txt_hashes.txt
    output_path = Path(str(input_path) + "_hashes.txt")

    total = 0
    hashed = 0
    failed = 0

    with input_path.open("r", encoding="utf-8", errors="replace") as infile, \
         output_path.open("w", encoding="utf-8", newline="\n") as outfile:

        for line_number, line in enumerate(infile, start=1):
            file_name = line.strip().strip('"')

            # Ignore blank lines in the input list.
            if not file_name:
                continue

            total += 1

            try:
                file_hash = sha256_file(file_name)

                # Output: original filename followed by its SHA-256 hash.
                outfile.write(f"{file_name} {file_hash}\n")

                hashed += 1
                print(f"[{line_number}] OK: {file_name}")

            except (OSError, PermissionError) as e:
                failed += 1

                # Keep an error record in the output file so every input entry
                # has a corresponding output line.
                outfile.write(f"{file_name} ERROR: {e}\n")

                print(f"[{line_number}] ERROR: {file_name}")
                print(f"    {e}")

    print()
    print(f"Output written to: {output_path}")
    print(f"Files listed: {total}")
    print(f"Successfully hashed: {hashed}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()