import json
import sys
import re
import pandas as pd
import csv
from datetime import datetime


class SpotifyDataAnalyzer:
    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self.data = self._read_csv_data()


    def _read_csv_data(self):
        data = []
        with open(self.csv_filename, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data


    def _convert_ms_to_minutes(self, ms):
        return ms / (1000 * 60)


    def get_listening_period(self):
        start_date = None
        end_date = None
        for row in self.data:
            end_time = datetime.strptime(row["endTime"], "%Y-%m-%d %H:%M")
            if start_date is None or end_time < start_date:
                start_date = end_time
            if end_date is None or end_time > end_date:
                end_date = end_time
        duration = end_date - start_date
        return (
            f" Start Date: {start_date.strftime('%Y-%m-%d')}\n"
            f" End Date:   {end_date.strftime('%Y-%m-%d')}\n"
            f" Duration:   {duration.days} days and {duration.seconds//3600} hours\n"
        )


    def get_total_listening_time(self):
        total_minutes = 0
        for row in self.data:
            minutes_played = self._convert_ms_to_minutes(int(row["msPlayed"]))
            total_minutes += minutes_played
        total_hours = total_minutes / 60
        total_days = total_minutes / (60 * 24)
        return (
            f" Total Minutes: {int(total_minutes)}\n"
            f" Total Hours:   {int(total_hours)}\n"
            f" Total Days:    {int(total_days)}\n"
        )


    def get_top_performers(self, n=5):
        performer_listening = {}
        for row in self.data:
            performer = row["artistName"]
            minutes_played = self._convert_ms_to_minutes(int(row["msPlayed"]))
            if performer in performer_listening:
                performer_listening[performer] += minutes_played
            else:
                performer_listening[performer] = minutes_played
        top_performers = sorted(
            performer_listening, key=performer_listening.get, reverse=True
        )[:n]
        result = ""
        for i, performer in enumerate(top_performers, start=1):
            result += f" {i}. {performer}\n"
        return result


    def get_top_songs(self, n=5):
        song_listening = {}
        for row in self.data:
            song = row["trackName"]
            minutes_played = self._convert_ms_to_minutes(int(row["msPlayed"]))
            if song in song_listening:
                song_listening[song] += minutes_played
            else:
                song_listening[song] = minutes_played
        top_songs = sorted(song_listening, key=song_listening.get, reverse=True)[:n]
        result = ""
        for i, song in enumerate(top_songs, start=1):
            result += f" {i}. {song}\n"
        return result


    def get_top_days(self, n=5):
        daily_listening = {}
        for row in self.data:
            end_time = datetime.strptime(row["endTime"], "%Y-%m-%d %H:%M")
            date = end_time.date()
            minutes_played = self._convert_ms_to_minutes(int(row["msPlayed"]))
            if date in daily_listening:
                daily_listening[date] += minutes_played
            else:
                daily_listening[date] = minutes_played
        top_days = sorted(daily_listening, key=daily_listening.get, reverse=True)[:n]
        result = ""
        for i, day in enumerate(top_days, start=1):
            result += f" {i}. {day.strftime('%Y-%m-%d')}\n"
        return result


class color:
    BLUE = "\033[94m"
    BOLD = "\033[1m"
    END = "\033[0m"


def main():
    check_command_line()
    print(f"Hello, {sys.argv[1]}!")
    print(
        "This attempt of a program provides some data analysis of your Spotify streaming histroy."
    )
    print("You can request this data from Spotify free of charge.")
    print(
        "Please, collaborate and provide us the JSON files that contain your streaming history."
    )
    print(
        "The files must be of your_file.json format, otherwise they won't be accepted."
    )
    print("When you're finished, please, input 'done' and press enter.")
    merge_json_files(collect_input())
    json_to_csv()
    get_data()


def get_data():
    analyzer = SpotifyDataAnalyzer("data.csv")

    print(color.BOLD + color.BLUE + "Listening Period:" + color.END)
    print(analyzer.get_listening_period())

    print(color.BOLD + color.BLUE + "Total Listening Time:" + color.END)
    print(analyzer.get_total_listening_time())

    print(color.BOLD + color.BLUE + "Top Performers:" + color.END)
    print(analyzer.get_top_performers())

    print(color.BOLD + color.BLUE + "Top Songs:" + color.END)
    print(analyzer.get_top_songs())

    print(color.BOLD + color.BLUE + "Top Streaming Days:" + color.END)
    print(analyzer.get_top_days())


def check_command_line():
    if len(sys.argv) != 2:
        sys.exit("usage: project.py your_name")


def collect_input():
    files = []
    print("")
    while True:
        file = input("File name: ")
        if re.search(r"^[a-zA-z0-9]*\.json$", file):
            files.append(file)
        elif file == "done":
            print("")
            break
        else:
            print("Incorrect input. Try again.")
    return files


def merge_json_files(files):
    result = list()
    for f1 in files:
        with open(f1, "r") as infile:
            result.extend(json.load(infile))
    with open("data.json", "w") as output_file:
        json.dump(result, output_file, indent=6)


def json_to_csv():
    df = pd.read_json(r"data.json")
    df.to_csv(r"data.csv", index=None)


if __name__ == "__main__":
    main()
