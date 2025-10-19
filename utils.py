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

def format_list(li: list):
    def strip_outer_quotes(s):
        if (s.startswith("'") and s.endswith("'")) or (s.startswith('"') and s.endswith('"')):
            return s[1:-1]
        return s

    return ' '.join(strip_outer_quotes(item) for item in li)
