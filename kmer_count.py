import sys
import collections

def count_kmers(filename, k):
    # We use a default dictionary for cleaner code (auto-initializes counts to 0)
    kmer_counts = collections.defaultdict(int)
    
    try:
        with open(filename, 'r') as file:
            # We need to buffer the sequence because k-mers can span across 
            # the newlines in a FASTA file.
            sequence_buffer = []
            
            for line in file:
                line = line.strip()
                if not line: continue

                if line.startswith(">"):
                    # Process the sequence we just finished reading
                    if sequence_buffer:
                        full_seq = "".join(sequence_buffer)
                        process_sequence(full_seq, k, kmer_counts)
                        
                    # Reset buffer for the new record
                    sequence_buffer = []
                else:
                    sequence_buffer.append(line)

            # Process the very last sequence in the file
            if sequence_buffer:
                full_seq = "".join(sequence_buffer)
                process_sequence(full_seq, k, kmer_counts)

        # Print the final dictionary
        # Convert to a standard dict for cleaner printing if desired
        print(dict(kmer_counts))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
         print("Error: Please ensure K is an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_sequence(sequence, k, counts_dict):
    """Updates the dictionary with k-mers from a single sequence string."""
    # Ensure the sequence is long enough for at least one k-mer
    if len(sequence) < k:
        return

    # Sliding window to find k-mers
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i : i+k]
        counts_dict[kmer] += 1

if __name__ == "__main__":
    # Check for correct arguments
    if len(sys.argv) < 3:
        print("Usage: python kmer_count.py <input_file.fasta> <k_value>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        k_val = int(sys.argv[2])
        count_kmers(input_file, k_val)
    except ValueError:
        print("Error: The K value must be an integer.")
        sys.exit(1)
