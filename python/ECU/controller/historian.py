import csv
import time


class Historian:

    def __init__(self):

        self.data = []


    def log(self,
            timestamp,
            ideal,
            commanded,
            measured):

        self.data.append({

            "timestamp": timestamp,

            "ideal": ideal,

            "commanded": commanded,

            "measured": measured

        })


    def latest(self, n=500):

        return self.data[-n:]


    def query(self,
              start,
              end,
              interval=0.5):

        results = []

        last = -1e99

        for sample in self.data:

            t = sample["timestamp"]

            if start <= t <= end:

                if t-last >= interval:

                    results.append(sample)

                    last = t

        return results


    def export_csv(self,
                   filename,
                   samples):

        with open(filename,
                  "w",
                  newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                "timestamp",
                "ideal",
                "commanded",
                "measured"
            ])

            for s in samples:

                writer.writerow([
                    s["timestamp"],
                    s["ideal"],
                    s["commanded"],
                    s["measured"]
                ])


    def clear(self):

        self.data.clear()

