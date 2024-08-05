version 1.0

workflow ComposedWorkflow {
    input {
    ${workflow_inputs}
    }
    # task calls

    ${task_calls}
    # task definitions

    ${task_definitions}


    # metadata(work in progress)
    output {
    ${workflow_outputs}
    }
}

