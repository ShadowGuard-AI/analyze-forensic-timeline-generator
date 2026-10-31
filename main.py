import argparse
import logging
import pandas as pd
import os
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define timestamp formats to try
TIMESTAMP_FORMATS = [
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M:%S.%f",
    "%m/%d/%Y %H:%M:%S",
    "%m/%d/%Y %H:%M:%S.%f",
    "%Y/%m/%d %H:%M:%S",
    "%Y/%m/%d %H:%M:%S.%f",
    "%a %b %d %H:%M:%S %Y", # Syslog format
    "%a %b %d %H:%M:%S.%f %Y"  # Extended Syslog format
]

def setup_argparse():
    """
    Sets up the argument parser for the command line interface.
    Returns:
        argparse.ArgumentParser: The argument parser object.
    """
    parser = argparse.ArgumentParser(description="Generates a timeline of system events from log files.")
    parser.add_argument("log_files", nargs="+", help="Path(s) to the log file(s).")
    parser.add_argument("-o", "--output", default="timeline.csv", help="Output CSV file (default: timeline.csv).")
    parser.add_argument("-tsf", "--timestamp_format",  action='append', help="Timestamp format(s) to try (e.g., '%%Y-%%m-%%d %%H:%%M:%%S').  Can specify multiple formats.") # Allow multiple timestamp formats to be specified
    # There is no --priority option. An earlier version accepted one and
    # then never used it, because these log lines carry no priority field
    # to filter on, and guessing a level from words in the message would
    # drop lines silently. Keyword filtering (-k) is the honest filter.
    parser.add_argument("-k", "--keywords", nargs="+", help="Keywords to filter for in log entries.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output for debugging.")
    parser.add_argument("--no-header", action="store_true", help="Omit the CSV header in the output file.") # Option to disable the header for easier processing downstream

    return parser


def parse_log_entry(log_entry, timestamp_formats):
    """
    Parses a single log entry and extracts the timestamp and event description.
    Args:
        log_entry (str): The log entry string.
        timestamp_formats (list): List of timestamp formats to attempt.

    Returns:
        tuple: A tuple containing the datetime object and the event description, or (None, None) if parsing fails.
    """
    for timestamp_format in timestamp_formats:
        # The candidate width has to come from the format being tried.
        # Taking only the first word can never match a format that itself
        # contains spaces, which is most of the default list, so those
        # formats were dead code before this counted the format's words.
        word_count = timestamp_format.count(" ") + 1
        words = log_entry.split(" ")
        if len(words) < word_count:
            continue
        timestamp_str = " ".join(words[:word_count])
        try:
            dt = datetime.strptime(timestamp_str, timestamp_format)
        except ValueError:
            continue # Try the next format
        description = " ".join(words[word_count:]).strip()
        return dt, description


    return None, log_entry  # If no format matches, return None and the raw log entry


def process_log_file(log_file_path, timestamp_formats, keywords=None):
    """
    Processes a single log file and extracts relevant events.
    Args:
        log_file_path (str): The path to the log file.
        timestamp_formats (list): List of timestamp formats to attempt.
        keywords (list): List of keywords to filter for.

    Returns:
        tuple: A pair (events, read_failed), where events is a list of
        dictionaries representing events, and read_failed is True when
        the named file could not be read.
    """
    events = []
    try:
        with open(log_file_path, "r", encoding="utf-8", errors='ignore') as f:  # Handle potential encoding issues
            for line in f:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue

                dt, description = parse_log_entry(line, timestamp_formats)

                if dt:
                    if keywords is None or any(keyword.lower() in description.lower() for keyword in keywords): #Keyword check and case-insensitive compare
                        events.append({"timestamp": dt, "description": description, "source": log_file_path})

                else:
                    logging.warning(f"Could not parse timestamp in line: {line} from {log_file_path}")

    except FileNotFoundError:
        logging.error(f"Log file not found: {log_file_path}")
        return events, True
    except Exception as e:
        logging.error(f"Error processing log file {log_file_path}: {e}")
        return events, True
    return events, False


def main():
    """
    Main function to parse arguments, process log files, and generate the timeline.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Validate log file paths
    for log_file in args.log_files:
        if not os.path.isfile(log_file):
            logging.error(f"Invalid log file path: {log_file}")
            sys.exit(1)

    # Validate timestamp formats
    if args.timestamp_format:
        timestamp_formats = args.timestamp_format
    else:
        timestamp_formats = TIMESTAMP_FORMATS # Fallback to the default list.

    all_events = []
    failed_files = []
    for log_file in args.log_files:
        events, read_failed = process_log_file(log_file, timestamp_formats, args.keywords)
        if read_failed:
            failed_files.append(log_file)
        all_events.extend(events)

    # Convert to Pandas DataFrame for easier sorting and output
    df = pd.DataFrame(all_events)

    if not df.empty:
        df = df.sort_values(by="timestamp")
        df = df[["timestamp", "source", "description"]]  # Reorder columns
        try:
            df.to_csv(args.output, index=False, header=not args.no_header)
        except Exception as e:
            logging.error(f"Error writing to CSV file: {e}")
            sys.exit(1)
        if failed_files:
            logging.error(f"Timeline written to {args.output}, but {len(failed_files)} log file(s) could not be read: {', '.join(failed_files)}")
            sys.exit(1)
        logging.info(f"Timeline generated successfully and saved to: {args.output}")

    else:
        if failed_files:
            logging.error(f"No timeline generated: {len(failed_files)} log file(s) could not be read: {', '.join(failed_files)}")
            sys.exit(1)
        logging.warning("No events found to generate timeline.")


if __name__ == "__main__":
    main()