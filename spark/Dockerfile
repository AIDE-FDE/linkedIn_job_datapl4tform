FROM bitnami/spark:3.4.3

USER root

RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

RUN cd /opt/bitnami/spark/jars && \
    curl -sLO https://repo1.maven.org/maven2/software/amazon/awssdk/s3/2.18.41/s3-2.18.41.jar && \
    curl -sLO https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.367/aws-java-sdk-1.12.367.jar && \
    curl -sLO https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.2.0/delta-core_2.12-2.2.0.jar && \
    curl -sLO https://repo1.maven.org/maven2/io/delta/delta-storage/2.2.0/delta-storage-2.2.0.jar

USER 1001
