#!/bin/bash

compress_pdf() {
    if [ $# -ne 1 ]; then
        echo "Usage: compress_pdf input_filename.pdf"
        return 1
    fi

    input_file="$1"
    output_file="${input_file%.pdf}-latest.pdf"

    # Get the size of the input file
    input_size=$(stat -f"%z" "$input_file")

    # Compress the PDF
    qpdf --stream-data=compress --recompress-flate --optimize-images "$input_file" "$output_file"

    # Get the size of the output file
    output_size=$(stat -f"%z" "$output_file")

    echo "Original PDF size: $input_size bytes"
    echo "Compressed PDF size: $output_size bytes"
    echo "Compressed PDF saved as: $output_file"
}
