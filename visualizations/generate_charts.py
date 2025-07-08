import os
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
from typing import List
from models import NormalizedHost


def plot_vendor_distribution(hosts: List[NormalizedHost], save_dir: str = "visualizations/charts"):
    os.makedirs(save_dir, exist_ok=True)
    vendor_counts = Counter([host.vendor for host in hosts])

    plt.figure(figsize=(6, 6))
    plt.pie(vendor_counts.values(), labels=vendor_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title("Vendor Distribution")
    plt.savefig(os.path.join(save_dir, "vendor_distribution.png"))
    plt.close()


def plot_os_distribution(hosts: List[NormalizedHost], save_dir: str = "visualizations/charts"):
    os.makedirs(save_dir, exist_ok=True)
    os_counts = Counter([host.os for host in hosts])

    plt.figure(figsize=(8, 6))
    plt.bar(os_counts.keys(), os_counts.values(), color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title("Operating System Distribution")
    plt.ylabel("Number of Hosts")
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "os_distribution.png"))
    plt.close()


def plot_last_seen_timeline(hosts: List[NormalizedHost], save_dir: str = "visualizations/charts"):
    os.makedirs(save_dir, exist_ok=True)
    dates = [host.last_seen.date() for host in hosts]
    date_counts = Counter(dates)

    sorted_dates = sorted(date_counts.items())
    x, y = zip(*sorted_dates)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='green')
    plt.title("Hosts Seen Over Time")
    plt.xlabel("Date")
    plt.ylabel("Host Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "last_seen_timeline.png"))
    plt.close()


def generate_all_charts(hosts: List[NormalizedHost]):
    plot_vendor_distribution(hosts)
    plot_os_distribution(hosts)
    plot_last_seen_timeline(hosts)
