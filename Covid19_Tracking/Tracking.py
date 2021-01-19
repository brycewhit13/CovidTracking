import DataRetrieval as dr
import sys

# Get state and metric from commandline
if len(sys.argv) == 4:
    state = sys.argv[1]
    metric = sys.argv[2]
    if sys.argv[3].lower() == 'true':
        update_first = True
    else:
        update_first = False
else:
    state = sys.argv[1]
    metric = sys.argv[2]
    update_first = False

# Plot the tracking
dr.ShowCovidTracking(state, metric, update_first)