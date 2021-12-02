def calculateHorizonalDepth(commands, nums):
    horizontal = 0
    depth = 0
    for i in range(len(commands)):
        if commands[i] == "forward":
            horizontal += int(nums[i])
        elif commands[i] == "down":
            depth += int(nums[i])
        elif commands[i] == "up":
            depth -= int(nums[i])
    return horizontal*depth

def calculateHorizontalDepthWithAim(commands, nums):
    horizontal = 0
    depth = 0
    aim = 0
    for i in range(len(commands)):
        if commands[i] == "forward":
            horizontal += int(nums[i])
            depth += aim*int(nums[i])
        elif commands[i] == "down":
            aim += int(nums[i])
        elif commands[i] == "up":
            aim -= int(nums[i])
    return horizontal*depth

def main():
    aList = [line.rstrip() for line in open('Day 2\day 2.txt')]
    commands = []
    nums = []
    for instruction in aList:
        num = instruction[-1]
        command = instruction[:-2]
        commands.append(command)
        nums.append(num)
    print(calculateHorizonalDepth(commands, nums))
    print(calculateHorizontalDepthWithAim(commands, nums))

main()

