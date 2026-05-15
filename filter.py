import requests

url = "https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt"
response = requests.get(url)

if response.status_code == 200:
    lines = response.text.splitlines()
    # Теперь ищем только "netherlands"
    filtered_lines = [line for line in lines if "netherlands" in line.lower()]
    
    with open("filtered_vless.txt", "w") as f:
        f.write("\n".join(filtered_lines))
