def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name']   = first
    profile['last_name']    = last

    for k, v in user_info.items():
        profile[k] = v

    return profile

user_profile = build_profile('muhammad isfaaq', 'goomany', age=18)

print(user_profile)