import os
import json
import shutil


def main():
    minecraft_path = os.environ["AppData"] + "/.minecraft"
    new_path = "c:/minecraft/assets"
    convert_asset(minecraft_path=minecraft_path, new_path=new_path, index_file="1.10.json")


def convert_asset(new_path, index_file, minecraft_path=os.environ["AppData"] + "/.minecraft"):
    indexes_path = minecraft_path + "/assets/indexes/" + index_file
    object_path = minecraft_path + "/assets/objects"
    json_data = read_object_indexes(indexes_path)

    for filename in json_data:
        hash_string = json_data[filename]["hash"]

        src_path = "%s/%s/%s" % (object_path, hash_string[:2], hash_string)
        dst_path = "%s/%s" % (new_path, filename)

        make_dir(dst_path)
        shutil.copy(src_path, src_path)

        print("복사중.. (%s from %s)" % (filename, hash_string))


def read_object_indexes(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data["objects"]


def make_dir(path):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


if __name__ == "__main__":
    main()
