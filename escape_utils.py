
def adjusted_time(raw_time, hints_used, penalty_per_hint=3):
    return raw_time + (hints_used * penalty_per_hint)


def classify_outcome(time, room_limit):
    if time <= 0.70 * room_limit:
        return "FAST ESCAPE"
    elif time <= room_limit:
        return "ESCAPED"
    else:
        return "TIME EXCEEDED"


def session_summary(team, room, time, outcome):
    return f"Team: {team} | Room: {room} | Time: {time} | Outcome: {outcome}"



def summarize_sessions(sessions):
    counts = {
        "FAST ESCAPE": 0,
        "ESCAPED": 0,
        "TIME EXCEEDED": 0
    }

    for session in sessions:
        counts[session["outcome"]] += 1

    best_team = min(sessions, key=lambda x: x["adjusted_time"])["team"] if sessions else "None"

    return counts, best_team

def total_hints(*hint_counts):
    return sum(hint_counts)

# Q5 - Save session records to a text file
def save_session(session):
    record = (
        f"{session['id']}|{session['team']}|{session['room']}|"
        f"{session['players']}|{session['raw_time']}|{session['hints']}|"
        f"{session['adjusted_time']}|{session['outcome']}\n"
    )

    with open("escape_sessions.txt", "a") as file:
        file.write(record)


# Read saved session records
def read_sessions():
    try:
        with open("escape_sessions.txt", "r") as file:
            print("\n===== SAVED SESSION RECORDS =====")

            for line in file:
                fields = line.strip().split("|")

                if len(fields) != 8:
                    print("Error: Malformed record detected.")
                    continue

                try:
                    int(fields[0])
                    int(fields[3])
                    float(fields[4])
                    int(fields[5])
                    float(fields[6])
                except ValueError:
                    print("Error: Invalid data in record.")
                    continue

                print(
                    "ID:", fields[0],
                    "| Team:", fields[1],
                    "| Room:", fields[2],
                    "| Adjusted Time:", fields[6],
                    "| Outcome:", fields[7]
                )

    except FileNotFoundError:
        print("Error: Session file not found.")
