#!/bin/bash

services=("MAP-Tentants-Service" "MAP-Data-Processor-Service" "MAP-Data-Ingestion-Service")
testPath="Tests"

for service in "${services[@]}"
do
    pip3 install -r "$service/requirements.txt"
    testFolder="$service/$testPath"

    if [[ -z "${WORKSPACE_MODE}" ]]; then
        pytest $testFolder
    else
        pytest-3 $testFolder
    fi
done