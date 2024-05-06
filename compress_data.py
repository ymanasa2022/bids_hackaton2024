#!/bin/usr/python

import pandas as pd
import os
import glob

data = {}
for case_file in glob.glob('input_data/*-*/*.tsv'):
    case_id = case_file.split('/')[1]
    case_id = case_id.split('/')[0]

    df = pd.read_csv(filepath, sep='\t')  # Assuming TSV files are tab-separated
    # Filter rows based on a condition (e.g., ignore rows starting with 'N_')
    df_filtered = df[~df['specified_column_name'].str.startswith('N_')]

    data[case_id] = df_filtered['fpkm_uq_unstranded'].values


df_output = pd.DataFrame(data)

output_file = 'compressed_data.tsv'
df_output.to_csv(output_file, sep='\t', index=False)
