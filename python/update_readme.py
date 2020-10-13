
# importing modules
import helper
import random
import pathlib
import json


# setup
root = pathlib.Path(__file__).parent.parent.resolve()
with open(root / "foodbank.json", 'r') as filehandle:
    data = json.load(filehandle)
    needs = data['need']['needs']
    date = data['need']['created']
    output = f"## List of needed items in Cheltenham\n\n"
    output += f"Last updated: {date}\n\n"
    output += f"- {needs}".replace("\n", "\n- ")
    output.rstrip("-")

# processing
if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()
    final_output = helper.replace_chunk(
        readme_contents,
        "summary_marker",
        f"{output}"
    )
    readme.open("w").write(final_output)
