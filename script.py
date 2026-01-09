import sys

def get_fasta_lengths(filename):
    try:
        with open(filename, 'r') as file:
            header = None
            sequence_len = 0
            
            for line in file:
                line = line.strip()
                if not line: continue  # Skip empty lines

                if line.startswith(">"):
                    # If we have a previous record, print its details
                    if header:
                        print(f"{header}\t{sequence_len}")
                    
                    # Start a new record
                    header = line[1:] # Remove the '>' character
                    sequence_len = 0
                else:
                    # Accumulate sequence length
                    sequence_len += len(line)

            # Don't forget to print the very last record after the loop finishes
            if header:
                print(f"{header}\t{sequence_len}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a filename was provided via command line
    if len(sys.argv) < 2:
        print("Usage: python fasta_len.py <input_file.fasta>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    get_fasta_lengths(input_file)
