#!/bin/bash

services=("BankingComponent" "UserComponent" "DriverComponent" "OrderComponent" "ProductComponent")

for service in "${services[@]}"
do
    SERVICE=$(echo "$service" | tr '[:upper:]' '[:lower:]')
    VERSION=$(git log -1 --pretty=%h)
    REPO="ghcr.io/lassebirk96/$SERVICE:"
    VERSIONTAG="$REPO$VERSION"
    LATESTTAG="${REPO}latest"

    docker build -t $VERSIONTAG -t $LATESTTAG . --build-arg COMPONENT_PATH=$service
    docker push $VERSIONTAG
    docker push $LATESTTAG
done