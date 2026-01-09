import sys

def count_fasta_records(filename):
    count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                # distinct FASTA headers always start with '>'
                if line.startswith(">"):
                    count += 1
        
        print(f"Total number of records: {count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python count_records.py <input_file.fasta>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    count_fasta_records(input_file)
