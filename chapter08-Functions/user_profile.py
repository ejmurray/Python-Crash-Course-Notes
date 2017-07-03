def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile

new_user = build_profile('Ernest', 'Murray', age=4, location='Leeds', marital_status=True)
print(new_user)
