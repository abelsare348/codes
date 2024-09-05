# Q1. How python supports multiple inheritance whereas java does not.?

# Method Resolution Order (MRO) is an approach that takes to resolve the variables or functions of a class.

# In the multiple inheritance use case, the attribute is first looked up in the current class. If it fails, then the next place to search is in the parent class.
# If there are multiple parent classes, then the preference order is depth-first followed by a left-right path.
# MRO ensures that a class always precedes its parents and for multiple parents, keeps the order as the tuple of base classes and avoids ambiguity.