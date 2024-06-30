def contains_keywords(keywords,substrings,text):

    # 检查是否包含任何关键词
    if any(keyword in text for keyword in keywords):
        return True

    # 检查是否包含任何子字符串（不区分大小写）
    if any(substring.lower() in text.lower() for substring in substrings):
        return True

    return False