# utils.py
import re

def replace_all_keywords(code, replacements):
    string_re = r'(\"\"\".*?\"\"\"|\'\'\'.*?\'\'\'|\".*?(?<!\\)\"|\'.*?(?<!\\)\')'
    parts = re.split(string_re, code, flags=re.DOTALL)

    for i in range(len(parts)):
        if i % 2 == 0:  # non-string parts
            for key, val in sorted(replacements.items(), key=lambda x: -len(x[0])):  # sort longest first
                # Just match the literal string
                pattern = re.escape(key)
                parts[i] = re.sub(pattern, val, parts[i])
    return ''.join(parts)