import threading

from segment.campain_push import (
    campain_seg2356_flow,
    campain_seg1_flow,
    campain_seg4_flow,
)

# Define a list of flows
flows = [
    campain_seg2356_flow.run,
    campain_seg1_flow.run,
    campain_seg4_flow.run,
]

# Create and start threads for each flow
threads = [threading.Thread(target=flow) for flow in flows]
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
