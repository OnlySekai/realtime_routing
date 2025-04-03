import threading

from segment.marketing_sub.dag.main import (
 main
)

# Define a list of flows
flows = [
    main.run
]

# Create and start threads for each flow
threads = [threading.Thread(target=flow) for flow in flows]
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
