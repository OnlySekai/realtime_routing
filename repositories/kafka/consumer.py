from lib.state.kafka_sink import KafkaSink
from contansts.config import *
consumer_logCentral = KafkaSink(LOG_CENTRAL_KAFKA_TOPIC,
                                                   {'bootstrap.servers': LOG_CENTRAL_BOOTSTRAP_SERVERS,
                                                    'group.id': LOG_CENTRAL_KAFKA_GROUP_ID,
                                                    'auto.offset.reset': ' '
                                                    }
                                                   )
consumer_hdfs = KafkaSink(HDFS_BATCH_TOPIC,
                                             {'bootstrap.servers': BOOTSTRAP_SERVERS_137,
                                              'security.protocol': 'SASL_PLAINTEXT',
                                              'sasl.mechanism': 'GSSAPI',
                                              'sasl.kerberos.service.name': KAFKA_137_KERBEROS_SERVICE_NAME,
                                              'sasl.kerberos.keytab': KEYTAB_137,
                                              'sasl.kerberos.principal': PRINCIPAL_137,
                                              'auto.offset.reset': 'earliest'
                                              }
                                             )
