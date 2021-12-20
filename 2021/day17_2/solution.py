
from dataclasses import dataclass


@dataclass
class Target:
    x_low: int
    x_high: int
    y_low: int
    y_high: int


def passed_target(x_curr: int, y_curr: int, target: Target) -> bool:
    if x_curr > target.x_high:
        return True
    if y_curr < target.y_low:
        return True
    return False


def test_trajectory(x_vel: int, y_vel: int, target: Target):
    x_curr = 0
    y_curr = 0
    while not passed_target(x_curr, y_curr, target):
        if (target.x_low <= x_curr <= target.x_high) and (target.y_low <= y_curr <= target.y_high):
            return True
        x_curr += x_vel
        y_curr += y_vel
        if x_vel > 0:
            x_vel -= 1
        if x_vel < 0:
            x_vel += 1
        y_vel -= 1
    return False


def main():
    target = Target(144, 178, -100, -76)
    count = 0
    for x_vel in range(1,target.x_high+1):
        for y_vel in range(target.y_low-1,-(target.y_low-1)):
            if test_trajectory(x_vel, y_vel, target):
                count+=1
    print(f"solution: {count}")


if __name__ == "__main__":
    main()

