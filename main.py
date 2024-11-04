import pandas as pd

db = {
    "F.I.SH": ["Aliyev Ali", "Karimova Dilnoza", "Rahimov Shokir", "Ismailova Shirin", "Rustamov Jasur", "Abdullayeva Nargiza", "Sodiqov Timur", "Azimova Gulchehra", "Abdullayev Farrux", "Iskandarova Dilorom"],
    "Yoshi": [18, 15, 16, 17, 19, 18, 13, 14, 15, 19],
    "Jinsi": ["Erkak", "Ayol", "Erkak", "Ayol", "Erkak", "Ayol", "Erkak", "Ayol", "Erkak", "Ayol"],
    "Maktab raqami": ["26-umumiy ta'lim", "Prezident maktabi", "55-IDUM", "20-umumiy ta'lim", "18-xususiy ta'lim", "68-IDUM", "Prezident maktabi", "31-IDUM", "2-umumiy ta'lim", "6-xususiy ta'lim"],
}

df = pd.DataFrame(db)
print(df)

print("\n\n18 va 18 yoshdan kotta bollar:")
filter = df[(df["Jinsi"] == "Erkak") & (df["Yoshi"] > 17)]
print(filter)

print("\n\nEng yoshi katta odam:")
print(df[df["Yoshi"] == df["Yoshi"].max()])