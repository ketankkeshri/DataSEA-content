```markdown
# Apache Flink Streaming — Cheatsheet

## [Section 1: Core syntax]

| Thing                | Syntax                                   | Notes                                            |
|---------------------|------------------------------------------|--------------------------------------------------|
| Stream Source       | `streamEnv.addSource(sourceFunction)`   | Use to create a stream from an external source. |
| Data Transformation  | `stream.map(function)`                  | Applies a function to each element of the stream.|
| Windowing           | `stream.window(TumblingEventTimeWindows.of(Time.seconds(10)))` | Groups elements by time intervals.              |
| Sink                | `stream.addSink(sinkFunction)`          | Outputs stream data to a specified sink.        |

## [Section 2: Event Time & Watermarks]

```python
from datetime import datetime
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import Time

env = StreamExecutionEnvironment.get_execution_environment()
source = env.from_collection([(1, datetime(2023, 1, 1, 12, 0, 0))], type_info=Types.TUPLE([Types.INT(), Types.SQL_TIMESTAMP()]))

watermark_strategy = WatermarkStrategy.for_bounded_out_of_orderness(Time.seconds(5))
stream = source.assign_timestamps_and_watermarks(watermark_strategy)
```

## [State Management]

```java
// Using keyed state for storing user count
public class UserCountFunction extends KeyedProcessFunction<String, UserEvent, Integer> {
    private ValueState<Integer> userCount;

    @Override
    public void open(Configuration parameters) {
        ValueStateDescriptor<Integer> descriptor = new ValueStateDescriptor<>("userCount", Integer.class, 0);
        userCount = getRuntimeContext().getState(descriptor);
    }
    
    @Override
    public void processElement(UserEvent event, Context ctx, Collector<Integer> out) {
        int count = userCount.value();
        count++;
        userCount.update(count);
        out.collect(count);
    }
}
```

## [Exactly-once Semantics]

```java
// Enabling exactly-once semantics
env.enableCheckpointing(1000); // Checkpointing interval
env.getCheckpointConfig().setCheckpointingMode(CheckpointingMode.EXACTLY_ONCE);
```

## [Gotchas]

- ⚠️ Event time processing can lead to late events being dropped if not handled with care.
- ⚠️ Ensure state is properly managed to avoid memory leaks in long-running applications.

## [Mental model]

- **Event Time vs Processing Time**: Think of event time as when the event occurred vs processing time as when it was processed.
- **Watermarks**: Watermarks help manage the event time and define when to trigger computations based on late data.
- **State Management**: State is scoped to keys; understand how to use keyed state for scalable applications.
```