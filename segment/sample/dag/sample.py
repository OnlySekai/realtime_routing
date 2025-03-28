from lib.state.sample_sink import SampleSink
from segment.sample.filter_odd import filter_odd
from lib.operator.simple import wrap_filter
from contansts.config import KAFKA_BOOTSTRAP_SERVERS

Sink = SampleSink(name="sample_sink", des="", log=True)
Source1 = Sink.fork("fork_sample_1", "", True).bind(wrap_filter(filter_odd))
Source2 = Source1.fork("fork_sample_2", "", True).bind(wrap_filter(filter_odd))
