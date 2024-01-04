def skill_cycle_calculator(default_rage_per_second, rage_added_after_skill, skill_threshold, total_time_seconds):
    rage = initial_rage
    skill_cycles = 0
    time_elapsed = 0

    while time_elapsed < total_time_seconds:
        rage += default_rage_per_second
        time_elapsed += 1

        if rage >= skill_threshold:
            skill_cycles += 1
            time_elapsed += 1
            print(f"Skill launched at {time_elapsed} seconds. Rage before launch: {rage}")
            rage -= skill_threshold
            rage += rage_added_after_skill
            rage += default_rage_per_second
            
            print(f"Rage after launch: {rage}")

    return skill_cycles

# Example usage
initial_rage = float(input("Enter rage when entering battle: "))
default_rage_per_second = float(input("Enter default rage per second: "))
rage_added_after_skill = float(input("Enter rage added after skill launch: "))
skill_threshold = float(input("Enter rage required: "))
total_time_seconds = int(input("Enter the total time in seconds: "))

result = skill_cycle_calculator(default_rage_per_second, rage_added_after_skill, skill_threshold, total_time_seconds)
print(f"Number of skill cycles in {total_time_seconds} seconds: {result}")


input("Press Enter to exit...")
