#program to replace the required data with the orginal one

letter ='''Dear <|Name|>
You are selected
<|Date|>'''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "19-July-2026"))
