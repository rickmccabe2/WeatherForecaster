from datetime import datetime

def write_to_file(text: str) -> str:
    """Writes data to a new file and returns filepath"""
    filepath = f"src/output/{datetime.today().strftime('%Y%m%d%H%M%S')}.txt"
    file = open(file=filepath, mode="a", encoding="utf-8")
   
    # write
    file.write(text)

    file.close

    return filepath