for batch in `ls -d data/batch*`; do
    batch_name=`basename $batch`
    cp vcf2lineage-job-template.yml vcf2lineage-${batch_name}-job.yml
    python create_job_file.py vcf2lineage-${batch_name}-job.yml $batch
    planemo run f4b02af7e642e75b vcf2lineage-${batch_name}-job.yml --profile planemo-tutorial
    sleep 300
    mv $batch data/completed/
done
