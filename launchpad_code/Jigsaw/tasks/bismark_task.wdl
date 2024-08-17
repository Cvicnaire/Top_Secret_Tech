# bismark task, default parameters
task bismark {
    input {
        File fastq_file1
        File fastq_file2
        String inputDir
        String base = basename(fastq_file1, ".fastq.gz")
        String dockerImage = "quay.io/biocontainers/bismark:0.24.2--hdfd78af_0"
    }

    command {
        /usr/local/bin/bismark \
        --genome ${inputDir} \
        -1 ${fastq_file1} \
        -2 ${fastq_file2} \ 
        bismark2summary
    }

    output {
        File bismark_output = "${base}_bismark.bam"
    }

    runtime {
        docker: dockerImage
        cpu: 10 
    }
}