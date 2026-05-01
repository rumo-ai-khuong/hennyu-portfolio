vocab_list = [
    {
        "word": "経営理念",
        "reading": "けいえいりねん",
        "meaning": "triết lý kinh doanh"
    },
    {
        "word": "経営戦略",
        "reading": "けいえいせんりゃく",
        "meaning": "chiến lược kinh doanh"
    },
    {
        "word": "コンプライアンス",
        "reading": "こんぷらいあんす",
        "meaning": "tuân thủ pháp luật"
    },
    {
        "word": "CSR",
        "reading": "しーえすあーる",
        "meaning": "trách nhiệm xã hội của doanh nghiệp"
    },
    {
        "word": "BCP",
        "reading": "びーしーぴー",
        "meaning": "kế hoạch duy trì hoạt động kinh doanh"
    },
    {
        "word": "BCM",
        "reading": "びーしーえむ",
        "meaning": "quản lý duy trì hoạt động kinh doanh"
    },
]

print("Japanese Vocabulary Review")
print("-" * 40)

for index, item in enumerate(vocab_list, start=1):
    print(f"{index}. {item['word']}（{item['reading']}）")
    print(f"   Meaning: {item['meaning']}")
    print()
