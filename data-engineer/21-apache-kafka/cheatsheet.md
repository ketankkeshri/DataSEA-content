```markdown
# Apache Kafka — Cheatsheet

## [Section 1: Core Concepts]

| Thing               | Syntax                                      | Notes                                                   |
|---------------------|---------------------------------------------|---------------------------------------------------------|
| Topic               | `my_topic`                                  | Logical channel for messages.                           |
| Partition           | `my_topic-0`, `my_topic-1`                 | Each topic can have multiple partitions for scalability.|
| Producer            | `KafkaProducer<String, String>`             | Sends records to a topic.                              |
| Consumer            | `KafkaConsumer<String, String>`             | Reads records from a topic.                            |
| Consumer Group      | `group.id=my-group`                         | Multiple consumers can share the load of reading.      |
| Kafka Streams       | `KStream<String, String> stream`            | For processing streams of data.                        |
| Schema              | `SchemaRegistryClient`                      | Manages Avro schemas for serialization.                |

## [Common Operations]

```java
// Producer Example
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

KafkaProducer<String, String> producer = new KafkaProducer<>(props);
producer.send(new ProducerRecord<>("my_topic", "key", "value"));
producer.close();

// Consumer Example
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "my-group");
props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
consumer.subscribe(Collections.singletonList("my_topic"));
while (true) {
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
    for (ConsumerRecord<String, String> record : records) {
        System.out.printf("offset = %d, key = %s, value = %s%n", record.offset(), record.key(), record.value());
    }
}
```

## [Gotchas]

- ⚠️ Ensure the number of partitions is set according to the expected load; too few can lead to bottlenecks.
- ⚠️ Be careful with consumer group IDs; using the same ID means consumers share messages, leading to load balancing.
- ⚠️ Message ordering is guaranteed within a partition but not across partitions.

## [Mental model]

- **Producers** send messages to **Topics**.
- Each **Topic** is divided into **Partitions** for parallel processing.
- **Consumers** read messages from **Topics** and can be part of **Consumer Groups** for distributed processing.
```