# Instructions

## Installation

1.  Install Graphviz:
    ```bash
    sudo apt-get update
    sudo apt-get install graphviz libgraphviz-dev
    ```
2.  Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Draw DAG:** Create a Directed Acyclic Graph (DAG).
2.  **Generate Operator Template:** Use AI Cline to generate a template file for operators.
3.  **Import Operators:** Use AI Cline to process and import operators in the DAGs.
4.  **Code Operator Logic:** Implement the logic for each operator.

## Modules

### `lib/utils.py`
This module provides utility functions for drawing DAG images and creating join points in a state machine.

### `lib/operator/simple.py`
This module provides simple operator data.

### `lib/state/state.py`
This module defines the base `State` class, which represents a state in the state machine. It provides methods for binding handlers, emitting data, and forking new states.

### `lib/state/kafka_sink.py`
This module defines the `KafkaSink` class, which is a subclass of `State`. It consumes messages from a Kafka topic and emits them to its listeners.

### `lib/state/sample_sink.py`
This module defines the `SampleSink` class, which is a subclass of `State`. It generates random integers and emits them to its listeners.
