import os
from flask import Flask, render_template, request
import requests
from random import randint


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def downlode():
    if request.method == "POST":
        url = request.form.get("url", None)
        response = requests.get(url)
        path_to_download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # name file
        name_company = "smart-industries-"
        code_name = url[:: url.index(":/")]
        name_file_code = code_name[code_name.index("h") + 2 :]
        rand = randint(0, 2007)
        name_file = name_company + name_file_code + "-" + str(rand)

        # image path
        image_path =os.path.join(path_to_download_folder, name_file)
        print(name_file)

        # save file
        with open(image_path, "wb") as file:
            file.write(response.content)

    return render_template("index.html")


# "smart-industries" + "-" + name_file + ".jpg",
if __name__ == "__main__":
    app.run(debug=True)
