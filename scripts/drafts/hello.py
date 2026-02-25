#!/usr/bin/env python3.13
import os
import json
import sys
import argparse

def main():
    # 1. Initialize the argument parser
    parser = argparse.ArgumentParser(
            description="Run the hello world script.")
    parser.add_argument(
        '--config-file', 
        type=str, 
        required=True, 
        help='Absolute or relative path to the configuration JSON file.'
    )
    
    # 2. Parse the arguments passed from the command line
    args = parser.parse_args()
    config_path = args.config_file

    # 3. Read the dynamic config path
    with open(config_path, 'r') as f:
        config = json.load(f)
    name = config.get("name", "Unknown Person")


    # Persistent Output Location
    output_dir = os.environ.get("OUTPUT_DIR")
    if not output_dir:
        raise ValueError("OUTPUT_DIR environment variable is not set.")
    
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_hello.txt")

    output_content = (f"Hello {name}")

    with open(output_file, 'w') as f:
        f.write(output_content)
    
    print(f"Job completed. Results safely written to {output_file}")

if __name__ == "__main__":
    main()
