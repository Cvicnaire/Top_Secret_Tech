version 1.0

workflow ComposedWorkflow {
    input {
    File fastqFile
    String? outdirPath
    String? dockerImage
    }

    # Task calls
    call FastQC {
        input:
            fastqFile = fastqFile,
            outdirPath = outdirPath,
            dockerImage = dockerImage,
    }

    output {
    File? fastqc_report = FastQC.fastqc_report
    }
}

# Task Definitions
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

# Metadata (To be added as needed)
