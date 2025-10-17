#!/usr/bin/env python3
import re

def replace_all_keywords(code, replacements): # Use regex parsing to replace arabic syntax back to normal syntax
    string_re = r'(\"\"\".*?\"\"\"|\'\'\'.*?\'\'\'|\".*?(?<!\\)\"|\'.*?(?<!\\)\')'
    parts = re.split(string_re, code, flags=re.DOTALL)

    for i in range(len(parts)):
        if i % 2 == 0:
            for key, val in sorted(replacements.items(), key=lambda x: -len(x[0])):
                pattern = re.escape(key)
                parts[i] = re.sub(pattern, val, parts[i])
    return ''.join(parts)