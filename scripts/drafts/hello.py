"""
Execution script for the hello-world job.

This script acts as the entry point. It resolves file paths, 
loads configurations, and orchestrates the processing utilities.
"""

import os
import argparse
from pathlib import Path

from mypkgs.utils import (
    load_json_config, 
    prepare_output_dir
)
from mypkgs.processor import write_hello


def main() -> None:
    """
    Main execution pipeline for the hello world script.

    Parses command line arguments, loads configurations from the 
    injected environment, prepares the output directory, and executes
    the greeting processor.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    SystemExit
        If required paths are neither provided via CLI nor defined 
        in the environment variables (handled by argparse).
    """
    parser = argparse.ArgumentParser(description="Run the hello world script.")
    
    parser.add_argument(
        '--config-file', 
        type=str,
        default=os.environ.get("CONFIG_PATH"),
        help='Path to config file. Defaults to CONFIG_PATH environment variable.'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default=os.environ.get("OUTPUT_DIR"),
        help='Path to output directory. Defaults to OUTPUT_DIR environment variable.'
    )
    
    args = parser.parse_args()

    # 1. Resolve paths (Strict Failure if missing)
    if not args.config_file:
        parser.error(
            "A configuration path must be provided either via the "
            "'--config-file' argument or the 'CONFIG_PATH' environment variable."
        )
        
    if not args.output_dir:
        parser.error(
            "An output directory must be provided either via the "
            "'--output-dir' argument or the 'OUTPUT_DIR' environment variable."
        )
    
    config_path = Path(args.config_file)
    out_dir_raw = args.output_dir

    # 2. Execute core logic using the utilities
    config = load_json_config(config_path)
    name = config.get("name", "Unknown Person")
    
    out_dir = prepare_output_dir(out_dir_raw)
    final_path = write_hello(name, out_dir)

    print(f"Job completed. Results safely written to {final_path}")


if __name__ == "__main__":
    main()
