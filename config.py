from decouple import config

KAFKA_BOOTSTRAP_SERVERS = config("KAFKA_BOOTSTRAP_SERVERS")
KAFKA_TOPIC = config("KAFKA_TOPIC")
REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT", cast=int)
REDIS_DB = config("REDIS_DB")
HDFS_BATCH_TOPIC = config("HDFS_BATCH_TOPIC")
CAMPAIGN_KAFKA_TOPIC = config("CAMPAIGN_KAFKA_TOPIC")

# Kafka 137
BOOTSTRAP_SERVERS_137 = config("BOOTSTRAP_SERVERS_137")
KAFKA_137_KERBEROS_SERVICE_NAME = config("KAFKA_137_KERBEROS_SERVICE_NAME")
KEYTAB_137 = config("KEYTAB_137")
PRINCIPAL_137 = config("PRINCIPAL_137")
KAFKA_137_BASED_CONSUMER_CONFIGS = {
    "bootstrap.servers": BOOTSTRAP_SERVERS_137,
    "security.protocol": "SASL_PLAINTEXT",
    "sasl.mechanism": "GSSAPI",
    "sasl.kerberos.service.name": KAFKA_137_KERBEROS_SERVICE_NAME,
    "sasl.kerberos.keytab": KEYTAB_137,
    "sasl.kerberos.principal": PRINCIPAL_137,
    "auto.offset.reset": "earliest",
}

# Kafka logCentral
LOG_CENTRAL_KAFKA_TOPIC = config("LOG_CENTRAL_KAFKA_TOPIC")
LOG_CENTRAL_BOOTSTRAP_SERVERS = config("LOG_CENTRAL_BOOTSTRAP_SERVERS")
LOG_CENTRAL_KAFKA_GROUP_ID = config("LOG_CENTRAL_KAFKA_GROUP_ID")
LOG_CENTRAL_KAFKA_USERNAME = config("LOG_CENTRAL_KAFKA_USERNAME")
LOG_CENTRAL_KAFKA_PASSWORD = config("LOG_CENTRAL_KAFKA_PASSWORD")
LOG_CENTRAL_KAFKA_CONSUMER_CONFIGS = {
    "bootstrap.servers": LOG_CENTRAL_BOOTSTRAP_SERVERS,
    "security.protocol": "SASL_PLAINTEXT",
    "sasl.mechanism": "PLAIN",
    "sasl.username": LOG_CENTRAL_KAFKA_USERNAME,
    "sasl.password": LOG_CENTRAL_KAFKA_PASSWORD,
    "group.id": LOG_CENTRAL_KAFKA_GROUP_ID,
    "auto.offset.reset": "earliest",
}
