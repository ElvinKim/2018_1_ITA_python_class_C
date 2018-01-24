score_dict = {"korean": 90, "math": 98, "english": 60}

print(score_dict.keys())
print(score_dict.values())
print(score_dict.items())
print("-" * 30)

print(score_dict.get("korean"))
print(score_dict["korean"])

print(score_dict.get("music"))  # None
#print(score_dict["music"])  Error

score_dict.clear()
print(score_dict)

