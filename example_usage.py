from client import MMRAccumulator

def main():
    print("=== Testing Merkle Mountain Range Accumulator ===")
    mmr = MMRAccumulator()
    
    blocks = ["genesis", "tx1_block", "tx2_block", "tx3_block", "tx4_block", "tx5_block", "tx6_block"]
    for b in blocks:
        h = mmr.append(b)
        print(f"Appended {b} -> leaf: {h}, peaks: {mmr.peak_count()}")

    bagged_root = mmr.get_bagged_root()
    print(f"Final Bagged MMR Root: {bagged_root}")
    assert len(bagged_root) == 16
    print("=== MMR Verification Complete ===")

if __name__ == "__main__":
    main()
