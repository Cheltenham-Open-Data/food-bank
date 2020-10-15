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
    address = data['address'].replace("\r\n"," ")
    contact_string = (f"- Email: {data['email']}\n"
                      f"- Tel: {data['phone']}\n"
                      f"- Address: {address}\n"
                      f"- Network: {data['network']}\n"
                      f"- Charity number: [{data['charity']['registration_id']}]({data['charity']['register_url']})")

# processing
if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()
    readme_contents = helper.replace_chunk(readme_contents,"summary_marker",output)
    readme_contents = helper.replace_chunk(readme_contents,"contact_marker",contact_string)
    readme.open("w").write(readme_contents)
