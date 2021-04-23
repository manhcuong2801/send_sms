import json as j

from django.conf import settings as s
from kafka import KafkaConsumer as KC, KafkaProducer as KP


class KafkaConnector:
    _bootstrap_server = s.KAFKA_SERVER
    _topic = "topic_example"
    _group_id = "group_example"

    def get_consumer(
        self,
        topic: str = _topic,
        group_id: str = _group_id,
        is_handle_json: bool = True,
    ):
        if not is_handle_json:
            return KC(
                topic, group_id=group_id, bootstrap_servers=[self._bootstrap_server]
            )
        return KC(
            topic,
            group_id=group_id,
            bootstrap_servers=[self._bootstrap_server],
            value_deserializer=lambda v: j.loads(v),
        )

    def get_producer(self, is_handle_json: bool = True):
        if not is_handle_json:
            return KP(bootstrap_servers=[self._bootstrap_server])
        return KP(
            bootstrap_servers=[self._bootstrap_server],
            value_serializer=lambda v: j.dumps(v).encode("utf-8"),
        )

    def send_message_to_topic(
        self,
        topic: str,
        bytes_msg: bytes = b"",
        json_msg: dict = {},
        is_handle_json: bool = True,
    ):
        if not is_handle_json:
            producer = self.get_producer(is_handle_json=False)
            future = producer.send(topic, bytes_msg)
        else:
            producer = self.get_producer()
            future = producer.send(topic, json_msg)
        return future
