# Question 1. Write a function to make a new list with the elements in
# reversed order
# ❑ If original_samples is [1,2,3], then this should return a new_list [3,2,1].
# ❑ You may not use the Python reversed function, or original_samples[::-1].
# ❑ Loop over the items in the list and build up a new list in the desired order.
# ❑ This function has been started for you.
# 11
# def make_reversed_samples(original_samples):
# new_samples = [] # start with an empty new list
# # Add code to make the function work as specified.
# return new_samples

def make_reversed_samples(original_samples):
    new_samples = []
    for i in range(len(original_samples) - 1, -1, -1):
        new_samples.append(original_samples[i])
    return new_samples




#  Question 2. Write a function to make a new list with each element of the old
# list
# ❑ multiplied by volume. This will have the effect of making the sound louder.
# ❑ If original_samples is [1,2,3] and volume is 2, then this should return a new list [2,4,6]. You
# must use a loop to get the elements in the original list and build up a new list in that loop.
# ❑ Return the new list


def make_louder_samples(original_samples, volume):
    new_samples = []
    for sample in original_samples:
        new_samples.append(sample * volume)
    return new_samples

original_samples = [1, 2, 3]
volume = 2
amplified_samples = make_louder_samples(original_samples, volume)
print(amplified_samples)
