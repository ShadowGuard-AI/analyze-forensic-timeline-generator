![Farmyard before a storm with no inscription anywhere: open sample case with rods on the cart tailboard in front, barn with a blackened gable and farmhouse with its older rod behind, still wash on a line, and a large sky with one distant sheet of rain](intro-banner.png)

# analyze-forensic-timeline-generator

![Farmyard in copper storm light with the salesman's cart and open sample case at the centre, an assembled rod on trestles, and the project name stencilled inside the case lid](banner.png)

![Farmyard in three planes: clouds drift and darken, the barn vane turns in small steps and a barometer needle trembles, and near the open case a brightening travels along the rod tips in sequence like an eye reading entries in order](scene.svg)


# analyze-forensic-timeline-generator
Generates a timeline of system events from log files to reconstruct attack sequences. Supports different timestamp formats. - Focused on Data analysis and reporting

## Install
`git clone https://github.com/ShadowGuardAI/analyze-forensic-timeline-generator`

## Usage
`./analyze-forensic-timeline-generator [params]`

## Parameters
- `-o`: No description provided
- `-tsf`: No description provided
- `-k`: Keywords to filter for in log entries.
- `-v`: Enable verbose output for debugging.
- `--no-header`: Omit the CSV header in the output file.

Exit status: the tool exits 1 if the output CSV cannot be written, or if any named log file could not be read. Exit 0 means the timeline was written and every named log file was read.

Note: an earlier `-p` / `--priority` option was removed in 2026. It accepted a minimum priority but never filtered anything, because the log lines this tool parses carry no priority field. Use `-k` to filter by keyword instead.

## License
Copyright (c) ShadowGuardAI

> Storm note: -o and -tsf are both listed with no description provided, and this page does not guess at either. A second storm note belongs to the retired model: the removed -p and --priority option never filtered anything, because the log lines this tool parses carry no priority field, and -k is the filter to use in its place.
