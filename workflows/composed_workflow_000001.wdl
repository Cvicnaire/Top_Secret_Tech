version 1.0

workflow ComposedWorkflow {
    input {
    ('File', 'fastqFile')? ('File', 'fastqFile')
    ('String', 'outdirPath')? ('String', 'outdirPath')
    ('String', 'dockerImage')? ('String', 'dockerImage')
    }
    # task calls

    call FastQC {
        ('File', 'fastqFile') = ('File', 'fastqFile')
        ('String', 'outdirPath') = ('String', 'outdirPath')
        ('String', 'dockerImage') = ('String', 'dockerImage')
    }
    # task definitions

    task FastQC {
    input {
        File fastqFile
        String outdirPath = "."
        String dockerImage = "quay.io/biocontainers/fastqc:0.12.1--hdfd78af_0"
    }

    command {
        /usr/local/bin/fastqc -o ${outdirPath} ${fastqFile}
    }

    output {
        File fastqc_report = "${outdirPath}/${basename(fastqFile, ".fastq.gz")}_fastqc.html"
    }

    runtime {
        docker: dockerImage
    }
}


    # metadata(work in progress)
    output {
    File? fastqc_report = FastQC.fastqc_report
    }
}
