import sys
from glob import glob
from pathlib import Path

import yaml

job_file_path = sys.argv[1]
batch_directory = sys.argv[2]

with open(job_file_path) as f:
    job = yaml.load(f, Loader=yaml.CLoader)

vcf_paths = glob(f'{batch_directory}/*.vcf')
elements = [{'class': 'File', 'identifier': Path(vcf_path).stem, 'path': vcf_path} for vcf_path in vcf_paths]
job['Variant calls']['elements'] = elements

with open(job_file_path, 'w') as f:
    yaml.dump(job, f)
