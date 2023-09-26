def make_windows_friendly(string):
    chars_to_replace = ["<", ">", ":", "\"", "/", "\\", "|", "?", "*"]
    for char in chars_to_replace:
        string = string.replace(char, "#")
    return string
