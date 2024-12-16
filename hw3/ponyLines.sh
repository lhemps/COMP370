#!/bin/bash

pony_name=$1

total_line_count=$(csvtool -c 3 clean_dialog.csv | grep -c -i "$pony_name")
lines=$(wc -l < clean_dialog.csv)
percent_all_lines=$(awk "BEGIN {print $total_line_count*100/$lines}")

echo "$pony_name, $total_line_count, $percent_all_lines %" >> Line_percentages.csv
