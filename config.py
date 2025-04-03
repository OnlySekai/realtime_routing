from decouple import config

FOR_DRAW = config("FOR_DRAW", default="0", cast=bool)
KAFKA_BOOTSTRAP_SERVERS = config("KAFKA_BOOTSTRAP_SERVERS", default=None)
REDIS_HOST = config("REDIS_HOST", default=None)
REDIS_PORT = config("REDIS_PORT", cast=int)
REDIS_DB = config("REDIS_DB", default=None)
HDFS_BATCH_TOPIC = config("HDFS_BATCH_TOPIC", default=None)
CAMPAIGN_KAFKA_TOPIC = config("CAMPAIGN_KAFKA_TOPIC", default=None)

# Kafka 137
BOOTSTRAP_SERVERS_137 = config("BOOTSTRAP_SERVERS_137", default=None)
KAFKA_137_KERBEROS_SERVICE_NAME = config(
    "KAFKA_137_KERBEROS_SERVICE_NAME", default=None
)
KEYTAB_137 = config("KEYTAB_137", default=None)
PRINCIPAL_137 = config("PRINCIPAL_137", default=None)
# KAFKA_137_BASED_CONSUMER_CONFIGS = {
#     "bootstrap.servers": BOOTSTRAP_SERVERS_137,
#     "security.protocol": "SASL_PLAINTEXT",
#     "sasl.mechanism": "GSSAPI",
#     "sasl.kerberos.service.name": KAFKA_137_KERBEROS_SERVICE_NAME,
#     "sasl.kerberos.keytab": KEYTAB_137,
#     "sasl.kerberos.principal": PRINCIPAL_137,
#     "auto.offset.reset": "earliest",
# }
KAFKA_137_BASED_CONSUMER_CONFIGS = {
    "bootstrap.servers": BOOTSTRAP_SERVERS_137,
    "auto.offset.reset": "earliest",
    "group.id": "KAFKA_137_BASED_CONSUMER_CONFIGS",
}

# Kafka logCentral
LOG_CENTRAL_KAFKA_TOPIC = config("LOG_CENTRAL_KAFKA_TOPIC", default=None)
LOG_CENTRAL_BOOTSTRAP_SERVERS = config("LOG_CENTRAL_BOOTSTRAP_SERVERS", default=None)
LOG_CENTRAL_KAFKA_GROUP_ID = config("LOG_CENTRAL_KAFKA_GROUP_ID", default=None)
LOG_CENTRAL_KAFKA_USERNAME = config("LOG_CENTRAL_KAFKA_USERNAME", default=None)
LOG_CENTRAL_KAFKA_PASSWORD = config("LOG_CENTRAL_KAFKA_PASSWORD", default=None)
# LOG_CENTRAL_KAFKA_CONSUMER_CONFIGS = {
#     "bootstrap.servers": LOG_CENTRAL_BOOTSTRAP_SERVERS,
#     "security.protocol": "SASL_PLAINTEXT",
#     "sasl.mechanism": "PLAIN",
#     "sasl.username": LOG_CENTRAL_KAFKA_USERNAME,
#     "sasl.password": LOG_CENTRAL_KAFKA_PASSWORD,
#     "group.id": LOG_CENTRAL_KAFKA_GROUP_ID,
#     "auto.offset.reset": "earliest",
# }
LOG_CENTRAL_KAFKA_CONSUMER_CONFIGS = {
    "bootstrap.servers": LOG_CENTRAL_BOOTSTRAP_SERVERS,
    "group.id": LOG_CENTRAL_KAFKA_GROUP_ID,
    "auto.offset.reset": "earliest",
}
