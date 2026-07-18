# ---------------- First Fit ----------------
def first_fit(items, capacity=1.0):

    bins = []               # Remaining space in each bin
    bin_contents = []       # Items stored in each bin

    for item in items:

        placed = False

        for i, space in enumerate(bins):

            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break

        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


# ---------------- First Fit Decreasing ----------------
def first_fit_decreasing(items, capacity=1.0):

    sorted_items = sorted(items, reverse=True)

    return first_fit(sorted_items, capacity)


# ---------------- Best Fit Decreasing ----------------
def best_fit_decreasing(items, capacity=1.0):

    sorted_items = sorted(items, reverse=True)

    bins = []
    bin_contents = []

    for item in sorted_items:

        best_index = -1
        minimum_space = float("inf")

        for i, space in enumerate(bins):

            if space >= item and (space - item) < minimum_space:
                minimum_space = space - item
                best_index = i

        if best_index != -1:
            bins[best_index] -= item
            bin_contents[best_index].append(item)

        else:
            bins.append(capacity - item)
            bin_contents.append([item])

    return bin_contents


# ---------------- Display Bins ----------------
def display_bins(title, bins):

    print(f"\n{title}")
    print(f"Total Bins Used : {len(bins)}\n")

    for i, b in enumerate(bins, start=1):

        used = sum(b)

        bar = "#" * int(used * 20)

        print(
            f"Bin {i}: {b} | Used = {used:.1f} "
            f"[{bar:<20}]"
        )


# ---------------- Main Program ----------------
items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]

capacity = 1.0

lower_bound = int(-(-sum(items) // capacity))

print("Items :", items)
print("Bin Capacity :", capacity)
print("Total Weight :", sum(items))
print("Lower Bound on Bins :", lower_bound)


ff_bins = first_fit(items)

ffd_bins = first_fit_decreasing(items)

bfd_bins = best_fit_decreasing(items)


display_bins("First Fit (FF)", ff_bins)

display_bins("First Fit Decreasing (FFD)", ffd_bins)

display_bins("Best Fit Decreasing (BFD)", bfd_bins)


print("\nSummary")
print("-------")
print("Lower Bound :", lower_bound)
print("First Fit :", len(ff_bins))
print("FFD :", len(ffd_bins))
print("BFD :", len(bfd_bins))