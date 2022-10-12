def save_to_file(file_name, file):
    file = open(f"{file_name}.csv", "w")
    file.write("Company, Position, region, link\n")
    for job in jobs:
        try:
            file.write(
                f"{job['Company']}, {job['Position']}, {job['region']}, {job['link']}\n")
        except(UnicodeEncodeError):
            pass
    file.close()
    return
