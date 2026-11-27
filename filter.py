import requests

url = "https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt"
response = requests.get(url)

if response.status_code == 200:
    lines = response.text.splitlines()
    filtered_lines = [line for line in lines if "germany" in line.lower()]

    with open("filtered_vless.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(filtered_lines))
