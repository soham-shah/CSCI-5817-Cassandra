FROM bitnami/minideb-extras:jessie-r24
LABEL maintainer "Bitnami <containers@bitnami.com>"

# Install required system packages and dependencies 
RUN install_packages libbz2-1.0 libc6 libjemalloc1 libncurses5 libreadline6 libsqlite3-0 libssl1.0.0 libtinfo5 zlib1g
RUN bitnami-pkg install python-2.7.14-0 --checksum 2ad513d9d4d4e2c2f98d96448617b5ab3c5dd48dc2e3cb02080ecc7215039ffa
RUN bitnami-pkg install java-1.8.161-0 --checksum eb289afc43eda33d5920294460dc256f6543318506ca5a540bba9073412cfd06
RUN bitnami-pkg unpack cassandra-3.11.2-1 --checksum 9119bf34b3209f8e748fdd2357e381d8897a3416ebe3b8595d5c38d751f5118e

COPY rootfs /

# install ntp
RUN apt-get -qq update
RUN apt-get install -y ntp

# use custom ntpd config file
COPY assets/ntp.conf /etc/ntp.conf

ENV BITNAMI_APP_NAME="cassandra" \ 
	BITNAMI_IMAGE_VERSION="3.11.2-r3" \ 
	CASSANDRA_CLUSTER_NAME="My Cluster" \ 
	CASSANDRA_CQL_PORT_NUMBER="9042" \ 
	CASSANDRA_ENABLE_REMOTE_CONNECTIONS="true" \ 
	CASSANDRA_ENDPOINT_SNITCH="SimpleSnitch" \ 
	CASSANDRA_HOST="" \ 
	CASSANDRA_JMX_PORT_NUMBER="7199" \ 
	CASSANDRA_NUM_TOKENS="256" \ 
	CASSANDRA_PASSWORD="cassandra" \ 
	CASSANDRA_PASSWORD_SEEDER="no" \ 
	CASSANDRA_SEEDS="" \ 
	CASSANDRA_TRANSPORT_PORT_NUMBER="7000" \ 
	CASSANDRA_USER="cassandra" \ 
	PATH="/opt/bitnami/python/bin:/opt/bitnami/java/bin:/opt/bitnami/cassandra/bin:$PATH" 

EXPOSE 9042 7000 
ENTRYPOINT ["/app-entrypoint.sh"]
CMD ["nami","start","--foreground","cassandra"]