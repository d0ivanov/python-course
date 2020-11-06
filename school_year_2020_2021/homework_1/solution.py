 def filter_logs(logs, key, value):
    return [log for log in logs if key in log and log[key] == value]


def top(logs, key, count):
    values = [log[key] for log in logs if key in log]
    counts = [(value, values.count(value)) for value in set(values)]

    return dict(sorted(counts, key=lambda x: x[1], reverse=True)[:count])


def complex_filter(logs, filter_params):
    filters = set(filter_params.items())
    return [log for log in logs if filters < log.items()]

