import datetime, os, requests, shutil
from dotenv import load_dotenv

SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

today = datetime.datetime.today()
day = today.day
year = today.year

if today.month != 12 or today.day > 25:
    year = int(input("Enter year: "))
    if year > today.year:
        raise ValueError(f"Invalid year entered (we haven't reached {year}) yet!")

    day = int(input("Enter day: "))
    if day > 25:
        raise ValueError(f"Invalid day entered (number must be at most 25)!")

new_year = f"{year}"
new_dir = f"Day {day:02}"
full_path = os.path.join(SCRIPT_PATH, new_year, new_dir)

url = f"https://adventofcode.com/{year}/day/{day}/input"


if os.path.isdir(full_path):
    print("Folder already exists, skipping setup...")

else:
    os.makedirs(full_path)

    print(f"Created folder \"{new_dir}\".")

    load_dotenv()

    cookies = dict(session=os.getenv("AOC_SESSION_ID"))
    result = requests.get(url, cookies=cookies)

    input_path = os.path.join(full_path, "input.txt")

    with open(input_path, "w+") as f:
        f.writelines(result.text)
        
    print("Created file \"input.txt\".")
    
    sample_path = os.path.join(full_path, "sample.txt")

    with open(sample_path, "w+") as f:
        f.writelines("Sample goes here")

    print("Created file \"sample.txt\".")

    print("Copying template files...")

    template_path = os.path.join(os.getcwd(), "template.py")
    part1_path = os.path.join(full_path, "part1.py")
    part2_path = os.path.join(full_path, "part2.py")

    shutil.copyfile(template_path, part1_path)
    shutil.copyfile(template_path, part2_path)

    print("Copied files \"part1.py\", \"part2.py\".")
