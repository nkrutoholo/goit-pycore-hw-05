import sys


def parse_log_line(line: str) -> dict[str, str]:
    parts: list[str] = line.strip().split(" ", 3)
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3] if len(parts) > 3 else "",
    }


def load_logs(file_path: str) -> list[dict[str, str]]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [parse_log_line(line) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)


def filter_logs_by_level(logs: list[dict[str, str]], level: str) -> list[dict[str, str]]:
    return list(filter(lambda log: log["level"] == level, logs))


def count_logs_by_level(logs: list[dict[str, str]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for log in logs:
        level: str = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: dict[str, int]):
    print(f"{'Рівень логування':<17}| {'Кількість'}")
    print(f"{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python task_3.py /path/to/logfile.log [level]")
        sys.exit(1)

    logs: list[dict[str, str]] = load_logs(sys.argv[1])
    counts: dict[str, int] = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level: str = sys.argv[2].upper()
        filtered: list[dict[str, str]] = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
