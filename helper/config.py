########################################
# Generates default configuration file #
########################################

import json

config = {
    "DEFAULT_PATH": "./static/",
    "CLI_OUTPUT_PATH": "./static/"
}

output_file = "../config.json"

with open(output_file, "w") as f:
    json.dump(config, f, indent=4)

print(f"Configuration file '{output_file}' generated successfully.")
