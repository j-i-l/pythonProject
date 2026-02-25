import argparse
from mypkgs.utils import get_config, set_output_dir
from mypkgs.processor import write_hello


def main():
    parser = argparse.ArgumentParser(description="Run the hello world script.")
    parser.add_argument(
        '--config-file',
        type=str,
        required=True,
        help='Path to the configuration JSON file.'
    )

    args = parser.parse_args()

    # Execution flow using split functions
    config = get_config(args.config_file)
    name = config.get("name", "Unknown Person")

    out_dir = set_output_dir()
    final_path = write_hello(name, out_dir)

    print(f"Job completed. Results safely written to {final_path}")


if __name__ == "__main__":
    main()
